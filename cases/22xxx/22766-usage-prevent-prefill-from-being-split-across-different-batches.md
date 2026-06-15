# vllm-project/vllm#22766: [Usage]: Prevent prefill from being split across different batches

| 字段 | 值 |
| --- | --- |
| Issue | [#22766](https://github.com/vllm-project/vllm/issues/22766) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Prevent prefill from being split across different batches

### Issue 正文摘录

### Your current environment ```text uv is set ============================== System Info ============================== OS : Debian GNU/Linux 12 (bookworm) (x86_64) GCC version : (Debian 12.2.0-14+deb12u1) 12.2.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.36 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.2 (main, Apr 28 2025, 14:11:48) [GCC 12.2.0] (64-bit runtime) Python platform : Linux-6.7.12+bpo-amd64-x86_64-with-glibc2.36 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3060 Ti Nvidia driver version : 575.57.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Arc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Debian GNU/Linux 12 (bookworm) (x86_64) GCC version : (Debian 12.2.0-14+deb12u1) 12.2.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.36 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.2 (m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: Prevent prefill from being split across different batches usage;stale ### Your current environment ```text uv is set ============================== System Info ============================== OS
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: sion : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3060 Ti Nvidia driver version : 575.57.08 cuDNN version : Could not collect HIP runtime version : N/A M...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.7.1 [pip3] torchvision==0.22.1 [pip3] transformers==4.53.3 [pip3] triton==3.3.1 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
