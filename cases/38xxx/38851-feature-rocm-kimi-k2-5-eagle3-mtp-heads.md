# vllm-project/vllm#38851: [Feature]: ROCm Kimi K2.5 EAGLE3 MTP heads

| 字段 | 值 |
| --- | --- |
| Issue | [#38851](https://github.com/vllm-project/vllm/issues/38851) |
| 状态 | open |
| 标签 | feature request;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: ROCm Kimi K2.5 EAGLE3 MTP heads

### Issue 正文摘录

### 🚀 The feature, motivation and pitch hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 spec decode is an common method widely used in production but unfortunately the kimi did not release their MTP heads. NVIDIA & production inference API endpoint providers like Baseten have trained their own MTP heads for kimi k2.5 nvidia has open sourced this https://huggingface.co/nvidia/Kimi-K2.5-Thinking-Eagle3 there is also this one trained on torchspec by the community https://huggingface.co/lightseekorg/kimi-k2.5-eagle3 . if this is the recommended mtp head architecture that amd chooses to support, please let me know. AMD does not have their own eagle3 MTP heads open sourced? when should we expect AMD have production features like MTP for kimi k2.5? https://huggingface.co/amd/models?search=kimi ### Alternatives not use spec decode and not bad perf per $ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: ROCm Kimi K2.5 EAGLE3 MTP heads feature request;rocm ### 🚀 The feature, motivation and pitch hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 spec decode is an common method widely used in production bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: ROCm Kimi K2.5 EAGLE3 MTP heads feature request;rocm ### 🚀 The feature, motivation and pitch hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 spec decode is an common method widely used in production bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: their own MTP heads for kimi k2.5 nvidia has open sourced this https://huggingface.co/nvidia/Kimi-K2.5-Thinking-Eagle3 there is also this one trained on torchspec by the community https://huggingface.co/lightseekorg/kim...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
