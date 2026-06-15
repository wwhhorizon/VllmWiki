# vllm-project/vllm#25450: [Feature]: Standalone Encoder Benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#25450](https://github.com/vllm-project/vllm/issues/25450) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Standalone Encoder Benchmark

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We want to be able to measure the performance for multimodal encoder alone quantitatively, which requires a benchmark that focuses on encoder forward pass. Ideally this benchmark should do: 1. Import encoder modules from model file and initialize it with dummy weights & vLLM config 2. Convert dummy images to inputs of the encoder via models's HF processor 3. Measure latency with processing a batch of `X` images with `Y` sizes. `X` and `Y` should be configurable. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: motivation and pitch We want to be able to measure the performance for multimodal encoder alone quantitatively, which requires a benchmark that focuses on encoder forward pass. Ideally this benchmark should do: 1. Impor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Feature]: Standalone Encoder Benchmark feature request;stale ### 🚀 The feature, motivation and pitch We want to be able to measure the performance for multimodal encoder alone quantitatively, which requires a benchmark...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Standalone Encoder Benchmark feature request;stale ### 🚀 The feature, motivation and pitch We want to be able to measure the performance for multimodal encoder alone quantitatively, which requires a benchmark...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t focuses on encoder forward pass. Ideally this benchmark should do: 1. Import encoder modules from model file and initialize it with dummy weights & vLLM config 2. Convert dummy images to inputs of the encoder via mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: want to be able to measure the performance for multimodal encoder alone quantitatively, which requires a benchmark that focuses on encoder forward pass. Ideally this benchmark should do: 1. Import encoder modules from m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
