# vllm-project/vllm#6682: [Bug]: CUDA OOM error when loading another model after exiting the first one.

| 字段 | 值 |
| --- | --- |
| Issue | [#6682](https://github.com/vllm-project/vllm/issues/6682) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA OOM error when loading another model after exiting the first one.

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.28.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-1058-aws-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-16GB Nvidia driver version: 555.42.06 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9.0.0 HIP runtime version: N/A MIOpen runtime ve...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: CUDA OOM error when loading another model after exiting the first one. bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: CUDA OOM error when loading another model after exiting the first one. bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: DA OOM error when loading another model after exiting the first one. bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 7.1a0 [pip3] torchtext==0.17.0a0 [pip3] torchvision==0.18.0+cu118 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
