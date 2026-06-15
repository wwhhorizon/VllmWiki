# vllm-project/vllm#42303: [Bug]: `prompt_token_ids` dropped in `EmbedsInput` pipeline

| 字段 | 值 |
| --- | --- |
| Issue | [#42303](https://github.com/vllm-project/vllm/issues/42303) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `prompt_token_ids` dropped in `EmbedsInput` pipeline

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `enable_prompt_embeds=True` with DFlash, users pass `prompt_embeds` (precomputed embeddings including vision tokens) instead of `prompt_token_ids`. However, DFlash's speculative decoding bookkeeping (`backup_next_token_ids`, `token_ids_cpu`, penalty computation) requires `prompt_token_ids` to function correctly. Currently, `EmbedsInput` has no `prompt_token_ids` field, so even if the user provides both `prompt_embeds` and `prompt_token_ids` in the prompt dict, the token IDs are silently dropped at multiple points: 1. `EmbedsInput` (in `vllm/inputs/engine.py`) has no `prompt_token_ids` field 2. `EmbedsPrompt` (in `vllm/inputs/llm.py`) has no `prompt_token_ids` field 3. `_process_embeds()` (in `vllm/renderers/base.py`) does not forward `prompt_token_ids` 4. `input_processor.py` hardcodes `prompt_token_ids = None` when `type == "embeds"` This causes `CachedRequestState.prompt_token_ids` to be `None`, which triggers: - `get_token_id()` raises `ValueError` (or returns `0` if patched), corrupting `backup_next_token_ids` - `token_ids_cpu` prompt region is uninitialized - DFlash verification produces garbled output with `syste...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: age ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ncluding vision tokens) instead of `prompt_token_ids`. However, DFlash's speculative decoding bookkeeping (`backup_next_token_ids`, `token_ids_cpu`, penalty computation) requires `prompt_token_ids` to function correctly...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
