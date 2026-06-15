# vllm-project/vllm#27343: [Usage]: Can't get result from /pooling api when using Qwen2.5-Math-PRM-7B online

| 字段 | 值 |
| --- | --- |
| Issue | [#27343](https://github.com/vllm-project/vllm/issues/27343) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Can't get result from /pooling api when using Qwen2.5-Math-PRM-7B online

### Issue 正文摘录

### Your current environment ``` The output of `python collect_env.py` Collecting environment information... [140/1781] ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 20:16:04) [GCC 11.2.0] (64-bit runti me) Python platform : Linux-5.15.0-153-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.99 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A800 80GB PCIe GPU 3: NVIDIA A800 80GB PCIe GPU 4: NVIDIA A100 80GB PCIe GPU 5: NVIDIA A100 80GB P...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Can't get result from /pooling api when using Qwen2.5-Math-PRM-7B online usage ### Your current environment ``` The output of `python collect_env.py` Collecting environment information...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Mitigation; Enhanced IBRS Vuln...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.8.0 [pip3] torchvision==0.23.0 [pip3] transformers==4.57.1 [pip3] triton==3.4.0 [conda] numpy 2.2.6 pypi_0 pypi [conda] nvidia-cublas-cu12 12.8.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.8.90

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
