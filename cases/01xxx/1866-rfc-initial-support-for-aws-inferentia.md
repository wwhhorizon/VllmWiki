# vllm-project/vllm#1866: [RFC] Initial Support for AWS Inferentia

| 字段 | 值 |
| --- | --- |
| Issue | [#1866](https://github.com/vllm-project/vllm/issues/1866) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;model_support;sampling_logits |
| 子分类 | install |
| Operator 关键词 | cache;cuda;kernel |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] Initial Support for AWS Inferentia

### Issue 正文摘录

## Proposal We propose to integrate transformers-neuronx to be the execution engine in vLLM for supporting LLM inference on Inferentia. This would require changes on both transformers-neuronx and vLLM. ### Changes to transformers-neuronx 1. Support batch size 1 prompt encoding, while share same cache space with max batch size decoding. 2. Support batch-dependent KV cache update. Each sequence will have a specified position_id to update cache. 3. Support virtual dynamic batching. This would enable multi-batch prompt encoding virtually agnostic to vLLM. ### Changes to vLLM - [x] Make CUDA kernel compilation optional, so that when we are trying to perform LLM inference on inf2 instances we don’t necessarily compile the CUDA kernels. Meanwhile, we would still keep CUDA kernel compilation enabled by default. https://github.com/vllm-project/vllm/pull/2065 - [x] Add transformers-neuronx package as a (optional) thirdparty dependency of vllm. Note that transformers-neuronx would further depend on torch-neuronx, torch-xla, neuronx-cc and many others. https://github.com/vllm-project/vllm/pull/2065 - [x] Configure transformers-neuronx to enable continuous batching feature in vLLM model loader...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 2. Support batch-dependent KV cache update. Each sequence will have a specified position_id to update cache. 3. Support virtual dynamic batching. This would enable multi-batch prompt encoding virtually agnostic to vLLM....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: or, positions: torch.Tensor, kv_caches: List[KVCache], input_metadata: InputMetadata, cache_events: Optional[List[torch.cuda.Event]], ) -> SamplerOutput: batch_size, n_active_tokens = input_ids.shape with torch.inferenc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: cc and many others. https://github.com/vllm-project/vllm/pull/2065 - [x] Configure transformers-neuronx to enable continuous batching feature in vLLM model loader. https://github.com/vllm-project/vllm/pull/2569 - [x] Co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: t_metadata.num_prompts seq_ids = torch.zeros(num_prompts, 1, dtype=torch.int64, device='cpu') anchor = 0 for prompt_id in range(num_prompts): seq_ids[prompt_id] = input_metadata.slot_mapping[anchor] // block_size anchor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pt encoding virtually agnostic to vLLM. ### Changes to vLLM - [x] Make CUDA kernel compilation optional, so that when we are trying to perform LLM inference on inf2 instances we don’t necessarily compile the CUDA kernel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
