# vllm-project/vllm#23880: [MM Encoder] ViT attention performance and consolidation

| 字段 | 值 |
| --- | --- |
| Issue | [#23880](https://github.com/vllm-project/vllm/issues/23880) |
| 状态 | closed |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [MM Encoder] ViT attention performance and consolidation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Today many vision transformers on vLLM leverage standard `F.scaled_dot_product_attention` to compute attention scores. While there has been some effort in [vision.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/vision.py) to help developers easily choose which backend to use, it would be great if vLLM can consolidate non-mask MHA implementations with different backends without caching so that developers can easily plug them in. We should also investigate integrating FA3 for a few vision models we have and make sure there's no accuracy regression. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: integrating FA3 for a few vision models we have and make sure there's no accuracy regression. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: /model_executor/models/vision.py) to help developers easily choose which backend to use, it would be great if vLLM can consolidate non-mask MHA implementations with different backends without caching so that developers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ntion performance and consolidation help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Today many vision transformers on vLLM leverage standard `F.scaled_dot_product_attention` to...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: integrating FA3 for a few vision models we have and make sure there's no accuracy regression. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: n and pitch Today many vision transformers on vLLM leverage standard `F.scaled_dot_product_attention` to compute attention scores. While there has been some effort in [vision.py](https://github.com/vllm-project/vllm/blo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
