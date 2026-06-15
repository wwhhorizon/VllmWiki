# vllm-project/vllm#10517: [Usage]: What's the relationship between KV cache and MAX_SEQUENCE_LENGTH.

| 字段 | 值 |
| --- | --- |
| Issue | [#10517](https://github.com/vllm-project/vllm/issues/10517) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: What's the relationship between KV cache and MAX_SEQUENCE_LENGTH.

### Issue 正文摘录

### Your current environment GPU : H100 80G *2 Model : Llama 3.1 70B Model Params: ~~~ env: - name: MODEL_NAME value: /mnt/models/models--meta-llama--llama-3-1-70b-instruct - name: DTYPE_STR value: float16 - name: MAX_SEQUENCE_LENGTH value: '20000' - name: MAX_BATCH_SIZE value: '4' - name: MAX_NEW_TOKENS value: '4096' - name: MAX_LOG_LEN value: '100' - name: DEFAULT_INCLUDE_STOP_SEQS value: 'false' - name: NUM_GPUS value: '2' - name: CUDA_VISIBLE_DEVICES value: '0,1' - name: HUGGINGFACE_HUB_CACHE value: /mnt/models/ - name: HF_MODULES_CACHE value: /tmp/huggingface/modules - name: PORT value: '3000' ~~~ Initializing an LLM engine (v0.5.4) with config ~~~ model='/mnt/models/models--meta-llama--llama-3-1-70b-instruct', speculative_config=None, tokenizer='/mnt/models/models--meta-llama--llama-3-1-70b-instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ENCE_LENGTH. usage;stale ### Your current environment GPU : H100 80G *2 Model : Llama 3.1 70B Model Params: ~~~ env: - name: MODEL_NAME value: /mnt/models/models--meta-llama--llama-3-1-70b-instruct - name: DTYPE_STR val...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Usage]: What's the relationship between KV cache and MAX_SEQUENCE_LENGTH. usage;stale ### Your current environment GPU : H100 80G *2 Model : Llama 3.1 70B Model Params: ~~~ env: - name: MODEL_NAME value: /mnt/models/mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: : /mnt/models/models--meta-llama--llama-3-1-70b-instruct - name: DTYPE_STR value: float16 - name: MAX_SEQUENCE_LENGTH value: '20000' - name: MAX_BATCH_SIZE value: '4' - name: MAX_NEW_TOKENS value: '4096' - name: M
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Usage]: What's the relationship between KV cache and MAX_SEQUENCE_LENGTH. usage;stale ### Your current environment GPU : H100 80G *2 Model : Llama 3.1 70B Model Params: ~~~ env: - name: MODEL_NAME value: /mnt/models/mo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: lue: '100' - name: DEFAULT_INCLUDE_STOP_SEQS value: 'false' - name: NUM_GPUS value: '2' - name: CUDA_VISIBLE_DEVICES value: '0,1' - name: HUGGINGFACE_HUB_CACHE value: /mnt/models/ - name: HF_MODULES_CACHE

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
