# vllm-project/vllm#8441: [Usage]: Batching in online inference

| 字段 | 值 |
| --- | --- |
| Issue | [#8441](https://github.com/vllm-project/vllm/issues/8441) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Batching in online inference

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I have set up an API server through the command: `docker pull vllm/vllm-openai:v0.5.3.post1`. The server is running fine when I am giving requests through normal curl commands i.e. one request at a time. But I want vLLM to process requests(assuming one prompt per request) parallelly in the specified batch size. Right now I don't know the batch size in which vLLM internally processes the prompts. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: you like to use vllm I have set up an API server through the command: `docker pull vllm/vllm-openai:v0.5.3.post1`. The server is running fine when I am giving requests through normal curl commands i.e. one request at a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: m/vllm-openai:v0.5.3.post1`. The server is running fine when I am giving requests through normal curl commands i.e. one request at a time. But I want vLLM to process requests(assuming one prompt per request) parallelly...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
