# vllm-project/vllm#6747: [Bug]: Error message returning plain string instead of f-string in image token string retrieval 

| 字段 | 值 |
| --- | --- |
| Issue | [#6747](https://github.com/vllm-project/vllm/issues/6747) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error message returning plain string instead of f-string in image token string retrieval 

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: macOS 14.5 (arm64) GCC version: Could not collect Clang version: 15.0.0 (clang-1500.3.9.4) CMake version: version 3.29.6 Libc version: N/A Python version: 3.10.4 (main, Jun 10 2022, 09:56:45) [Clang 13.1.6 (clang-1316.0.21.2.5)] (64-bit runtime) Python platform: macOS-14.5-arm64-arm-64bit Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Apple M1 Max Versions of relevant libraries: [pip3] mypy-extensions==0.4.3 [pip3] numpy==1.23.4 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: Could not collect ``` ### 🐛 Describe the bug When calling a model that does not support images, such: ```request POST http://vllm:8000/chat/co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rrent environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: macOS 14.5 (arm64) GCC version: Could not coll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: macOS 14.5 (arm64) GCC version: Could not collect Clang version: 15.0.0 (clang...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eval bug ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: macOS 14.5 (arm64) GCC ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ibe the bug When calling a model that does not support images, such: ```request POST http://vllm:8000/chat/completion/v1 Content-Type: application/json Accept: application/json { "messages":[ { "role": "user", "content"...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ge returning plain string instead of f-string in image token string retrieval bug ### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build Py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
