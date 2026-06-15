# vllm-project/vllm#7408: [RFC]: Refactor the service pipeline to overlap GPU execution and CPU operations

| 字段 | 值 |
| --- | --- |
| Issue | [#7408](https://github.com/vllm-project/vllm/issues/7408) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel |
| 子分类 | latency_reg |
| Operator 关键词 | kernel |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Refactor the service pipeline to overlap GPU execution and CPU operations

### Issue 正文摘录

### Motivation. Hi all, I'm trying to optimize the gpu utilization for large batches. I talked about this here: https://github.com/vllm-project/vllm/issues/6560 I notice that, the GPU kernel launch only takes a short time, so it's possible to do something while waiting for the GPU to complete inference. I did some modification on the non-distributed inference worker, and I get 10% higher token throughput on my single H100 using vicuna 13B with a slight cost: the TTFT is at most 10ms higher than before. And also, if I take out the detokenization to overlap with gpu, the performance can be even higher, about 17%. But the side effect is: the parameter for requested number of tokens doesn't take effect accurately, the generated tokens is usually 1 or 2 more than wanted. ### Proposed Change. ![image](https://github.com/user-attachments/assets/cdef8b09-a290-4498-9330-f9bd065c90da) ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tor the service pipeline to overlap GPU execution and CPU operations RFC;stale ### Motivation. Hi all, I'm trying to optimize the gpu utilization for large batches. I talked about this here: https://github.com/vllm-proj...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ted inference worker, and I get 10% higher token throughput on my single H100 using vicuna 13B with a slight cost: the TTFT is at most 10ms higher than before. And also, if I take out the detokenization to overlap with...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tion on the non-distributed inference worker, and I get 10% higher token throughput on my single H100 using vicuna 13B with a slight cost: the TTFT is at most 10ms higher than before. And also, if I take out the detoken...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
