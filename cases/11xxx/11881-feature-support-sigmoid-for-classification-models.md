# vllm-project/vllm#11881: [Feature]: Support sigmoid for classification models

| 字段 | 值 |
| --- | --- |
| Issue | [#11881](https://github.com/vllm-project/vllm/issues/11881) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support sigmoid for classification models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Right now, we only support softmax for classification models but sigmoid is equally as prevalent, depending on the usecase. I think the simplest way is just to return the logits and let us handle it ourselves. Alternatively, returning both softmax and sigmoid is probably not too much more computation. ### Additional context See: https://wandb.ai/amanarora/Written-Reports/reports/Understanding-Logits-Sigmoid-Softmax-and-Cross-Entropy-Loss-in-Deep-Learning--Vmlldzo0NDMzNTU3#conclusion > Thus, sigmoid is preferred for binary & multi-label classification problems whereas softmax is preferred for multi-class classification problems where we want the model to “pick a class”. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support sigmoid for classification models feature request;stale ### 🚀 The feature, motivation and pitch Right now, we only support softmax for classification models but sigmoid is equally as prevalent, depend...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ly support softmax for classification models but sigmoid is equally as prevalent, depending on the usecase. I think the simplest way is just to return the logits and let us handle it ourselves. Alternatively, returning...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s”. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support sigmoid for classification models feature request;stale ### 🚀 The feature, motivation and pitch Right now, we only support softmax for classification models but sigmoid is equally as prevalent, depend...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
