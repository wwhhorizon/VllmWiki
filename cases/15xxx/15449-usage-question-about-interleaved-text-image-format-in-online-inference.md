# vllm-project/vllm#15449: [Usage]: Question about Interleaved Text/Image Format in Online Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#15449](https://github.com/vllm-project/vllm/issues/15449) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Question about Interleaved Text/Image Format in Online Inference

### Issue 正文摘录

### Your current environment ollecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.16.3 Libc version: glibc-2.31 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.250-2-velinux1u1-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB GPU 2: NVIDIA A800-SXM4-80GB GPU 3: NVIDIA A800-SXM4-80GB GPU 4: NVIDIA A800-SXM4-80GB GPU 5: NVIDIA A800-SXM4-80GB GPU 6: NVIDIA A800-SXM4-80GB GPU 7: NVIDIA A800-SXM4-80GB Nvidia driver version: 470.161.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: # Your current environment ollecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Question about Interleaved Text/Image Format in Online Inference usage;stale ### Your current environment ollecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to bui...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : Question about Interleaved Text/Image Format in Online Inference usage;stale ### Your current environment ollecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.50.0.dev0 [pip3] triton==3.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
