# vllm-project/vllm#4287: [Bug]: _raise_exception_on_finish throw asyncio.exceptions.CancelledError for vLLM on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#4287](https://github.com/vllm-project/vllm/issues/4287) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: _raise_exception_on_finish throw asyncio.exceptions.CancelledError for vLLM on CPU

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 04-23 06:09:11 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For distributed inference, please install Ray with `pip install ray`. PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.1 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-101-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: 12.2.91 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 112 On-line CPU(s) list: 0-111 Vendor ID: GenuineIntel Model name: I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: _raise_exception_on_finish throw asyncio.exceptions.CancelledError for vLLM on CPU bug;stale ### Your current environment ```text Collecting environment information... WARNING 04-23 06:09:11 ray_utils.py:46] Fail...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: with `pip install ray`. PyTorch version: 2.2.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.1 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: bug;stale ### Your current environment ```text Collecting environment information... WARNING 04-23 06:09:11 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For distributed infere...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: relevant libraries: [pip3] numpy==1.26.4 [pip3] torch==2.2.1+cpu [pip3] triton==2.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] torch 2.2.1+cpu pypi_0 pypi [conda] triton 2.3.0
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /Llama-2-7b-hf", trust_remote_code=True, dtype="float32", disable_log_requests=True, max_num_seqs=10, device="cpu" ) engine = AsyncLLMEngine.from_engine_args(args) results_generator = engine.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
