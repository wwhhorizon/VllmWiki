# vllm-project/vllm#3902: [Feature]: Support Ray-free multi-node distributed inference on resource managers like Kubernetes

| 字段 | 值 |
| --- | --- |
| Issue | [#3902](https://github.com/vllm-project/vllm/issues/3902) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Ray-free multi-node distributed inference on resource managers like Kubernetes

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, distributed inference (TP) in vLLM relies on ray to orchestrate the gpu workers. I briefly check the code and seems the core distributed communication is provided by `torch.distributed` with nccl backend, actor's communication is not done in Ray's own protocol. In this case, Ray just plays the role of orchestration and resource reservation (placement group). Please correct me if I am wrong. We do use Ray and KubeRay on Kubernetes and I've successfully tested vLLM distributed inference on this setup, confirming its functional operation. However, we have many users/platforms, we do not want to lock on Ray since some teams may not have enough Ray knowledge to cover the operation. My proposal is to provide a simple orchestration on top of `GPUExecutor` for those users who are familiar with cloud native techs. They would like to use Kubernetes's capability for orchestration (ray actors) and scheduling (placement group). Ideally, we would have both Ray and Kubernetes as orchestrators for vLLMs, providing our platform users with alternative options for their needs. Please help check whether this proposal makes sense. I can contribute to...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -node distributed inference on resource managers like Kubernetes feature request;stale ### 🚀 The feature, motivation and pitch Currently, distributed inference (TP) in vLLM relies on ray to orchestrate the gpu workers....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e distributed communication is provided by `torch.distributed` with nccl backend, actor's communication is not done in Ray's own protocol. In this case, Ray just plays the role of orchestration and resource reservation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re familiar with cloud native techs. They would like to use Kubernetes's capability for orchestration (ray actors) and scheduling (placement group). Ideally, we would have both Ray and Kubernetes as orchestrators for vL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: am wrong. We do use Ray and KubeRay on Kubernetes and I've successfully tested vLLM distributed inference on this setup, confirming its functional operation. However, we have many users/platforms, we do not want to lock...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
