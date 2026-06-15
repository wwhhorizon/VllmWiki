# vllm-project/vllm#12399: [Feature]: Consider integrating SVDquant (W4A4 quantization) from Nunchaku project

| 字段 | 值 |
| --- | --- |
| Issue | [#12399](https://github.com/vllm-project/vllm/issues/12399) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Consider integrating SVDquant (W4A4 quantization) from Nunchaku project

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I noticed the Nunchaku project (https://github.com/mit-han-lab/nunchaku) has implemented SVDquant, which seems highly compatible with LLM scenarios, particularly their W4A4 quantization approach. This looks very interesting and promising for model optimization. Would vLLM consider supporting or integrating this quantization method? It could potentially offer significant benefits for memory efficiency while maintaining model performance in LLM serving scenarios. The Nunchaku project’s implementation appears to be well-suited for LLM use cases, and integration could be valuable for the vLLM community. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r integrating SVDquant (W4A4 quantization) from Nunchaku project feature request;stale ### 🚀 The feature, motivation and pitch I noticed the Nunchaku project (https://github.com/mit-han-lab/nunchaku) has implemented SVD...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n method? It could potentially offer significant benefits for memory efficiency while maintaining model performance in LLM serving scenarios. The Nunchaku project’s implementation appears to be well-suited for LLM use c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Consider integrating SVDquant (W4A4 quantization) from Nunchaku project feature request;stale ### 🚀 The feature, motivation and pitch I noticed the Nunchaku project (https://github.com/mit-han-lab/nunchaku) h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 4A4 quantization approach. This looks very interesting and promising for model optimization. Would vLLM consider supporting or integrating this quantization method? It could potentially offer significant benefits for me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
