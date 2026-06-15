# vllm-project/vllm#4635: [Bug]: Not picking up Neuron on instance (AssertionError: CUDA_HOME is not set)

| 字段 | 值 |
| --- | --- |
| Issue | [#4635](https://github.com/vllm-project/vllm/issues/4635) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Not picking up Neuron on instance (AssertionError: CUDA_HOME is not set)

### Issue 正文摘录

### Your current environment ```text Collecting environment information... /opt/conda/lib/python3.10/site-packages/transformers/utils/hub.py:124: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( WARNING 05-06 16:56:29 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For distributed inference, please install Ray with `pip install ray`. PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.10.12 | packaged by conda-forge | (main, Jun 23 2023, 22:40:32) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.10.214-202.855.amzn2.x86_64-x86_64-with-glibc2.31 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True C...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: tead. warnings.warn( WARNING 05-06 16:56:29 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For distributed inference, please install Ray with `pip install ray`. PyTorch version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Not picking up Neuron on instance (AssertionError: CUDA_HOME is not set) bug;stale ### Your current environment ```text Collecting environment information... /opt/conda/lib/python3.10/site-packages/transformers/u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: bug;stale ### Your current environment ```text Collecting environment information... /opt/conda/lib/python3.10/site-packages/transformers/utils/hub.py:124: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and wil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: picking up Neuron on instance (AssertionError: CUDA_HOME is not set) bug;stale ### Your current environment ```text Collecting environment information... /opt/conda/lib/python3.10/site-packages/transformers/utils/hub.py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: h-xla==2.1.2 [pip3] torchserve==0.10.0 [pip3] torchvision==0.16.2 [pip3] triton==2.1.0 [conda] mkl 2024.1.0 ha957f24_692 conda-forge [conda] mkl-include 2024.1.0 ha957f24_692 conda-forge [conda] numpy 1.25.2

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
