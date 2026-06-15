# vllm-project/vllm#33920: [Bug]: GLM-4.7-Flash OOM during sampler warmup with tensor parallelism on RTX 4090

| 字段 | 值 |
| --- | --- |
| Issue | [#33920](https://github.com/vllm-project/vllm/issues/33920) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4.7-Flash OOM during sampler warmup with tensor parallelism on RTX 4090

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### System Info - **vLLM version**: 0.15.0rc2.dev40+g2e8de8677.cu130 - **GPU**: 2x NVIDIA GeForce RTX 4090 (24564 MiB each, compute capability 8.9) - **NVIDIA Driver**: 580.126.09 - **CUDA**: 13.0 - **OS**: Ubuntu 22.04.5 LTS (Docker) - **Model**: GLM-4.7-Flash - **Tensor Parallel Size**: 2 ### Describe the bug GLM-4.7-Flash fails to initialize with `CUDA out of memory` during sampler warmup phase when using tensor parallelism, even with `gpu_memory_utilization=0.90`. **Error occurs at:** ``` RuntimeError: CUDA out of memory occurred when warming up sampler with 256 dummy requests. Please try lowering `max_num_seqs` or `gpu_memory_utilization` when initializing the engine. ``` **Memory allocation details from error log:** ``` GPU 0: total capacity 23.52 GiB, only 212.62 MiB free (23.30 GiB in use) GPU 1: total capacity 23.51 GiB, only 201.62 MiB free (23.30 GiB in use) Per GPU breakdown: - PyTorch allocated: 20.10 GiB - CUDA Graphs (private pools): 52.00 MiB - Reserved but unallocated: ~914 MiB ``` **The failure happens in `vllm/v1/sample/ops/topk_topp_sampler.py:262`:** ```python logits_sort, logits_idx = logits.sort(dim=-1, des...

## 现有链接修复摘要

#37518 [Core] Preallocate sampler logits workspace during memory profiling

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: urrent environment ### 🐛 Describe the bug ### System Info - **vLLM version**: 0.15.0rc2.dev40+g2e8de8677.cu130 - **GPU**: 2x NVIDIA GeForce RTX 4090 (24564 MiB each, compute capability 8.9) - **NVIDIA Driver**: 580.126....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: GLM-4.7-Flash OOM during sampler warmup with tensor parallelism on RTX 4090 bug;stale ### Your current environment ### 🐛 Describe the bug ### System Info - **vLLM version**: 0.15.0rc2.dev40+g2e8de8677.cu130 - **G...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: *: 580.126.09 - **CUDA**: 13.0 - **OS**: Ubuntu 22.04.5 LTS (Docker) - **Model**: GLM-4.7-Flash - **Tensor Parallel Size**: 2 ### Describe the bug GLM-4.7-Flash fails to initialize with `CUDA out of memory` during sampl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: y changes: 1. Added `gqa_ratio=4` support for GLM-4.7-Flash 2. Optimized Flash Attention kernel selection for `head_size=576` 3. Added tile kernel configurations to avoid CPU fallback: ```cpp if (head_size_kq == 576 &&...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: y) 4. Setting `PYTORCH_ALLOC_CONF=expandable_segments:True` 5. Disabling FP8 KV cache (already incompatible with RTX 4090 compute 8.9) 6. Reducing context length to 65k tokens #### 3. **Add GLM-4.7 architecture support*...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37518](https://github.com/vllm-project/vllm/pull/37518) | closes_keyword | 0.95 | [Core] Preallocate sampler logits workspace during memory profiling | fix a 24 GB `0.99` boot OOM or #33920 specifically, that needs a separate original-condition reproduction and broader memory-sizing fix. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
