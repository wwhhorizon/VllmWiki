# vllm-project/vllm#15066: [Installation]: Build from source on macOS, unable to load _C.abi3.so

| 字段 | 值 |
| --- | --- |
| Issue | [#15066](https://github.com/vllm-project/vllm/issues/15066) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Build from source on macOS, unable to load _C.abi3.so

### Issue 正文摘录

### Your current environment ```text (py312) ❯ python collect_env.py vllm/git/main INFO 03-19 00:13:33 [__init__.py:256] Automatically detected platform cpu. Collecting environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 15.3.2 (arm64) GCC version: Could not collect Clang version: 16.0.0 (clang-1600.0.26.6) CMake version: version 3.30.5 Libc version: N/A Python version: 3.12.7 (main, Oct 16 2024, 07:12:08) [Clang 18.1.8 ] (64-bit runtime) Python platform: macOS-15.3.2-arm64-arm-64bit Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Apple M3 Max Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] pyzmq==26.3.0 [pip3] torch==2.5.1 [pip3] torchaudio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.49.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.8.0rc3.dev24+g027827cc vLLM Build Flags: CUDA Archs: Not Set; ROCm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: Build from source on macOS, unable to load _C.abi3.so installation ### Your current environment ```text (py312) ❯ python collect_env.py
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 15.3.2 (arm64) GCC version: Could not collect Clang version: 16.0.0 (cla...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: __.py:256] Automatically detected platform cpu. Collecting environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 15.3.2 (arm64...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ting environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: macOS 15.3.2 (arm64) GCC version: Could not collect Clang version: 16.0.0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting cuda build_error env_dependency Your current en...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
