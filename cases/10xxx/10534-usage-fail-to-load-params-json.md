# vllm-project/vllm#10534: [Usage]: Fail to load params.json 

| 字段 | 值 |
| --- | --- |
| Issue | [#10534](https://github.com/vllm-project/vllm/issues/10534) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | activation;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Fail to load params.json 

### Issue 正文摘录

### Your current environment ```text $ python collect_env.py Collecting environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.6 (Green Obsidian) (x86_64) GCC version: (GCC) 12.2.0 Clang version: Could not collect CMake version: version 3.20.2 Libc version: glibc-2.28 Python version: 3.10.15 (main, Oct 3 2024, 07:27:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-372.32.1.el8_6.x86_64-x86_64-with-glibc2.28 Is CUDA available: False CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 Thread(s) per core: 1 Core(s) per socket: 16 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 106 Model name: Intel(R) Xeon(R) Silver 4314 CPU @ 2.40GHz Stepping: 6 CPU MHz: 3400.000 CPU max MHz: 3400.0000 CPU min MHz: 800.0000 Bog...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: t $ python collect_env.py Collecting environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.6 (Green Obsidian)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.6 (Green Obsidian) (x86_64) GCC version: (GCC) 12.2.0 Cl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t environment ```text $ python collect_env.py Collecting environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 00.0, "sliding_window": null, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.42.0.dev0", "use_cache": true, "vocab_size": 32768 } ``` I use the folloing code to run the model: ```pyt...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.46.3 [pip3] triton==3.1.0 [conda] blas 1.0 mkl [conda] cuda-cudart 12.1.105 0 nvidia [conda] cuda-cupti 12.1.105

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
