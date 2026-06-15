# vllm-project/vllm#822:  Why the vllm loading model has a large memory footprint

| 字段 | 值 |
| --- | --- |
| Issue | [#822](https://github.com/vllm-project/vllm/issues/822) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

>  Why the vllm loading model has a large memory footprint

### Issue 正文摘录

The normal loading of the baichuan-13b takes up about 25G of GPU, and the loading of vllm takes up 35G of GPU

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Why the vllm loading model has a large memory footprint The normal loading of the baichuan-13b takes up about 25G of GPU, and the loading of vllm takes up 35G of GPU

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
