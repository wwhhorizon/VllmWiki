# vllm-project/vllm#40605: [Usage]: Missing vllm:num_requests_running and other metrics in vLLM v0.18 when deploying Qwen3.5 27B

| 字段 | 值 |
| --- | --- |
| Issue | [#40605](https://github.com/vllm-project/vllm/issues/40605) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Missing vllm:num_requests_running and other metrics in vLLM v0.18 when deploying Qwen3.5 27B

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am using vLLM v0.18 to deploy the Qwen3.5 27B model. When accessing performance metrics via the /metrics endpoint, I noticed that some expected metrics, such as vllm:num_requests_running, are missing. What could be the reason for this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vllm:num_requests_running and other metrics in vLLM v0.18 when deploying Qwen3.5 27B usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am using vLL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Missing vllm:num_requests_running and other metrics in vLLM v0.18 when deploying Qwen3.5 27B usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
