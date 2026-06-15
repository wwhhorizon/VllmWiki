# vllm-project/vllm#1676: Is there anyway to run 1+ vllm models in one process?

| 字段 | 值 |
| --- | --- |
| Issue | [#1676](https://github.com/vllm-project/vllm/issues/1676) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is there anyway to run 1+ vllm models in one process?

### Issue 正文摘录

When init 2 vllm models I got the following error: ``` assert _TENSOR_MODEL_PARALLEL_GROUP is None, ( AssertionError: tensor model parallel group is already initialized ``` Is there anyway to create multiple vllm model as my project require different conversation outputs from different models

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Is there anyway to run 1+ vllm models in one process? When init 2 vllm models I got the following error: ``` assert _TENSOR_MODEL_PARALLEL_GROUP is None, ( AssertionError: tensor model parallel group is already initiali...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
