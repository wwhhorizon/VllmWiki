# vllm-project/vllm#11012: [Bug]: Qwen2ForSequenceClassification does not work for custom classification head.

| 字段 | 值 |
| --- | --- |
| Issue | [#11012](https://github.com/vllm-project/vllm/issues/11012) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2ForSequenceClassification does not work for custom classification head.

### Issue 正文摘录

### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.119.1.el7.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.5.82 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100S-PCIE-32GB GPU 1: Tesla V100S-PCIE-32GB Nvidia driver version: 550.90.07 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.2.1 /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9.2.1 HIP runtime version: N/A MIOpen runtime ver...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: tom classification head. bug;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen2ForSequenceClassification does not work for custom classification head. bug;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: SequenceClassification does not work for custom classification head. bug;stale ### Your current environment PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.47.0 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.4.post1 vLLM Build Flags: CUDA A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
