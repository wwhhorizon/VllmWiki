# vllm-project/vllm#5111: [Bug]: vLLM embeddings example code doesn't work

| 字段 | 值 |
| --- | --- |
| Issue | [#5111](https://github.com/vllm-project/vllm/issues/5111) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM embeddings example code doesn't work

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 10 (buster) (x86_64) GCC version: (Debian 8.3.0-6) 8.3.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.28 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-4.19.0-26-cloud-amd64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 11.3.109 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 12 On-line CPU(s) list: 0-11 Thread(s) per core: 2 Core(s) per socket: 6 Socket(s): 1 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) CPU @ 2.20GHz Stepping: 7 CPU MHz: 2200.182 BogoMIPS: 4400.36 H...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 10 (buster) (x86_64...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: work bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 10 (buster) (x86_64) GCC version: (Debian 8.3.0-6) 8.3.0 Cla...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: -nccl-cu12==2.20.5 [pip3] onnxruntime==1.18.0 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
