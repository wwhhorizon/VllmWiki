# vllm-project/vllm#4865: [Usage]: distributed inference with kuberay

| 字段 | 值 |
| --- | --- |
| Issue | [#4865](https://github.com/vllm-project/vllm/issues/4865) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: distributed inference with kuberay

### Issue 正文摘录

### Your current environment kuberay，vllm 0.4.0 L40 GPU server *2， each one with L40*8, CX6 IB card 200G*2 ### How would you like to use vllm I plan to use KubeRay to implement multi-node distributed inference based on the vLLM framework. In the current environment, each GPU server node is interconnected with an IB network. How can I achieve RDMA between multiple nodes?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: distributed inference with kuberay usage;stale ### Your current environment kuberay，vllm 0.4.0 L40 GPU server *2， each one with L40*8, CX6 IB card 200G*2 ### How would you like to use vllm I plan to use KubeRay...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
