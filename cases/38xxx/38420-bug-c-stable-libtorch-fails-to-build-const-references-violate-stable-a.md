# vllm-project/vllm#38420: [Bug]: _C_stable_libtorch fails to build: const& references violate stable ABI trivially_copyable requirement

| 字段 | 值 |
| --- | --- |
| Issue | [#38420](https://github.com/vllm-project/vllm/issues/38420) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;quantization;speculative_decoding |
| 子分类 | install |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: _C_stable_libtorch fails to build: const& references violate stable ABI trivially_copyable requirement

### Issue 正文摘录

### Your current environment - vLLM: main branch (commit 0e9358c11, 2026-03-27) - PyTorch: NGC `nvcr.io/nvidia/pytorch:26.01-py3` (PyTorch 2.10.0a0) - Platform: aarch64 (NVIDIA DGX Spark GB10, SM121) - CUDA: 13.1 - Build: `TORCH_CUDA_ARCH_LIST="12.1a"` ### Bug description `_C_stable_libtorch` fails to compile with: ``` torch/csrc/stable/stableivalue_conversions.h:450:24: error: static assertion failed torch/csrc/stable/stableivalue_conversions.h:457:9: error: non-static data member in a union may not have reference type 'const torch::stable::Tensor&' ``` ### Root cause `csrc/libtorch_stable/ops.h` uses `const torch::stable::Tensor&` (pass-by-reference) for all function signatures. The stable ABI requires trivially copyable types and uses `memcpy` across the C-shim boundary. Reference types are not trivially copyable. Current signatures (all broken): ```cpp torch::stable::Tensor permute_cols(torch::stable::Tensor const& A, torch::stable::Tensor const& perm); void per_token_group_quant_fp8(const torch::stable::Tensor& input, torch::stable::Tensor& output_q, torch::stable::Tensor& output_s, ...); // Same for per_token_group_quant_8bit_packed, per_token_group_quant_int8 ``` ### Fix Ch...

## 现有链接修复摘要

#37744 [Bugfix] Fix PyTorch stable ABI compatibility for permute_cols | #38126 [NVIDIA] Fix DGX Spark logic | #38421 -[Bugfix] Fix stable ABI build: pass torch::stable::Tensor by value

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: _C_stable_libtorch fails to build: const& references violate stable ABI trivially_copyable requirement ### Your current environment - vLLM: main branch (commit 0e9358c11, 2026-03-27) - PyTorch: NGC `nvcr.io/nvidi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: torch::stable::Tensor const& perm); void per_token_group_quant_fp8(const torch::stable::Tensor& input, torch::stable::Tensor& output_q, torch::stable::Tensor& output_s, ...); // Same for per_token_group_quant_8bit_p
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: : NGC `nvcr.io/nvidia/pytorch:26.01-py3` (PyTorch 2.10.0a0) - Platform: aarch64 (NVIDIA DGX Spark GB10, SM121) - CUDA: 13.1 - Build: `TORCH_CUDA_ARCH_LIST="12.1a"` ### Bug description `_C_stable_libtorch` fails to compi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ops `per_token_group_fp8_quant` and `permute_cols` are unavailable. This blocks MTP speculative decoding with NVFP4 quantization on DGX Spark (SM121), since the MTP code path requires `per_token_group_fp8_quant`. Workar...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: copyable. Current signatures (all broken): ```cpp torch::stable::Tensor permute_cols(torch::stable::Tensor const& A, torch::stable::Tensor const& perm); void per_token_group_quant_fp8(const torch::stable::Tensor& input,...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37744](https://github.com/vllm-project/vllm/pull/37744) | mentioned | 0.45 | [Bugfix] Fix PyTorch stable ABI compatibility for permute_cols | dings.cpp` signatures to match. this was previously identified in pr #37744 but closed prematurely ("seems like not need anymore"). the bug persists on current main. ### impact wi… |
| [#38126](https://github.com/vllm-project/vllm/pull/38126) | mentioned | 0.45 | [NVIDIA] Fix DGX Spark logic | ingle dgx spark gb10 (sm121, 128gb uma), building vllm from main + pr #38126 (merged). |
| [#38421](https://github.com/vllm-project/vllm/pull/38421) | closes_keyword | 0.95 | -[Bugfix] Fix stable ABI build: pass torch::stable::Tensor by value | Fixes #38420 ## Purpose Fix `_C_stable_libtorch` compilation failure caused by `const torch::stable::Tensor&` references violating the stable ABI `trivially_copyable` r |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
