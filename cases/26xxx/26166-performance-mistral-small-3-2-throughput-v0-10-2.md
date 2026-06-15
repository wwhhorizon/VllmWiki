# vllm-project/vllm#26166: [Performance]: Mistral Small 3.2 throughput v0.10.2

| 字段 | 值 |
| --- | --- |
| Issue | [#26166](https://github.com/vllm-project/vllm/issues/26166) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Mistral Small 3.2 throughput v0.10.2

### Issue 正文摘录

### Proposal to improve performance Unknown ### Report of performance regression When running Mistral Small 3.2 in vLLM with version 0.10.2, the throughput speed is incredibly low (generation tokens are on 0.1 tokens/s). Downgrading to vLLM v0.9.* solves this issue and returns the throughput to expected numbers. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.8.0-78-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA ava...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t of performance regression When running Mistral Small 3.2 in vLLM with version 0.10.2, the throughput speed is incredibly low (generation tokens are on 0.1 tokens/s). Downgrading to vLLM v0.9.* solves this issue and re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Performance]: Mistral Small 3.2 throughput v0.10.2 performance;stale ### Proposal to improve performance Unknown ### Report of performance regression When running Mistral Small 3.2 in vLLM with version 0.10.2, the thro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ntime version : 12.2.140 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA L40S GPU 1: NVIDIA L40S Nvidia driver version : 535.247.01 cuDNN version : Could not collect HIP runtime version :...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Mistral Small 3.2 throughput v0.10.2 performance;stale ### Proposal to improve performance Unknown ### Report of performance regression When running Mistral Small 3.2 in vLLM with version 0.10.2, the thro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.3.1.post1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.6.4.1 [pip3] nvidia-cuda-cupti-cu12==12.6.80 [pip3] nvidia-cuda-n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
