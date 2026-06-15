# vllm-project/vllm#18481: [Bug]: benchmark_fp8_block_dense_gemm.py RuntimeError: Expected a.dtype() == torch::kInt8 to be true, but got false.

| 字段 | 值 |
| --- | --- |
| Issue | [#18481](https://github.com/vllm-project/vllm/issues/18481) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;gemm_linear;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark_fp8_block_dense_gemm.py RuntimeError: Expected a.dtype() == torch::kInt8 to be true, but got false.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash python3 benchmark_fp8_block_dense_gemm.py INFO 05-21 19:54:40 [__init__.py:248] Automatically detected platform cuda. ===== STARTING FP8 GEMM BENCHMARK ===== PyTorch version: 2.7.0+cu126 CUDA version: 12.6 Triton version: 3.3.0 Using device: NVIDIA H800 WARNING 05-21 19:54:44 [fp8_utils.py:519] Using default W8A8 Block FP8 kernel config. Performance might be sub-optimal! Config file not found at /vllm-workspace/code/vllm/vllm/model_executor/layers/quantization/utils/configs/N=24576,K=1536,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json Traceback (most recent call last): File "/vllm-workspace/code/vllm/benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py", line 466, in run_benchmarks(verbose=False) File "/vllm-workspace/code/vllm/benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py", line 322, in run_benchmarks result = benchmark_shape(m, n, k, verbose=verbose) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/vllm-workspace/code/vllm/benchmarks/kernels/deepgemm/benchmark_fp8_block_dense_gemm.py", line 125, in benchmark_shape C_vllm_cutlass = vllm_cutlass_gemm() ^^^^^^^^^^^^^^^^...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: benchmark_fp8_block_dense_gemm.py RuntimeError: Expected a.dtype() == torch::kInt8 to be true, but got false. bug;stale ### Your current environment ### 🐛 Describe the bug ```bash python3 benchmark_fp8_block_dens...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: py INFO 05-21 19:54:40 [__init__.py:248] Automatically detected platform cuda. ===== STARTING FP8 GEMM BENCHMARK ===== PyTorch version: 2.7.0+cu126 CUDA version: 12.6 Triton version: 3.3.0 Using device: NVIDIA H800 WARN...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: benchmark_fp8_block_dense_gemm.py RuntimeError: Expected a.dtype() == torch::kInt8 to be true, but got false. bug;stale ### Your current environment ### 🐛 Describe the bug ```bash python3 benchmark_fp8_block_dens...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: FP8 GEMM BENCHMARK ===== PyTorch version: 2.7.0+cu126 CUDA version: 12.6 Triton version: 3.3.0 Using device: NVIDIA H800 WARNING 05-21 19:54:44 [fp8_utils.py:519] Using default W8A8 Block FP8 kernel config. Performance...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: detected platform cuda. ===== STARTING FP8 GEMM BENCHMARK ===== PyTorch version: 2.7.0+cu126 CUDA version: 12.6 Triton version: 3.3.0 Using device: NVIDIA H800 WARNING 05-21 19:54:44 [fp8_utils.py:519] Using default W8A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
