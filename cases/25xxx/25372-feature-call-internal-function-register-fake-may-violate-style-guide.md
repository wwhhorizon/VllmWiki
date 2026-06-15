# vllm-project/vllm#25372: [Feature]: call internal function `_register_fake` may violate style guide.

| 字段 | 值 |
| --- | --- |
| Issue | [#25372](https://github.com/vllm-project/vllm/issues/25372) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: call internal function `_register_fake` may violate style guide.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch To start with, it's not a feature request basically, I didn't find a good label to match any issues related to style guide. When investigating https://github.com/vllm-project/vllm/issues/24917#issuecomment-3314130792 . I found some code invoking a internal function from torch which may violate style guide and lead to potential compatibility problem in the future. Here it is: https://github.com/vllm-project/vllm/blob/21467f9a1c6219cbd66640e539b1f23221cff375/vllm/utils/__init__.py#L2617 In fact, torch supported a interface to register fake tensor which refers to internal function as follows: https://github.com/pytorch/pytorch/blob/ba56102387ef21a3b04b357e5b183d48f0afefc7/torch/library.py#L945 It's a really minor point, but negligible code leads to problem hard to locate must be annoying as we all know. @youkaichao ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: call internal function `_register_fake` may violate style guide. feature request;stale ### 🚀 The feature, motivation and pitch To start with, it's not a feature request basically, I didn't find a good label to match any...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
