# vllm-project/vllm#7342: [Bug]: `ops.scaled_fp8_quant` returns wrong shape when input shape is ()

| 字段 | 值 |
| --- | --- |
| Issue | [#7342](https://github.com/vllm-project/vllm/issues/7342) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `ops.scaled_fp8_quant` returns wrong shape when input shape is ()

### Issue 正文摘录

### Your current environment Main ### 🐛 Describe the bug `ops.scaled_fp8_quant` returns wrong shape when input shape is () Discovered in https://github.com/vllm-project/vllm/pull/7324

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: `ops.scaled_fp8_quant` returns wrong shape when input shape is () bug ### Your current environment Main ### 🐛 Describe the bug `ops.scaled_fp8_quant` returns wrong shape when input shape is () Discovered in https...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
