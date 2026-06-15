# vllm-project/vllm#1530: What are the ways we can change the system prompt template?

| 字段 | 值 |
| --- | --- |
| Issue | [#1530](https://github.com/vllm-project/vllm/issues/1530) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What are the ways we can change the system prompt template?

### Issue 正文摘录

Hi, can you direct me to where can I edit the system prompts for chat models? I tried vllm (editing the endpoint code of `async def generate()` with Zephyr-7B and the results in terms of speed and accuracy is pretty good but **I think it will be even better if I can tweak the default system prompt** to according to my task. Currently, I can only edit the prompts going into `engine.generate(prompt....)` Thanks in advance.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ync def generate()` with Zephyr-7B and the results in terms of speed and accuracy is pretty good but **I think it will be even better if I can tweak the default system prompt** to according to my task. Currently, I can...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e? Hi, can you direct me to where can I edit the system prompts for chat models? I tried vllm (editing the endpoint code of `async def generate()` with Zephyr-7B and the results in terms of speed and accuracy is pretty...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ync def generate()` with Zephyr-7B and the results in terms of speed and accuracy is pretty good but **I think it will be even better if I can tweak the default system prompt** to according to my task. Currently, I can...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
