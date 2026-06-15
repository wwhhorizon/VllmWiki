# vllm-project/vllm#14307: Issue with Mistral Small and greek characters

| 字段 | 值 |
| --- | --- |
| Issue | [#14307](https://github.com/vllm-project/vllm/issues/14307) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issue with Mistral Small and greek characters

### Issue 正文摘录

### Your current environment ```text --model mistralai/Mistral-Small-24B-Instruct-2501 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice ``` ### How would you like to use vllm I run inference for the Mistral Small model with the parameters defined before i have issues with greek characters on llm responses.some of them are clear some are unkown characters.Using the same model with ollama greek is perfect without any issues. Can i use some other parameter for my usecase when inferencing with vllm? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nd greek characters usage;stale ### Your current environment ```text --model mistralai/Mistral-Small-24B-Instruct-2501 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Issue with Mistral Small and greek characters usage;stale ### Your current environment ```text --model mistralai/Mistral-Small-24B-Instruct-2501 --tokenizer_mode mistral --config_format mistral --load_format mistral --t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ut any issues. Can i use some other parameter for my usecase when inferencing with vllm? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Issue with Mistral Small and greek characters usage;stale ### Your current environment ```text --model mistralai/Mistral-Small-24B-Instruct-2501 --tokenizer_mode mistral --config_format mistral --load_format mistral --t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
