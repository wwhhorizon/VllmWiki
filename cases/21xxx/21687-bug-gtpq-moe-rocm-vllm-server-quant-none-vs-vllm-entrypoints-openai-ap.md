# vllm-project/vllm#21687: [Bug]: GTPQ moe ROCM vllm server quant none vs vllm.entrypoints.openai.api_server doesnt fail

| 字段 | 值 |
| --- | --- |
| Issue | [#21687](https://github.com/vllm-project/vllm/issues/21687) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GTPQ moe ROCM vllm server quant none vs vllm.entrypoints.openai.api_server doesnt fail

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : 19.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.4.1 25184 c87081df219c42dc27c5b6d86c0525bc7d01f727) CMake version : version 3.31.6 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+gitf717b2a Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43483-a187df25c ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.15.7-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : Radeon RX 7900 XTX (gfx1100) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 6.4.43483 MIOpen runtime version : 3.4.0 Is XNNPAC...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : 19.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.4.1 25184 c87081df219c42dc27c5b6d86c0525b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: GTPQ moe ROCM vllm server quant none vs vllm.entrypoints.openai.api_server doesnt fail bug;stale ### Your current environment ============================== System Info ============================== OS
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: sion : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : Radeon RX 7900 XTX (gfx1100) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 6....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: GTPQ moe ROCM vllm server quant none vs vllm.entrypoints.openai.api_server doesnt fail bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: GTPQ moe ROCM vllm server quant none vs vllm.entrypoints.openai.api_server doesnt fail bug;stale ### Your current environment ============================== System Info ============================== OS

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
