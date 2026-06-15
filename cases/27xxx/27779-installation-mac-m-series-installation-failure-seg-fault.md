# vllm-project/vllm#27779: [Installation]: Mac M Series Installation Failure + Seg Fault

| 字段 | 值 |
| --- | --- |
| Issue | [#27779](https://github.com/vllm-project/vllm/issues/27779) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
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

> [Installation]: Mac M Series Installation Failure + Seg Fault

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ============================== System Info ============================== OS : macOS 26.0.1 (arm64) GCC version : Could not collect Clang version : 17.0.0 (clang-1700.0.13.5) CMake version : version 4.0.3 Libc version : N/A ============================== PyTorch Info ============================== PyTorch version : 2.8.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.10 (main, Jul 19 2025, 19:15:43) [Clang 17.0.0 (clang-1700.0.13.5)] (64-bit runtime) Python platform : macOS-26.0.1-arm64-arm-64bit ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Apple M2 ============================== Versions of relevan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Mac M Series Installation Failure + Seg Fault installation ### Your current environment ```text The output of `python collect_env.py` ============================== System Info ===================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: yTorch version : 2.8.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.10...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: init__.py:225] Automatically detected platform cpu. INFO 10-29 22:18:47 [triton_utils/importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. ``` With exit code 139...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: == PyTorch version : 2.8.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
