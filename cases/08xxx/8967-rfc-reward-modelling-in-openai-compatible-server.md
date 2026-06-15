# vllm-project/vllm#8967: [RFC]: Reward Modelling in OpenAI Compatible Server

| 字段 | 值 |
| --- | --- |
| Issue | [#8967](https://github.com/vllm-project/vllm/issues/8967) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Reward Modelling in OpenAI Compatible Server

### Issue 正文摘录

### Motivation. Reward models are an important tool in NLP / AI workflows, especially in agentic flows which use them to verify quality of intermediate outputs, or rank between several attempts at performing a single task. vLLM just added support for a reward model in https://github.com/vllm-project/vllm/pull/8896#issuecomment-2381912003 . This requires a workaround in order to work with the OpenAI Compatible Server - it piggybacks the embedding endpoint. The workaround requires the client to know which tokenizer is being used by the server, apply the chat template to the conversation, and send the resulting string to the embedding endpoint. This isn't ideal and it breaks the decoupling between the client and server. A short discussion in the same issue led to the creation of the RFC. ### Proposed Change. The reason that no endpoint currently matches the needs of the reward model is as follows: - The embedding endpoint receives a string as the input, not a conversation - The chat endpoint returns a string, not a series of numbers. Even if you ask for logprobs, they are after softmax was applied, which is not a reversable process. I see several ways to more elegantly support reward...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ng in OpenAI Compatible Server RFC ### Motivation. Reward models are an important tool in NLP / AI workflows, especially in agentic flows which use them to verify quality of intermediate outputs, or rank between several...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: me! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [RFC]: Reward Modelling in OpenAI Compatible Server RFC ### Motivation. Reward models are an important tool in NLP / AI workflows, especially in agentic flows which use them to verify quality of intermediate outputs, or...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sation object (`List[Dict[str, str]]`) as a potential input to `EmbeddingRequest` class. It already supports a variety of options: ``` input: Union[List[int], List[List[int]], str, List[str]]``` Upon detecting that a co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
