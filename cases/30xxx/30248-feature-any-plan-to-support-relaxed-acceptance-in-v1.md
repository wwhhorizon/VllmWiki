# vllm-project/vllm#30248: [Feature]: any plan to support Relaxed Acceptance in v1?

| 字段 | 值 |
| --- | --- |
| Issue | [#30248](https://github.com/vllm-project/vllm/issues/30248) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: any plan to support Relaxed Acceptance in v1?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [NV Relaxed Acceptance](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/tech_blog/blog2_DeepSeek_R1_MTP_Implementation_and_Optimization.md#relaxed-acceptance) There are PRs ([vllm](https://github.com/vllm-project/vllm/pull/21506), [vllm](https://github.com/vllm-project/vllm/pull/22238), [sglang](https://github.com/sgl-project/sglang/pull/7702), [sglang](https://github.com/sgl-project/sglang/pull/8068)) in both sglang and vllm. However, none of them has been merged. What's the story behind this? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: any plan to support Relaxed Acceptance in v1? feature request;stale ### 🚀 The feature, motivation and pitch [NV Relaxed Acceptance](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/tech_blog...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
