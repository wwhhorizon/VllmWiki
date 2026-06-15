# vllm-project/vllm#16602: [Bug]: vllm docker inage miss benchmarks dir

| 字段 | 值 |
| --- | --- |
| Issue | [#16602](https://github.com/vllm-project/vllm/issues/16602) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm docker inage miss benchmarks dir

### Issue 正文摘录

### Your current environment This sh it need benchmarks file ,but in docker image is not exist. https://github.com/vllm-project/vllm/blob/1dd23386ecab7b7c50ea61b8ff37ca14d2dbc0f7/examples/online_serving/disaggregated_prefill.sh#L79 ### 🐛 Describe the bug no ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: vllm docker inage miss benchmarks dir bug ### Your current environment This sh it need benchmarks file ,but in docker image is not exist. https://github.com/vllm-project/vllm/blob/1dd23386ecab7b7c50ea61b8ff37ca14...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: vllm docker inage miss benchmarks dir bug ### Your current environment This sh it need benchmarks file ,but in docker image is not exist. https://github.com/vllm-project/vllm/blob/1dd23386ecab7b7c50ea61b8ff37ca14...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: no ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 86ecab7b7c50ea61b8ff37ca14d2dbc0f7/examples/online_serving/disaggregated_prefill.sh#L79 ### 🐛 Describe the bug no ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
