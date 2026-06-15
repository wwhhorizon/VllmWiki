# vllm-project/vllm#34586: [Bug]: RTX 6000 Pro Workstation Edition isn't supported by torch inside docker container

| 字段 | 值 |
| --- | --- |
| Issue | [#34586](https://github.com/vllm-project/vllm/issues/34586) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RTX 6000 Pro Workstation Edition isn't supported by torch inside docker container

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Docker image doesn't support RTX 6000 Pro Blackwell Workstation Edition ```docker docker run --rm --gpus all --entrypoint /usr/bin/python3 vllm/vllm-openai:cu130-nightly -c "import torch; print(torch.__version__); print(torch.version.cuda); print(torch.cuda.is_available())" ``` /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:184: UserWarning: CUDA initialization: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 803: system has unsupported display driver / cuda driver combination (Triggered internally at /pytorch/c10/cuda/CUDAFunctions.cpp:119.) return torch._C._cuda_getDeviceCount() > 0 2.10.0+cu130 13.0 False ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: RTX 6000 Pro Workstation Edition isn't supported by torch inside docker container bug;stale ### Your current environment ### 🐛 Describe the bug Docker image doesn't support RTX 6000 Pro Blackwell Workstation Edit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: RTX 6000 Pro Workstation Edition isn't supported by torch inside docker container bug;stale ### Your current environment ### 🐛 Describe the bug Docker image doesn't support RTX 6000 Pro Blackwell Workstation Edit...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: p:119.) return torch._C._cuda_getDeviceCount() > 0 2.10.0+cu130 13.0 False ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Workstation Edition isn't supported by torch inside docker container bug;stale ### Your current environment ### 🐛 Describe the bug Docker image doesn't support RTX 6000 Pro Blackwell Workstation Edition ```docker docker...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;hardware_porting cuda crash env_dependency Your current environm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
