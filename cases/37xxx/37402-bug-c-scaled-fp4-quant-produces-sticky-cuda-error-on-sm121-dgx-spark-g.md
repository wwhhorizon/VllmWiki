# vllm-project/vllm#37402: [Bug]: _C.scaled_fp4_quant produces sticky CUDA error on SM121 (DGX Spark GB10) — contaminates CUDA context

| 字段 | 值 |
| --- | --- |
| Issue | [#37402](https://github.com/vllm-project/vllm/issues/37402) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: _C.scaled_fp4_quant produces sticky CUDA error on SM121 (DGX Spark GB10) — contaminates CUDA context

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Simplified Current environment:** ``` vLLM: 0.17.1 (vllm/vllm-openai:latest) PyTorch: 2.10.0+cu129 CUDA: 12.9 FlashInfer: 0.6.6 GPU: NVIDIA GB10 (SM121, compute capability 12.1) Platform: aarch64 (NVIDIA DGX Spark) Python: 3.12.13 ``` **Describe the bug:** `torch.ops._C.scaled_fp4_quant()` produces a **sticky CUDA error** (`cudaErrorNoKernelImageForDevice`) on SM121 (DGX Spark GB10). The function itself returns results successfully, but it leaves the CUDA context in a corrupted state — all subsequent CUDA operations fail with `no kernel image is available for execution on the device`. This blocks all FlashInfer-based NVFP4 backends (`flashinfer-cutlass`, `flashinfer-cudnn`, etc.) on SM121 because `apply_nvfp4_linear()` calls `scaled_fp4_quant()` for activation quantization before calling the FlashInfer FP4 GEMM kernel. **Minimal reproduction:** ```python import torch torch.cuda.set_device(0) import vllm._C # Load the extension x = torch.randn(32, 256, device="cuda", dtype=torch.bfloat16) gs = torch.tensor(100.0, device="cuda") # This succeeds and returns correct results out = torch.empty(32, 128, device="cuda", dtype=torch.uint...

## 现有链接修复摘要

#37410 Fix SM121 GB10 FP4 quantization sticky CUDA error

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: _C.scaled_fp4_quant produces sticky CUDA error on SM121 (DGX Spark GB10) — contaminates CUDA context bug ### Your current environment ### 🐛 Describe the bug **Simplified Current environment:** ``` vLLM: 0.17.1 (v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ng the FlashInfer FP4 GEMM kernel. **Minimal reproduction:** ```python import torch torch.cuda.set_device(0) import vllm._C # Load the extension x = torch.randn(32, 256, device="cuda", dtype=torch.bfloat16) gs = torch.t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: vLLM: 0.17.1 (vllm/vllm-openai:latest) PyTorch: 2.10.0+cu129 CUDA: 12.9 FlashInfer: 0.6.6 GPU: NVIDIA GB10 (SM121, compute capability 12.1) Platform: aarch64 (NVIDIA DGX Spark) Python: 3.12.13 ``` **Describe the bug:**...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: _C.scaled_fp4_quant produces sticky CUDA error on SM121 (DGX Spark GB10) — contaminates CUDA context bug ### Your current environment ### 🐛 Describe the bug **Simplified Current environment:** ``` vLLM: 0.17.1 (v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: l with `no kernel image is available for execution on the device`. This blocks all FlashInfer-based NVFP4 backends (`flashinfer-cutlass`, `flashinfer-cudnn`, etc.) on SM121 because `apply_nvfp4_linear()` calls `scaled_f...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37410](https://github.com/vllm-project/vllm/pull/37410) | closes_keyword | 0.95 | Fix SM121 GB10 FP4 quantization sticky CUDA error | Fix for issue #37402: scaled_fp4_quant produces sticky CUDA error on SM121 (DGX Spark GB10). Root cause: _C.abi3.so contains sm_120 cubins but lacks sm_121a compatible kernels. Th |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
