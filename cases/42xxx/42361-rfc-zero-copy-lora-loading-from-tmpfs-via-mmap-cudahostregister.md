# vllm-project/vllm#42361: [RFC]: Zero-copy LoRA loading from tmpfs via mmap + cudaHostRegister

| 字段 | 值 |
| --- | --- |
| Issue | [#42361](https://github.com/vllm-project/vllm/issues/42361) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;moe;operator;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Zero-copy LoRA loading from tmpfs via mmap + cudaHostRegister

### Issue 正文摘录

### Motivation. vLLM's LoRA load path goes through `safetensors.safe_open(...).get_tensor(...)`. The library's Mmap backend, while called "mmap", actually **copies** each tensor's bytes from the mmap'd file region into a freshly-allocated Python `PyByteArray` (`safetensors/bindings/python/src/lib.rs:825-830`): ```rust Storage::Mmap(mmap) => { let data = &mmap[...]; PyByteArray::new(py, data) // alloc + memcpy, NOT a view } ``` The resulting tensor views the `PyByteArray`, not the original mmap region. Three consequences for a downstream that stages LoRA into tmpfs + `cudaHostRegister` to skip disk IO and pinning overhead (e.g. `verl-project/verl#5616`): 1. The caller-side `cudaHostRegister` on the tmpfs file region is **completely invisible** to PyTorch — `is_pinned()` returns False because the tensor's `data_ptr` is on Python heap, not in the registered region. 2. `from_lora_tensors`'s `.pin_memory()` allocates a fresh pinned buffer and memcpys (the work the caller was trying to avoid). 3. `.to("cuda", non_blocking=True)` goes through PyTorch's bounce buffer for unpinned source. For SSD-backed LoRA loading (the common case), this is fine — the copy fits in the disk read latency....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: for everything else. ```python # vllm/lora/lora_model.py _SAFETENSORS_DTYPE_MAP = { "F32": torch.float32, "F16": torch.float16, "BF16": torch.bfloat16, "F64": torch.float64, "I64": torch.int64, "I32": torch.int32, "I16"...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: region is **completely invisible** to PyTorch — `is_pinned()` returns False because the tensor's `data_ptr` is on Python heap, not in the registered region. 2. `from_lora_tensors`'s `.pin_memory()` allocates a fresh pin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: loading (the common case), this is fine — the copy fits in the disk read latency. For tmpfs-backed loading (the in-memory rollout case), the copy + pin + bounce buffer dominate end-to-end cost and explain why `verl` had...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: /vllm ``` None of these returned an open issue or PR addressing this specific gap (safetensors PyByteArray copy defeating caller-side `cudaHostRegister`). The closest prior work, `safetensors/safetensors#760` (merged up...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: through `safetensors.safe_open(...).get_tensor(...)`. The library's Mmap backend, while called "mmap", actually **copies** each tensor's bytes from the mmap'd file region into a freshly-allocated Python `PyByteArray` (`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
