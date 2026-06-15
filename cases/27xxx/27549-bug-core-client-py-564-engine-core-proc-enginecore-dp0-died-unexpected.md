# vllm-project/vllm#27549: [Bug]: [core_client.py:564] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.

| 字段 | 值 |
| --- | --- |
| Issue | [#27549](https://github.com/vllm-project/vllm/issues/27549) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [core_client.py:564] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.30.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 20:16:04) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.0-85-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.1.105 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 2080 Ti Nvidia driver version : 580.95.05 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.1.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.1.1 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.1.1 /usr/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : version 3.30.1 Libc version : glibc-2.35 ===============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ntime version : 12.1.105 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA GeForce RTX 2080 Ti Nvidia driver version : 580.95.05 cuDNN version : Probably one of the following: /usr/lib/x86_6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Mitigation; Clear Register File Vulnerability Retbleed: Not affected Vulnerability Spec rstack ov...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ngineCore_DP0 pid=127416) INFO 10-27 13:36:22 [core.py:210] init engine (profile, create kv cache, warmup model) took 34.70 seconds INFO 10-27 13:36:23 [llm.py:306] Supported_tasks: ['generate'] WARNING 10-27 13:36:23 [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
