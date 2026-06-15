# vllm-project/vllm#30101: [RFC]: Add Buffered Response Scheduling Policy

| 字段 | 值 |
| --- | --- |
| Issue | [#30101](https://github.com/vllm-project/vllm/issues/30101) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add Buffered Response Scheduling Policy

### Issue 正文摘录

--- authors: - Chen Jie @HiC4Sh1e - Jiahong Zhang @JiahongZhang-Work - Weichen Zhu @Pr0Wh1teGivee - Zhexu Liu @henryxuxu0716 --- ### Motivation. In vLLM online inference, requests complete token generation through iterative decode steps. The system streams responses back to users immediately after each iteration. However, when multiple requests (e.g., a new Prefill request B arriving during an existing request A's Decode phase) compete for computational resources (e.g., in PD contention or PD fusion scenarios), the subsequent decode iterations of request A can experience significant latency spikes. This leads to a poor user experience: after receiving the first few responses with low latency, the user suddenly encounters noticeably delayed responses, creating a perception of "stuttering." The Buffer Response mechanism addresses this issue by intentionally buffering and controlling the release of request responses. It leverages any available latency slack (the difference between the actual response time and the required SLO deadlines like TTFT and TPOT) to smooth out the response stream. From the user's perspective, responses are returned at a more consistent pace, even when system...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [RFC]: Add Buffered Response Scheduling Policy RFC;stale --- authors: - Chen Jie @HiC4Sh1e - Jiahong Zhang @JiahongZhang-Work - Weichen Zhu @Pr0Wh1teGivee - Zhexu Liu @henryxuxu0716 --- ### Motivation. In vLLM online in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: the subsequent decode iterations of request A can experience significant latency spikes. This leads to a poor user experience: after receiving the first few responses with low latency, the user suddenly encounters notic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: edResponse` and `ProcessCallback`: * `BufferedResponse`: Records key information about a response, with the full response assigned to an `output` field (type not strictly defined). * `ProcessCallback`: Registers the sta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nses, creating a perception of "stuttering." The Buffer Response mechanism addresses this issue by intentionally buffering and controlling the release of request responses. It leverages any available latency slack (the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Buffer Response strategy: * ​**Generalized Component Design**​, interfacing with different frameworks via `BufferedResponse` and `ProcessCallback`: * `BufferedResponse`: Records key information about a response, with th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
