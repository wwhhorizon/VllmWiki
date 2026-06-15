# vllm-project/vllm#43499: [Feature]: Porting `AllReduceFusionPass` to manual fusion

| 字段 | 值 |
| --- | --- |
| Issue | [#43499](https://github.com/vllm-project/vllm/issues/43499) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Porting `AllReduceFusionPass` to manual fusion

### Issue 正文摘录

### 🚀 The feature, motivation and pitch See https://github.com/vllm-project/vllm/issues/43224 I'm working on prototyping this one, but will need help to apply+test to the wide variety of model architectures ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: this one, but will need help to apply+test to the wide variety of model architectures ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: typing this one, but will need help to apply+test to the wide variety of model architectures ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Porting `AllReduceFusionPass` to manual fusion feature request ### 🚀 The feature, motivation and pitch See https://github.com/vllm-project/vllm/issues/43224 I'm working on prototyping this one, but will need...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: /43224 I'm working on prototyping this one, but will need help to apply+test to the wide variety of model architectures ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new iss...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
