# vllm-project/vllm#3990: [Usage]: When to use fp8 and when to use fp8_e5m2

| 字段 | 值 |
| --- | --- |
| Issue | [#3990](https://github.com/vllm-project/vllm/issues/3990) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;fp8;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: When to use fp8 and when to use fp8_e5m2

### Issue 正文摘录

### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.7 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-16) Clang version: Could not collect CMake version: version 3.29.0 Libc version: glibc-2.28 Python version: 3.9.19 (main, Mar 21 2024, 17:11:28) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-425.10.1.el8_7.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidia driver version: 530.30.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 64 On-line CPU(s) list: 0-63 Thread(s) per core: 1 Core(s) per socket: 32 Socket(s): 2 NUMA node(s): 4 Vendor ID: AuthenticAMD CPU family: 25 Model: 1 Model name: AMD EPYC 7513 32-Core Processor Stepping: 1 CPU MHz: 2595.071 BogoM...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: fp8 and when to use fp8_e5m2 usage ### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.7 (Green Obsidian) (x...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux 8.7 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Re...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: When to use fp8 and when to use fp8_e5m2 usage ### Your current environment PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux 8....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: function _verify_cache_dtype of config.py will cause an error——"Unknown kv cache dtype: fp8"——because the judging conditions is self.cache_dtype == "fp8_e5m2". But in another judging conditions such as The 232nd line of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
