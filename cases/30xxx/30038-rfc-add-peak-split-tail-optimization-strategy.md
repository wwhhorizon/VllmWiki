# vllm-project/vllm#30038: [RFC]: Add Peak Split & Tail Optimization Strategy

| 字段 | 值 |
| --- | --- |
| Issue | [#30038](https://github.com/vllm-project/vllm/issues/30038) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add Peak Split & Tail Optimization Strategy

### Issue 正文摘录

--- authors: - Chen Jie @HiC4Sh1e - Jiahong Zhang @JiahongZhang-Work - Weichen Zhu @Pr0Wh1teGivee - Zhexu Liu @henryxuxu0716 --- ### Motivation. Chunked prefill is a significant scheduling feature in the vLLM V1 scheduler, designed to fully utilize the token budget per round for processing partial Prefill requests. In the Splitfuse + chunked prefill scenario, when the number of system requests is low during the ramp-up phase, a single prefill request may require multiple splits/scheduling rounds before it can be converted into a Decode request. This can lead to a smaller batch size during this phase, reducing throughput. ### Proposed Change. ## Feature Overview The peak splitting strategy attempts to address this by disabling chunked prefill for mixed execution when the number of running requests falls below a certain threshold of the maximum number of requests schedulable per round. This aims to quickly convert Prefill requests into running requests, as illustrated in the second scheduling round in the diagram below. Conversely, when the system has a sufficient number of running requests, chunked prefill is re-enabled to ensure Decode performance is not impacted, as shown in the...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Add Peak Split & Tail Optimization Strategy RFC;stale --- authors: - Chen Jie @HiC4Sh1e - Jiahong Zhang @JiahongZhang-Work - Weichen Zhu @Pr0Wh1teGivee - Zhexu Liu @henryxuxu0716 --- ### Motivation. Chunked prefi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: switch is re-enabled. Tail optimization requires awareness of the user-configured chunk size (`long_prefill_token_threshold` in vLLM, default 0, meaning unrestricted). vLLM schedules chunked prefill by calculating the n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: quest. This can lead to a smaller batch size during this phase, reducing throughput. ### Proposed Change. ## Feature Overview The peak splitting strategy attempts to address this by disabling chunked prefill for mixed e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: de request. This can lead to a smaller batch size during this phase, reducing throughput. ### Proposed Change. ## Feature Overview The peak splitting strategy attempts to address this by disabling chunked prefill for mi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nds before it can be converted into a Decode request. This can lead to a smaller batch size during this phase, reducing throughput. ### Proposed Change. ## Feature Overview The peak splitting strategy attempts to addres...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
