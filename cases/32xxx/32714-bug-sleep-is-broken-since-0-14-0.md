# vllm-project/vllm#32714: [Bug]: ❗️ Sleep is broken since 0.14.0 ❗️

| 字段 | 值 |
| --- | --- |
| Issue | [#32714](https://github.com/vllm-project/vllm/issues/32714) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ❗️ Sleep is broken since 0.14.0 ❗️

### Issue 正文摘录

### Your current environment -- ### 🐛 Describe the bug In v 0.13.0 sleep level 1 with 4x3090 and qwen3 30b model results in 1.14Gb used on each GPU after sleep enabled. Sleep is freed 20Gb+ In v 0.14 sleep level 1 results in 16Gb used on each GPU after sleep enabled, tested multiple times, sleep is freed ~6GB. Reverting to 0.13 fixes problem. Using official docker images. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e times, sleep is freed ~6GB. Reverting to 0.13 fixes problem. Using official docker images. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t -- ### 🐛 Describe the bug In v 0.13.0 sleep level 1 with 4x3090 and qwen3 30b model results in 1.14Gb used on each GPU after sleep enabled. Sleep is freed 20Gb+ In v 0.14 sleep level 1 results in 16Gb used on each GPU...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 0.14 sleep level 1 results in 16Gb used on each GPU after sleep enabled, tested multiple times, sleep is freed ~6GB. Reverting to 0.13 fixes problem. Using official docker images. ### Before submitting a new issue... -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
