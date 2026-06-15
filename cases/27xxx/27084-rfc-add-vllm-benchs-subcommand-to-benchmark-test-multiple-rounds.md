# vllm-project/vllm#27084: [RFC]: Add vllm benchs subcommand to benchmark test  multiple rounds

| 字段 | 值 |
| --- | --- |
| Issue | [#27084](https://github.com/vllm-project/vllm/issues/27084) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add vllm benchs subcommand to benchmark test  multiple rounds

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Current `vllm bench serve` command only benchmark test one time account user set param, but same time we hope can get a performance curve, go through multiple rounds benchmark test after. e.g: i hope got a input_length is variable, ttft is result of relationship curve. So, we can add a new subcommand `vllm benchs`, it can set we need how many rounds, and set horizontal and vertical axis and other param. like: ``` $ -m vllm.entrypoints.cli.main benchs --model Qwen/Qwen3-0.6B --step 5 --horizontal-axis input-length --vertical-axis ttft --step-start 10 --step-interval 100 --result plot --backend openai --base-url http://localhost:8000 ``` Then it can exec `vllm bench serve` ten number, after got a plot. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: . e.g: i hope got a input_length is variable, ttft is result of relationship curve. So, we can add a new subcommand `vllm benchs`, it can set we need how many rounds, and set horizontal and vertical axis and other param...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: axis and other param. like: ``` $ -m vllm.entrypoints.cli.main benchs --model Qwen/Qwen3-0.6B --step 5 --horizontal-axis input-length --vertical-axis ttft --step-start 10 --step-interval 100 --result plot --backend open...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [RFC]: Add vllm benchs subcommand to benchmark test multiple rounds feature request ### 🚀 The feature, motivation and pitch Current `vllm bench serve` command only benchmark test one time account user set param, but sam...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: --vertical-axis ttft --step-start 10 --step-interval 100 --result plot --backend openai --base-url http://localhost:8000 ``` Then it can exec `vllm bench serve` ten number, after got a plot. ### Alternatives _No respons...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Add vllm benchs subcommand to benchmark test multiple rounds feature request ### 🚀 The feature, motivation and pitch Current `vllm bench serve` command only benchmark test one time account user set param, but same ti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
