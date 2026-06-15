# vllm-project/vllm#28352: [Installation]: Installation failed on Mac OS(Apple silicon), Error: Triton not installed or not compatible

| 字段 | 值 |
| --- | --- |
| Issue | [#28352](https://github.com/vllm-project/vllm/issues/28352) |
| 状态 | open |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Installation failed on Mac OS(Apple silicon), Error: Triton not installed or not compatible

### Issue 正文摘录

### Your current environment My environment: ============================== System Info ============================== OS : macOS 26.1 (arm64) GCC version : Could not collect Clang version : 17.0.0 (clang-1700.4.4.1) CMake version : Could not collect Libc version : N/A ============================== PyTorch Info ============================== PyTorch version : 2.8.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Apr 9 2024, 08:09:14) [Clang 15.0.0 (clang-1500.1.0.2.5)] (64-bit runtime) Python platform : macOS-26.1-arm64-arm-64bit ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Apple M2 ============================== Versions of relevant libraries ====================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Installation failed on Mac OS(Apple silicon), Error: Triton not installed or not compatible installation ### Your current environment My environment: ============================== System Info ===
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: yTorch version : 2.8.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Installation]: Installation failed on Mac OS(Apple silicon), Error: Triton not installed or not compatible installation ### Your current environment My environment: ============================== System Info ==========...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: == PyTorch version : 2.8.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
