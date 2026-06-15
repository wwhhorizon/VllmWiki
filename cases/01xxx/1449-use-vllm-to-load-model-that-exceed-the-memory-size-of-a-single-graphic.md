# vllm-project/vllm#1449: Use vLLM to load model that exceed the memory size of a single graphics card

| 字段 | 值 |
| --- | --- |
| Issue | [#1449](https://github.com/vllm-project/vllm/issues/1449) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Use vLLM to load model that exceed the memory size of a single graphics card

### Issue 正文摘录

Can increasing tensor_parallel_size parameter solve the problem that the single graphics card's memory is not enough to deploy the model? Apart from modifying this parameter, is there any way to solve this problem when loading the model using vLLM?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Use vLLM to load model that exceed the memory size of a single graphics card Can increasing tensor_parallel_size parameter solve the problem that the single graphics card's memory is not enough to deploy the model? Apar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
