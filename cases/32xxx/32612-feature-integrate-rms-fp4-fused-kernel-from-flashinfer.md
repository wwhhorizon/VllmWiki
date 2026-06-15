# vllm-project/vllm#32612: [Feature]: Integrate RMS+fp4 fused kernel from FlashInfer

| 字段 | 值 |
| --- | --- |
| Issue | [#32612](https://github.com/vllm-project/vllm/issues/32612) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request;torch.compile;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Integrate RMS+fp4 fused kernel from FlashInfer

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Kernel: https://github.com/flashinfer-ai/flashinfer/blob/main/flashinfer/norm.py#L406-L409 This should be integrated in the existing rms + quant fusion pass using a similar approach as the silu+fp4 fusion in the act quant fusion pass. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Feature]: Integrate RMS+fp4 fused kernel from FlashInfer help wanted;good first issue;feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch Kernel: https://github.com/flashinfer-ai/flashinfer/blob...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: MS+fp4 fused kernel from FlashInfer help wanted;good first issue;feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch Kernel: https://github.com/flashinfer-ai/flashinfer/blob/main/flashinfer/norm....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Integrate RMS+fp4 fused kernel from FlashInfer help wanted;good first issue;feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch Kernel: https://github.com/flashinfer-ai/flashinfer/blob...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ernel from FlashInfer help wanted;good first issue;feature request;torch.compile;stale ### 🚀 The feature, motivation and pitch Kernel: https://github.com/flashinfer-ai/flashinfer/blob/main/flashinfer/norm.py#L406-L409 T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
