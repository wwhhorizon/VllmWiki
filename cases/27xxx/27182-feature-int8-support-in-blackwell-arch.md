# vllm-project/vllm#27182: [Feature]: INT8 Support in Blackwell Arch

| 字段 | 值 |
| --- | --- |
| Issue | [#27182](https://github.com/vllm-project/vllm/issues/27182) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: INT8 Support in Blackwell Arch

### Issue 正文摘录

### 🚀 The feature, motivation and pitch hello, I want to use w8a8(int8) in blackwell gpus, and when I read the source code, it says, the int8 is not support by sm120. According to the nvidia-ptx-instructions, blackwell series gpus still have a int8 tensor, is there another way we use w8a8 int8 in rtx5090 by vllm now ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature]: INT8 Support in Blackwell Arch feature request;stale ### 🚀 The feature, motivation and pitch hello, I want to use w8a8(int8) in blackwell gpus, and when I read the source code, it says, the int8 is not suppor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: INT8 Support in Blackwell Arch feature request;stale ### 🚀 The feature, motivation and pitch hello, I want to use w8a8(int8) in blackwell gpus, and when I read the source code, it says, the int8 is not suppor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
