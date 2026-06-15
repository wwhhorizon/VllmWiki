# vllm-project/vllm#38176: [Bug]: qwen3 235B model with latest vllm is going to generate only 1 token.

| 字段 | 值 |
| --- | --- |
| Issue | [#38176](https://github.com/vllm-project/vllm/issues/38176) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen3 235B model with latest vllm is going to generate only 1 token.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug after I upgraded to the latest vllm version, qwen3 235b can't produce any tokens. not sure where is the problem. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen3 235B model with latest vllm is going to generate only 1 token. bug ### Your current environment ### 🐛 Describe the bug after I upgraded to the latest vllm version, qwen3 235b can't produce any tokens. not s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ironment ### 🐛 Describe the bug after I upgraded to the latest vllm version, qwen3 235b can't produce any tokens. not sure where is the problem. ### Before submitting a new issue... - [x] Make sure you already searched...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: em. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: qwen3 235B model with latest vllm is going to generate only 1 token. bug ### Your current environment ### 🐛 Describe the bug after I upgraded to the latest vllm version, qwen3 235b can't produce any tokens. not s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
