# vllm-project/vllm#11505: [Question]: vllm是否乐意支持基于其他人工智能框架的模型，如Mindspore，PaddlePaddle

| 字段 | 值 |
| --- | --- |
| Issue | [#11505](https://github.com/vllm-project/vllm/issues/11505) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Question]: vllm是否乐意支持基于其他人工智能框架的模型，如Mindspore，PaddlePaddle

### Issue 正文摘录

### 🚀 The feature, motivation and pitch 你好！目前vllm支持的模型大多是pytorch实现的模型，想问一下vllm是否愿意支持基于其他人工智能框架的模型呢？现在paddlepaddle的一些模型也已经集成到了huggingface上 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 模型大多是pytorch实现的模型，想问一下vllm是否愿意支持基于其他人工智能框架的模型呢？现在paddlepaddle的一些模型也已经集成到了huggingface上 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Question]: vllm是否乐意支持基于其他人工智能框架的模型，如Mindspore，PaddlePaddle feature request ### 🚀 The feature, motivation and pitch 你好！目前vllm支持的模型大多是pytorch实现的模型，想问一下vllm是否愿意支持基于其他人工智能框架的模型呢？现在paddlepaddle的一些模型也已经集成到了huggingface上 ### A...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
