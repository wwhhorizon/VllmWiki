# vllm-project/vllm#16353: [Feature]: Run performance benchmarks for multi-modal models in CI

| 字段 | 值 |
| --- | --- |
| Issue | [#16353](https://github.com/vllm-project/vllm/issues/16353) |
| 状态 | open |
| 标签 | help wanted;feature request;keep-open;multi-modality |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Run performance benchmarks for multi-modal models in CI

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We currently only have benchmarks for text-only models such as Llama. With the increasing importance of multi-modality and related optimizations such as processor cache, we should add performance benchmarks for multi-modal models to avoid regressions (e.g. memory leaks, slow batching). We can measure the peak memory usage based on this code: ```python import resource max_self_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1 << 20) max_children_usage = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / (1 << 20) print(f"Peak memory usage: {max_self_usage} (self) + {max_children_usage} (children) GiB") ``` ### Alternatives _No response_ ### Additional context cc @mgoin @ywang96 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Feature]: Run performance benchmarks for multi-modal models in CI help wanted;feature request;keep-open;multi-modality ### 🚀 The feature, motivation and pitch We currently only have benchmarks for text-only models such...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Run performance benchmarks for multi-modal models in CI help wanted;feature request;keep-open;multi-modality ### 🚀 The feature, motivation and pitch We currently only have benchmarks for text-only models such...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Run performance benchmarks for multi-modal models in CI help wanted;feature request;keep-open;multi-modality ### 🚀 The feature, motivation and pitch We currently only have benchmarks for text-only models such...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 96 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: performance benchmarks for multi-modal models in CI help wanted;feature request;keep-open;multi-modality ### 🚀 The feature, motivation and pitch We currently only have benchmarks for text-only models such as Llama. With...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
