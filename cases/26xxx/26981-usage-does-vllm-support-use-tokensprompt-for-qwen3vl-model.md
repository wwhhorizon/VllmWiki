# vllm-project/vllm#26981: [Usage]: Does vllm support use TokensPrompt for Qwen3VL model

| 字段 | 值 |
| --- | --- |
| Issue | [#26981](https://github.com/vllm-project/vllm/issues/26981) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vllm support use TokensPrompt for Qwen3VL model

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm My truncation strategy differs slightly from the standard approach (I wish to preserve the system prompt and the final suffix, only truncating the middle portion). It seems that the current version of vLLM does not support this, so I attempted to pass pre-processed token IDs along with mm_data as input, for example: TokensPrompt(prompt_token_ids=text[:self.max_model_length] + self.suffix_tokens, multi_modal_data=mm_data, mm_processor_kwargs=video_kwargs). However, I encountered an error. Could you please advise on the correct way to use this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Does vllm support use TokensPrompt for Qwen3VL model usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm My truncation strategy differs...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l suffix, only truncating the middle portion). It seems that the current version of vLLM does not support this, so I attempted to pass pre-processed token IDs along with mm_data as input, for example: TokensPrompt(promp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Does vllm support use TokensPrompt for Qwen3VL model usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm My truncation strategy differs...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
