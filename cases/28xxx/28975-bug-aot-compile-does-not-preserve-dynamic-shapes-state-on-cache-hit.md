# vllm-project/vllm#28975: [Bug]: aot_compile does not preserve dynamic shapes state on cache hit.

| 字段 | 值 |
| --- | --- |
| Issue | [#28975](https://github.com/vllm-project/vllm/issues/28975) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: aot_compile does not preserve dynamic shapes state on cache hit.

### Issue 正文摘录

### Your current environment latest pytorch commit and latest vLLM commit. ### 🐛 Describe the bug ok on a cache hit more things are marked dynamic than needed, this seems very similar to what happen in https://github.com/vllm-project/vllm/issues/27899 (read my last comment) this is risky because marking more things dynamic with duck shapes can cause silent specialization that are not wanted. to repo run any model +dynamic logs For example for "Qwen/Qwen2-7B-Instruct" on a cold run we will see only three things dynamic. on a warm run we will see so many things marked dynamic. This is. BAD! We need to 1) disable automatic dynamic. 2) on a warm run know what things to be marked dynamic and mark them explicitly. OR serialize fake tensor for the warm run! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: aot_compile does not preserve dynamic shapes state on cache hit. bug;torch.compile ### Your current environment latest pytorch commit and latest vLLM commit. ### 🐛 Describe the bug ok on a cache hit more things a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: es can cause silent specialization that are not wanted. to repo run any model +dynamic logs For example for "Qwen/Qwen2-7B-Instruct" on a cold run we will see only three things dynamic. on a warm run we will see so many...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: aot_compile does not preserve dynamic shapes state on cache hit. bug;torch.compile ### Your current environment latest pytorch commit and latest vLLM commit. ### 🐛 Describe the bug ok on a cache hit more things a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: un! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: es state on cache hit. bug;torch.compile ### Your current environment latest pytorch commit and latest vLLM commit. ### 🐛 Describe the bug ok on a cache hit more things are marked dynamic than needed, this seems very si...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
