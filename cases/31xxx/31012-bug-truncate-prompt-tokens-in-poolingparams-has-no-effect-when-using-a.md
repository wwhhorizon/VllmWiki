# vllm-project/vllm#31012: [Bug]: truncate_prompt_tokens in PoolingParams has no effect when using AsyncLLM.encode()

| 字段 | 值 |
| --- | --- |
| Issue | [#31012](https://github.com/vllm-project/vllm/issues/31012) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: truncate_prompt_tokens in PoolingParams has no effect when using AsyncLLM.encode()

### Issue 正文摘录

### Your current environment vLLM master. ### 🐛 Describe the bug ### Decsription `AsyncLLM.encode()` accepts `truncate_prompt_tokens` as a separate parameter but ignores `pooling_params.truncate_prompt_tokens`. This causes confusion and is inconsistent with `generate()`, which reads `truncate_prompt_tokens` directly from `sampling_params`. ### Impact Users setting `truncate_prompt_tokens` in `PoolingParams` expect it to work: ``` pooling_params = PoolingParams(truncate_prompt_tokens=-1) # Has no effect! async for output in engine.encode(prompt, pooling_params, request_id): ... ``` This causes long prompts to fail with `ValueError: prompt is longer than max_model_len` instead of being truncated. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: causes long prompts to fail with `ValueError: prompt is longer than max_model_len` instead of being truncated. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Has no effect! async for output in engine.encode(prompt, pooling_params, request_id): ... ``` This causes long prompts to fail with `ValueError: prompt is longer than max_model_len` instead of being truncated. ### Befor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
