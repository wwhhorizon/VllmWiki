# vllm-project/vllm#16885: [Usage]: Is it true that vllm doesn't support deepseek r1 yet with the v1 engine?

| 字段 | 值 |
| --- | --- |
| Issue | [#16885](https://github.com/vllm-project/vllm/issues/16885) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is it true that vllm doesn't support deepseek r1 yet with the v1 engine?

### Issue 正文摘录

### Your current environment ```text In vllm v0.8,4 GPU: H100 * 16 1) TP8 + PP2 with VLLM_USE_V1=1 : experimetal 2) TP16 + TP1 : it runs as V1, but Crash during run Right? So the most efficient deploy method right now is TP8 + PP2 with VLLM_USE_V1=0 Right? ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: P16 + TP1 : it runs as V1, but Crash during run Right? So the most efficient deploy method right now is TP8 + PP2 with VLLM_USE_V1=0 Right? ``` ### How would you like to use vllm I want to run inference of a [specific m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e? usage;stale ### Your current environment ```text In vllm v0.8,4 GPU: H100 * 16 1) TP8 + PP2 with VLLM_USE_V1=1 : experimetal 2) TP16 + TP1 : it runs as V1, but Crash during run Right? So the most efficient deploy met...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: true that vllm doesn't support deepseek r1 yet with the v1 engine? usage;stale ### Your current environment ```text In vllm v0.8,4 GPU: H100 * 16 1) TP8 + PP2 with VLLM_USE_V1=1 : experimetal 2) TP16 + TP1 : it runs as...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
