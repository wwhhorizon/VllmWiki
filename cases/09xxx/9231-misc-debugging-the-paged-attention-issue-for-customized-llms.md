# vllm-project/vllm#9231: [Misc]: Debugging the paged attention issue for customized LLMs

| 字段 | 值 |
| --- | --- |
| Issue | [#9231](https://github.com/vllm-project/vllm/issues/9231) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Debugging the paged attention issue for customized LLMs

### Issue 正文摘录

### Anything you want to discuss about vllm. I am trying to add a proprietary model (a pretty standard LLM with hf model.py) to VLLM, I finished the porting script but the generation results does not match and goes terribly wrong. Then I start to comparing the output of the VLLM model and the HF model side by side. I noticed that everything is correct except when calling the `flash_attn_with_kvcache` function. This is very strange behavior since the result of `flash_attn_varlen_func` function call does match the HF output. Let's say you have a prompt ABC, and HF model completes it with DEF. If you run the prompt on VLLM model, the first generated result is D, but then with some random stuff. If you change prompt to ABCD, VLLM can generate E correctly and then followed with random stuff. It seems the qkv passed into `FlashAttentionImpl.forward()` all matches the HF values. Seems to me the kv cache stored in the paged attention has something wrong. Any ideas on how to debug this issue? Currently I am having difficult to slice the correct indices from the paged attention data (kv_cache). I know I can use `block_tables' to select the block, but now sure how to select the relevant data...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ything you want to discuss about vllm. I am trying to add a proprietary model (a pretty standard LLM with hf model.py) to VLLM, I finished the porting script but the generation results does not match and goes terribly w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ectly and then followed with random stuff. It seems the qkv passed into `FlashAttentionImpl.forward()` all matches the HF values. Seems to me the kv cache stored in the paged attention has something wrong. Any ideas on...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _values, what would be the possible issues? Any help would be much appreciated. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: FlashAttentionImpl.forward()` all matches the HF values. Seems to me the kv cache stored in the paged attention has something wrong. Any ideas on how to debug this issue? Currently I am having difficult to slice the cor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
