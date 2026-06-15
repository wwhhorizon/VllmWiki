# vllm-project/vllm#1410: Falcon-180B Quantization Support

| 字段 | 值 |
| --- | --- |
| Issue | [#1410](https://github.com/vllm-project/vllm/issues/1410) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Falcon-180B Quantization Support

### Issue 正文摘录

Love the LLAMA2-AWQ support, really handy! Are there any plans to support Falcon-180B-AWQ in the near future?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Falcon-180B Quantization Support Love the LLAMA2-AWQ support, really handy! Are there any plans to support Falcon-180B-AWQ in the near future?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Falcon-180B Quantization Support Love the LLAMA2-AWQ support, really handy! Are there any plans to support Falcon-180B-AWQ in the near future?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
