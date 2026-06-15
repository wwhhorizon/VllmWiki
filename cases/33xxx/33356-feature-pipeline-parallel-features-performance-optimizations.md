# vllm-project/vllm#33356: [Feature]: Pipeline Parallel Features & Performance Optimizations

| 字段 | 值 |
| --- | --- |
| Issue | [#33356](https://github.com/vllm-project/vllm/issues/33356) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Pipeline Parallel Features & Performance Optimizations

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We can further optimize pipeline parallelism in vLLM for better performance Tasks: - [x] Enable async scheduling with Pipeline Parallel - [x] https://github.com/vllm-project/vllm/pull/32359 - [x] Under review: https://github.com/vllm-project/vllm/pull/32618 - [x] Using `isend/irecv` for async communication. https://github.com/vllm-project/vllm/pull/33368 - [x] Support for V2 https://github.com/vllm-project/vllm/pull/33960 - [ ] ~Chunked Pipeline Prefill for long context prefill (idea introduced by https://lmsys.org/blog/2026-01-15-chunked-pipeline/)~ - [ ] ~Optional: Dynamic Chunking mechanism~ CC: @robertgshaw2-redhat @njhill @NickLucche @LucasWilkinson @tlrmchlsmth ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: feature, motivation and pitch We can further optimize pipeline parallelism in vLLM for better performance Tasks: - [x] Enable async scheduling with Pipeline Parallel - [x] https://github.com/vllm-project/vllm/pull/32359...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: Pipeline Parallel Features & Performance Optimizations feature request ### 🚀 The feature, motivation and pitch We can further optimize pipeline parallelism in vLLM for better performance Tasks: - [x] Enable as...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
