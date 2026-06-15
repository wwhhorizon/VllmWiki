# vllm-project/vllm#24650: [Feature]: support messages input for classify api skywork-reward model

| 字段 | 值 |
| --- | --- |
| Issue | [#24650](https://github.com/vllm-project/vllm/issues/24650) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support messages input for classify api skywork-reward model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the current inference of reward models, classification models are often used, such as the skywork reward model. There is an issue where the concepts and actual functions of several existing interfaces do not correspond: 1. The reward interface does not return the score of the BT model (pooling method and softmax also need to be considered). 2. The classification model is restricted to using only the classify interface, but this interface does not support message input. 3. If classify can only use list[str], there seems to be no apply_chat_template interface (it is not desirable to place too many elements on the client side). Thanks. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: support messages input for classify api skywork-reward model feature request;stale ### 🚀 The feature, motivation and pitch In the current inference of reward models, classification models are often used, such as the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: support messages input for classify api skywork-reward model feature request;stale ### 🚀 The feature, motivation and pitch In the current inference of reward models, classification models are often used, such...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
