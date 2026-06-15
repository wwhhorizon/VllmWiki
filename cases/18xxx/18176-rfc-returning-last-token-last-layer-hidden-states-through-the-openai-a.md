# vllm-project/vllm#18176: [RFC]: Returning Last Token, Last Layer Hidden States Through The OpenAI API

| 字段 | 值 |
| --- | --- |
| Issue | [#18176](https://github.com/vllm-project/vllm/issues/18176) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Returning Last Token, Last Layer Hidden States Through The OpenAI API

### Issue 正文摘录

### Motivation. As a distributed inference provider, we use vLLM because it is fast, has cutting edge capabilities, and is well-maintained. We serve millions of inference requests per day, all using the OpenAI API format. Because we run a distributed network, we need to verify that our operators ran the model that was requested (and did not substitute some smaller model or use a canned response). [TopLOC](https://arxiv.org/pdf/2501.16007) is a very robust inference verification technique. However, TopLOC requires the last layer's hidden states for a single token (typically the last token) of the response, something that isn't exposed through the OpenAI API. Rather than rebuilding an entire API stack, we'd love to leverage vLLM's OpenAI API by incorporating the ability to return the last layer's hidden states, but specifically for the last token only. Then, we will be able to easily implement TopLOC verification as part of our network. Please note that this is a different use case from mechaninterp. ### Proposed Change. We are proposing the following schema changes: * ServerArgs: Add `return_hidden_states` to turn the feature on at the engine level. **`ChatCompletionResponseChoice`...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e serve millions of inference requests per day, all using the OpenAI API format. Because we run a distributed network, we need to verify that our operators ran the model that was requested (and did not substitute some s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nse, something that isn't exposed through the OpenAI API. Rather than rebuilding an entire API stack, we'd love to leverage vLLM's OpenAI API by incorporating the ability to return the last layer's hidden states, but sp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: operators ran the model that was requested (and did not substitute some smaller model or use a canned response). [TopLOC](https://arxiv.org/pdf/2501.16007) is a very robust inference verification technique. However, Top...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eturning Last Token, Last Layer Hidden States Through The OpenAI API RFC;stale ### Motivation. As a distributed inference provider, we use vLLM because it is fast, has cutting edge capabilities, and is well-maintained....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
