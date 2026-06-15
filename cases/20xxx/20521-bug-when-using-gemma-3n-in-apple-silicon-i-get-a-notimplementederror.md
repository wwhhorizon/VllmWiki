# vllm-project/vllm#20521: [Bug]: When using gemma-3n in Apple Silicon I get a NotImplementedError

| 字段 | 值 |
| --- | --- |
| Issue | [#20521](https://github.com/vllm-project/vllm/issues/20521) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using gemma-3n in Apple Silicon I get a NotImplementedError

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : macOS 15.5 (arm64) GCC version : Could not collect Clang version : 17.0.0 (clang-1700.0.13.5) CMake version : version 4.0.3 Libc version : N/A ============================== PyTorch Info ============================== PyTorch version : 2.7.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)] (64-bit runtime) Python platform : macOS-15.5-arm64-arm-64bit ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Apple M3 Max ============================== Versions of relevant libraries ============================== [pip...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ================== OS : macOS 15.5 (arm64) GCC version : Could not collect Clang version : 17.0.0 (clang-1700.0.13.5) CMake version : version 4.0.3 Libc version : N/A ==============================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: yTorch version : 2.7.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: When using gemma-3n in Apple Silicon I get a NotImplementedError bug;stale ### Your current environment ============================== System Info ============================== OS : macOS 15.5 (a
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ] File "/Users/achilleas.voutsas/Development/Tools/vllm/vllm/attention/backends/torch_sdpa.py", line 415, in __init__ ERROR 07-06 10:33:15 [engine.py:458] raise NotImplementedError("KV sharing is not supported in V0.")...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g]: When using gemma-3n in Apple Silicon I get a NotImplementedError bug;stale ### Your current environment ============================== System Info ============================== OS : macOS 15.5 (arm64) GCC version :...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
