# vllm-project/vllm#13409: [Feature]: Prompt logprobs + APC compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#13409](https://github.com/vllm-project/vllm/issues/13409) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Prompt logprobs + APC compatibility

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [#9880](https://github.com/vllm-project/vllm/pull/9880) adds sample and prompt logprobs support, however prompt logprobs currently require the server to be instantiated with `--no-enable-prefix-caching`; otherwise, a request with `prompt_logprobs=true` will cause the request to fail with the message "Prefix caching with prompt logprobs not yet supported on VLLM V1." The challenge of using prompt logprobs alongside APC is how to recover the topk prompt logprobs from an APC cache hit. The existing APC implementation does not cache prompt logprobs; upon a cache hit, cached blocks are treated as "computed" & no prompt logprobs are available for the computed blocks. ### Alternatives A few possible solutions: * **Use APC cached KVs to recompute prompt logprobs if a request with `prompt_logprobs=true` triggers an APC cache hit.** This requires model code and `model_executor` code to support re-running prefill using cached KVs. * **Cache prompt logprobs in the APC.** The problem with this solution is that a request which triggers an APC cache hit may require a greater number of topk prompt logprobs than the request which filled the cache, in which c...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Prompt logprobs + APC compatibility feature request ### 🚀 The feature, motivation and pitch [#9880](https://github.com/vllm-project/vllm/pull/9880) adds sample and prompt logprobs support, however prompt logp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: obs alongside APC is how to recover the topk prompt logprobs from an APC cache hit. The existing APC implementation does not cache prompt logprobs; upon a cache hit, cached blocks are treated as "computed" & no prompt l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: implementation does not cache prompt logprobs; upon a cache hit, cached blocks are treated as "computed" & no prompt logprobs are available for the computed blocks. ### Alternatives A few possible solutions: * **Use APC...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t with `prompt_logprobs=true` triggers an APC cache hit.** This requires model code and `model_executor` code to support re-running prefill using cached KVs. * **Cache prompt logprobs in the APC.** The problem with this...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
