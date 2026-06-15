# vllm-project/vllm#18854: [Bug]: Non-torch memory tracking fails to account for gpu usage of other processes

| 字段 | 值 |
| --- | --- |
| Issue | [#18854](https://github.com/vllm-project/vllm/issues/18854) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Non-torch memory tracking fails to account for gpu usage of other processes

### Issue 正文摘录

### Your current environment ``` ============================== System Info ============================== OS : Red Hat Enterprise Linux 9.5 (Plow) (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.5 (main, Apr 2 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] (64-bit runtime) Python platform : Linux-5.14.0-284.88.1.el9_2.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidia driver version : 550.127.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: : Red Hat Enterprise Linux 9.5 (Plow) (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ===========
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.5 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: sion : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidia driver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ch memory tracking fails to account for gpu usage of other processes bug;stale ### Your current environment ``` ============================== System Info ============================== OS : Red Hat Enterprise Linux 9.5...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: transformers==4.52.3 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.3.0 [pip3] tritonclient==2.51.0 [pip3] vector-quantize-pytorch==1.21.2 [conda] Could not collect ============================== vLLM Info...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
