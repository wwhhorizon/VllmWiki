# vllm-project/vllm#26493: [Feature]: expose model revisions in OpenAI v1/models endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#26493](https://github.com/vllm-project/vllm/issues/26493) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: expose model revisions in OpenAI v1/models endpoint

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I would appreciate if the `v1/models` output included a model revision value for each of the models. (i.e. the git checksum of the model repo in huggingface, settable via `--revision` at the CLI level) My use case is that I want to ensure the expected revision is actually being used, because any change in model setup needs to be at least recorded in my client workflow. So my client scripts would like to log the model revision numbers. Additionally, I'm providing both (a) scripts to set up the model and (b) scripts to talk to the model, deployed in two different ways. And this would let me ensure that downstream users have correctly updated and are using the matching model & script. ### Alternatives If it's hard to throw it in the models endpoint, any other way of retrieving this information as an http client would be fine. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: expose model revisions in OpenAI v1/models endpoint feature request;stale ### 🚀 The feature, motivation and pitch I would appreciate if the `v1/models` output included a model revision value for each of the m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: expose model revisions in OpenAI v1/models endpoint feature request;stale ### 🚀 The feature, motivation and pitch I would appreciate if the `v1/models` output included a model revision value for each of the m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ture request;stale ### 🚀 The feature, motivation and pitch I would appreciate if the `v1/models` output included a model revision value for each of the models. (i.e. the git checksum of the model repo in huggingface, se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
