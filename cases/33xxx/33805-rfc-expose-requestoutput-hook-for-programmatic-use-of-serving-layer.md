# vllm-project/vllm#33805: [RFC]: Expose RequestOutput hook for programmatic use of Serving layer

| 字段 | 值 |
| --- | --- |
| Issue | [#33805](https://github.com/vllm-project/vllm/issues/33805) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Expose RequestOutput hook for programmatic use of Serving layer

### Issue 正文摘录

### Motivation. As chat formats for LLMs and APIs for LLMs get more complicated, there is logic that is critical to model correctness and performance that lives in the serving layer. The best example of this is the gpt-oss + harmony + responses API implementation in vLLM. It is critical that these APIs match the public API spec exactly, or else they will not work seamlessly in applications or agentic harnesses like Codex or Claude Code. By matching the public API spec exactly, vLLM now only returns a subset of information about what was generated, instead of the full sequence. For example, for gpt-oss, messages generated on the analysis channel are not meant to be shown to users. If this is the case it will generate an assistant message on the commentary channel that, unlike the chain-of-thought, is intended to be shown to the end-user. However, this obfuscation also prevents production deployments of vLLM which wrap interfaces like OpenAIServingResponses.create_responses() from accessing this information as well. This creates friction when using ResponsesAPI in production. For example, to properly capture engine metrics when using ResponsesAPI, they would have to add those metric...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: for programmatic use of Serving layer RFC;stale ### Motivation. As chat formats for LLMs and APIs for LLMs get more complicated, there is logic that is critical to model correctness and performance that lives in the ser...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: M. It is critical that these APIs match the public API spec exactly, or else they will not work seamlessly in applications or agentic harnesses like Codex or Claude Code. By matching the public API spec exactly, vLLM no...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Expose RequestOutput hook for programmatic use of Serving layer RFC;stale ### Motivation. As chat formats for LLMs and APIs for LLMs get more complicated, there is logic that is critical to model correctness and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
