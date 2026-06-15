# vllm-project/vllm#7397: [Misc]: Cross-attention QKV computation is inefficient

| 字段 | 值 |
| --- | --- |
| Issue | [#7397](https://github.com/vllm-project/vllm/issues/7397) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Cross-attention QKV computation is inefficient

### Issue 正文摘录

This issue is not in response to a performance regression. The method of performing cross-attention QKV computations introduced in #4942 could be improved. Because this issue relates to cross-attention, it only impacts encoder/decoder models, not decoder-only models. For context, `QKVParallelLinear` computes QKV from the previous decoder layer's hidden state output, i.e. only a single input. The problem is that cross attention requires QKV to be computed from two inputs: Q must be computed from the previous decoder layer's hidden state output, and KV must be computed from the encoder's output hidden states. Additionally, * During prefill phase, both Q and KV must be computed * During decode phase, only Q is computed because the encoder sequence is static so there are no new encoder KVs The current, inefficient workaround for cross-attention is to construct a `QKVParallelLinear` layer & apply it at most 2 times in a given run of the cross-attention `forward()` method: once to `decoder_hidden_states` to obtain Q, and (only during prefill) a second time to `encoder_hidden_states` to obtain KV: ``` # (afeldman-nm 2024/07/22) TODO: # Need a more efficient solution for q/k/v qkv_dec, _...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Misc]: Cross-attention QKV computation is inefficient stale This issue is not in response to a performance regression. The method of performing cross-attention QKV computations introduced in #4942 could be improved. Be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Misc]: Cross-attention QKV computation is inefficient stale This issue is not in response to a performance regression. The method of performing cross-attention QKV computations introduced in #4942 could be improved. Be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: to `QKVParallelLinear` with the following properties * Exploits parallelism over multiple GPUs * `forward()` takes a decoder hidden states argument, and an optional encoder hidden states argument * `forward()` always co...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: dim=-1) if encoder_hidden_states is None: k = None v = None else: qkv_enc, _ = self.qkv_proj(encoder_hidden_states) _, k, v = qkv_enc.split([self.q_size, self.kv_size, self.kv_size], dim=-1) ``` ## Cost breakdown of the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e this issue relates to cross-attention, it only impacts encoder/decoder models, not decoder-only models. For context, `QKVParallelLinear` computes QKV from the previous decoder layer's hidden state output, i.e. only a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
