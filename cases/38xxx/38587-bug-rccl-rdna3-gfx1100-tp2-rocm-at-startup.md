# vllm-project/vllm#38587: [Bug]: RCCL RDNA3 gfx1100 Tp2 ROCM at startup

| 字段 | 值 |
| --- | --- |
| Issue | [#38587](https://github.com/vllm-project/vllm/issues/38587) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RCCL RDNA3 gfx1100 Tp2 ROCM at startup

### Issue 正文摘录

### Your current environment `==============================` System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : 22.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.2.1 26084 f58b06dce1f9c15707c5f808fd002e18c2accf7e) CMake version : version 3.31.10 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+git8514f05 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 7.2.53211 ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.12.67-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : (gfx1100) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 7.2.53211 MIOpen runtime version : 3.5.1 Is XNNPACK available : True ========...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Clang version : 22.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-7.2.1 26084 f58b06dce1f9c15707c5f808fd002...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: RCCL RDNA3 gfx1100 Tp2 ROCM at startup bug;rocm ### Your current environment `==============================` System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : (gfx1100) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 7.2.53211 MIOpen runtim...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: rsions of relevant libraries ============================== [pip3] conch-triton-kernels==1.2.1 [pip3] numpy==2.1.3 [pip3] onnx==1.19.0 [pip3] onnx-ir==0.2.0 [pip3] onnxscript==0.6.2 [pip3] onnxslim==0.1.90 [pip3] pyzmq=...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: gnment_asserts': False, 'scalar_asserts': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': , 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [1, 2, 4, 8,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
