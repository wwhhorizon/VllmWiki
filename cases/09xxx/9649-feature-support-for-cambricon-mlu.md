# vllm-project/vllm#9649: [Feature]: support for Cambricon MLU

| 字段 | 值 |
| --- | --- |
| Issue | [#9649](https://github.com/vllm-project/vllm/issues/9649) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support for Cambricon MLU

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am a developer from Cambricon, an AI chip vendor in China. We have already supported vLLM 0.6.1.post2 on Cambricon MLU internally. We wish to contribute the MLU adaptation code to the vLLM project, and the pull request (PR) will be ready in November. Additionally, we welcome contributions from other developers. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e feature, motivation and pitch I am a developer from Cambricon, an AI chip vendor in China. We have already supported vLLM 0.6.1.post2 on Cambricon MLU internally. We wish to contribute the MLU adaptation code to the v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support for Cambricon MLU feature request;stale ### 🚀 The feature, motivation and pitch I am a developer from Cambricon, an AI chip vendor in China. We have already supported vLLM 0.6.1.post2 on Cambricon MLU...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
