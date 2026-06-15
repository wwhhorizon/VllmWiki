# vllm-project/vllm#11365: [Feature]: Add support for attention score output

| 字段 | 值 |
| --- | --- |
| Issue | [#11365](https://github.com/vllm-project/vllm/issues/11365) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for attention score output

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Problem vLLM currently doesn't provide access to attention scores during inference, which are essential for model analysis and interpretability research. #11862 ## Feature Request Add the ability to retrieve attention scores during model inference, similar to HuggingFace's output_attentions=True parameter. ## Motivation Need to analyze token-level relationships in model outputs Required for building visualization tools and debugging model behavior Critical for research into attention mechanisms ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ference, which are essential for model analysis and interpretability research. #11862 ## Feature Request Add the ability to retrieve attention scores during model inference, similar to HuggingFace's output_attentions=Tr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ide access to attention scores during inference, which are essential for model analysis and interpretability research. #11862 ## Feature Request Add the ability to retrieve attention scores during model inference, simil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add support for attention score output feature request;stale ### 🚀 The feature, motivation and pitch ## Problem vLLM currently doesn't provide access to attention scores during inference, which are essential...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Need to analyze token-level relationships in model outputs Required for building visualization tools and debugging model behavior Critical for research into attention mechanisms ### Alternatives _No response_ ### Additi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
