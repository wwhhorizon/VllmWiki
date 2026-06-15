# vllm-project/vllm#4184: [Performance]: Questions about Distributed Inference: A comparison of the two deployment approaches

| 字段 | 值 |
| --- | --- |
| Issue | [#4184](https://github.com/vllm-project/vllm/issues/4184) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Questions about Distributed Inference: A comparison of the two deployment approaches

### Issue 正文摘录

### Misc discussion on performance When deploying two GPUs for a vllm service, there are two approaches. The first method involves starting two ports and services, with one vllm service running on each GPU, and using Nginx to implement load balancing. The second approach entails starting a single port and service, utilizing `tensor_parallel_size=2`, and distributing the model weights across different GPUs. Which of these methods is better, and why? This problem has been bothering me, I need your help, thank you.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vllm service running on each GPU, and using Nginx to implement load balancing. The second approach entails starting a single port and service, utilizing `tensor_parallel_size=2`, and distributing the model weights acros...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rt and service, utilizing `tensor_parallel_size=2`, and distributing the model weights across different GPUs. Which of these methods is better, and why? This problem has been bothering me, I need your help, thank you.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
