# vllm-project/vllm#3707: [Bug]: logprobs=0 behavior inconsistent with OpenAI spec

| 字段 | 值 |
| --- | --- |
| Issue | [#3707](https://github.com/vllm-project/vllm/issues/3707) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: logprobs=0 behavior inconsistent with OpenAI spec

### Issue 正文摘录

### Your current environment vLLM 0.3.3 ### 🐛 Describe the bug I'm using AsyncLlmEngine with vLLM 0.3.3 to serve OpenAI-compatible chat and completions endpoints. I noticed that there are some discrepancies between vLLM's and OpenAI's logprobs behavior. For example, providing logprobs=0 to SamplingParams causes `generate` to return `None` in its output logprobs, whereas OpenAI returns logprobs for the sampled tokens: ``` response = openai.Completion.create( engine="gpt-3.5-turbo-instruct", prompt="Translate the following English text to French: 'Hello, world!'", temperature=0.7, max_tokens=60, logprobs=0 ) ... { "id": "cmpl-97v6aQwrliFerfnhQKh1NwnO43Uup", "object": "text_completion", "created": 1711674836, "model": "gpt-3.5-turbo-instruct", "choices": [ { "text": "\n\nBonjour, monde !", "index": 0, "logprobs": { "tokens": [ "\n\n", "Bonjour", ",", " monde", " !" ], "token_logprobs": [ -0.16840062, -0.5103194, -0.010852911, -0.19059794, -0.48192957 ], "top_logprobs": null, "text_offset": [ 63, 65, 72, 73, 79 ] }, "finish_reason": "stop" } ], "usage": { "prompt_tokens": 13, "completion_tokens": 5, "total_tokens": 18 } } ``` The vLLM documentation https://docs.vllm.ai/en/latest/dev/s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e chat and completions endpoints. I noticed that there are some discrepancies between vLLM's and OpenAI's logprobs behavior. For example, providing logprobs=0 to SamplingParams causes `generate` to return `None` in its...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: h1NwnO43Uup", "object": "text_completion", "created": 1711674836, "model": "gpt-3.5-turbo-instruct", "choices": [ { "text": "\n\nBonjour, monde !", "index": 0, "logprobs": { "tokens": [ "\n\n", "Bonjour", ",", " mon
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: _tokens": 18 } } ``` The vLLM documentation https://docs.vllm.ai/en/latest/dev/sampling_params.html claims to also have this behavior but it does not.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
