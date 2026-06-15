# vllm-project/vllm#1571: a possible improvement for gpu memory cache in llama

| 字段 | 值 |
| --- | --- |
| Issue | [#1571](https://github.com/vllm-project/vllm/issues/1571) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> a possible improvement for gpu memory cache in llama

### Issue 正文摘录

in short: add "` torch.cuda.empty_cache()`" at last of `LlamaDecoderLayer.forward()` may help lessen the temporary gpu cache when model forwarding. ___ i'm using llama of vllm for inferencing and i was confused by the large memory usage shown in nvidia-smi. it always happened in `worker.profile_num_available_blocks()` when initializing, which may use out 35+gb memory, but not didnt bother too much on runtime. after checking cuda memory status(using `torch.cuda.max_memory_reserved()`) step by step, i found there is an increasing cuda cache each time after `LlamaDecoderLayer.forward()`. in my opinion this part of increased cache may be caused by the mlp in layer, and if true, this cache won't be used again and ` torch.cuda.empty_cache()` here can help lessen the memory while not slow down the forward process. change( vllm/model_executor/models/llama.py line 217 started) # Fully Connected residual = hidden_states hidden_states = self.post_attention_layernorm(hidden_states) hidden_states = self.mlp(hidden_states) hidden_states = residual + hidden_states return hidden_states to # Fully Connected residual = hidden_states hidden_states = self.post_attention_layernorm(hidden_states) hidde...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: gpu cache when model forwarding. ___ i'm using llama of vllm for inferencing and i was confused by the large memory usage shown in nvidia-smi. it always happened in `worker.profile_num_available_blocks()` when initializ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ossible improvement for gpu memory cache in llama in short: add "` torch.cuda.empty_cache()`" at last of `LlamaDecoderLayer.forward()` may help lessen the temporary gpu cache when model forwarding. ___ i'm using llama o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a possible improvement for gpu memory cache in llama in short: add "` torch.cuda.empty_cache()`" at last of `LlamaDecoderLayer.forward()` may help lessen the temporary gpu cache when model forwarding. ___ i'm using llam...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: a possible improvement for gpu memory cache in llama in short: add "` torch.cuda.empty_cache()`" at last of `LlamaDecoderLayer.forward()` may help lessen the temporary gpu cache when model forwarding. ___ i'm using llam...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: shown in nvidia-smi. it always happened in `worker.profile_num_available_blocks()` when initializing, which may use out 35+gb memory, but not didnt bother too much on runtime. after checking cuda memory status(using `to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
