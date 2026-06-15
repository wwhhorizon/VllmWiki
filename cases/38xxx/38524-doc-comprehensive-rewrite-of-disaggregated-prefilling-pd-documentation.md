# vllm-project/vllm#38524: [Doc]: comprehensive rewrite of disaggregated prefilling (PD) documentation

| 字段 | 值 |
| --- | --- |
| Issue | [#38524](https://github.com/vllm-project/vllm/issues/38524) |
| 状态 | open |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: comprehensive rewrite of disaggregated prefilling (PD) documentation

### Issue 正文摘录

### 📚 The doc issue ## Proposed Improvement Enhance the documentation to include: - Conceptual explanation and usage scenarios - End-to-end workflow (Prefill → KV transfer → Decode) - Deployment prerequisites and best practices - Detailed connector documentation and comparison - Design considerations for different environments - Internal architecture (Connector, LookupBuffer, Pipe) ## Expected Outcome - Better onboarding experience - Easier production adoption - Clearer understanding of system design - Improved extensibility for contributors ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Doc]: comprehensive rewrite of disaggregated prefilling (PD) documentation documentation ### 📚 The doc issue ## Proposed Improvement Enhance the documentation to include: - Conceptual explanation and usage scenarios -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: comparison - Design considerations for different environments - Internal architecture (Connector, LookupBuffer, Pipe) ## Expected Outcome - Better onboarding experience - Easier production adoption - Clearer understandi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
