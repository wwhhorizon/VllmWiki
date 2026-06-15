# vllm-project/vllm#10709: [Performance]: [V1] Increasing the request batch size causes a significant drop in performance.

| 字段 | 值 |
| --- | --- |
| Issue | [#10709](https://github.com/vllm-project/vllm/issues/10709) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: [V1] Increasing the request batch size causes a significant drop in performance.

### Issue 正文摘录

### Proposal to improve performance I try to start multiple workers to simulate a large batchsize (for example, 256, 512). Each worker sends a request (sharegpt data set), and immediately initiates the next round of requests after the completion, ensuring that there are always batchsize requests to vllm-server. Testing under the latest V1 found that under bs=256, 512, the performance dropped significantly under 512. I did two sets of tests and log additions https://github.com/vllm-project/vllm/blob/main/vllm/v1/core/scheduler.py#L249 ``` print(f"schedule queue running: {len(self.running)} preempted_reqs: {len(preempted_reqs)} waiting: {len(self.waiting)} request_nums: {len(self.requests)}") ``` When using V1pr for the first time, it basically meets expectations. When bs=256, each scheduling request is about 240. When bs=512, each scheduling request is about 500. But the performance is terrible when using the latest code. **test1** use pr `https://github.com/vllm-project/vllm/pull/9289` the performance was basically the same under the first PR of V1 [https://github.com/vllm-project/vllm/pull/9289](url) (256 vs 512). bs=256 and 512 did not appear preempted_reqs > 0 during the entire...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Performance]: [V1] Increasing the request batch size causes a significant drop in performance. performance;stale ### Proposal to improve performance I try to start multiple workers to simulate a large batchsize (for ex...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: tion, ensuring that there are always batchsize requests to vllm-server. Testing under the latest V1 found that under bs=256, 512, the performance dropped significantly under 512. I did two sets of tests and log addition...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: . Can you help me take a look? what changes were made that resulted in a small number of requests per schedule? I guess there were some changes that caused additional time-consuming points? ### Report of performance reg...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ring the entire test process. I understand that the video memory is sufficient at this time. ``` Observing the results of each scheduling, the following data is basically maintained bs=256 schedule queue running: 244 pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
