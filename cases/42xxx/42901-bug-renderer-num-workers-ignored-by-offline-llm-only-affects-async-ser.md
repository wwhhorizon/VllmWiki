# vllm-project/vllm#42901: [Bug]: `renderer_num_workers` ignored by offline `LLM` (only affects  async serving)

| 字段 | 值 |
| --- | --- |
| Issue | [#42901](https://github.com/vllm-project/vllm/issues/42901) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `renderer_num_workers` ignored by offline `LLM` (only affects  async serving)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Version:** vllm main @ `966903eb9` (2026-05-17), verified against source. **Summary:** For offline `LLM.generate`/`.chat`, `renderer_num_workers > 1` does not parallelize multimodal preprocessing — it has no effect. **Why:** The thread pool sized by `renderer_num_workers` (`BaseRenderer._executor`) is only ever consumed by `_process_multimodal_async`, which is reached exclusively through the async path (`render_chat_async`). Offline `LLM` calls the sync `render_chat`, which calls `_process_multimodal` directly, so `mm_processor.apply` runs serially on the calling thread, one prompt at a time. The pool is constructed and never submitted to. (Default is `1`; with the mm processor cache enabled, `>1` is rejected at config time instead.) **Docs:** The `renderer_num_workers` docstring says it "handles ... multimodal preprocessing" with no note that this applies to async serving only — so on a preprocessing-bound offline batch it's a silent no-op. **Question:** Is the serial offline path intended? If so, the docstring should state that `renderer_num_workers` only affects async serving. If not, would a one-time warning when it's set `...

## 现有链接修复摘要

#42905 [Bugfix] Warn when renderer_num_workers has no effect on offline LLM

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: serving) bug ### Your current environment ### 🐛 Describe the bug **Version:** vllm main @ `966903eb9` (2026-05-17), verified against source. **Summary:** For offline `LLM.generate`/`.chat`, `renderer_num_workers > 1` do...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `LLM.generate`/`.chat`, `renderer_num_workers > 1` does not parallelize multimodal preprocessing — it has no effect. **Why:** The thread pool sized by `renderer_num_workers` (`BaseRenderer._executor`) is only ever consu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: me? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency;shape #42905 [Bugfix] Warn when renderer_num_workers has no effect on offline LLM Your current environme...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_i...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42905](https://github.com/vllm-project/vllm/pull/42905) | closes_keyword | 0.95 | [Bugfix] Warn when renderer_num_workers has no effect on offline LLM | Fixes #42901. ## Duplicate-work check (per AGENTS.md) ``` gh issue view 42901 --repo vllm-project/vllm --comments # 0 comments gh pr list --repo vllm-project/vllm --state o |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
