# vllm-project/vllm#5637: [Bug]: RuntimeError with tensor_parallel_size > 1 in Process Bootstrapping Phase

| 字段 | 值 |
| --- | --- |
| Issue | [#5637](https://github.com/vllm-project/vllm/issues/5637) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError with tensor_parallel_size > 1 in Process Bootstrapping Phase

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.9 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-20) Clang version: 16.0.6 (Red Hat 16.0.6-2.module+el8.9.0+1651+e10a8f6d) CMake version: version 3.29.5 Libc version: glibc-2.28 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-4.18.0-513.24.1.el8_9.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-PCIE-40GB GPU 1: NVIDIA A100-PCIE-40GB GPU 2: NVIDIA A100-PCIE-40GB GPU 3: NVIDIA A100-PCIE-40GB GPU 4: NVIDIA A100-PCIE-40GB GPU 5: NVIDIA A100-PCIE-40GB GPU 6: NVIDIA A100-PCIE-40GB GPU 7: NVIDIA A100-PCIE-40GB Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.9 (Green Obs...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux release 8.9 (Green Obsidian) (x86_64) GCC version: (GCC) 8.5.0 20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Rocky Linux rel...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, disable_custom_all_reduce=False, q...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: post0 [pip3] torchvision==0.18.1 [pip3] transformers==4.42.0.dev0 [pip3] triton==2.3.0 [conda] blas 2.116 mkl conda-forge [conda] blas-devel 3.9.0 16_linux64_mkl conda-forge [conda] libblas 3.9.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
