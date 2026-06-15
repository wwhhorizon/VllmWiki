# vllm-project/vllm#43080: [Bug]: vLLM 0.21: DeepSeek-V4-pro crashes with tensor size mismatch & CUBLAS error during PP+TP inference on 2x8 H800

| 字段 | 值 |
| --- | --- |
| Issue | [#43080](https://github.com/vllm-project/vllm/issues/43080) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;scheduler_memory |
| 子分类 | shape_align |
| Operator 关键词 | cache;cuda;gemm;kernel;triton |
| 症状 | build_error;crash;mismatch;oom;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.21: DeepSeek-V4-pro crashes with tensor size mismatch & CUBLAS error during PP+TP inference on 2x8 H800

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [Warnings] Triton JIT compilation during inference (may indicate insufficient warmup): 05-18 08:23:00 (Worker_PP0_TP0) _compute_slot_mapping_kernel 05-18 08:23:00 (Worker_PP0_TP0) _build_prefill_chunk_metadata_kernel 05-18 08:23:00 (Worker_PP0_TP0) _compute_prefill_metadata_kernel 05-18 08:23:00 (Worker_PP0_TP0) _dequantize_and_gather_k_kernel 05-18 08:23:00 (Worker_PP0_TP0) _combine_topk_swa_indices_kernel 05-18 08:36:40 (Worker_PP0_TP0) _fused_inv_rope_fp8_quant_per_head (Same warnings on other workers, e.g., Worker_PP1_TP0) [INFO] 05-18 08:22:39 Graph capturing finished in 33 secs, took 1.22 GiB [INFO] 05-18 08:22:40 CUDA graph pool memory: actual 1.22 GiB, estimated 3.15 GiB (157.8% difference) [INFO] 05-18 08:22:40 Kernel JIT monitor activated === CRASH at 05-18 12:46:50 === [ERROR] Worker_PP1_TP4 (pid=44045, ip=172.21.6.7): RuntimeError: The size of tensor a (3360) must match the size of tensor b (4) at non-singleton dimension 0 Traceback (most recent call last): File ".../vllm/v1/executor/multiproc_executor.py", line 957, in worker_busy_loop output = func(*args, **kwargs) File ".../vllm/v1/worker/worker_base.py", line 337,...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: indicate insufficient warmup): 05-18 08:23:00 (Worker_PP0_TP0) _compute_slot_mapping_kernel 05-18 08:23:00 (Worker_PP0_TP0) _build_prefill_chunk_metadata_kernel 05-18 08:23:00 (Worker_PP0_TP0) _compute_prefill_metadata_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Warnings] Triton JIT compilation during inference (may indicate insufficient warmup): 05-18 08:23:00 (Worker_PP0_TP0) _compute_slot_mapping_kernel 05-18 08:23:00 (Worker_PP0_TP0) _build_prefill_chunk_metadata_kernel 05...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 0_TP0) _compute_prefill_metadata_kernel 05-18 08:23:00 (Worker_PP0_TP0) _dequantize_and_gather_k_kernel 05-18 08:23:00 (Worker_PP0_TP0) _combine_topk_swa_indices_kernel 05-18 08:36:40 (Worker_PP0_TP0) _fused_inv_rope_fp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vLLM 0.21: DeepSeek-V4-pro crashes with tensor size mismatch & CUBLAS error during PP+TP inference on 2x8 H800 bug ### Your current environment ### 🐛 Describe the bug [Warnings] Triton JIT compilation during infe...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: okens/s, Avg generation throughput: 139.1 tokens/s, Running: 3 reqs, GPU KV cache usage: 11.8%, Prefix cache hit rate: 69.0% [rank12] (Worker_PP1_TP4, pid=44045) NCCL timeout: RECV (SeqNum=478570, Timeout=600000ms) Stac...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
