# vllm-project/vllm#8156: [Misc]: Use of response_format and guided output in LLMEngine and AsyncLLMEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#8156](https://github.com/vllm-project/vllm/issues/8156) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Use of response_format and guided output in LLMEngine and AsyncLLMEngine

### Issue 正文摘录

### Anything you want to discuss about vllm. Documentation detail how to use guided output with the OpenAI compatible completion API: [AsyncLLMEngine](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#extra-parameters-for-completions-api) namely `response_format`and `guided_json`. But I cannot find how to do the same using LLMEngine or AsyncLLMEngine. Is it supported? If so can we have some documentation about it? Thanks 🙂 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s 🙂 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Misc]: Use of response_format and guided output in LLMEngine and AsyncLLMEngine ### Anything you want to discuss about vllm. Documentation detail how to use guided output with the OpenAI compatible completion API: [Asy...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: AI compatible completion API: [AsyncLLMEngine](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#extra-parameters-for-completions-api) namely `response_format`and `guided_json`. But I cannot find how...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
