# vllm-project/vllm#34452: [Usage]: Issue Running Nemotron 3 Nano NVFP4 on sm12x (RTX 5090 / Blackwell Pro 6000)

| 字段 | 值 |
| --- | --- |
| Issue | [#34452](https://github.com/vllm-project/vllm/issues/34452) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Issue Running Nemotron 3 Nano NVFP4 on sm12x (RTX 5090 / Blackwell Pro 6000)

### Issue 正文摘录

### Your current environment ```text Collecting environment information... uv is set ============================== System **Info** ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.2.1 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Jan 22 2026, 20:57:42) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.14.0-37-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5090 Nvidia driver version : 580.95.05 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ==========...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: ========= OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.2.1 Libc version : glibc-2.39 ==================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Usage]: Issue Running Nemotron 3 Nano NVFP4 on sm12x (RTX 5090 / Blackwell Pro 6000) usage ### Your current environment ```text Collecting environment information... uv is set ============================== System **In...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Usage]: Issue Running Nemotron 3 Nano NVFP4 on sm12x (RTX 5090 / Blackwell Pro 6000) usage ### Your current environment ```text Collecting environment information... uv is set ============================== System **In...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 00) usage ### Your current environment ```text Collecting environment information... uv is set ============================== System **Info** ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version :...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected V...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
