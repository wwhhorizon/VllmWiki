# vllm-project/vllm#36037: [Feature]: Supports Speculative Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#36037](https://github.com/vllm-project/vllm/issues/36037) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Supports Speculative Speculative Decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # Motivation vLLM already supports speculative decoding to accelerate autoregressive generation using a draft model. However, speculative decoding still suffers from a sequential dependency between drafting and verification: the draft model must wait for the target model to finish verifying tokens before generating the next speculation batch. Recent work proposes Speculative Speculative Decoding (SSD), which removes this dependency by running drafting and verification asynchronously and precomputing speculations for predicted verification outcomes. paper link: [https://arxiv.org/pdf/2603.03251](https://arxiv.org/pdf/2603.03251) In SSD, while the target model verifies a speculation, the draft model predicts likely verification outcomes and pre-speculates tokens for those outcomes in advance. If the actual verification result matches one of the predicted outcomes, the next speculation can be returned immediately, eliminating drafting latency. This approach enables overlapping speculation and verification and significantly reduces idle GPU time. The paper reports: - Up to 2× speedup over optimized speculative decoding - Up to 5× speedup over au...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Supports Speculative Speculative Decoding feature request ### 🚀 The feature, motivation and pitch # Motivation vLLM already supports speculative decoding to accelerate autoregressive generation using a draft...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: aft model. However, speculative decoding still suffers from a sequential dependency between drafting and verification: the draft model must wait for the target model to finish verifying tokens before generating the next...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: , the next speculation can be returned immediately, eliminating drafting latency. This approach enables overlapping speculation and verification and significantly reduces idle GPU time. The paper reports: - Up to 2× spe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sd) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eculative decoding to accelerate autoregressive generation using a draft model. However, speculative decoding still suffers from a sequential dependency between drafting and verification: the draft model must wait for t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
