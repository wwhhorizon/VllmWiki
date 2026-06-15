# vllm-project/vllm#25940: [Feature]: image2text supports SVG image

| 字段 | 值 |
| --- | --- |
| Issue | [#25940](https://github.com/vllm-project/vllm/issues/25940) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: image2text supports SVG image

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am using [InternVL3](https://huggingface.co/OpenGVLab/InternVL3_5-1B) iamge2text model. In the model card, it says it supports SVG image. But vLLM failed to recognize a SVG image. The following is my test payload. ```json { "model": "OpenGVLab/InternVL3_5-1B", "messages": [ { "role": "user", "content": [ { "type": "text", "text": "What does the image show?" }, { "type": "image_url", "image_url": { "url": "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPg0KPHN2ZyB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNi40MjQzNiAwSDkuNTc1NjVMMTQuOTk1IDE2SDExLjgyNzZMMTAuODExNSAxM0g1LjE4ODU1TDQuMTcyNDIgMTZIMS4wMDVMNi40MjQzNiAwWk02LjIwNDY4IDEwSDkuNzk1MzNMOCA0LjY5OTUyTDYuMjA0NjggMTBaIiBmaWxsPSIjMDAwMDAwIi8+DQo8L3N2Zz4=" } } ] } ] } ``` It results in "cannot identify image file" error because the [PIL lib doesn't supports SVG](https://github.com/python-pillow/Pillow/issues/3...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ature request;stale ### 🚀 The feature, motivation and pitch I am using [InternVL3](https://huggingface.co/OpenGVLab/InternVL3_5-1B) iamge2text model. In the model card, it says it supports SVG image. But vLLM failed to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: image2text supports SVG image feature request;stale ### 🚀 The feature, motivation and pitch I am using [InternVL3](https://huggingface.co/OpenGVLab/InternVL3_5-1B) iamge2text model. In the model card, it says...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNi40MjQzNiAwSDkuNTc1NjVMMTQuOTk1IDE2SDExLjgyNzZMMTAuODExNSAxM0g1LjE4ODU1TDQuMTcyNDIgMTZIMS4wMDVMNi40MjQzNiAwWk0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: VG image. But vLLM failed to recognize a SVG image. The following is my test payload. ```json { "model": "OpenGVLab/InternVL3_5-1B", "messages": [ { "role": "user", "content": [ { "type": "text", "text": "What does the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
