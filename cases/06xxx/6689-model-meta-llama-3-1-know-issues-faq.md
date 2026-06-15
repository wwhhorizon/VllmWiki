# vllm-project/vllm#6689: [Model] Meta Llama 3.1 Know Issues & FAQ

| 字段 | 值 |
| --- | --- |
| Issue | [#6689](https://github.com/vllm-project/vllm/issues/6689) |
| 状态 | closed |
| 标签 |  |
| 评论 | 85; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Model] Meta Llama 3.1 Know Issues & FAQ

### Issue 正文摘录

## Please checkout [Announcing Llama 3.1 Support in vLLM](https://blog.vllm.ai/2024/07/23/llama31.html) ## * Chunked prefill is turned on for all Llama 3.1 models. However, it is currently incompatible with prefix caching, sliding window, and multi-lora. In order to use those features, you can set `--enable-chunked-prefill=false` then optionally combine it with `--max-model-len=4096` if turning it out cause OOM. You can change the length for the context window you desired. * Rope scaling `if rope_scaling is not None and rope_scaling["type"] not in, KeyError: 'type'.` * Please update to [v0.5.3.post1](https://github.com/vllm-project/vllm/releases/tag/v0.5.3.post1) which included a fix. * Rope scaling `ValueError: 'rope_scaling' must be a dictionary with two fields, 'type' and 'factor', got {'factor': 8.0, 'low_freq_factor': 1.0, 'high_freq_factor': 4.0, 'original_max_position_embeddings': 8192, 'rope_type': 'llama3'}` * Please upgrade transformers to 4.43.1 (`pip install transformers --upgrade`) * Using a per-request random seed currently does not work with pipeline parallel deployments (https://github.com/vllm-project/vllm/issues/6449). This will be fixed soon. UPDATE: [`meta-llam...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Model] Meta Llama 3.1 Know Issues & FAQ ## Please checkout [Announcing Llama 3.1 Support in vLLM](https://blog.vllm.ai/2024/07/23/llama31.html) ## * Chunked prefill is turned on for all Llama 3.1 models. However, it is
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Model] Meta Llama 3.1 Know Issues & FAQ ## Please checkout [Announcing Llama 3.1 Support in vLLM](https://blog.vllm.ai/2024/07/23/llama31.html) ## * Chunked prefill is turned on for all Llama 3.1 models. However, it is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ort in vLLM](https://blog.vllm.ai/2024/07/23/llama31.html) ## * Chunked prefill is turned on for all Llama 3.1 models. However, it is currently incompatible with prefix caching, sliding window, and multi-lora. In order...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s will be fixed soon. UPDATE: [`meta-llama/Meta-Llama-3.1-405B-Instruct-FP8`](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct-FP8) model repository has been fixed with the correct number of kv heads. Plea...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ptionally combine it with `--max-model-len=4096` if turning it out cause OOM. You can change the length for the context window you desired. * Rope scaling `if rope_scaling is not None and rope_scaling["type"] not in, Ke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
