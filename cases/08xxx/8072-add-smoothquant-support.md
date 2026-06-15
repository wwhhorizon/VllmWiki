# vllm-project/vllm#8072: Add smoothquant support 

| 字段 | 值 |
| --- | --- |
| Issue | [#8072](https://github.com/vllm-project/vllm/issues/8072) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add smoothquant support 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This is smoothquant: https://github.com/mit-han-lab/smoothquant It's awesome. It's been added in Aphrodite here: https://github.com/PygmalionAI/aphrodite-engine/pull/294 I would like to request smoothquant in vllm. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Add smoothquant support feature request ### 🚀 The feature, motivation and pitch This is smoothquant: https://github.com/mit-han-lab/smoothquant It's awesome. It's been added in Aphrodite here: https://github.com/Pygmalio
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Add smoothquant support feature request ### 🚀 The feature, motivation and pitch This is smoothquant: https://github.com/mit-han-lab/smoothquant It's awesome. It's been added in Aphrodite here: https://github.com/Pygmali...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Add smoothquant support feature request ### 🚀 The feature, motivation and pitch This is smoothquant: https://github.com/mit-han-lab/smoothquant It's awesome. It's been added in Aphrodite here: https://github.com/Pygmali...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
