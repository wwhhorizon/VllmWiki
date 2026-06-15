# vllm-project/vllm#10298: [Bug]: Get meaningless output when run long context inference of Qwen2.5 model with vllm>=0.6.3

| 字段 | 值 |
| --- | --- |
| Issue | [#10298](https://github.com/vllm-project/vllm/issues/10298) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Get meaningless output when run long context inference of Qwen2.5 model with vllm>=0.6.3

### Issue 正文摘录

### Your current environment ### Model Input Dumps models: Qwen2.5-Coder-7B-Instcut, Qwen2.5-7B-Instruct vllm: 0.6.3 input token: >8000 tokens ### 🐛 Describe the bug I have tested vllm 0.6.0~0.6.2, 0.5.5, all old versions are just ok. So this bug was introduced since 0.6.3 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Get meaningless output when run long context inference of Qwen2.5 model with vllm>=0.6.3 bug;stale ### Your current environment ### Model Input Dumps models: Qwen2.5-Coder-7B-Instcut, Qwen2.5-7B-Instruct vllm: 0....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### 🐛 Describe the bug I have tested vllm 0.6.0~0.6.2, 0.5.5, all old versions are just ok. So this bug was introduced since 0.6.3 ### Before submitting a new issue... - [X] Make sure you already searched for relevant i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 6.3 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ut when run long context inference of Qwen2.5 model with vllm>=0.6.3 bug;stale ### Your current environment ### Model Input Dumps models: Qwen2.5-Coder-7B-Instcut, Qwen2.5-7B-Instruct vllm: 0.6.3 input token: >8000 toke...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ct vllm: 0.6.3 input token: >8000 tokens ### 🐛 Describe the bug I have tested vllm 0.6.0~0.6.2, 0.5.5, all old versions are just ok. So this bug was introduced since 0.6.3 ### Before submitting a new issue... - [X] Make...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
