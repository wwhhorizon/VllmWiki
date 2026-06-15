# vllm-project/vllm#12753: [Bug]: Pooling request fails for classification task

| 字段 | 值 |
| --- | --- |
| Issue | [#12753](https://github.com/vllm-project/vllm/issues/12753) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pooling request fails for classification task

### Issue 正文摘录

### Your current environment Here is the output from `python3 collect_env.py` script that I ran inside the docker container. ```text root@83c981d8de30:/workspace/vllm# python3 collect_env.py INFO 02-04 22:49:20 __init__.py:186] Automatically detected platform cpu. Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: version 3.31.4 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jan 17 2025, 14:35:34) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 14 On-line CPU(s) list: 0-13 Vendor ID: GenuineI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: is the output from `python3 collect_env.py` script that I ran inside the docker container. ```text root@83c981d8de30:/workspace/vllm# python3 collect_env.py INFO 02-04 22:49:20 __init__.py:186] Automatically detected pl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Pooling request fails for classification task bug;stale ### Your current environment Here is the output from `python3 collect_env.py` script that I ran inside the docker container. ```text root@83c981d8de30:/work...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ironment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
