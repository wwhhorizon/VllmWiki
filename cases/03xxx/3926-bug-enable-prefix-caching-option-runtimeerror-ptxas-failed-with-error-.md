# vllm-project/vllm#3926: [Bug]: enable-prefix-caching option: RuntimeError: `ptxas` failed with error code 1

| 字段 | 值 |
| --- | --- |
| Issue | [#3926](https://github.com/vllm-project/vllm/issues/3926) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: enable-prefix-caching option: RuntimeError: `ptxas` failed with error code 1

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.27.6 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-4.15.0-213-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 GPU 4: NVIDIA GeForce RTX 3090 GPU 5: NVIDIA GeForce RTX 3090 GPU 6: NVIDIA GeForce RTX 3090 GPU 7: NVIDIA GeForce RTX 3090 Nvidia driver version: 535.86.05 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.5 /usr/lib/x86_64-linux-gnu/libcudnn...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: enable-prefix-caching option: RuntimeError: `ptxas` failed with error code 1 bug ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.1.2+cu121 Is debug build: False C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec store bypass: Mitigation; Sp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ==0.7.0a0 [pip3] torchtext==0.16.0a0 [pip3] torchvision==0.16.0a0 [pip3] triton==2.1.0+e621604 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.0 vLLM Build Flags: CUDA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
