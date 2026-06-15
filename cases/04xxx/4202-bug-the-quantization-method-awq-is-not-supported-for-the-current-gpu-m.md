# vllm-project/vllm#4202: [Bug]: The quantization method awq is not supported for the current GPU. Minimum capability: 75. Current capability: 70.

| 字段 | 值 |
| --- | --- |
| Issue | [#4202](https://github.com/vllm-project/vllm/issues/4202) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The quantization method awq is not supported for the current GPU. Minimum capability: 75. Current capability: 70.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.17 Python version: 3.10.14 (main, Mar 21 2024, 16:24:04) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.88.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 10 On-line CPU(s) list: 0-9 Thread(s) per core: 1 Core(s) per socket: 10 Socket(s): 1 NUMA node(s): 1 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) Platinum 8255C CPU @ 2.50GHz Stepping: 5 CPU MHz: 2500.000 Bog...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: python collect_env.py` ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: he quantization method awq is not supported for the current GPU. Minimum capability: 75. Current capability: 70. bug ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: `text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: s of relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.1.2 [pip3] triton==2.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] triton 2.1.0
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: The quantization method awq is not supported for the current GPU. Minimum capability: 75. Current capability: 70. bug ### Your current environment ```text The output of `python collect_env.py` ``` Collecting envi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
