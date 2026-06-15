# vllm-project/vllm#8708: Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher

| 字段 | 值 |
| --- | --- |
| Issue | [#8708](https://github.com/vllm-project/vllm/issues/8708) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.136-tegra-aarch64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Orin (nvgpu) Nvidia driver version: N/A cuDNN version: Probably one of the following: /usr/lib/aarch64-linux-gnu/libcudnn.so.8.9.4 /usr/lib/aarch64-linux-gnu/libcudnn_adv_infer.so.8.9.4 /usr/lib/aarch64-linux-gnu/libcudnn_adv_train.so.8.9.4 /usr/lib/aarch64-linux-gnu/libcudnn_cnn_infer.so.8.9.4 /usr/lib/aarch64-linux-gnu/libcudnn_cnn_train.so.8.9.4 /usr/lib/aarch64-linux-gnu/libcudnn_ops_infer.so.8.9.4 /usr/lib/aarch64-linux-gnu/libcudnn_ops_train.so.8.9.4 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: aarch64 CPU op-mode(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (aarch64) GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: igher usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: hemetic and compare instructions' requires .target sm_53 or higher usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] torchvision==0.18.0a0+6043bc2 [pip3] transformers==4.41.1 [pip3] tritonclient==2.48.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Arc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
