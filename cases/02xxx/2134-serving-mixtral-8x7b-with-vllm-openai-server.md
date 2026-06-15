# vllm-project/vllm#2134: Serving Mixtral 8x7B with vllm OpenAI Server

| 字段 | 值 |
| --- | --- |
| Issue | [#2134](https://github.com/vllm-project/vllm/issues/2134) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Serving Mixtral 8x7B with vllm OpenAI Server

### Issue 正文摘录

I want to serve Mixtral with the openai compatible server but its not obvious to me reading the documentation how to set: `tensor_parallel_size = 2` I have 2xA100s so i can split Mixtral across both GPUs but I dont see how to configure that anywhere... Is this even possible?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ding the documentation how to set: `tensor_parallel_size = 2` I have 2xA100s so i can split Mixtral across both GPUs but I dont see how to configure that anywhere... Is this even possible?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ve 2xA100s so i can split Mixtral across both GPUs but I dont see how to configure that anywhere... Is this even possible?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
