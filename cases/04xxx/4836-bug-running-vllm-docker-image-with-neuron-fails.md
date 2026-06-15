# vllm-project/vllm#4836: [Bug]: Running vllm docker image with neuron fails

| 字段 | 值 |
| --- | --- |
| Issue | [#4836](https://github.com/vllm-project/vllm/issues/4836) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Running vllm docker image with neuron fails

### Issue 正文摘录

### Your current environment root@9c92d584ab5f:/app# python3 ./collect_env.py Collecting environment information... WARNING 05-15 15:13:52 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For multi-node inference, please install Ray with `pip install ray`. PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.31 Python version: 3.10.12 | packaged by conda-forge | (main, Jun 23 2023, 22:40:32) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-4.14.343-260.564.amzn2.x86_64-x86_64-with-glibc2.31 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 4 On-line CPU(s) list: 0-3 Th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: Running vllm docker image with neuron fails bug;stale ### Your current environment root@9c92d584ab5f:/app# python3 ./collect_env.py Collecting environment information... WARNING 05-15 15:13:52 ray_utils.py:46] Fa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: th `pip install ray`. PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ot@9c92d584ab5f:/app# python3 ./collect_env.py Collecting environment information... WARNING 05-15 15:13:52 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For multi-node inferen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, disable_custom_all_reduce=False, q...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Running vllm docker image with neuron fails bug;stale ### Your current environment root@9c92d584ab5f:/app# python3 ./collect_env.py Collecting environment information... WARNING 05-15 15:13:52 ray_utils.py:46] Fa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
