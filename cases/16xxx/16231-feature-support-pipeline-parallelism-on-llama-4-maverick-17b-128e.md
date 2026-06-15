# vllm-project/vllm#16231: [Feature]: Support Pipeline Parallelism on Llama-4-Maverick-17B-128E

| 字段 | 值 |
| --- | --- |
| Issue | [#16231](https://github.com/vllm-project/vllm/issues/16231) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Pipeline Parallelism on Llama-4-Maverick-17B-128E

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm attempting to deploy Llama-4-Maverick-17B-128E across 16 H100s on two nodes, running this command: ``` python3 -m vllm.entrypoints.openai.api_server --port 8080 --model meta-llama/Llama-4-Maverick-17B-128E-Instruct --tensor-parallel-size 8 --pipeline-parallel-size 2 ``` I got this message saying that PP isn't supported ``` NotImplementedError: Pipeline parallelism is not supported for this model. Supported models implement the `SupportsPP` interface. ``` Llama-4-Maverick-17B-128E is a large LLM that most people will be running across multiple GPU nodes. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Support Pipeline Parallelism on Llama-4-Maverick-17B-128E feature request ### 🚀 The feature, motivation and pitch I'm attempting to deploy Llama-4-Maverick-17B-128E across 16 H100s on two nodes, running this...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support Pipeline Parallelism on Llama-4-Maverick-17B-128E feature request ### 🚀 The feature, motivation and pitch I'm attempting to deploy Llama-4-Maverick-17B-128E across 16 H100s on two nodes, running this...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ture]: Support Pipeline Parallelism on Llama-4-Maverick-17B-128E feature request ### 🚀 The feature, motivation and pitch I'm attempting to deploy Llama-4-Maverick-17B-128E across 16 H100s on two nodes, running this comm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
