# vllm-project/vllm#17352: [Performance]: first token latency during inference is longer when the number of input tokens is small

| 字段 | 值 |
| --- | --- |
| Issue | [#17352](https://github.com/vllm-project/vllm/issues/17352) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: first token latency during inference is longer when the number of input tokens is small

### Issue 正文摘录

### Proposal to improve performance **Describe the question** In vLLM, I noticed that the first token latency during inference is longer when the number of input tokens is small (e.g., 30 tokens), compared to when the number of input tokens is large (e.g., 800 tokens). Is this expected behavior? Could you help explain why this happens? **Environment** vLLM version: (v0.8.4) Model: (DeepSeek-R1) GPU: (H200 * 8) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: first token latency during inference is longer when the number of input tokens is small performance;stale ### Proposal to improve performance **Describe the question** In vLLM, I noticed that the first to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: en latency during inference is longer when the number of input tokens is small performance;stale ### Proposal to improve performance **Describe the question** In vLLM, I noticed that the first token latency during infer...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ehavior? Could you help explain why this happens? **Environment** vLLM version: (v0.8.4) Model: (DeepSeek-R1) GPU: (H200 * 8) ### Report of performance regression _No response_ ### Misc discussion on performance _No res...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: help explain why this happens? **Environment** vLLM version: (v0.8.4) Model: (DeepSeek-R1) GPU: (H200 * 8) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your cur...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: inference is longer when the number of input tokens is small performance;stale ### Proposal to improve performance **Describe the question** In vLLM, I noticed that the first token latency during inference is longer whe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
