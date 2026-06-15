# vllm-project/vllm#16709: [Usage]: "How can I register Logits Processors in the args?"

| 字段 | 值 |
| --- | --- |
| Issue | [#16709](https://github.com/vllm-project/vllm/issues/16709) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: "How can I register Logits Processors in the args?"

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` I'm using a Git-cloned version of vLLM to register a custom function, so I'm getting an error when trying to print the current vLLM version. However, I'm using a recent version of vLLM. ``` ### How would you like to use vllm Hello, While serving with vLLM, I encountered cases where foreign languages were being generated, so I created a custom LogitsProcessor to block the generation of specific foreign languages. This works well when I use `llm.chat()` directly. However, I want to use this through OpenAI's `client.chat` interface instead. The issue is that OpenAI's client does not support custom `SamplingParams`. I'm trying to register my custom LogitsProcessor or related `SamplingParams` via the `python3 -m vllm.entrypoints.openai.api_server` command. While exploring the code, I came across an argument called `logits-processor-pattern`, which seems related to what I'm trying to achieve, but there are no usage examples, so I'm not sure how to use it. If `logits-processor-pattern` is not intended for this purpose, I’d like to ask how I can register my custom LogitsProcessor using args instead. Thank you for y...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t ```text The output of `python collect_env.py` I'm using a Git-cloned version of vLLM to register a custom function, so I'm getting an error when trying to print the current vLLM version. However, I'm using a recent ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: me! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: languages were being generated, so I created a custom LogitsProcessor to block the generation of specific foreign languages. This works well when I use `llm.chat()` directly. However, I want to use this through OpenAI's...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: "How can I register Logits Processors in the args?" usage;stale ### Your current environment ```text The output of `python collect_env.py` I'm using a Git-cloned version of vLLM to register a custom function, s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
