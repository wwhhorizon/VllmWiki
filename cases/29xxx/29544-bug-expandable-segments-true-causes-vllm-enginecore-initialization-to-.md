# vllm-project/vllm#29544: [Bug]: "expandable_segments: True" causes vLLM EngineCore initialization to fail when running Qwen3 VL models

| 字段 | 值 |
| --- | --- |
| Issue | [#29544](https://github.com/vllm-project/vllm/issues/29544) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;sampling |
| 症状 | crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "expandable_segments: True" causes vLLM EngineCore initialization to fail when running Qwen3 VL models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug description When running vLLM with the CUDA memory allocator setting: ``` export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True ``` the EngineCore process fails to initialize and crashes with: - `RuntimeError: cancelled` - `Fatal Python error: Aborted` - `*** SIGABRT received ***` However, the exact same code runs normally when: ``` export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:False ``` Doubt `expandable_segments=True` is incompatible with vLLM’s CUDA memory usage (CUDA Graph capture + KV cache initialization + multiprocess EngineCore). ## Minimal reproducible example export OMP_NUM_THREADS=1 export NCCL_DEBUG=WARN export TOKENIZERS_PARALLELISM=false export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True module load openmpi module load gcc/12.2.0 module load cuda/12.2 then run vllm-ray-offline-batch-inference for Qwen3-VL-32B on 4 A100GPU with --batch_size 16 \ --max_model_len 3072 \ --max_num_batched_tokens 48000 \ --max_num_seqs 16 \ --max_tokens 1000 \ --temperature 0.7 \ --top_p 0.95 \ --tensor_parallel_size 4 \ --pipeline_parallel_size 1 \ --gpu_memory_utilization 0.9 \ --enable_chunked_prefill \ --trust_remo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: + KV cache initialization + multiprocess EngineCore). ## Minimal reproducible example export OMP_NUM_THREADS=1 export NCCL_DEBUG=WARN export TOKENIZERS_PARALLELISM=false export PYTORCH_CUDA_ALLOC_CONF=expandable_segment...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ### 🐛 Describe the bug ## Bug description When running vLLM with the CUDA memory allocator setting: ``` export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True ``` the EngineCore process fails to initialize and crashes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: vLLM EngineCore initialization to fail when running Qwen3 VL models bug;stale ### Your current environment ### 🐛 Describe the bug ## Bug description When running vLLM with the CUDA memory allocator setting: ``` export P...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: gments: True" causes vLLM EngineCore initialization to fail when running Qwen3 VL models bug;stale ### Your current environment ### 🐛 Describe the bug ## Bug description When running vLLM with the CUDA memory allocator...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: apture + KV cache initialization + multiprocess EngineCore). ## Minimal reproducible example export OMP_NUM_THREADS=1 export NCCL_DEBUG=WARN export TOKENIZERS_PARALLELISM=false export PYTORCH_CUDA_ALLOC_CONF=expandable_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
