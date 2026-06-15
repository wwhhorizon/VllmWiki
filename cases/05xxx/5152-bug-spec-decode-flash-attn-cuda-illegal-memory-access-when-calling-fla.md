# vllm-project/vllm#5152: [Bug] [spec decode] [flash_attn]: CUDA illegal memory access when calling flash_attn_cuda.fwd_kvcache

| 字段 | 值 |
| --- | --- |
| Issue | [#5152](https://github.com/vllm-project/vllm/issues/5152) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [spec decode] [flash_attn]: CUDA illegal memory access when calling flash_attn_cuda.fwd_kvcache

### Issue 正文摘录

### My environment setup 1st environment (running on ec2 `g6.4xlarge`) ``` [2024-06-01T10:14:23Z] Collecting environment information... [2024-06-01T10:14:26Z] PyTorch version: 2.3.0+cu121 [2024-06-01T10:14:26Z] Is debug build: False [2024-06-01T10:14:26Z] CUDA used to build PyTorch: 12.1 [2024-06-01T10:14:26Z] ROCM used to build PyTorch: N/A [2024-06-01T10:14:26Z] [2024-06-01T10:14:26Z] OS: Ubuntu 22.04.4 LTS (x86_64) [2024-06-01T10:14:26Z] GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 [2024-06-01T10:14:26Z] Clang version: Could not collect [2024-06-01T10:14:26Z] CMake version: version 3.29.3 [2024-06-01T10:14:26Z] Libc version: glibc-2.35 [2024-06-01T10:14:26Z] [2024-06-01T10:14:26Z] Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) [2024-06-01T10:14:26Z] Python platform: Linux-6.1.90-99.173.amzn2023.x86_64-x86_64-with-glibc2.35 [2024-06-01T10:14:26Z] Is CUDA available: True [2024-06-01T10:14:26Z] CUDA runtime version: Could not collect [2024-06-01T10:14:26Z] CUDA_MODULE_LOADING set to: LAZY [2024-06-01T10:14:26Z] GPU models and configuration: GPU 0: NVIDIA L4 [2024-06-01T10:14:26Z] Nvidia driver version: 525.147.05 [2024-06-01T10:14:26Z] cu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 3Z] Collecting environment information... [2024-06-01T10:14:26Z] PyTorch version: 2.3.0+cu121 [2024-06-01T10:14:26Z] Is debug build: False [2024-06-01T10:14:26Z] CUDA used to build PyTorch: 12.1 [2024-06-01T10:14:26Z] R...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug] [spec decode] [flash_attn]: CUDA illegal memory access when calling flash_attn_cuda.fwd_kvcache bug ### My environment setup 1st environment (running on ec2 `g6.4xlarge`) ``` [2024-06-01T10:14:23Z] Collecting envi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: on ec2 `g6.4xlarge`) ``` [2024-06-01T10:14:23Z] Collecting environment information... [2024-06-01T10:14:26Z] PyTorch version: 2.3.0+cu121 [2024-06-01T10:14:26Z] Is debug build: False [2024-06-01T10:14:26Z] CUDA used to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug] [spec decode] [flash_attn]: CUDA illegal memory access when calling flash_attn_cuda.fwd_kvcache bug ### My environment setup 1st environment (running on ec2 `g6.4xlarge`) ``` [2024-06-01T10:14:23Z] Collecting envi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [2024-06-01T10:14:26Z] [pip3] torch==2.3.0 [2024-06-01T10:14:26Z] [pip3] triton==2.3.0 [2024-06-01T10:14:26Z] [conda] Could not collectROCM Version: Could not collect [2024-06-01T10:14:26Z] Neuron SDK Version: N/A [2024...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
