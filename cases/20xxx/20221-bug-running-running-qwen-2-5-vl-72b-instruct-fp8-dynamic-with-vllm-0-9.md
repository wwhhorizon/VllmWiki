# vllm-project/vllm#20221: [Bug]: Running Running **Qwen-2.5-VL-72B-Instruct-FP8-Dynamic** with vLLM 0.9.1/0.9.2-dev on an **RTX 6000 Blackwell (96 GB)** throws RuntimeError: Expected a.dtype() == torch::kInt8 to be true, but got false at torch.ops._C.cutlass_scaled_mm

| 字段 | 值 |
| --- | --- |
| Issue | [#20221](https://github.com/vllm-project/vllm/issues/20221) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Running Running **Qwen-2.5-VL-72B-Instruct-FP8-Dynamic** with vLLM 0.9.1/0.9.2-dev on an **RTX 6000 Blackwell (96 GB)** throws RuntimeError: Expected a.dtype() == torch::kInt8 to be true, but got false at torch.ops._C.cutlass_scaled_mm

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.3 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 | packaged by conda-forge | (main, Jun 4 2025, 14:45:41) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-60-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA RTX PRO 6000 Blackwell Workstation Edition Nvidia driver version : 575.57.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info =======================...

## 现有链接修复摘要

#25935 Fix INT8 quantization error on Blackwell GPUs (SM100+)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.3 Libc version : glibc-2.35 ==================
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Running Running **Qwen-2.5-VL-72B-Instruct-FP8-Dynamic** with vLLM 0.9.1/0.9.2-dev on an **RTX 6000 Blackwell (96 GB)** throws RuntimeError: Expected a.dtype() == torch::kInt8 to be true, but got false at torch.o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: Qwen-2.5-VL-72B-Instruct-FP8-Dynamic** with vLLM 0.9.1/0.9.2-dev on an **RTX 6000 Blackwell (96 GB)** throws RuntimeError: Expected a.dtype() == torch::kInt8 to be true, but got false at torch.ops._C.cutlass_scaled_mm b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Running Running **Qwen-2.5-VL-72B-Instruct-FP8-Dynamic** with vLLM 0.9.1/0.9.2-dev on an **RTX 6000 Blackwell (96 GB)** throws RuntimeError: Expected a.dtype() == torch::kInt8 to be true, but got false at torch.o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: :kInt8 to be true, but got false at torch.ops._C.cutlass_scaled_mm bug;unstale ### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25935](https://github.com/vllm-project/vllm/pull/25935) | closes_keyword | 0.95 | Fix INT8 quantization error on Blackwell GPUs (SM100+) | Fixes #20221 This PR addresses a runtime error when running models with INT8 quantization (e.g., Qwen-2.5-VL-72B-Instruct-FP8-Dynamic) on Blackwell architecture GPUs (SM100+, lik |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
