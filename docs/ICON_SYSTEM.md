# 图标系统

## 选型

- 图标库：Phosphor Icons
- 版本：`@phosphor-icons/core@2.0.8`
- 风格：Regular
- 许可：MIT
- 官网：https://phosphoricons.com/
- 源码：https://github.com/phosphor-icons/core

## 使用策略

- 不通过 CDN 加载整套图标字体。
- 只从官方 Core 包提取实际使用的 SVG path，并保存进 `assets/icons.svg`。
- 当前页面同时内联正在使用的 symbol，并用页面内 `#id` 引用，确保直接通过 `file://` 打开时不受外部 SVG 安全限制影响。
- 图标统一通过 `currentColor` 接收页面颜色。
- 品牌 Logo 与箭头属于项目自有基础图形，不计入 Phosphor 图标映射。

## 01 Header Hero 映射

| 页面语义 | Phosphor 图标 | Sprite ID |
| --- | --- | --- |
| 智慧采购 | `shopping-cart-simple` | `cart` |
| BIM 预测 | `cube` | `cube` |
| 过磅防作弊 | `scales` | `scale` |
| 智能财务 | `currency-jpy` | `yen` |
| 企业微信协同 | `wechat-logo` | `wechat` |

许可证副本位于 `assets/vendor/phosphor-icons/LICENSE`。
