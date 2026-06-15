# vllm-project/vllm#14740: [Usage]: How to deploy DeepSeek R1 in a K8s environment

| 字段 | 值 |
| --- | --- |
| Issue | [#14740](https://github.com/vllm-project/vllm/issues/14740) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to deploy DeepSeek R1 in a K8s environment

### Issue 正文摘录

### Your current environment ```text I have 4 A100 GPUs. Each GPU has 8 cards. Since DeepSeek has over 640GB of memory, I need to deploy it using RayCluster. So I successfully deployed it using Docker by following the vllm guide. https://docs.vllm.ai/en/latest/serving/distributed_serving.html#running-vllm-on-multiple-nodes I want to do this in a k8s environment. Because it is an operational environment, I want to launch multiple pods. How can I do this? I would appreciate it if you could share a yaml example. ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: need to deploy it using RayCluster. So I successfully deployed it using Docker by following the vllm guide. https://docs.vllm.ai/en/latest/serving/distributed_serving.html#running-vllm-on-multiple-nodes I want to do thi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n a K8s environment usage ### Your current environment ```text I have 4 A100 GPUs. Each GPU has 8 cards. Since DeepSeek has over 640GB of memory, I need to deploy it using RayCluster. So I successfully deployed it using...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: d it using Docker by following the vllm guide. https://docs.vllm.ai/en/latest/serving/distributed_serving.html#running-vllm-on-multiple-nodes I want to do this in a k8s environment. Because it is an operational environm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
