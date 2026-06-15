# vllm-project/vllm#3525: [Usage]: How to inference model with multi-gpus

| 字段 | 值 |
| --- | --- |
| Issue | [#3525](https://github.com/vllm-project/vllm/issues/3525) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to inference model with multi-gpus

### Issue 正文摘录

### Your current environment llm = LLM(model=model_name, max_model_len=8192, gpu_memory_utilization=0.8, tensor_parallel_size=8, dtype="bfloat16") INFO 03-20 06:43:28 config.py:433] Custom all-reduce kernels are temporarily disabled due to stability issues. We will re-enable them once the issues are resolved. 2024-03-20 06:43:30,508 WARNING services.py:1996 -- WARNING: The object store is using /tmp instead of /dev/shm because /dev/shm has only 62910464 bytes available. This will harm performance! You may be able to free up space by deleting files in /dev/shm. If you are inside a Docker container, you can increase /dev/shm size by passing '--shm-size=10.24gb' to 'docker run' (or add it to the run_options list in a Ray cluster config). Make sure to set this to more than 30% of available RAM. 2024-03-20 06:43:31,684 INFO worker.py:1724 -- Started a local Ray instance. INFO 03-20 06:43:33 llm_engine.py:87] Initializing an LLM engine with config: model='deepseek-ai/deepseek-coder-33b-base', tokenizer='deepseek-ai/deepseek-coder-33b-base', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, loa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: able to free up space by deleting files in /dev/shm. If you are inside a Docker container, you can increase /dev/shm size by passing '--shm-size=10.24gb' to 'docker run' (or add it to the run_options list in a Ray clust...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: max_model_len=8192, gpu_memory_utilization=0.8, tensor_parallel_size=8, dtype="bfloat16") INFO 03-20 06:43:28 config.py:433] Custom all-reduce kernels are temporarily disabled due to stability issues. We will re-enable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How to inference model with multi-gpus usage ### Your current environment llm = LLM(model=model_name, max_model_len=8192, gpu_memory_utilization=0.8, tensor_parallel_size=8, dtype="bfloat16") INFO 03-20 06:43:2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: antization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, seed=0) Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. RuntimeError:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=8, disable_custom_all_reduce=True, quantiza...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
