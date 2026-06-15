# vllm-project/vllm#41967: [Bug]: Gemma4 + MTP speculative decoding drops first tool-call arguments in streaming multi-tool auto-tool-choice

| 字段 | 值 |
| --- | --- |
| Issue | [#41967](https://github.com/vllm-project/vllm/issues/41967) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4 + MTP speculative decoding drops first tool-call arguments in streaming multi-tool auto-tool-choice

### Issue 正文摘录

## 🐛 Describe the bug I hit a streaming tool-calling corruption bug with Gemma4 when MTP speculative decoding is enabled. Setup: - Docker image: `vllm/vllm-openai:gemma4-0505-cu130` - vLLM version reported by the server: `0.20.2rc1.dev49+g9b4e83934` - model: `google/gemma-4-31B-it` - server args include: - `--enable-auto-tool-choice` - `--tool-call-parser gemma4` - `--reasoning-parser gemma4` - `--speculative-config '{"model": "google/gemma-4-31B-it-assistant", "num_speculative_tokens": 4}'` Observed behavior: - with `stream=true`, when the model emits **two tool calls in one turn**, the first tool call's arguments are corrupted / dropped in the streamed deltas - with `stream=false`, the same request returns the correct final two tool calls - if I restart the same server **without** `--speculative-config`, the streaming output becomes correct across repeated runs So this appears to be a speculative-decoding + streaming + multi-tool-call interaction, not a base-model issue. I searched and found related issues, but this one seems distinct: - #38106 (`tool_choice=required` + speculative decoding + failed tool calls) - #40875 (ngram speculative decoding corrupting structured outputs /...

## 现有链接修复摘要

#42006 [Bugfix] Fix Gemma4 MTP streaming multi-tool calls

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: tion bug with Gemma4 when MTP speculative decoding is enabled. Setup: - Docker image: `vllm/vllm-openai:gemma4-0505-cu130` - vLLM version reported by the server: `0.20.2rc1.dev49+g9b4e83934` - model: `google/gemma-4-31B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma4 + MTP speculative decoding drops first tool-call arguments in streaming multi-tool auto-tool-choice ## 🐛 Describe the bug I hit a streaming tool-calling corruption bug with Gemma4 when MTP speculative deco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: + streaming + multi-tool-call interaction, not a base-model issue. I searched and found related issues, but this one seems distinct: - #38106 (`tool_choice=required` + speculative decoding + failed tool calls) - #40875...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Gemma4 + MTP speculative decoding drops first tool-call arguments in streaming multi-tool auto-tool-choice ## 🐛 Describe the bug I hit a streaming tool-calling corruption bug with Gemma4 when MTP speculative deco...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ng;model_support;sampling_logits;speculative_decoding cuda;gemm;operator;triton build_error env_dependency #42006 [Bugfix] Fix Gemma4 MTP streaming multi-tool calls <details>

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42006](https://github.com/vllm-project/vllm/pull/42006) | closes_keyword | 0.95 | [Bugfix] Fix Gemma4 MTP streaming multi-tool calls | Fixes #41967. ## Summary - Split Gemma4 streaming deltas on `<\|tool_call>` / `<tool_call\|>` boundaries before feeding them through the existing parser state machine. - Reconcile |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
