# vllm-project/vllm#5547: [Bug]: RuntimeError: CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#5547](https://github.com/vllm-project/vllm/issues/5547) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-107-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.7.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB Nvidia driver version: 535.171.04 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.5.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True Versions of relevan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: RuntimeError: CUDA error: no kernel image is available for execution on the device bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0 Is debug build: F...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 11.7.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-PCIE-32GB Nvidia driver version: 535.171.04 cuDNN version: Probably one of the following: /usr/lib/x86_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: CUDA error: no kernel image is available for execution on the device bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0 Is debug build: False CUDA used to bui...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ics==1.1.2 [pip3] torchvision==0.18.0 [pip3] transformers==4.41.2 [pip3] triton==2.3.0 [conda] blas 1.0 mkl [conda] ctransformers 0.2.27 pypi_0 pypi [conda] ffmpeg 4.3 hf484d3e_

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
