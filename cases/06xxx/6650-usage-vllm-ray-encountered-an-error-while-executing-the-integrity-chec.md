# vllm-project/vllm#6650: [Usage]: VLLM + RAY encountered an error while executing the integrity check script.

| 字段 | 值 |
| --- | --- |
| Issue | [#6650](https://github.com/vllm-project/vllm/issues/6650) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: VLLM + RAY encountered an error while executing the integrity check script.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-116-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 Nvidia driver version: 550.90.07 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.6 /usr/lib/x86_64-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.42.4 [pip3] triton==2.3.1 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.2 vLLM Build Flags: CUDA Archs:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Y encountered an error while executing the integrity check script. usage;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.1+cu12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
