# vllm-project/vllm#8184: [Bug]: (OOM) Find two places that cause a significant increase in GPU memory usage (probably lead to memory leak)

| 字段 | 值 |
| --- | --- |
| Issue | [#8184](https://github.com/vllm-project/vllm/issues/8184) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (OOM) Find two places that cause a significant increase in GPU memory usage (probably lead to memory leak)

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.31 Python version: 3.11.9 | packaged by conda-forge | (main, Apr 19 2024, 18:36:13) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.4.0-190-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.4.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L40 GPU 1: NVIDIA L40 GPU 2: NVIDIA L40 GPU 3: NVIDIA L40 GPU 4: NVIDIA L40 Nvidia driver version: 550.54.14 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.2.1 /usr/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: y leak) bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: nificant increase in GPU memory usage (probably lead to memory leak) bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rdpid overflow_recov succor smca Versions of relevant libraries: [pip3] flashinfer==0.1.1+cu121torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvidia-cuda...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
