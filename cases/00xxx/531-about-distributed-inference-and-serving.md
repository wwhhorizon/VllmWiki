# vllm-project/vllm#531: About Distributed Inference and Serving

| 字段 | 值 |
| --- | --- |
| Issue | [#531](https://github.com/vllm-project/vllm/issues/531) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> About Distributed Inference and Serving

### Issue 正文摘录

We are now using some RTX4090(24G) cards to load the vicuna-13b(30G of one model). Can we set the number of loading parameters on each graphics card? Requirements :4 graphics cards loaded 3 models, 24*4/3 = 32G。

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: About Distributed Inference and Serving We are now using some RTX4090(24G) cards to load the vicuna-13b(30G of one model). Can we set the number of loading parameters on each graphics card? Requirements :4 graphics card...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: are now using some RTX4090(24G) cards to load the vicuna-13b(30G of one model). Can we set the number of loading parameters on each graphics card? Requirements :4 graphics cards loaded 3 models, 24*4/3 = 32G。

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
