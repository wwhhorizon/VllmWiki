# vllm-project/vllm#811: Is that possible to do one_step forward in vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#811](https://github.com/vllm-project/vllm/issues/811) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is that possible to do one_step forward in vllm?

### Issue 正文摘录

I want to have one step forward and output only one token in each step like: `output = model.generate(prompt=prompt, past_key_value=past_key_value)` This is super important for streaming output. Is this possible in vllm?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l.generate(prompt=prompt, past_key_value=past_key_value)` This is super important for streaming output. Is this possible in vllm?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: one step forward and output only one token in each step like: `output = model.generate(prompt=prompt, past_key_value=past_key_value)` This is super important for streaming output. Is this possible in vllm?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
