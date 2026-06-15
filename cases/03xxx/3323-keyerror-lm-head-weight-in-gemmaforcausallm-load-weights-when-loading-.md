# vllm-project/vllm#3323: KeyError: lm_head.weight in GemmaForCausalLM.load_weights when loading finetuned Gemma 2B

| 字段 | 值 |
| --- | --- |
| Issue | [#3323](https://github.com/vllm-project/vllm/issues/3323) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> KeyError: lm_head.weight in GemmaForCausalLM.load_weights when loading finetuned Gemma 2B

### Issue 正文摘录

Hello, I finetuned Gemma 2B with [Unsloth](https://github.com/unslothai/unsloth). It uses LoRA and merges the weights back into the base model. When I try to load this model, it gives me the following error: ``` ... File "/home/ubuntu/projects/cql-ml/.venv/lib/python3.10/site-packages/vlm/model_executor/model_loader.py", line 86, in get _model model. load weights(model_config.model, model_config.download_ config. model, model_ config. download dir, File "/home/ubuntu/projects/cql-ml/.venv/lib/python3.10/site-packages/vlm/model_executor/models/gemma.py", line 339, in load weights param = params_dict [name] KeyError: 'lm_head.weight' ``` My `pytorch_model.bin.index.json` looks like this: ``` { "metadata": { "total_size": 6060920832 }, "weight_map": { "lm_head.weight": "pytorch_model-00002-of-00002.bin", "model.embed_tokens.weight": "pytorch_model-00001-of-00002.bin", "model.layers.0.input_layernorm.weight": "pytorch_model-00001-of-00002.bin", "model.layers.0.mlp.down_proj.weight": "pytorch_model-00001-of-00002.bin", "model.layers.0.mlp.gate_proj.weight": "pytorch_model-00001-of-00002.bin", ... ``` I saw in a few of the other classes a similar check for `lm_head.weight` so I replicat...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: KeyError: lm_head.weight in GemmaForCausalLM.load_weights when loading finetuned Gemma 2B Hello, I finetuned Gemma 2B with [Unsloth](https://github.com/unslothai/unsloth). It uses LoRA and merges the weights back into t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: hts when loading finetuned Gemma 2B Hello, I finetuned Gemma 2B with [Unsloth](https://github.com/unslothai/unsloth). It uses LoRA and merges the weights back into the base model. When I try to load this model, it gives...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: what the internals of the model should look like. Any help would be appreciated! I'm unsure if this is related to https://github.com/vllm-project/vllm/issues/2816 My model is Private, so unfortunately I can't share it....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ob/4c922709b65ff5c0652ae36b93047016bdeaace8/vllm/model_executor/models/bloom.py#L306) [2]([vllm/model_executor/models/gpt_bigcode.py](https://github.com/vllm-project/vllm/blob/4c922709b65ff5c0652ae36b93047016bdeaace8/vl...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: KeyError: lm_head.weight in GemmaForCausalLM.load_weights when loading finetuned Gemma 2B Hello, I finetuned Gemma 2B with [Unsloth](https://github.com/unslothai/unsloth). It uses LoRA and merges the weights back into t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
