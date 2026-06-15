# vllm-project/vllm#4777: [Feature]: Support the OpenAI Batch Chat Completions file format

| 字段 | 值 |
| --- | --- |
| Issue | [#4777](https://github.com/vllm-project/vllm/issues/4777) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support the OpenAI Batch Chat Completions file format

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm working on a use case that involves running a the same dataset/prompt across multiple models (including some OpenAI and some open source models). I would like to be able to do batch inference on many requests in a file that follow the [OpenAI Batch file format](https://platform.openai.com/docs/guides/batch/1-preparing-your-batch-file). 1. This follows the spirit/pattern of the popular openai api server interface for using vllm. 2. It is easy to adapt existing code that calls web endpoints to generate these files (since the `body` field is essentially what you would pass into web endpoint). 3. This format doesn't require the user to think about rate limits, parallelism, etc. I'll lay out an implementation plan here, which **I'm willing to contribute an implementation for**. # Interface The primary interface would be via CLI command. ``` $ python -m vllm.entrypoints.openai_batch --help Usage: openai_batch [OPTIONS] Run offline inference on a file which conforms to the OpenAI Batch file format. https://platform.openai.com/docs/guides/batch/getting-started Options: --version Show the version and exit. --help Show this message and exit. -i --...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ps://platform.openai.com/docs/guides/batch/getting-started Options: --version Show the version and exit. --help Show this message and exit. -i --input-file The path or url to a single input file. Currently supports loca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: his format doesn't require the user to think about rate limits, parallelism, etc. I'll lay out an implementation plan here, which **I'm willing to contribute an implementation for**. # Interface The primary interface wo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support the OpenAI Batch Chat Completions file format feature request ### 🚀 The feature, motivation and pitch I'm working on a use case that involves running a the same dataset/prompt across multiple models (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support the OpenAI Batch Chat Completions file format feature request ### 🚀 The feature, motivation and pitch I'm working on a use case that involves running a the same dataset/prompt across multiple models (...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
