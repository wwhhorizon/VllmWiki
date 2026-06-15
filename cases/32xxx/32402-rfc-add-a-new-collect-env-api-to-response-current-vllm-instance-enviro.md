# vllm-project/vllm#32402: [RFC]: Add a new `/collect_env` api to response current vllm instance environment

| 字段 | 值 |
| --- | --- |
| Issue | [#32402](https://github.com/vllm-project/vllm/issues/32402) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add a new `/collect_env` api to response current vllm instance environment

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Motivation: We automate long-term, multi-round performance tests on different environments, collecting and analyzing the test data. However, we currently cannot collect the environment information of the VLLM instance. Change: I want to add an API that can return the environment information of the current VLLM instance. This would be achieved by calling functions in `collect_env.py`. In multi-process scenarios, it's also necessary to obtain the environment information of each process. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ng the test data. However, we currently cannot collect the environment information of the VLLM instance. Change: I want to add an API that can return the environment information of the current VLLM instance. This would...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: `/collect_env` api to response current vllm instance environment feature request ### 🚀 The feature, motivation and pitch Motivation: We automate long-term, multi-round performance tests on different environments, collec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: and pitch Motivation: We automate long-term, multi-round performance tests on different environments, collecting and analyzing the test data. However, we currently cannot collect the environment information of the VLLM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
