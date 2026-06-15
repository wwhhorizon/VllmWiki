# vllm-project/vllm#28438: [Usage]: How do I install vLLM nightly?

| 字段 | 值 |
| --- | --- |
| Issue | [#28438](https://github.com/vllm-project/vllm/issues/28438) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How do I install vLLM nightly?

### Issue 正文摘录

### Your current environment The output of collect_env.py ```text ============================== System Info ============================== OS : Ubuntu 20.04.5 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.16.3 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.5.1+cu121 Is debug build : False CUDA used to build PyTorch : 12.1 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (main, Jun 5 2025, 13:14:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.4.250-2-velinux1u1-amd64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.131 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver vers...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Usage]: How do I install vLLM nightly? usage ### Your current environment The output of collect_env.py ```text ============================== System Info ============================== OS : Ubuntu 20.04
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.5.1+cu121 Is debug build : False CUDA used to build PyTorch : 12.1 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ntime version : 12.4.131 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Not affected Vulnerability Spec store byp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: u121 [pip3] torchvision==0.20.1+cu121 [pip3] transformers==4.52.4 [pip3] triton==3.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
