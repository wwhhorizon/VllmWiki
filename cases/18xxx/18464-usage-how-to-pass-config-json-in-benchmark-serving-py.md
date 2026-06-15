# vllm-project/vllm#18464: [Usage]: how to pass config.json in benchmark_serving.py

| 字段 | 值 |
| --- | --- |
| Issue | [#18464](https://github.com/vllm-project/vllm/issues/18464) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to pass config.json in benchmark_serving.py

### Issue 正文摘录

### Your current environment when benchmarking if gated model name is provided, it will try to download config.json from hf repo with no access, how to pass in config.json? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: how to pass config.json in benchmark_serving.py usage;stale ### Your current environment when benchmarking if gated model name is provided, it will try to download config.json from hf repo with no access, how t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: how to pass config.json in benchmark_serving.py usage;stale ### Your current environment when benchmarking if gated model name is provided, it will try to download config.json from hf repo with no access, how t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: how to pass config.json in benchmark_serving.py usage;stale ### Your current environment when benchmarking if gated model name is provided, it will try to download config.json from hf repo with no access, how t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
