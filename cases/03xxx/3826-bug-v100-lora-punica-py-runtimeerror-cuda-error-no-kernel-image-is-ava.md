# vllm-project/vllm#3826: [Bug]: V100  lora运行  punica.py  RuntimeError: CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#3826](https://github.com/vllm-project/vllm/issues/3826) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V100  lora运行  punica.py  RuntimeError: CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ```text Collecting environment information... PyTorch version: 2.1.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 9.3.1 20200408 (Red Hat 9.3.1-2) Clang version: Could not collect CMake version: version 3.27.1 Libc version: glibc-2.17 Python version: 3.11.8 (main, Feb 26 2024, 21:39:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.76.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB GPU 2: Tesla V100-SXM2-32GB GPU 3: Tesla V100-SXM2-32GB Nvidia driver version: 535.54.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Thread(s) per core: 2 Core(s) per socket: 24 Socket(s): 1 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: llect_env.py` ``` ```text Collecting environment information... PyTorch version: 2.1.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: V100 lora运行 punica.py RuntimeError: CUDA error: no kernel image is available for execution on the device bug ### Your current environment ```text The output of `python collect_env.py` ``` ```text Collecting envir...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: output of `python collect_env.py` ``` ```text Collecting environment information... PyTorch version: 2.1.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux re...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: Qwen1.5-14B-Chat \ --max-loras 16 --tensor-parallel-size 1 --dtype float16 --max-lora-rank 64 --gpu-memory-utilization 0.9 \ --enable-lora --enforce-eager --disable-log-requests --lora-modules lora1=XXXXX ``` ```text IN...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 1 [pip3] torchaudio==2.1.0+cu121 [pip3] torchvision==0.16.0+cu121 [pip3] triton==2.1.0 [conda] numpy 1.26.3 pypi_0 pypi [conda] torch 2.1.0+cu121 pypi_0 pypi [conda] torchaudio 2.1.0+cu121

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
