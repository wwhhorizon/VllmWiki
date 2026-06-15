# vllm-project/vllm#1671: when load baichuan-7b   in  28G memory

| 字段 | 值 |
| --- | --- |
| Issue | [#1671](https://github.com/vllm-project/vllm/issues/1671) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> when load baichuan-7b   in  28G memory

### Issue 正文摘录

compare three mode huggingface load baichuan7B lightllm load baichuan7B vllm load baichuan7B find vllm use more memory why vllm cost more memory，use gunicorn or something wrong？ ![image](https://github.com/vllm-project/vllm/assets/38561924/0559f0ed-74bc-4426-a73a-44e139625945)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: when load baichuan-7b in 28G memory compare three mode huggingface load baichuan7B lightllm load baichuan7B vllm load baichuan7B find vllm use more memory why vllm cost more memory，use gunicorn or something wrong？ ![ima...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
