# vllm-project/vllm#25234: [Usage]: How to enable the thinking mode in deepseekv3.1 by default？

| 字段 | 值 |
| --- | --- |
| Issue | [#25234](https://github.com/vllm-project/vllm/issues/25234) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to enable the thinking mode in deepseekv3.1 by default？

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ============================== System Info ============================== OS : Microsoft Windows 10 家庭中文版 GCC version : (Rev7, Built by MSYS2 project) 13.1.0 Clang version : Could not collect CMake version : version 4.0.1 Libc version : N/A ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.1 (tags/v3.12.1:2305ca5, Dec 7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] (64-bit runtime) Python platform : Windows-10-10.0.19045-SP0 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3060 Laptop GPU Nvidia driver version : 577.03 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ========== OS : Microsoft Windows 10 家庭中文版 GCC version : (Rev7, Built by MSYS2 project) 13.1.0 Clang version : Could not collect CMake version : version 4.0.1 Libc version : N/A =========================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.1 (t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: untime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3060 Laptop GPU Nvidia driver version : 577.03 cuDNN version : Could not collect HIP runtime version :...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sage]: How to enable the thinking mode in deepseekv3.1 by default？ usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ============================== System Info ==================...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: orch version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
