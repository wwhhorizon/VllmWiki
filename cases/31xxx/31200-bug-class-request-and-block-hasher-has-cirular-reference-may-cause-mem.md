# vllm-project/vllm#31200: [Bug]: class Request and  block_hasher has cirular reference, may cause memory leak.

| 字段 | 值 |
| --- | --- |
| Issue | [#31200](https://github.com/vllm-project/vllm/issues/31200) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: class Request and  block_hasher has cirular reference, may cause memory leak.

### Issue 正文摘录

### Your current environment Running MultiModal Network with prefix caching will cause memory leak. ### 🐛 Describe the bug Runing a multimodal, will cause memory leak. Because the following leak trace: block_hasher -> MultiModalFeatureSpec -> MultiModalKwargsItem -> MultiModalFiledElem -> image_pixels(Tensor) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: class Request and block_hasher has cirular reference, may cause memory leak. bug;stale ### Your current environment Running MultiModal Network with prefix caching will cause memory leak. ### 🐛 Describe the bug Ru...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: class Request and block_hasher has cirular reference, may cause memory leak. bug;stale ### Your current environment Running MultiModal Network with prefix caching will cause memory leak. ### 🐛 Describe the bug Ru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: class Request and block_hasher has cirular reference, may cause memory leak. bug;stale ### Your current environment Running MultiModal Network with prefix caching will cause memory leak. ### 🐛 Describe the bug Ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: may cause memory leak. bug;stale ### Your current environment Running MultiModal Network with prefix caching will cause memory leak. ### 🐛 Describe the bug Runing a multimodal, will cause memory leak. Because the follow...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
