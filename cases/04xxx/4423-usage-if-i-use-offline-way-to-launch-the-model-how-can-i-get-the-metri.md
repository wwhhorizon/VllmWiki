# vllm-project/vllm#4423: [Usage]: If I use Offline way to launch the model, how can I get the metrics?

| 字段 | 值 |
| --- | --- |
| Issue | [#4423](https://github.com/vllm-project/vllm/issues/4423) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;quantization;sampling |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: If I use Offline way to launch the model, how can I get the metrics?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I use `xinference` to launch model `Qwen1.5-chat`, it use `vllm` in its origin code. ``` 2024-04-28 03:36:06,220 xinference.model.llm.core 3456676 DEBUG Launching qwen1.5-chat-1-0 with VLLMChatModel 2024-04-28 03:36:06,223 xinference.model.llm.vllm.core 3457436 INFO Loading qwen1.5-chat with following model config: {'tokenizer_mode': 'auto', 'trust_remote_code': True, 'tensor_parallel_size': 1, 'block_size': 16, 'swap_space': 4, 'gpu_memory_utilization': 0.9, 'max_num_seqs': 256, 'quantization': None, 'max_model_len': 4096} INFO 04-28 03:36:06 llm_engine.py:72] Initializing an LLM engine with config: model='/new_data3/wuzhaoxin/cache/qwen1.5-chat-pytorch-7b', tokenizer='/new_data3/wuzhaoxin/cache/qwen1.5-chat-pytorch-7b', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, seed=0) Special tokens have been added in the vocabulary, make sure the a...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 6, 'swap_space': 4, 'gpu_memory_utilization': 0.9, 'max_num_seqs': 256, 'quantization': None, 'max_model_len': 4096} INFO 04-28 03:36:06 llm_engine.py:72] Initializing an LLM engine with config: model='/new_data3/wuzhao...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: If I use Offline way to launch the model, how can I get the metrics? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I use `xinferen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: I use Offline way to launch the model, how can I get the metrics? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I use `xinference` to launc...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.3%, CPU KV cache usage: 0.0% INFO 04-26 11:20:32 async_llm_engine.py:110] Finished request fe7ec064-03be-11ef-96c2-047c1643e4f5....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: quantization=None, enforce_eager=False, kv_cache_dtype=auto, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. INFO 04-28 03:36:10 llm_engine.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
