# vllm-project/vllm#1257: Option to not apply the frequency penalty to some tokens or strings.

| 字段 | 值 |
| --- | --- |
| Issue | [#1257](https://github.com/vllm-project/vllm/issues/1257) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Option to not apply the frequency penalty to some tokens or strings.

### Issue 正文摘录

I couldn't find any option to not apply the frequency penalty to some tokens or strings. One instance where this can be useful is when you want to use a frequency penalty to avoid repetitive output but this causes some output formats to break, e.g. when you need a list of dictionaries (a JSON output) where the keys of the dictionaries are the same. In such a scenario, a higher frequency penalty causes the format to break but a low penalty is not desirable as it causes repetitive language in the output. Can we add this feature? I'll be happy to work on it.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: frequency penalty to avoid repetitive output but this causes some output formats to break, e.g. when you need a list of dictionaries (a JSON output) where the keys of the dictionaries are the same. In such a scenario, a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
