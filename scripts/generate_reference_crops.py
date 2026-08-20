#!/usr/bin/env python3
"""Generate reproducible, lossless working crops from the visual SSOT."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reference" / "site-reference.jpg"
OUTPUT = ROOT / "reference" / "sections"
MANIFEST_JSON = OUTPUT / "manifest.json"
MANIFEST_MD = ROOT / "docs" / "REFERENCE_CROPS.md"
CONTACT_SHEET = OUTPUT / "contact-sheet.png"
EXPECTED_SHA256 = "a39dac4287deeb97196c12257ba25bc85d06f977804716dc36b4742c1e7e5632"
OVERLAP_MARGIN = 80

# content_top/content_bottom are semantic boundaries on the 2876 × 8752 source.
SECTIONS = [
    ("01-header-hero", "顶部导航与首屏 Hero", 0, 1530, "全局导航、主标题、CTA、工程大脑主视觉与 Agent 标签"),
    ("02-key-metrics", "四项核心指标", 1530, 2180, "采购响应、成本降低、核算周期与 BIM 预测数据卡"),
    ("03-management-problems", "传统管理四大黑箱", 2180, 2940, "区块标题及进度、材料、成本、协同四张问题卡"),
    ("04-platform-architecture", "工程大脑中枢与业务层级", 2940, 4300, "工程大脑、Agent 标签、五层业务架构说明"),
    ("05-intelligent-modules", "五大智能模块", 4300, 5320, "五张模块卡及对应 3D 功能插画"),
    ("06-case-study", "真实项目案例", 5320, 6540, "项目鸟瞰图、案例说明、指标数据与执行时间轴"),
    ("07-whitepapers", "AI 白皮书资源区", 6540, 7740, "白皮书封面、三张资源卡与下载操作"),
    ("08-bottom-cta", "底部行动召唤", 7740, 8290, "底部 CTA、双按钮与未来城市插画"),
    ("09-footer", "页脚", 8290, 8752, "品牌简介、链接栏目、联系方式与版权信息"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_contact_sheet(items: list[dict]) -> None:
    thumb_width = 620
    gap = 24
    label_height = 56
    thumbs = []
    for item in items:
        image = Image.open(ROOT / item["file"]).convert("RGB")
        height = round(image.height * thumb_width / image.width)
        image = image.resize((thumb_width, height), Image.Resampling.LANCZOS)
        thumbs.append((item, image))

    sheet_height = gap + sum(label_height + image.height + gap for _, image in thumbs)
    sheet = Image.new("RGB", (thumb_width + gap * 2, sheet_height), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    y = gap
    for item, image in thumbs:
        label = f'{item["id"]} | crop y={item["crop"]["y"]}, h={item["crop"]["height"]}'
        draw.text((gap, y + 14), label, fill="#15192d", font=font)
        y += label_height
        sheet.paste(image, (gap, y))
        y += image.height + gap
    sheet.save(CONTACT_SHEET, "PNG", optimize=True)


def main() -> None:
    source_hash = sha256(SOURCE)
    if source_hash != EXPECTED_SHA256:
        raise SystemExit(f"Source checksum mismatch: {source_hash}")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    with Image.open(SOURCE) as source:
        source.load()
        width, height = source.size
        if (width, height) != (2876, 8752):
            raise SystemExit(f"Unexpected source dimensions: {width} × {height}")

        items = []
        for index, (slug, title, content_top, content_bottom, purpose) in enumerate(SECTIONS):
            crop_top = max(0, content_top - (OVERLAP_MARGIN if index else 0))
            crop_bottom = min(height, content_bottom + (OVERLAP_MARGIN if index < len(SECTIONS) - 1 else 0))
            filename = f"{slug}.png"
            target = OUTPUT / filename
            crop = source.crop((0, crop_top, width, crop_bottom))
            crop.save(target, "PNG", optimize=True)
            items.append(
                {
                    "id": slug,
                    "title": title,
                    "file": str(target.relative_to(ROOT)),
                    "content_bounds": {"x": 0, "y": content_top, "width": width, "height": content_bottom - content_top},
                    "crop": {"x": 0, "y": crop_top, "width": width, "height": crop_bottom - crop_top},
                    "overlap": {
                        "top": content_top - crop_top,
                        "bottom": crop_bottom - content_bottom,
                        "with_previous": 0 if index == 0 else OVERLAP_MARGIN * 2,
                        "with_next": 0 if index == len(SECTIONS) - 1 else OVERLAP_MARGIN * 2,
                    },
                    "purpose": purpose,
                    "sha256": sha256(target),
                }
            )

    manifest = {
        "source": {
            "file": str(SOURCE.relative_to(ROOT)),
            "width": 2876,
            "height": 8752,
            "detected_format": "PNG",
            "filename_extension": ".jpg",
            "sha256": source_hash,
            "authority": "唯一视觉事实源；所有裁图均为可再生派生工作视图",
        },
        "coordinate_system": "原图左上角为 (0, 0)，x 向右、y 向下，单位为像素；裁切矩形采用 x/y/width/height",
        "overlap_policy": "语义边界上下各扩展 80px；因此相邻裁图的实际交叠为 160px。首尾仅向页面内部扩展。",
        "sections": items,
    }
    MANIFEST_JSON.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    rows = []
    for item in items:
        bounds = item["content_bounds"]
        crop = item["crop"]
        overlap = item["overlap"]
        rows.append(
            f'| `{item["id"]}` | `{item["file"]}` | '
            f'({bounds["x"]}, {bounds["y"]}, {bounds["width"]}, {bounds["height"]}) | '
            f'({crop["x"]}, {crop["y"]}, {crop["width"]}, {crop["height"]}) | '
            f'{overlap["top"]} / {overlap["bottom"]} px | {item["purpose"]} |'
        )

    markdown = f"""# 参考图分区裁图清单

## 事实源

- 文件：`reference/site-reference.jpg`
- 原始尺寸：2876 × 8752 px
- 实际编码：PNG（虽然文件扩展名为 `.jpg`）
- SHA-256：`{source_hash}`
- 地位：唯一视觉事实源；本清单中的裁图均为可再生的派生工作视图。

## 坐标与重叠规则

- 坐标原点位于原图左上角，x 向右、y 向下，单位为像素。
- 表格坐标格式统一为 `(x, y, width, height)`。
- “内容范围”表示语义区块边界；“实际裁图”在内容边界上下各保留 {OVERLAP_MARGIN}px。
- 相邻裁图因此有 {OVERLAP_MARGIN * 2}px 实际重叠；首张和末张只向页面内部扩展。
- 裁图保持原始宽度和像素，不缩放、不调色、不锐化。
- 若裁图与完整图产生任何疑义，完整事实源具有最高优先级。

## 清单

| 区块 | 文件 | 内容范围 | 实际裁图 | 上 / 下余量 | 用途 |
| --- | --- | --- | --- | --- | --- |
{"\n".join(rows)}

## 再生成

运行 `scripts/generate_reference_crops.py` 可从唯一事实源重新生成全部裁图、JSON 清单和联系表。脚本会先校验事实源 SHA-256 与尺寸，校验失败时不会继续生成。

机器可读清单位于 `reference/sections/manifest.json`，快速总览位于 `reference/sections/contact-sheet.png`。
"""
    MANIFEST_MD.write_text(markdown, encoding="utf-8")
    build_contact_sheet(items)


if __name__ == "__main__":
    main()
