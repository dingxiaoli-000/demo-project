# 页面配图替换规格

## 01 Header Hero

| 页面槽位 | 正式文件路径 | 推荐画布 | 比例 | 背景 | 页面适配 |
| --- | --- | --- | --- | --- | --- |
| 工程大脑主视觉 | `assets/images/hero-brain.png` | 1520 × 1520 px | 1:1 | 透明 | `object-fit: contain` |
| 工程大脑动画 | `assets/videos/hero.mp4` | 960 × 960 px | 1:1 | 近白纯色 | `darken` 混合 + 径向遮罩 |
| 工程大脑透明动画 | `assets/videos/hero-transparent.webm` | 960 × 960 px | 1:1 | Alpha 透明 | VP9 WebM，浏览器优先加载 |
| 系统品牌 Logo | `assets/images/logo.svg` | 1807 × 429 viewBox | 约 4.21:1 | 文件内置 | 宽度自适应，高度自动 |

### 主视觉安全区域

- 主体几何图形建议限制在画布中央 72% 范围内。
- 底座可以延伸至画布宽度的 78%，但不要触碰画布边缘。
- 画布四周至少保留 8% 透明留白，避免阴影和光晕被裁掉。
- 不要在正式图片中加入智慧采购、BIM、财务等 Agent 标签；这些标签由 HTML/CSS 负责。
- 不要加入页面文案、按钮、Logo 或水印。
- 建议保留参考图的正面略俯视角、蓝色透明底座、紫红橙交叉核心和柔和蓝色体积光。

### 替换方法

正式图片已接入为 `assets/images/hero-brain.png`。后续若再次更新，保持 1520 × 1520 px 透明 PNG 并覆盖该文件即可，无需修改 HTML 或 CSS。

动画已接入为 `assets/videos/hero.mp4`，静态 PNG 同时作为视频 poster 和降级资源。当前原片约 4.5MB、4.1 秒、H.264/AAC、约 9.36Mbps；建议最终发布前压缩到 1–2MB 并移除无用音轨。

页面优先加载 `hero-transparent.webm`：约 2.7MB、VP9、透明 Alpha、无音轨。MP4 仅作为不支持 WebM 时的兼容回退，并由脚本自动启用纯色背景混合样式。

重新生成透明视频可运行 `scripts/generate_hero_video.sh`。默认读取 `assets/videos/hero.mp4` 并输出 `assets/videos/hero-transparent.webm`；也可以传入自定义输入和输出路径。

透明化采用分区混合抠像：画面上方使用色度软键清除纯色背景和中性灰白阴影；底座区域使用较保守的颜色距离键保留白色玻璃、高光和蓝色透明结构；Y=480–650px 之间渐变混合，避免接缝。网页端不再额外调整视频饱和度或对比度。

## 02 Key Metrics

| 页面槽位 | 正式文件路径 | 画布 | 背景 |
| --- | --- | --- | --- |
| 采购响应 | `assets/images/metric-purchase-response.png` | 500 × 500 px | Alpha 透明 |
| 成本降低 | `assets/images/metric-cost-reduction.png` | 500 × 500 px | Alpha 透明 |
| 核算周期 | `assets/images/metric-accounting-cycle.png` | 500 × 500 px | Alpha 透明 |
| BIM 预测 | `assets/images/metric-bim-prediction.png` | 500 × 500 px | Alpha 透明 |

四张图片使用 `object-fit: contain`，后续更新时保持语义文件名和 1:1 透明画布即可直接覆盖。

## 03 Management Problems

| 页面槽位 | 正式文件路径 | 画布 | 背景 |
| --- | --- | --- | --- |
| 进度黑箱 | `assets/images/problem-schedule.png` | 500 × 500 px | Alpha 透明 |
| 材料黑箱 | `assets/images/problem-material.png` | 500 × 500 px | Alpha 透明 |
| 成本黑箱 | `assets/images/problem-cost.png` | 500 × 500 px | Alpha 透明 |
| 协同黑箱 | `assets/images/problem-collaboration.png` | 500 × 500 px | Alpha 透明 |

四张图片均使用 `object-fit: contain`。后续更新时保持语义文件名、透明背景和 1:1 画布即可直接覆盖。

## 06 Case Study

| 页面槽位 | 正式文件路径 | 推荐画布 | 比例 | 背景 | 页面适配 |
| --- | --- | --- | --- | --- | --- |
| 湖州织东控规单元项目鸟瞰图 | `assets/images/case-study-aerial.png` | 1254 × 1254 px | 1:1 | 不透明 | `object-fit: cover` |

- 构图以高层住宅项目临水鸟瞰为主体，水面占画面下半部，楼群集中在上半部，整体为冷蓝色调。
- 图片中不得包含文字、Logo、水印、指标卡或时间轴。
- 用户提供的正式鸟瞰图已接入。后续更新时保持语义文件名和 1:1 画布，直接覆盖该路径即可。

## 04 Platform Architecture

| 页面槽位 | 正式文件路径 | 推荐画布 | 比例 | 背景 |
| --- | --- | --- | --- | --- |
| 平台架构中央工程大脑 | `assets/images/platform-architecture-core.png` | 1520 × 1520 px | 1:1 | Alpha 透明 |
| 数据矩阵层图标 | `assets/images/architecture-data-layer.png` | 400 × 400 px | 1:1 | Alpha 透明 |
| 智能分析层图标 | `assets/images/architecture-analysis-layer.png` | 400 × 400 px | 1:1 | Alpha 透明 |
| Agent 编排层图标 | `assets/images/architecture-agent-layer.png` | 400 × 400 px | 1:1 | Alpha 透明 |
| 业务执行层图标 | `assets/images/architecture-execution-layer.png` | 400 × 400 px | 1:1 | Alpha 透明 |
| 审计保障层图标 | `assets/images/architecture-audit-layer.png` | 400 × 400 px | 1:1 | Alpha 透明 |

- 主体限制在画布中央约 72%，底座可扩展到画布宽度约 82%。
- 只绘制彩色交叉几何中枢和蓝色透明玻璃底座，不包含轨道、节点、Agent 标签、标题或文字。
- 页面通过 `object-fit: contain` 接入；轨道和业务标签继续由 HTML/CSS 实现，以支持响应式与文本替换。

## 07 Whitepapers

| 页面槽位 | 正式文件路径 | 实际画布 | 比例 | 背景 |
| --- | --- | --- | --- | --- |
| 白皮书立体封面 | `assets/images/whitepaper-book.png` | 1254 × 1254 px | 1:1 | 不透明 |
| 多 Agent 架构预览 | `assets/images/whitepaper-agent-architecture.png` | 672 × 666 px | 约 1:1 | Alpha 透明 |
| 智慧采购流程预览 | `assets/images/whitepaper-procurement-flow.png` | 686 × 530 px | 约 1.29:1 | Alpha 透明 |
| 项目成本图表预览 | `assets/images/whitepaper-cost-chart.png` | 691 × 540 px | 约 1.28:1 | Alpha 透明 |

- 用户提供的四张正式配图已接入，后续更新时保持语义文件名即可直接覆盖。
- 正式封面图应包含书本主体、侧面和页张层次，不应包含右侧区块标题、资源卡或按钮。
- 三张预览图只保留图表与必要图内标注，卡片标题、摘要、书签和按钮继续由 HTML/CSS 负责。

## 08 Bottom CTA

| 页面槽位 | 正式文件路径 | 推荐画布 | 比例 | 背景 | 页面适配 |
| --- | --- | --- | --- | --- | --- |
| 未来智能城市 | `assets/images/bottom-cta-city.png` | 1464 × 864 px | 约 1.69:1 | Alpha 透明 | `object-fit: contain` |

- 参考图可确认为正面略俯视的冷蓝色玻璃城市群，中心为一组高楼，外围由粉紫至蓝色双层光带横向环绕。
- 主体建议集中在画布中央偏右，城市底座与光带可占画布宽度约 90%，四周保留柔和的透明光晕。
- 图片不包含标题、副标题、按钮、Logo 或水印；这些由 HTML/CSS 独立实现。
- 用户提供的正式透明配图已接入。后续更新时保持语义文件名即可直接覆盖；CSS 降级层仅在配图加载失败时显示。
