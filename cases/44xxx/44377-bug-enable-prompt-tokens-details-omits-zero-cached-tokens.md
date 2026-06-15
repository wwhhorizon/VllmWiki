# vllm-project/vllm#44377: [Bug]: --enable-prompt-tokens-details omits zero cached tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#44377](https://github.com/vllm-project/vllm/issues/44377) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --enable-prompt-tokens-details omits zero cached tokens

### Issue 正文摘录

### Your current environment Observed in two current source trees: - Pinned vLLM used by vllm-ascend: `/vllm-workspace/vllm` at `bc150f50299199599673614f80d12a196f377655` - Latest fetched upstream `main`: `27a93cd4266151beaf7c8a89227418e86e187f30` ### 🐛 Describe the bug When `--enable-prompt-tokens-details` is enabled, OpenAI chat/completion usage only includes `prompt_tokens_details` if `num_cached_tokens` is truthy. As a result, `num_cached_tokens == 0` is treated the same as missing data and the response omits the field in streaming usage chunks or returns `prompt_tokens_details: null` in non-streaming responses. This makes it impossible for clients to distinguish: - prompt token details were enabled and the request had `cached_tokens: 0` - prompt token details were not available The relevant conditions currently use truthiness checks, for example on current upstream `main`: - `vllm/entrypoints/openai/chat_completion/serving.py`: `if self.enable_prompt_tokens_details and num_cached_tokens:` - `vllm/entrypoints/openai/chat_completion/serving.py`: `if self.enable_prompt_tokens_details and final_res.num_cached_tokens:` - `vllm/entrypoints/openai/completion/serving.py`: `if self.en...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ro-cache omission. It does not by itself prove any model-specific prefix-cache-hit accounting problem when a model is expected to report a nonzero cache hit. Related vllm-ascend PRs: - vllm-project/vllm-ascend#9911 - vl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ompt-tokens-details`, usage should include zero cached tokens as an explicit value when the engine reports `num_cached_tokens == 0`: ```json "usage": { "prompt_tokens": 123, "completion_tokens": 10, "total_tokens": 133,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is specifically the zero-cache omission. It does not by itself prove any model-specific prefix-cache-hit accounting problem when a model is expected to report a nonzero cache hit. Related vllm-ascend PRs: - vllm-project...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: for clients to distinguish: - prompt token details were enabled and the request had `cached_tokens: 0` - prompt token details were not available The relevant conditions currently use truthiness checks, for example on cu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: `/vllm-workspace/vllm` at `bc150f50299199599673614f80d12a196f377655` - Latest fetched upstream `main`: `27a93cd4266151beaf7c8a89227418e86e187f30` ### 🐛 Describe the bug When `--enable-prompt-tokens-details` is enabled,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
