# vllm-project/vllm#9126: [Usage]: Not getting the infrence metrics in the api response

| 字段 | 值 |
| --- | --- |
| Issue | [#9126](https://github.com/vllm-project/vllm/issues/9126) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Not getting the infrence metrics in the api response

### Issue 正文摘录

### Your current environment "done_reason": "stop", "total_duration": 2236243396, "load_duration": 62450715, "prompt_eval_count": 29, "prompt_eval_duration": 61634000, "eval_count": 429, "eval_duration": 2065715000 i want these infrence metrics in the response or in the logs is there any way to get these? ### How would you like to use vllm i want these infrence metrics in the response or in the logs is there any way to get these? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: "total_duration": 2236243396, "load_duration": 62450715, "prompt_eval_count": 29, "prompt_eval_duration": 61634000, "eval_count": 429, "eval_duration": 2065715000 i want these infrence metrics in the response or in the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Not getting the infrence metrics in the api response usage;stale ### Your current environment "done_reason": "stop", "total_duration": 2236243396, "load_duration": 62450715, "prompt_eval_count": 29, "prompt_eva...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
