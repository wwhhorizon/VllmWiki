# vllm-project/vllm#18826: [RFC]: Controlling the maximum length of the waiting queue

| 字段 | 值 |
| --- | --- |
| Issue | [#18826](https://github.com/vllm-project/vllm/issues/18826) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Controlling the maximum length of the waiting queue

### Issue 正文摘录

### Motivation. Currently, there appears to be no mechanism in vLLM to reject incoming requests based on the waiting queue length. Instead, all incoming requests are added to the queue. The waiting queue is implemented as an unbounded deque residing in CPU memory, where each element represents a pending request. In scenarios of service overload or when using low-performance GPUs, the queue length may grow indefinitely if users do not actively cancel their requests. This can lead to excessive memory consumption and eventually result in an out-of-memory (OOM) failure. Waiting Queue: https://github.com/vllm-project/vllm/blob/6825d9a998df3f22b5e19fb600d0a0c09950db28/vllm/v1/core/sched/scheduler.py#L90-L92 To address this issue, we propose introducing a new mechanism to control the maximum length of the waiting queue. Once the queue reaches a specified threshold, any new incoming requests will be rejected immediately with an HTTP 503 (Service Unavailable) response. Additionally, at a higher level, such as in `Kubernetes`, we can use Istio, Envoy, and other tools to perform load balancing based on whether the request returns a 503 status code. ### Proposed Change. Introduce a parameter...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Controlling the maximum length of the waiting queue RFC ### Motivation. Currently, there appears to be no mechanism in vLLM to reject incoming requests based on the waiting queue length. Instead, all incoming req...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ting queue RFC ### Motivation. Currently, there appears to be no mechanism in vLLM to reject incoming requests based on the waiting queue length. Instead, all incoming requests are added to the queue. The waiting queue...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ore/sched/scheduler.py#L90-L92 To address this issue, we propose introducing a new mechanism to control the maximum length of the waiting queue. Once the queue reaches a specified threshold, any new incoming requests wi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: excessive memory consumption and eventually result in an out-of-memory (OOM) failure. Waiting Queue: https://github.com/vllm-project/vllm/blob/6825d9a998df3f22b5e19fb600d0a0c09950db28/vllm/v1/core/sched/scheduler.py#L90...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: example ``` python3 def add_request(self, request: Request, dummy=False) -> None: if self.max_waiting_queue_length and \ len(self.waiting) >= self.max_waiting_queue_length: raise SchedulerWaitingQueueFullError( f"Schedu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
