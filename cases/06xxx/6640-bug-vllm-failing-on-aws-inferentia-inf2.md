# vllm-project/vllm#6640: [Bug]: vLLM failing on AWS Inferentia (inf2) 

| 字段 | 值 |
| --- | --- |
| Issue | [#6640](https://github.com/vllm-project/vllm/issues/6640) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM failing on AWS Inferentia (inf2) 

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 07-22 09:16:28 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.31 Python version: 3.10.12 | packaged by conda-forge | (main, Jun 23 2023, 22:40:32) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-6.1.92-x86_64-with-glibc2.31 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 96 On-line CPU(s) list: 0-95 Thread(s) per core: 2 Core(s) per socket: 48 Socket(s): 1 NUMA node(s): 2 Vendor ID: AuthenticAMD CPU family: 25 Model:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: nment information... WARNING 07-22 09:16:28 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build Py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: bug;stale ### Your current environment ```text Collecting environment information... WARNING 07-22 09:16:28 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: vLLM failing on AWS Inferentia (inf2) bug;stale ### Your current environment ```text Collecting environment information... WARNING 07-22 09:16:28 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ule named 'vllm._C'") PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: te_code=False, download_dir='/workspace/.cache/hub', load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=8192, guided_decoding_backend='outlines', distributed_executor_ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
