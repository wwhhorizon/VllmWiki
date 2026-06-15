# vllm-project/vllm#977: Potential Speedup for model loading: populating sin-cos cache is slow / repeated 

| 字段 | 值 |
| --- | --- |
| Issue | [#977](https://github.com/vllm-project/vllm/issues/977) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Potential Speedup for model loading: populating sin-cos cache is slow / repeated 

### Issue 正文摘录

## Why startup times are important for some users ## In production some use autoscaling in order to increase / decrease servers in response to demand. In this scenario startup times are super important because then you can respond quickly to changes in demand without users experiencing worse experience during changes. A build up of pending servers can cause technical issues like network overload. ## the issue ## When debugging our startup times I saw that populating the cos-sin cache in PagedAttentionWithRope is repeated work that is responsible for a lot of the startup times. For a 13B model it was responsible for about 35s out of 90s total model load times.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: g: populating sin-cos cache is slow / repeated ## Why startup times are important for some users ## In production some use autoscaling in order to increase / decrease servers in response to demand. In this scenario star...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Potential Speedup for model loading: populating sin-cos cache is slow / repeated ## Why startup times are important for some users ## In production some use autoscaling in order to increase / decrease servers in respons...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
