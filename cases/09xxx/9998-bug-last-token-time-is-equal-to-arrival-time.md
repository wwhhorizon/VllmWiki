# vllm-project/vllm#9998: [Bug]: last_token_time is equal to arrival_time

| 字段 | 值 |
| --- | --- |
| Issue | [#9998](https://github.com/vllm-project/vllm/issues/9998) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: last_token_time is equal to arrival_time

### Issue 正文摘录

### Your current environment The bug is not related to the envirement ### Model Input Dumps The bug does not related to the model ### 🐛 Describe the bug ### QUESTION 1: How do you calculate the `RequestMetrics` in `RequestOutput` please look at screen-shot below (in *YELLOW*): ![image](https://github.com/user-attachments/assets/a4ace1ce-e3f1-4acd-8982-3824346829ed) I have found [here in L. 696](https://github.com/vllm-project/vllm/blob/ccb5376a9a88bb6251c4434b79c173151e6f7729/vllm/sequence.py#L696C39-L696C54) that `last_token_time` is equal to `arrival_time` !!! **IS IT A BUG?** Could you please tell me what unit is the time is it second? nanosecond? I believe it is something like this example below (***correct me if I am wrong***): ```python import time arrival_time = time.perf_counter() ``` ### QUESTION 2: How can I calculate the **tokens/second (for output)**, **TTFT**, **TBT**, **throughput** and **total time** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: can I calculate the **tokens/second (for output)**, **TTFT**, **TBT**, **throughput** and **total time** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatb...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hing like this example below (***correct me if I am wrong***): ```python import time arrival_time = time.perf_counter() ``` ### QUESTION 2: How can I calculate the **tokens/second (for output)**, **TTFT**, **TBT**, **th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Your current environment The bug is not related to the envirement ### Model Input Dumps The bug does not related to the model ### 🐛 Describe the bug ### QUESTION 1: How do you calculate the `RequestMetrics` in `RequestO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: model ### 🐛 Describe the bug ### QUESTION 1: How do you calculate the `RequestMetrics` in `RequestOutput` please look at screen-shot below (in *YELLOW*): ![image](https://github.com/user-attachments/assets/a4ace1ce-e3f1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
