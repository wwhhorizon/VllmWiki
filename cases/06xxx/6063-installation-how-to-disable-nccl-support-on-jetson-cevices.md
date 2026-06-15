# vllm-project/vllm#6063: [Installation]: how to disable NCCL support on Jetson cevices

| 字段 | 值 |
| --- | --- |
| Issue | [#6063](https://github.com/vllm-project/vllm/issues/6063) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
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

> [Installation]: how to disable NCCL support on Jetson cevices

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.6 Libc version: glibc-2.35 Python version: 3.10.14 (main, May 6 2024, 19:36:58) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.122-tegra-aarch64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: aarch64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 8 On-line CPU(s) list: 0-7 Vendor ID: ARM Model name: Cortex-A78AE Model: 1 Thread(s) per core: 1 Core(s) per cluster: 4 Socket(s): - Cluster(s): 2 Stepping: r0p1 CPU max MHz: 2188.8000 CPU min MHz: 115.2000 BogoMIPS: 62.50 Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atom...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: how to disable NCCL support on Jetson cevices installation ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0 Is debug
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=True, q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.2 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [pip3] torchvision==0.18.0a0+6043bc2 [pip3] transformers==4.42.3 [pip3] triton==3.0.0 [conda] torch 2.3.0 pypi_0 pypi [conda] torchvision 0.18.0a0+6043bc2 pypi_0 pypi [conda] triton 3.0.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
