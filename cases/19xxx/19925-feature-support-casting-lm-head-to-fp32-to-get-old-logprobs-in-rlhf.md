# vllm-project/vllm#19925: [Feature]: Support casting lm_head to FP32 to get old logprobs in RLHF

| 字段 | 值 |
| --- | --- |
| Issue | [#19925](https://github.com/vllm-project/vllm/issues/19925) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support casting lm_head to FP32 to get old logprobs in RLHF

### Issue 正文摘录

### 🚀 The feature, motivation and pitch From https://www.arxiv.org/pdf/2506.13585#page=7.62 ![Image](https://github.com/user-attachments/assets/4b81be7d-2b8b-4dc9-a309-98ee954c4846) ![Image](https://github.com/user-attachments/assets/e8fd6686-f34f-4791-be19-323ec9eccd55) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: re]: Support casting lm_head to FP32 to get old logprobs in RLHF feature request;stale ### 🚀 The feature, motivation and pitch From https://www.arxiv.org/pdf/2506.13585#page=7.62 ![Image](https://github.com/user-attachm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support casting lm_head to FP32 to get old logprobs in RLHF feature request;stale ### 🚀 The feature, motivation and pitch From https://www.arxiv.org/pdf/2506.13585#page=7.62 ![Image](https://github.com/user-a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
