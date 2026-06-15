# vllm-project/vllm#1566: Tensor parallelism on ray cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#1566](https://github.com/vllm-project/vllm/issues/1566) |
| 状态 | closed |
| 标签 |  |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tensor parallelism on ray cluster

### Issue 正文摘录

I am using vllm on a ray cluster, multiple nodes and 4 gpus on each node. I am trying to load llama model with more than one gpu by setting tensor_parallel_size=2. The model won't load. It works fine on a single instance when I don't use a ray cluster. I can only set tensor_parallel_size=1 on ray cluster. Is there a way to use tensor parallelism on a ray cluster?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ray cluster, multiple nodes and 4 gpus on each node. I am trying to load llama model with more than one gpu by setting tensor_parallel_size=2. The model won't load. It works fine on a single instance when I don't use a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Tensor parallelism on ray cluster I am using vllm on a ray cluster, multiple nodes and 4 gpus on each node. I am trying to load llama model with more than one gpu by setting tensor_parallel_size=2. The model won't load....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
