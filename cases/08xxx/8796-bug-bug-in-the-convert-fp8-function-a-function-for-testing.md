# vllm-project/vllm#8796: [Bug]: Bug in the convert_fp8 function, a function for testing.

| 字段 | 值 |
| --- | --- |
| Issue | [#8796](https://github.com/vllm-project/vllm/issues/8796) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8 |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Bug in the convert_fp8 function, a function for testing.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The bug appears in the convert_fp8 function within csrc/cache_kernels.cu, as shown below: ``` // Only for testing. void convert_fp8(torch::Tensor& dst_cache, torch::Tensor& src_cache, const double scale, const std::string& kv_cache_dtype) { torch::Device src_device = src_cache.device(); torch::Device dst_device = dst_cache.device(); TORCH_CHECK(src_device.is_cuda(), "src must be on a GPU") TORCH_CHECK(dst_device.is_cuda(), "dst must be on a GPU") TORCH_CHECK(src_device.index() == dst_device.index(), "src and dst must be on the same GPU"); at::cuda::OptionalCUDAGuard device_guard(src_device); int64_t num_blocks = src_cache.size(0); int64_t block_stride = src_cache.stride(0); dim3 grid(num_blocks); dim3 block(std::min(block_stride, int64_t(512))); const cudaStream_t stream = at::cuda::getCurrentCUDAStream(); if (kv_cache_dtype == "auto") { if (src_cache.dtype() == at::ScalarType::Float) { CALL_CONVERT_FP8(uint8_t, float, vllm::Fp8KVCacheDataType::kAuto); } else if (src_cache.dtype() == at::ScalarType::Half) { CALL_CONVERT_FP8(uint8_t, uint16_t, vllm::Fp8KVCacheDataType::kAuto); } else if (src_cac...

## 现有链接修复摘要

#8797 [Bugfix] Fix bug in convert_fp8

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Bug in the convert_fp8 function, a function for testing. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The bug appears in the convert_fp8 function within csrc/c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ; at::cuda::OptionalCUDAGuard device_guard(src_device); int64_t num_blocks = src_cache.size(0); int64_t block_stride = src_cache.stride(0); dim3 grid(num_blocks); dim3 block(std::min(block_stride, int64_t(512))); const...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: y is "auto" incorrect? The scaled_convert function, which handles the conversion, supports only two Fp8KVCacheDataType values: kFp8E4M3 and kFp8E5M2. kAuto is not included. If kAuto is used, the function should raise an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rch::Device dst_device = dst_cache.device(); TORCH_CHECK(src_device.is_cuda(), "src must be on a GPU") TORCH_CHECK(dst_device.is_cuda(), "dst must be on a GPU") TORCH_CHECK(src_device.index() == dst_device.index(), "src...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: questions. correctness frontend_api;model_support;quantization cuda;fp8 mismatch dtype;env_dependency;memory_layout #8797 [Bugfix] Fix bug in convert_fp8 Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8797](https://github.com/vllm-project/vllm/pull/8797) | closes_keyword | 0.95 | [Bugfix] Fix bug in convert_fp8 | FIX #8796 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- insid |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
