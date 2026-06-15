# vllm-project/vllm#19694: [Bug]: In the DP online scenario of DeepSeek, when concurrency and request rate increase, TTFT drops sharply.

| 字段 | 值 |
| --- | --- |
| Issue | [#19694](https://github.com/vllm-project/vllm/issues/19694) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: In the DP online scenario of DeepSeek, when concurrency and request rate increase, TTFT drops sharply.

### Issue 正文摘录

### Your current environment INFO 06-16 07:33:32 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.31.4 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.9 (main, Feb 5 2025, 08:49:00) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-25-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.1.105 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU 4: NVIDIA H20 GPU 5: NVIDIA H20 GPU 6: NVIDIA H20 GPU 7: NVIDIA H20 Nvidia driver version : 550.127.08 cuDN...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.31.4 Libc version : glibc-2.35 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: t INFO 06-16 07:33:32 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: In the DP online scenario of DeepSeek, when concurrency and request rate increase, TTFT drops sharply. bug;stale ### Your current environment INFO 06-16 07:33:32 [__init__.py:244] Automatically detected platform...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dio==2.7.0 [pip3] torchvision==0.22.0 [pip3] transformers==4.52.2 [pip3] triton==3.3.0 [pip3] tritonclient==2.55.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM V...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
