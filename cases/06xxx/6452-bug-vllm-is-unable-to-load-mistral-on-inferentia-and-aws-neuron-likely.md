# vllm-project/vllm#6452: [Bug]: vLLM is unable to load Mistral on Inferentia and AWS neuron, likely memory issue.

| 字段 | 值 |
| --- | --- |
| Issue | [#6452](https://github.com/vllm-project/vllm/issues/6452) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM is unable to load Mistral on Inferentia and AWS neuron, likely memory issue.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING 07-15 19:13:04 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-1020-aws-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 4 On-line CPU(s) list: 0-3 Vendor ID: AuthenticAMD Model name: AMD EPYC 7R13 Processor CPU family:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: nment information... WARNING 07-15 19:13:04 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build Py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ule named 'vllm._C'") PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e to load Mistral on Inferentia and AWS neuron, likely memory issue. bug;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING 07-15 19:13:04 _cus...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: uto', trust_remote_code=False, download_dir='/tmp/', load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... WARNING 07-15 19:13:04 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
