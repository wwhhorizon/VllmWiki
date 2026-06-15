# vllm-project/vllm#4439: [Bug]: OpenAI API request doesn't go through with 'guided_json'

| 字段 | 值 |
| --- | --- |
| Issue | [#4439](https://github.com/vllm-project/vllm/issues/4439) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenAI API request doesn't go through with 'guided_json'

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 14.4.1 (arm64) GCC version: Could not collect Clang version: 15.0.0 (clang-1500.3.9.4) CMake version: Could not collect Libc version: N/A Python version: 3.11.2 (main, Sep 24 2023, 00:07:45) [Clang 15.0.0 (clang-1500.0.38.1)] (64-bit runtime) Python platform: macOS-14.4.1-arm64-arm-64bit Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Apple M1 Versions of relevant libraries: [pip3] flake8==6.0.0 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.3 [pip3] onnx==1.15.0 [pip3] onnxruntime==1.17.3 [pip3] torch==2.3.0 [pip3] torchaudio==2.1.1 [pip3] torchvision==0.16.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: Could not collect ``` ### 🐛 Descri...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 14.4.1 (arm64) GCC version: Could n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 14.4.1 (arm64) GCC version: Could not collect Clang version: 15.0.0 (cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 14.4.1 (arm64)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 14.4.1 (arm64) GCC version: Could not collect Clang version: 15.0.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: OpenAI API request doesn't go through with 'guided_json' bug;stale ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
