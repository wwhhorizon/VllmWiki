# vllm-project/vllm#42302: [Bug]: `prompt_token_ids` dropped in `EmbedsInput` pipeline

| 字段 | 值 |
| --- | --- |
| Issue | [#42302](https://github.com/vllm-project/vllm/issues/42302) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `prompt_token_ids` dropped in `EmbedsInput` pipeline

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `enable_prompt_embeds=True` with DFlash, users pass `prompt_embeds` (precomputed embeddings including vision tokens) instead of `prompt_token_ids`. However, DFlash's speculative decoding bookkeeping (`backup_next_token_ids`, `token_ids_cpu`, penalty computation) requires `prompt_token_ids` to function correctly. Currently, `EmbedsInput` has no `prompt_token_ids` field, so even if the user provides both `prompt_embeds` and `prompt_token_ids` in the prompt dict, the token IDs are silently dropped at multiple points: 1. `EmbedsInput` (in `vllm/inputs/engine.py`) has no `prompt_token_ids` field 2. `EmbedsPrompt` (in `vllm/inputs/llm.py`) has no `prompt_token_ids` field 3. `_process_embeds()` (in `vllm/renderers/base.py`) does not forward `prompt_token_ids` 4. `input_processor.py` hardcodes `prompt_token_ids = None` when `type == "embeds"` This causes `CachedRequestState.prompt_token_ids` to be `None`, which triggers: - `get_token_id()` raises `ValueError` (or returns `0` if patched), corrupting `backup_next_token_ids` - `token_ids_cpu` prompt region is uninitialized - DFlash verification produces garbled output with `syste...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ncluding vision tokens) instead of `prompt_token_ids`. However, DFlash's speculative decoding bookkeeping (`backup_next_token_ids`, `token_ids_cpu`, penalty computation) requires `prompt_token_ids` to function correctly...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: age ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
