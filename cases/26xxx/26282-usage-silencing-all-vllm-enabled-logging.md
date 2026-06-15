# vllm-project/vllm#26282: [Usage]: silencing ALL vLLM-enabled logging

| 字段 | 值 |
| --- | --- |
| Issue | [#26282](https://github.com/vllm-project/vllm/issues/26282) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: silencing ALL vLLM-enabled logging

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Rocky Linux 9.6 (Blue Onyx) (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version : 19.1.7 (RESF 19.1.7-1.el9) CMake version : version 3.26.5 Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.9 (main, Aug 14 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] (64-bit runtime) Python platform : Linux-5.14.0-503.40.1.el9_5.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 11.8.89 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 Nvidia driver version : 575.51.03 cuDNN version : Probably one of the following: /usr/lib64/libcudnn.so.8.9.7 /us...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Usage]: silencing ALL vLLM-enabled logging usage;stale ### Your current environment ============================== System Info ============================== OS : Rocky Linux 9.6 (Blue Onyx) (x86_64
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.9 (m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: silencing ALL vLLM-enabled logging usage;stale ### Your current environment ============================== System Info ============================== OS : Rocky Linux 9.6 (Blue Onyx) (x86_64) GCC version : (GC
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: untime version : 11.8.89 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 Nvidi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dio==2.8.0 [pip3] torchvision==0.23.0 [pip3] transformers==4.57.0 [pip3] triton==3.4.0 [conda] cudatoolkit 11.8.0 h37601d7_11 conda-forge ============================== vLLM Info ============================== ROCM Vers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
