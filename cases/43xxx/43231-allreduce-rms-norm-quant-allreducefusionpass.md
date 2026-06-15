# vllm-project/vllm#43231: `allreduce + rms_norm[+quant]` (`AllReduceFusionPass`)

| 字段 | 值 |
| --- | --- |
| Issue | [#43231](https://github.com/vllm-project/vllm/issues/43231) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> `allreduce + rms_norm[+quant]` (`AllReduceFusionPass`)

### Issue 正文摘录

_本地原始数据中没有 issue 正文。_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: `allreduce + rms_norm[+quant]` (`AllReduceFusionPass`)

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
