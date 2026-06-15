# vllm-project/vllm#41841: Stale padded request metadata can misclassify Mamba CUDA graph rows

| 字段 | 值 |
| --- | --- |
| Issue | [#41841](https://github.com/vllm-project/vllm/issues/41841) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Stale padded request metadata can misclassify Mamba CUDA graph rows

### Issue 正文摘录

### Summary Full CUDA graph metadata can include stale CPU request-state values for padded rows. For Mamba backends this can make padding rows look like prefills, so a decode-only CUDA graph replay can be classified as mixed decode/prefill metadata. The relevant path is: - `GPUModelRunner._build_attention_metadata` slices `num_computed_tokens_cpu_tensor[:num_reqs_padded]` and `num_prompt_tokens_cpu_tensor[:num_reqs_padded]`. - Other padded metadata is explicitly neutralized, e.g. padded block table entries are filled with `NULL_BLOCK_ID` and padded sequence lengths are zeroed. - The request-state tensors are not neutralized beyond `num_reqs`. - `is_prefilling = num_computed_tokens_cpu num_reqs`, clone and zero `num_computed_tokens_cpu` and `num_prompt_tokens_cpu` for padded rows before computing `is_prefilling`.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Stale padded request metadata can misclassify Mamba CUDA graph rows ### Summary Full CUDA graph metadata can include stale CPU request-state values for padded rows. For Mamba backends this can make padding rows look lik
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ixed decode/prefill metadata. The relevant path is: - `GPUModelRunner._build_attention_metadata` slices `num_computed_tokens_cpu_tensor[:num_reqs_padded]` and `num_prompt_tokens_cpu_tensor[:num_reqs_padded]`. - Other pa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Stale padded request metadata can misclassify Mamba CUDA graph rows ### Summary Full CUDA graph metadata can include stale CPU request-state values for padded rows. For Mamba backends this can make padding rows look lik...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ta can include stale CPU request-state values for padded rows. For Mamba backends this can make padding rows look like prefills, so a decode-only CUDA graph replay can be classified as mixed decode/prefill metadata. The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Stale padded request metadata can misclassify Mamba CUDA graph rows ### Summary Full CUDA graph metadata can include stale CPU request-state values for padded rows. For Mamba backends this can make padding rows look lik...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
