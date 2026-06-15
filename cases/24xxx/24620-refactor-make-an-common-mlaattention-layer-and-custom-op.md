# vllm-project/vllm#24620: [Refactor]: Make an common MLAAttention Layer and custom OP

| 字段 | 值 |
| --- | --- |
| Issue | [#24620](https://github.com/vllm-project/vllm/issues/24620) |
| 状态 | closed |
| 标签 | help wanted |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Refactor]: Make an common MLAAttention Layer and custom OP

### Issue 正文摘录

One long term overarching goal is to refactor different attention types into their own dedicated layer implementations that are a subclass [AttentionLayerBase](https://github.com/vllm-project/vllm/blob/cc99baf14dacc2497d0c5ed84e076ef2c37f6a4d/vllm/model_executor/layers/attention_layer_base.py#L11), e.g. currently we have the subclasses [MambaBase](https://github.com/vllm-project/vllm/blob/cc99baf14dacc2497d0c5ed84e076ef2c37f6a4d/vllm/model_executor/layers/mamba/abstract.py#L15) and [Attention](https://github.com/vllm-project/vllm/blob/cc99baf14dacc2497d0c5ed84e076ef2c37f6a4d/vllm/attention/layer.py#L58C7-L58C16). Currently `Attention` implements both MLA and the more standard MHA/GQA/MQA schemes; we should separate out MLA into its own `AttentionLayerBase` subclass using the existing [MultiHeadLatentAttention](https://github.com/vllm-project/vllm/blob/cc99baf14dacc2497d0c5ed84e076ef2c37f6a4d/vllm/model_executor/layers/mla.py#L30) This will have a few material benefits: 1) will allow us to drop the [use_mla](https://github.com/vllm-project/vllm/blob/cc99baf14dacc2497d0c5ed84e076ef2c37f6a4d/vllm/attention/layer.py#L81) flag from Attention 2) will allow us to have a separate backend...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: an common MLAAttention Layer and custom OP help wanted One long term overarching goal is to refactor different attention types into their own dedicated layer implementations that are a subclass [AttentionLayerBase](http...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ope` and `q_rope` independently instead of concatenated 5) look at move decode and prefill splitting into the `torch.compile`d section - by using a new dynamic shape (returned from a new custom op) for `n_decode_tokens`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: on/layer.py#L81) flag from Attention 2) will allow us to have a separate backend selector for MLA backends separate from that or the MHA/GQA/MQA (like we have for Mamba) 3) will allow use to pull `concat_and_cache_mla`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ncatenated 5) look at move decode and prefill splitting into the `torch.compile`d section - by using a new dynamic shape (returned from a new custom op) for `n_decode_tokens`, we could unwrap the decode/prefill batch sp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/cc99baf14dacc2497d0c5ed84e076ef2c37f6a4d/vllm/model_executor/layers/attention_layer_base.py#L11), e.g. currently we have the subclasses [MambaBase](https://github.com/vllm-project/vllm/blob/cc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
