# vllm-project/vllm#20669: [Feature]: Add Enable EPLB condition

| 字段 | 值 |
| --- | --- |
| Issue | [#20669](https://github.com/vllm-project/vllm/issues/20669) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Enable EPLB condition

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Current enable eplb after only check current platform wether is cuda, if current platform only a one cuda device, should eplb be disabled or given a warning? only one cuda device, ep is no't need load blancing. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d pitch Current enable eplb after only check current platform wether is cuda, if current platform only a one cuda device, should eplb be disabled or given a warning? only one cuda device, ep is no't need load blancing....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: bled or given a warning? only one cuda device, ep is no't need load blancing. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add Enable EPLB condition feature request ### 🚀 The feature, motivation and pitch Current enable eplb after only check current platform wether is cuda, if current platform only a one cuda device, should eplb...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
