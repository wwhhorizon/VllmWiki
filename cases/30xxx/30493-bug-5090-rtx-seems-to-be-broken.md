# vllm-project/vllm#30493: [Bug]: 5090 RTX seems to be broken

| 字段 | 值 |
| --- | --- |
| Issue | [#30493](https://github.com/vllm-project/vllm/issues/30493) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;gemm;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 5090 RTX seems to be broken

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 5090 RTX support seems to be broken, mainly because of an incompatibility between the 5090 / cuda 12.9 and pytorch 2.9. Either using cuda 12.9 via `cuda-compat-12-9` or via the official pytorch docker image `ghcr.io/pytorch/pytorch:2.9.1-cuda12.9-cudnn9-devel` results in `Unexpected error from cudaGetDeviceCount()`. Running vLLM with cuda12.8 results in `torch.AcceleratorError: CUDA error: the provided PTX was compiled with an unsupported toolchain`. The strange thing is that `cuda-compat-12-9` works fine with the RTX PRO 6000. Unfortunately it's not possible to run cuda13 because of driver issues. I see a similar issue here , but it doesn't seem to be solved 🤔 Any tips would be super helpful, thank you very much 🙏 ``` python3 -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-VL-8B-Instruct-FP8 \ --async-scheduling \ --skip-mm-profiling \ --host 0.0.0.0 \ --port 8000 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: orch 2.9. Either using cuda 12.9 via `cuda-compat-12-9` or via the official pytorch docker image `ghcr.io/pytorch/pytorch:2.9.1-cuda12.9-cudnn9-devel` results in `Unexpected error from cudaGetDeviceCount()`. Running vLL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: lm.entrypoints.openai.api_server \ --model Qwen/Qwen3-VL-8B-Instruct-FP8 \ --async-scheduling \ --skip-mm-profiling \ --host 0.0.0.0 \ --port 8000 ``` ### Before submitting a new issue... - [x] Make sure you already sea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: 5090 RTX seems to be broken bug ### Your current environment ### 🐛 Describe the bug 5090 RTX support seems to be broken, mainly because of an incompatibility between the 5090 / cuda 12.9 and pytorch 2.9. Either u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: very much 🙏 ``` python3 -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-VL-8B-Instruct-FP8 \ --async-scheduling \ --skip-mm-profiling \ --host 0.0.0.0 \ --port 8000 ``` ### Before submitting a new issue... -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: l Qwen/Qwen3-VL-8B-Instruct-FP8 \ --async-scheduling \ --skip-mm-profiling \ --host 0.0.0.0 \ --port 8000 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
