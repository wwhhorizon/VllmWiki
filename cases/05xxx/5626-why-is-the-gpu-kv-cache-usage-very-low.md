# vllm-project/vllm#5626: Why is the GPU KV cache usage very low? 

| 字段 | 值 |
| --- | --- |
| Issue | [#5626](https://github.com/vllm-project/vllm/issues/5626) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Why is the GPU KV cache usage very low? 

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.26.3 Libc version: glibc-2.31 Python version: 3.9.12 (main, Apr 5 2022, 06:56:58) [GCC 7.5.0] (64-bit runtime) Python platform: Linux-5.10.0-182.0.0.95.oe2203sp3.x86_64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.2.91 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 Nvidia driver version: 535.154.05 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.2.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.2.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: 架构： x86_64 CPU 运行模式： 32-bit,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: che usage very low? usage ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.2.91 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 Nvidia driver version: 535.154.05 cuDNN version: Probably one of the following: /usr/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: transformers==4.41.2 [pip3] transformers-stream-generator==0.0.4 [pip3] triton==2.3.0 [conda] blas 1.0 mkl [conda] cudatoolkit 11.3.1 h2bc3f7f_2 [conda] ffmpeg 4.3 hf484d3e_0 p

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
