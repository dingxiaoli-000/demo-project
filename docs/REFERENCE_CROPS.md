# 参考图分区裁图清单

## 事实源

- 文件：`reference/site-reference.jpg`
- 原始尺寸：2876 × 8752 px
- 实际编码：PNG（虽然文件扩展名为 `.jpg`）
- SHA-256：`a39dac4287deeb97196c12257ba25bc85d06f977804716dc36b4742c1e7e5632`
- 地位：唯一视觉事实源；本清单中的裁图均为可再生的派生工作视图。

## 坐标与重叠规则

- 坐标原点位于原图左上角，x 向右、y 向下，单位为像素。
- 表格坐标格式统一为 `(x, y, width, height)`。
- “内容范围”表示语义区块边界；“实际裁图”在内容边界上下各保留 80px。
- 相邻裁图因此有 160px 实际重叠；首张和末张只向页面内部扩展。
- 裁图保持原始宽度和像素，不缩放、不调色、不锐化。
- 若裁图与完整图产生任何疑义，完整事实源具有最高优先级。

## 清单

| 区块 | 文件 | 内容范围 | 实际裁图 | 上 / 下余量 | 用途 |
| --- | --- | --- | --- | --- | --- |
| `01-header-hero` | `reference/sections/01-header-hero.png` | (0, 0, 2876, 1530) | (0, 0, 2876, 1610) | 0 / 80 px | 全局导航、主标题、CTA、工程大脑主视觉与 Agent 标签 |
| `02-key-metrics` | `reference/sections/02-key-metrics.png` | (0, 1530, 2876, 650) | (0, 1450, 2876, 810) | 80 / 80 px | 采购响应、成本降低、核算周期与 BIM 预测数据卡 |
| `03-management-problems` | `reference/sections/03-management-problems.png` | (0, 2180, 2876, 760) | (0, 2100, 2876, 920) | 80 / 80 px | 区块标题及进度、材料、成本、协同四张问题卡 |
| `04-platform-architecture` | `reference/sections/04-platform-architecture.png` | (0, 2940, 2876, 1360) | (0, 2860, 2876, 1520) | 80 / 80 px | 工程大脑、Agent 标签、五层业务架构说明 |
| `05-intelligent-modules` | `reference/sections/05-intelligent-modules.png` | (0, 4300, 2876, 1020) | (0, 4220, 2876, 1180) | 80 / 80 px | 五张模块卡及对应 3D 功能插画 |
| `06-case-study` | `reference/sections/06-case-study.png` | (0, 5320, 2876, 1220) | (0, 5240, 2876, 1380) | 80 / 80 px | 项目鸟瞰图、案例说明、指标数据与执行时间轴 |
| `07-whitepapers` | `reference/sections/07-whitepapers.png` | (0, 6540, 2876, 1200) | (0, 6460, 2876, 1360) | 80 / 80 px | 白皮书封面、三张资源卡与下载操作 |
| `08-bottom-cta` | `reference/sections/08-bottom-cta.png` | (0, 7740, 2876, 550) | (0, 7660, 2876, 710) | 80 / 80 px | 底部 CTA、双按钮与未来城市插画 |
| `09-footer` | `reference/sections/09-footer.png` | (0, 8290, 2876, 462) | (0, 8210, 2876, 542) | 80 / 0 px | 品牌简介、链接栏目、联系方式与版权信息 |

## 再生成

运行 `scripts/generate_reference_crops.py` 可从唯一事实源重新生成全部裁图、JSON 清单和联系表。脚本会先校验事实源 SHA-256 与尺寸，校验失败时不会继续生成。

机器可读清单位于 `reference/sections/manifest.json`。为控制仓库体积，九张分区工作图和快速总览不纳入版本库；需要时运行 `python3 scripts/generate_reference_crops.py` 从唯一事实源重新生成。
