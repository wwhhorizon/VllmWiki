# vllm-project/vllm#3688: [Bug]: Custom all reduce not work.

| 字段 | 值 |
| --- | --- |
| Issue | [#3688](https://github.com/vllm-project/vllm/issues/3688) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Custom all reduce not work.

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.28.4 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 5 2023, 18:54:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.2.0-39-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla T4 GPU 1: Tesla T4 Nvidia driver version: 545.29.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 104 On-line CPU(s) list: 0-103 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Platinum 8269CY CPU @ 2.50GHz CPU family: 6 Model: 85 Thread(s) per core: 2 Core(s) per socket: 26 Socket(s): 2 Stepping: 7 CPU max MHz: 3800.0000 CPU min MHz: 1200.0000 BogoMIPS: 5000.00 Flags: fpu vme de pse tsc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: all reduce not work. bug;stale ### Your current environment ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rent environment ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla T4 GPU 1: Tesla T4 Nvidia driver version: 545.29.06 cuDNN version: Could not collect HIP runtime version: N...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Custom all reduce not work. bug;stale ### Your current environment ``` PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: .api_server --model /TinyLlama-1.1B-Chat-v0.6 --tensor-parallel-size 2 --dtype half --enforce-eager ``` Log: ```shell INFO 03-28 21:38:07 api_server.py:147] vLLM API server version 0.3.3 INFO 03-28 21:38:07 api_server.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
