# Pmagic AI Landing Page

根据视觉参考图实现的独立响应式产品官网，使用语义化 HTML、CSS 与原生 JavaScript 构建。

## 本地预览

直接打开 `index.html`，或在项目目录启动任意静态文件服务器：

```bash
python3 -m http.server 8000
```

然后访问 `http://localhost:8000`。

## 项目结构

- `index.html`：页面语义结构
- `style.css`：响应式布局、视觉样式与动画
- `main.js`：导航、媒体降级、滚动动画与指标计数
- `assets/`：页面实际使用的图片、视频和图标资源
- `reference/site-reference.jpg`：唯一视觉参考源
- `scripts/`：参考裁图与透明视频生成脚本
- `docs/`：设计决策、素材规范和实现记录

`reference/sections/*.png` 是可再生的工作图，不纳入仓库。需要时运行：

```bash
python3 scripts/generate_reference_crops.py
```

