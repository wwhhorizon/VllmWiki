# vllm-project/vllm#578: vocab size cannot be divided by num GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#578](https://github.com/vllm-project/vllm/issues/578) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vocab size cannot be divided by num GPUs

### Issue 正文摘录

We have a Chinese llama model with a 49954 vocab size, where 49954=24977*2, and 24977 is seemed to be a prime. We want to use vLLM to serve our model on 16GPUs, but 49954 cannot be divided by 16. Our vocab size cannot be changed recently. Is there any method to solve our serving problem? (I think it's quite unreasonable, if we want to serve our model using vLLM, we can only use 2GPUs or 24977 GPUs?)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vocab size cannot be divided by num GPUs We have a Chinese llama model with a 49954 vocab size, where 49954=24977*2, and 24977 is seemed to be a prime. We want to use vLLM to serve our model on 16GPUs, but 49954 cannot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
