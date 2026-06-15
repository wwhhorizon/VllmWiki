# vllm-project/vllm#3815: [Bug]: RuntimeError: Loading lora model failed

| 字段 | 值 |
| --- | --- |
| Issue | [#3815](https://github.com/vllm-project/vllm/issues/3815) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Loading lora model failed

### Issue 正文摘录

### Your current environment ```text $ python collect_env.py Collecting environment information... PyTorch version: 2.2.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.18.4 Libc version: glibc-2.31 Python version: 3.10.13 | packaged by conda-forge | (main, Dec 23 2023, 15:36:39) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.10.0-28-cloud-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 Nvidia driver version: 535.86.10 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 12 On-line CPU(s) list: 0-11 Thread(s) per core: 2 Core(s) per socket: 6 Socket(s): 1 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) CPU @ 2.20GHz Stepping: 7...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: xt $ python collect_env.py Collecting environment information... PyTorch version: 2.2.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: RuntimeError: Loading lora model failed bug;stale ### Your current environment ```text $ python collect_env.py Collecting environment information... PyTorch version: 2.2.0+cu121 Is debug build: False CUDA used to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.2.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: RuntimeError: Loading lora model failed bug;stale ### Your current environment ```text $ python collect_env.py Collecting environment information... PyTorch version: 2.2.0+cu121 Is debug build: False CUDA used to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: FACE_HUB_TOKEN= " vllm/vllm-openai --model="mistralai/Mistral-7B-v0.1" --dtype auto --tensor-parallel-size 1 --gpu-memory-utilization 0.9 --max-model-len 4096 --enable-lora --lora-modules ai-lora="ai-maker-space/mistral...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
