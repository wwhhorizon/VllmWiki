# vllm-project/vllm#14933: [Usage]: Distributed inference not supported with OpenVINO?

| 字段 | 值 |
| --- | --- |
| Issue | [#14933](https://github.com/vllm-project/vllm/issues/14933) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Distributed inference not supported with OpenVINO?

### Issue 正文摘录

### How would you like to use vllm The [installation page for OpenVINO](https://docs.vllm.ai/en/latest/getting_started/installation/ai_accelerator.html?device=openvino) mentions using the environment variable "VLLM_OPENVINO_DEVICE to specify which device utilize for the inference. If there are multiple GPUs in the system, additional indexes can be used to choose the proper one (e.g, VLLM_OPENVINO_DEVICE=GPU.1). If the value is not specified, CPU device is used by default." So is it not possible to use multiple GPUs or GPU + CPU for running inference on OpenVINO backend? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rted with OpenVINO? usage;stale ### How would you like to use vllm The [installation page for OpenVINO](https://docs.vllm.ai/en/latest/getting_started/installation/ai_accelerator.html?device=openvino) mentions using the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ible to use multiple GPUs or GPU + CPU for running inference on OpenVINO backend? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nd? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Distributed inference not supported with OpenVINO? usage;stale ### How would you like to use vllm The [installation page for OpenVINO](https://docs.vllm.ai/en/latest/getting_started/installation/ai_accelerator....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: use vllm The [installation page for OpenVINO](https://docs.vllm.ai/en/latest/getting_started/installation/ai_accelerator.html?device=openvino) mentions using the environment variable "VLLM_OPENVINO_DEVICE to specify whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
