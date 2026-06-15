# vllm-project/vllm#2118: How to configure which GPU to use

| 字段 | 值 |
| --- | --- |
| Issue | [#2118](https://github.com/vllm-project/vllm/issues/2118) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to configure which GPU to use

### Issue 正文摘录

there is no config parameter to configure which GPU to use,it always to find GPU:0 I want to change the GPU number,what should i do ? PS : i used os.environ["CUDA_VISIBLE_DEVICES"] = "3" but it also to run on GPU:0

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: want to change the GPU number,what should i do ? PS : i used os.environ["CUDA_VISIBLE_DEVICES"] = "3" but it also to run on GPU:0
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How to configure which GPU to use there is no config parameter to configure which GPU to use,it always to find GPU:0 I want to change the GPU number,what should i do ? PS : i used os.environ["CUDA_VISIBLE_DEVICES"] = "3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
