# vllm-project/vllm#26934: [RFC][ResponsesAPI]: Separating State & Providing Flexibility for serving ResponsesAPI

| 字段 | 值 |
| --- | --- |
| Issue | [#26934](https://github.com/vllm-project/vllm/issues/26934) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][ResponsesAPI]: Separating State & Providing Flexibility for serving ResponsesAPI

### Issue 正文摘录

# Motivation. A lot of recent work has been done in vLLM, after the launch of GPT-OSS, to support serving GPTOSS and responsesAPI. ResponsesAPI was introduced by OpenAI in March 2025 as a new API, which has better state management. **State management** is becoming more essential as we move towards longer turn LLM agentic flows. We should note that there are 2 user personas who use vLLM: 1. **Large scale production traffic**: this is us at Meta. With many industry use cases, the [api_server](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/api_server.py) in vLLM is not the entrypoint into using vLLM. Separate components outside of the scope of vLLM will be responsible for being the API layer and manage other parts of LLM inference such as state management. The expectation of vLLM as an inference engine is that it should be stateless, and simply function as tokens in, tokens out. 2. **Researchers / small-scale products**. For this, the current implementation of state in vLLM is probably fine, as vLLM functions as an end to end inference engine (with API server, state management, etc all included). There are two main points in vLLM that we've noticed: 1. vLLM is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ill handle retrieveResponses from its state store. This will improve efficiency of the system overall, as retrieveResponses will no longer hit the node serving the LLM (with GPUs being a scarce resource). ## provide an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rving GPTOSS and responsesAPI. ResponsesAPI was introduced by OpenAI in March 2025 as a new API, which has better state management. **State management** is becoming more essential as we move towards longer turn LLM agen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vation. A lot of recent work has been done in vLLM, after the launch of GPT-OSS, to support serving GPTOSS and responsesAPI. ResponsesAPI was introduced by OpenAI in March 2025 as a new API, which has better state manag...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Separating State & Providing Flexibility for serving ResponsesAPI RFC;unstale # Motivation. A lot of recent work has been done in vLLM, after the launch of GPT-OSS, to support serving GPTOSS and responsesAPI. ResponsesA...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: We should note that there are 2 user personas who use vLLM: 1. **Large scale production traffic**: this is us at Meta. With many industry use cases, the [api_server](https://github.com/vllm-project/vllm/blob/main/vllm/e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
