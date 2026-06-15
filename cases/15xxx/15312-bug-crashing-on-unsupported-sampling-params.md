# vllm-project/vllm#15312: [Bug]: Crashing on unsupported Sampling params

| 字段 | 值 |
| --- | --- |
| Issue | [#15312](https://github.com/vllm-project/vllm/issues/15312) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Crashing on unsupported Sampling params

### Issue 正文摘录

### Your current environment TPU v6e on GKE ### 🐛 Describe the bug Deploy the latest nightly: vllm/vllm-tpu:7297941b383a62d0212186f4615db857cd932b0 IF you have clients that set top_p to any value, vLLM crashes ![Image](https://github.com/user-attachments/assets/8e6ec212-6a11-4018-8c1e-ffcbb0c7c4be) Crashing the entire service due to an unsupported input seems at odds with building a reliable inference stack. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ashing the entire service due to an unsupported input seems at odds with building a reliable inference stack. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: k. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Crashing on unsupported Sampling params bug;stale ### Your current environment TPU v6e on GKE ### 🐛 Describe the bug Deploy the latest nightly: vllm/vllm-tpu:7297941b383a62d0212186f4615db857cd932b0 IF you have cl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: urrent environment TPU v6e on GKE ### 🐛 Describe the bug Deploy the latest nightly: vllm/vllm-tpu:7297941b383a62d0212186f4615db857cd932b0 IF you have clients that set top_p to any value, vLLM crashes ![Image](https://gi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
