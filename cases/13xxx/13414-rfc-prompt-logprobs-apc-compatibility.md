# vllm-project/vllm#13414: [RFC]: Prompt logprobs + APC compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#13414](https://github.com/vllm-project/vllm/issues/13414) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Prompt logprobs + APC compatibility

### Issue 正文摘录

### Motivation. Porting logprobs support to v1 was key for completeness. APC is an important performance optimization. [#9880](https://github.com/vllm-project/vllm/pull/9880) adds sample and prompt logprobs support, however prompt logprobs currently require the server to be instantiated with `--no-enable-prefix-caching`; otherwise, a request with `prompt_logprobs=true` will cause the request to fail with the message "Prefix caching with prompt logprobs not yet supported on VLLM V1." The challenge of using prompt logprobs alongside APC is how to recover the topk prompt logprobs from an APC cache hit. The existing APC implementation does not cache prompt logprobs; upon a cache hit, cached blocks are treated as "computed" & no prompt logprobs are available for the computed blocks. ### Proposed Choices for Implementation 1. **Use APC cached KVs to recompute prompt logprobs if a request with `prompt_logprobs=true` triggers an APC cache hit.** This requires model code and `model_executor` code to support re-running prefill using cached KVs. 2. **Cache prompt logprobs in the APC.** The problem with this solution is that a request which triggers an APC cache hit may require a greater numb...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: erver to be instantiated with `--no-enable-prefix-caching`; otherwise, a request with `prompt_logprobs=true` will cause the request to fail with the message "Prefix caching with prompt logprobs not yet supported on VLLM...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: obs alongside APC is how to recover the topk prompt logprobs from an APC cache hit. The existing APC implementation does not cache prompt logprobs; upon a cache hit, cached blocks are treated as "computed" & no prompt l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ion. Porting logprobs support to v1 was key for completeness. APC is an important performance optimization. [#9880](https://github.com/vllm-project/vllm/pull/9880) adds sample and prompt logprobs support, however prompt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: implementation does not cache prompt logprobs; upon a cache hit, cached blocks are treated as "computed" & no prompt logprobs are available for the computed blocks. ### Proposed Choices for Implementation 1. **Use APC c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
