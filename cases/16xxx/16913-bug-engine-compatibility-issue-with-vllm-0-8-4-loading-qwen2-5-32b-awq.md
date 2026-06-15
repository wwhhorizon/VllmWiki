# vllm-project/vllm#16913: [Bug]:Engine Compatibility Issue with vllm 0.8.4 Loading Qwen2.5-32B-AWQ: Abnormal Behavior of v1 Engine Under High Concurrency and Solutions

| 字段 | 值 |
| --- | --- |
| Issue | [#16913](https://github.com/vllm-project/vllm/issues/16913) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:Engine Compatibility Issue with vllm 0.8.4 Loading Qwen2.5-32B-AWQ: Abnormal Behavior of v1 Engine Under High Concurrency and Solutions

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I load Qwen2.5-32B-AWQ using vllm 0.8.4, the default engine used is v1. When the concurrency exceeds a certain level, the model output becomes abnormal — sometimes it outputs only one or two characters, and other times it endlessly repeats meaningless content. However, when I forcibly switch to using the v0 engine, everything returns to normal. This issue occurs when using A100-40G, 4090, and 4090 GPUs, but does not happen with H20 or H800 GPUs. ![Image](https://github.com/user-attachments/assets/3c3b1ddc-6a9b-4ab6-899d-413b0dd03542) ![Image](https://github.com/user-attachments/assets/6a4ddc9c-4440-42f7-8117-eafa5ae07199) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: he v0 engine, everything returns to normal. This issue occurs when using A100-40G, 4090, and 4090 GPUs, but does not happen with H20 or H800 GPUs. ![Image](https://github.com/user-attachments/assets/3c3b1ddc-6a9b-4ab6-8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]:Engine Compatibility Issue with vllm 0.8.4 Loading Qwen2.5-32B-AWQ: Abnormal Behavior of v1 Engine Under High Concurrency and Solutions bug;stale ### Your current environment ### 🐛 Describe the bug When I load Qwe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: other times it endlessly repeats meaningless content. However, when I forcibly switch to using the v0 engine, everything returns to normal. This issue occurs when using A100-40G, 4090, and 4090 GPUs, but does not happen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Abnormal Behavior of v1 Engine Under High Concurrency and Solutions bug;stale ### Your current environment ### 🐛 Describe the bug When I load Qwen2.5-32B-AWQ using vllm 0.8.4, the default engine used is v1. When the con...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
