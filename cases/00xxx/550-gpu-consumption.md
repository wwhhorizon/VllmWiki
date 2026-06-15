# vllm-project/vllm#550: GPU consumption

| 字段 | 值 |
| --- | --- |
| Issue | [#550](https://github.com/vllm-project/vllm/issues/550) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GPU consumption

### Issue 正文摘录

when i load 13b llama in HF, GPU usage is about 26G. However, when load 13b llama in vllm, GPU usage is about 73G. Is this ususal?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: GPU consumption when i load 13b llama in HF, GPU usage is about 26G. However, when load 13b llama in vllm, GPU usage is about 73G. Is this ususal?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
