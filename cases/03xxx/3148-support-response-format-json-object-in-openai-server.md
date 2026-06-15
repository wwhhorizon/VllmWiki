# vllm-project/vllm#3148: Support `response_format: json_object` in OpenAI server

| 字段 | 值 |
| --- | --- |
| Issue | [#3148](https://github.com/vllm-project/vllm/issues/3148) |
| 状态 | closed |
| 标签 | help wanted;good first issue |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support `response_format: json_object` in OpenAI server

### Issue 正文摘录

We just merged the support for structured generation support with Outlines. The next step is to integreate with Grammar based finite state machine https://github.com/outlines-dev/outlines/pull/541 into vLLM to support arbitrary JSON format.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Support `response_format: json_object` in OpenAI server help wanted;good first issue We just merged the support for structured generation support with Outlines. The next step is to integreate with Grammar based finite s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
