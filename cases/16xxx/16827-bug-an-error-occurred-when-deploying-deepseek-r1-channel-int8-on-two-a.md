# vllm-project/vllm#16827: [Bug]:  An error occurred when deploying DeepSeek-R1-Channel-INT8 on two A100 machines using lws

| 字段 | 值 |
| --- | --- |
| Issue | [#16827](https://github.com/vllm-project/vllm/issues/16827) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  An error occurred when deploying DeepSeek-R1-Channel-INT8 on two A100 machines using lws

### Issue 正文摘录

### Your current environment NFO 04-18 01:47:48 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 4.0.0 Libc version: glibc-2.35 Python version: 3.12.10 (main, Apr 9 2025, 08:55:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version: 560.35.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little End...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ly detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: An error occurred when deploying DeepSeek-R1-Channel-INT8 on two A100 machines using lws bug;stale ### Your current environment NFO 04-18 01:47:48 [__init__.py:239] Automatically detected platform cuda. Collectin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: en deploying DeepSeek-R1-Channel-INT8 on two A100 machines using lws bug;stale ### Your current environment NFO 04-18 01:47:48 [__init__.py:239] Automatically detected platform cuda. Collecting environment information.....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _.py:239] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 08] enabled custom ops: Counter({'rms_norm': 124, 'silu_and_mul': 31, 'unquantized_fused_moe': 28, 'rotary_embedding': 1}) DEBUG 04-18 01:30:29 [config.py:3910] disabled custom ops: Counter() (RayWorkerWrapper pid=582)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
