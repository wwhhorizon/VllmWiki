# vllm-project/vllm#26894: [Bug]: ModernBertConfig missing layer_norm_eps attribute causing initialization failure

| 字段 | 值 |
| --- | --- |
| Issue | [#26894](https://github.com/vllm-project/vllm/issues/26894) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ModernBertConfig missing layer_norm_eps attribute causing initialization failure

### Issue 正文摘录

System Info ============================== OS : Fedora Linux 42 (Workstation Edition) (x86_64) GCC version : (GCC) 15.2.1 20250808 (Red Hat 15.2.1-1) Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.41 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Aug 28 2025, 17:07:59) [Clang 20.1.4 ] (64-bit runtime) Python platform : Linux-6.16.9-200.fc42.x86_64-x86_64-with-glibc2.41 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 4060 Laptop GPU Nvidia driver version : 580.82.09 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Fedora Linux 42 (Workstation Edition) (x86_64) GCC version : (GCC) 15.2.1 20250808 (Red Hat 15.2.1-1) Clang version : Could not collect CMake version : version 3.31.6 Libc version : glibc-2.41 ==============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: ModernBertConfig missing layer_norm_eps attribute causing initialization failure bug System Info ============================== OS : Fedora Linux 42 (Workstation Edition) (x86_64) GCC version
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Old microcode: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerab...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.8.0 [pip3] torchvision==0.23.0 [pip3] transformers==4.57.1 [pip3] triton==3.4.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect v...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
