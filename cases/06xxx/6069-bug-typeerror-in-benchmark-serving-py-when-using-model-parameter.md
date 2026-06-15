# vllm-project/vllm#6069: [Bug]: TypeError in benchmark_serving.py when using --model parameter

| 字段 | 值 |
| --- | --- |
| Issue | [#6069](https://github.com/vllm-project/vllm/issues/6069) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError in benchmark_serving.py when using --model parameter

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Microsoft Windows 11 Pro GCC version: Could not collect Clang version: Could not collect CMake version: Could not collect Libc version: N/A Python version: 3.10.11 (tags/v3.10.11:7d4cc5a, Apr 5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] (64-bit runtime) Python platform: Windows-10-10.0.22621-SP0 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture=9 CurrentClockSpeed=1910 DeviceID=CPU0 Family=198 L2CacheSize=1024 L2CacheSpeed= Manufacturer=GenuineIntel MaxClockSpeed=2112 Name=Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz ProcessorType=3 Revision= Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] optree==0.11.0 [pip3] torch==2.3.1 [pip3] transformers==4.41.2 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM B...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Microsoft Windows 11 Pro GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: hon collect_env.py` ``` PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Microsoft Windows 11 Pro GCC version: Could not collect Clang version: Could...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: TypeError in benchmark_serving.py when using --model parameter bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.1+cpu Is debug build: False CUDA used t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: TypeError in benchmark_serving.py when using --model parameter bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ` **Root cause:** The issue lies in the get_model() function defined in backend_request_func.py. This function calls snapshot_download() from either modelscope or huggingface_hub depending on the VLLM_USE_MODELSCOPE env...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
