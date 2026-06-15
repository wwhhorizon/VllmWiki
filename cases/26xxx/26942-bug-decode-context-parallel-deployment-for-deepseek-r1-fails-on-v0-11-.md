# vllm-project/vllm#26942: [Bug]: --decode-context-parallel deployment for DeepSeek-R1 fails on v0.11.0 but works on v0.10.2

| 字段 | 值 |
| --- | --- |
| Issue | [#26942](https://github.com/vllm-project/vllm/issues/26942) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --decode-context-parallel deployment for DeepSeek-R1 fails on v0.11.0 but works on v0.10.2

### Issue 正文摘录

### Your current environment . ### 🐛 Describe the bug Deploying deepseek-ai/DeepSeek-R1-0528 with decode context parallelism enabled succeeds on vLLM 0.10.2 but fails on vLLM 0.11.0 with the same hardware/flags. Logs for both cases are attached. Environment: Model: deepseek-ai/DeepSeek-R1-0528 GPU: NVIDIA H200-PCIe-141GB GPU (4x, single node), TP=4 NVIDIA driver version: 570.148.08 CUDA version: 12.8 NCCL: 2.27.3 vLLM versions tested: 0.10.2 — deployment runs successfully. 0.11.0 — deployment fails to start serving (see attached log). Runtime args: max-model-len: 8192 tensor-parallel-size: 8 decode-context-parallel-size: 8 gpu-memory-utilization: 0.92 no-enable-prefix-caching: True uvicorn-log-level: debug trust-remote-code: True disable-log-requests: True Attached logs: https://gist.github.com/Harshith-umesh/897a31785da0395f2ace594aec4ec677 — successful run (shows vLLM 0.10.2 and DCP=8). https://gist.github.com/Harshith-umesh/6cfb9f2a0d3a8485e27567f554bfce24 — failing run (shows vLLM 0.11.0 and DCP=8). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](h...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ed. Environment: Model: deepseek-ai/DeepSeek-R1-0528 GPU: NVIDIA H200-PCIe-141GB GPU (4x, single node), TP=4 NVIDIA driver version: 570.148.08 CUDA version: 12.8 NCCL: 2.27.3 vLLM versions tested: 0.10.2 — deployment ru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: bug Deploying deepseek-ai/DeepSeek-R1-0528 with decode context parallelism enabled succeeds on vLLM 0.10.2 but fails on vLLM 0.11.0 with the same hardware/flags. Logs for both cases are attached. Environment: Model: dee...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: --decode-context-parallel deployment for DeepSeek-R1 fails on v0.11.0 but works on v0.10.2 bug;stale ### Your current environment . ### 🐛 Describe the bug Deploying deepseek-ai/DeepSeek-R1-0528 with decode contex...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: he same hardware/flags. Logs for both cases are attached. Environment: Model: deepseek-ai/DeepSeek-R1-0528 GPU: NVIDIA H200-PCIe-141GB GPU (4x, single node), TP=4 NVIDIA driver version: 570.148.08 CUDA version: 12.8 NCC...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: driver version: 570.148.08 CUDA version: 12.8 NCCL: 2.27.3 vLLM versions tested: 0.10.2 — deployment runs successfully. 0.11.0 — deployment fails to start serving (see attached log). Runtime args: max-model-len: 8192 te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
