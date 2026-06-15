# vllm-project/vllm#18107: [Usage]: how to run Qwen3-30B-A3B-AWQ in vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#18107](https://github.com/vllm-project/vllm/issues/18107) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to run Qwen3-30B-A3B-AWQ in vllm

### Issue 正文摘录

### Your current environment vLLM API server version 0.8.4.dev0+g296c6572d.d20250513 cuda12.8 gpu 5090 32G PyTorch version: 2.7.0a0+7c8ec84dab.nv25.03 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: Could not collect CMake version: version 3.31.6 Libc version: glibc-2.39 Python version: 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-6.11.0-21-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: 12.8.93 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 5090 D Nvidia driver version: 570.133.07 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.8.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: 3B-AWQ in vllm usage;stale ### Your current environment vLLM API server version 0.8.4.dev0+g296c6572d.d20250513 cuda12.8 gpu 5090 32G PyTorch version: 2.7.0a0+7c8ec84dab.nv25.03 Is debug build: False CUDA used to build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ent environment vLLM API server version 0.8.4.dev0+g296c6572d.d20250513 cuda12.8 gpu 5090 32G PyTorch version: 2.7.0a0+7c8ec84dab.nv25.03 Is debug build: False CUDA used to build PyTorch: 12.8 ROCM used to build PyTorch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: how to run Qwen3-30B-A3B-AWQ in vllm usage;stale ### Your current environment vLLM API server version 0.8.4.dev0+g296c6572d.d20250513 cuda12.8 gpu 5090 32G PyTorch version: 2.7.0a0+7c8ec84dab.nv25.03 Is debug b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: onnx==1.17.0 [pip3] optree==0.14.1 [pip3] pynvml==12.0.0 [pip3] pytorch-triton==3.2.0+gitb2684bf3b.nvinternal [pip3] pyzmq==26.2.1 [pip3] torch==2.7.0a0+7c8ec84dab.nv25.3 [pip3] torch-geometric==2.6.1 [pip3] torch_tenso...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: how to run Qwen3-30B-A3B-AWQ in vllm usage;stale ### Your current environment vLLM API server version 0.8.4.dev0+g296c6572d.d20250513 cuda12.8 gpu 5090 32G PyTorch version: 2.7.0a0+7c8ec84dab.nv25.03 Is debug b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
