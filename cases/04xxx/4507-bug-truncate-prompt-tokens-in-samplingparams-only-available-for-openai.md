# vllm-project/vllm#4507: [Bug]: `truncate_prompt_tokens` in SamplingParams only available for openai entrypoints, not for offline vLLM engine

| 字段 | 值 |
| --- | --- |
| Issue | [#4507](https://github.com/vllm-project/vllm/issues/4507) |
| 状态 | closed |
| 标签 | bug;feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `truncate_prompt_tokens` in SamplingParams only available for openai entrypoints, not for offline vLLM engine

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CBL-Mariner/Linux (x86_64) GCC version: (GCC) 11.2.0 Clang version: Could not collect CMake version: version 3.21.4 Libc version: glibc-2.35 Python version: 3.10.2 (main, Feb 22 2024, 00:00:03) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.138.1-4.cm2-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidia driver version: 525.85.12 cuDNN version: Probably one of the following: /usr/lib/libcudnn.so.8.9.5 /usr/lib/libcudnn_adv_infer.so.8.9.5 /usr/lib/libcudnn_adv_train.so.8.9.5 /usr/lib/libcudnn_cnn_infer.so.8.9.5 /usr/lib/libcudnn_cnn_train.so.8.9.5 /usr/lib/libcudnn_ops_infer.so.8.9.5 /usr/lib/libcudnn_ops_train.so.8.9.5 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CBL-Mariner/Linux (x86_64) GCC versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CBL-Mariner/Linux (x86_64) GCC version: (GCC) 11.2.0 Clang version: Could not...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: vailable for openai entrypoints, not for offline vLLM engine bug;feature request;stale ### Your current environment Collecting environment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ure request;stale ### Your current environment Collecting environment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CBL-Mariner/Li...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ==2.2.1+cu118 [pip3] torch-lib==0.1.25 [pip3] torchmetrics==1.3.1 [pip3] triton==2.2.0 [pip3] vllm-nccl-cu11==2.18.1.0.4.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
