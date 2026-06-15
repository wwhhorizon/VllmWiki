# vllm-project/vllm#16969: [RFC]: scheduling policy optimization  in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16969](https://github.com/vllm-project/vllm/issues/16969) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: scheduling policy optimization  in vLLM

### Issue 正文摘录

### Motivation. Motivated by "Accelerating LLM Serving for Multi-turn Dialogues with Efficient Resource Management"， the first-come-first-served (FCFS) scheduling policy often leads to head-of-line blocking issues, causing GPU memory resources to be underutilized, especially as prompt lengths increase due to multi-turn interactions. Moreover, I propose a sjf-based scheduling policy. ### Proposed Change. **Design** At each scheduling instance, select as many runnable requests as possible from the request queue (i.e., those that the current GPU memory can accommodate), rather than just choosing a single "next runnable request." In doing so, aim to fill up the idle memory space of the GPU as much as possible, thereby increasing batch size and throughput. **Implementation Details** ![Image](https://github.com/user-attachments/assets/4980bc35-fa01-45d5-9b2f-72f5b5b6f844) - Request Sorting: First, sort the requests in the request queue by their required memory size (from smallest to largest). This prioritizes smaller requests that occupy less memory, making better use of fragmented memory. - Greedy Selection: Starting from the head of the queue, sequentially select requests until the cu...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: scheduling policy optimization in vLLM RFC;stale ### Motivation. Motivated by "Accelerating LLM Serving for Multi-turn Dialogues with Efficient Resource Management"， the first-come-first-served (FCFS) scheduling...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rt the requests in the request queue by their required memory size (from smallest to largest). This prioritizes smaller requests that occupy less memory, making better use of fragmented memory. - Greedy Selection: Start...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: space of the GPU as much as possible, thereby increasing batch size and throughput. **Implementation Details** ![Image](https://github.com/user-attachments/assets/4980bc35-fa01-45d5-9b2f-72f5b5b6f844) - Request Sorting:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Motivated by "Accelerating LLM Serving for Multi-turn Dialogues with Efficient Resource Management"， the first-come-first-served (FCFS) scheduling policy often leads to head-of-line blocking issues, causing GPU memory r...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ) scheduling policy often leads to head-of-line blocking issues, causing GPU memory resources to be underutilized, especially as prompt lengths increase due to multi-turn interactions. Moreover, I propose a sjf-based sc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
