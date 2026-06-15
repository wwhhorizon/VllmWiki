# vllm-project/vllm#20798: [Usage]: How to implement request abortion in vLLM OpenAI API Server?​

| 字段 | 值 |
| --- | --- |
| Issue | [#20798](https://github.com/vllm-project/vllm/issues/20798) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to implement request abortion in vLLM OpenAI API Server?​

### Issue 正文摘录

### Your current environment ```text I’m deploying vLLM’s OpenAI-compatible API server (python -m vllm.entrypoints.openai.api_server) for real-time inference. In production, users may need to ​​cancel long-running requests​​ (e.g., closing a chat session). However, the official documentation lacks details on interrupting ongoing inference tasks via the API. Can I implement an endpoint (e.g., POST /v1/completions/{request_id}/cancel) to ​​terminate a specific inference request​​ mid-generation, freeing GPU resources immediately？ please give me some advice ``` ### How would you like to use vllm I want to abort a request inference of a [qwen3:8b]. I don't know how to do with the api with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to implement request abortion in vLLM OpenAI API Server?​ usage;stale ### Your current environment ```text I’m deploying vLLM’s OpenAI-compatible API server (python -m vllm.entrypoints.openai.api_server) fo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: long-running requests​​ (e.g., closing a chat session). However, the official documentation lacks details on interrupting ongoing inference tasks via the API. Can I implement an endpoint (e.g., POST /v1/completions/{req...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ow would you like to use vllm I want to abort a request inference of a [qwen3:8b]. I don't know how to do with the api with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
