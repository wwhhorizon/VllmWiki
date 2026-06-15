# vllm-project/vllm#31424: [Bug]: NVIDIA NGC container nvcr.io/nvidia/vllm:25.12-py3 ships outdated vLLM 0.11.1 instead of 0.13.x

| 字段 | 值 |
| --- | --- |
| Issue | [#31424](https://github.com/vllm-project/vllm/issues/31424) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVIDIA NGC container nvcr.io/nvidia/vllm:25.12-py3 ships outdated vLLM 0.11.1 instead of 0.13.x

### Issue 正文摘录

### Your current environment Environment Container: nvcr.io/nvidia/vllm:25.12-py3 CUDA: 13.1 GPU: NVIDIA RTX 6000 Blackwell (SM120) ### 🐛 Describe the bug Bug Description The latest NVIDIA NGC vLLM container (nvcr.io/nvidia/vllm:25.12-py3, December 2025 release) ships with a significantly outdated version of vLLM. Expected: vLLM 0.13.x (current stable release) Actual: NVIDIA Release 25.12 (build 245720121) vLLM Version 0.11.1+9114fd76 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: NVIDIA NGC container nvcr.io/nvidia/vllm:25.12-py3 ships outdated vLLM 0.11.1 instead of 0.13.x bug;stale ### Your current environment Environment Container: nvcr.io/nvidia/vllm:25.12-py3 CUDA: 13.1 GPU: NVIDIA R...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lm:25.12-py3, December 2025 release) ships with a significantly outdated version of vLLM. Expected: vLLM 0.13.x (current stable release) Actual: NVIDIA Release 25.12 (build 245720121) vLLM Version 0.11.1+9114fd76 ### Be...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: o/nvidia/vllm:25.12-py3 ships outdated vLLM 0.11.1 instead of 0.13.x bug;stale ### Your current environment Environment Container: nvcr.io/nvidia/vllm:25.12-py3 CUDA: 13.1 GPU: NVIDIA RTX 6000 Blackwell (SM120) ### 🐛 De...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: TX 6000 Blackwell (SM120) ### 🐛 Describe the bug Bug Description The latest NVIDIA NGC vLLM container (nvcr.io/nvidia/vllm:25.12-py3, December 2025 release) ships with a significantly outdated version of vLLM. Expected:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
