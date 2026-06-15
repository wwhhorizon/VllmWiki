# vllm-project/vllm#1979: StarCoder-trained VLLM vs. HF: Why the output is different?

| 字段 | 值 |
| --- | --- |
| Issue | [#1979](https://github.com/vllm-project/vllm/issues/1979) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> StarCoder-trained VLLM vs. HF: Why the output is different?

### Issue 正文摘录

Hi, Thank you very much for your contributions to inference acceleration. I am currently having a problem. I am using a model trained by StarCoder, and I am using the same input ids for inference. However, I found that the output of vllm is very different from the output of HF. vllm seems to be constantly outputting ```\n```. How can I solve this problem? Thank you for your help.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: StarCoder-trained VLLM vs. HF: Why the output is different? Hi, Thank you very much for your contributions to inference acceleration. I am currently having a problem. I am using a model trained by StarCoder, and I am us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
