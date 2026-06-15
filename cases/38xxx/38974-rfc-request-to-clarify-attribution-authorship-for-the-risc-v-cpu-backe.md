# vllm-project/vllm#38974: [RFC]: Request to clarify attribution/authorship for the RISC-V CPU backend PR chain (#20292, #32405, #36538, #36578)

| 字段 | 值 |
| --- | --- |
| Issue | [#38974](https://github.com/vllm-project/vllm/issues/38974) |
| 状态 | closed |
| 标签 | RFC;cpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Request to clarify attribution/authorship for the RISC-V CPU backend PR chain (#20292, #32405, #36538, #36578)

### Issue 正文摘录

### Motivation. I am opening this RFC to request clarification of the attribution/authorship history for the RISC-V CPU backend work. This is not a request to remove the merged functionality. The motivation is to ensure that the development history for this work is recorded accurately and transparently. The concern is that the visible PR chain does not fully reflect the implementation lineage. In particular: - #32405 explicitly stated that it continues and extends the work from #20292. - Later PRs #36538 and #36578 continued the same line of RISC-V CPU backend work, but the visible attribution chain no longer acknowledged #32405. - As a result, the current merged record may give future readers an incomplete understanding of who implemented the earlier follow-on work and how the final merged result evolved. Regarding authorship, the core follow-on implementation after #20292 was originally developed by me during my internship at ISCAS. After I left, that work was further continued and submitted as #32405. Because of this history, I believe the current public record should be clarified so that earlier implementation work is not omitted from the attribution chain. ### Proposed Change...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t fully reflect the implementation lineage. In particular: - #32405 explicitly stated that it continues and extends the work from #20292. - Later PRs #36538 and #36578 continued the same line of RISC-V CPU backend work,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Request to clarify attribution/authorship for the RISC-V CPU backend PR chain (#20292, #32405, #36538, #36578) RFC;cpu ### Motivation. I am opening this RFC to request clarification of the attribution/authorship...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [RFC]: Request to clarify attribution/authorship for the RISC-V CPU backend PR chain (#20292, #32405, #36538, #36578) RFC;cpu ### Motivation. I am opening this RFC to request clarification of the attribution/authorship...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Request to clarify attribution/authorship for the RISC-V CPU backend PR chain (#20292, #32405, #36538, #36578) RFC;cpu ### Motivation. I am opening this RFC to request clarification of the attribution/authorship...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
