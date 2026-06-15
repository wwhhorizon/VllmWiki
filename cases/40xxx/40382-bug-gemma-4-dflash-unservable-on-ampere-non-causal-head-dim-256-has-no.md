# vllm-project/vllm#40382: [Bug]: Gemma-4 + DFlash unservable on Ampere — non-causal + head_dim=256 has no compatible attention backend

| 字段 | 值 |
| --- | --- |
| Issue | [#40382](https://github.com/vllm-project/vllm/issues/40382) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma-4 + DFlash unservable on Ampere — non-causal + head_dim=256 has no compatible attention backend

### Issue 正文摘录

### Your current environment 2× NVIDIA RTX 3090 (Ampere sm_86), CUDA 12.9, vLLM `v0.19.2rc1.dev21+g893611813` (nightly). Full `collect-env` at the bottom. ### 🐛 Describe the bug Serving `RedHatAI/gemma-4-31B-it-speculator.dflash` (DFlash draft for Gemma-4) against an AutoRound-Int4 Gemma-4 target on TP=2 fails to initialize on every available Ampere-compatible attention backend. DFlash's block-parallel drafting requires **non-causal attention**; Gemma-4 has **head_dim=256**. On sm_86, no backend supports both. ### Backend matrix | Backend | Error / constraint | |-------------------|----------------------------------------------------| | FLASH_ATTN (FA2) | `head_size not supported` — head_dim=256 is not enabled in the stock FA2 wheel on sm_86 | | FLASH_ATTN_DIFFKV | `head_size not supported` | | FLASHINFER | `non-causal attention not supported` | | TRITON_ATTN | `non-causal attention not supported` | | FLEX_ATTENTION | `non-causal attention not supported` | | TREE_ATTN | `non-causal attention not supported` | ### Minor pydantic auto-detect gap Separate smaller issue: speculators auto-detect doesn't populate `num_speculative_tokens` from the draft's `speculators_config.proposal_meth...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: `head_size not supported` — head_dim=256 is not enabled in the stock FA2 wheel on sm_86 | | FLASH_ATTN_DIFFKV | `head_size not supported` | | FLASHINFER | `non-causal attention not supported` | | TRITON_ATTN | `non-caus...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Bug]: Gemma-4 + DFlash unservable on Ampere — non-causal + head_dim=256 has no compatible attention backend ### Your current environment 2× NVIDIA RTX 3090 (Ampere sm_86), CUDA 12.9, vLLM `v0.19.2rc1.dev21+g893611813`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Gemma-4 + DFlash unservable on Ampere — non-causal + head_dim=256 has no compatible attention backend ### Your current environment 2× NVIDIA RTX 3090 (Ampere sm_86), CUDA 12.9, vLLM `v0.19.2rc1.dev21+g893611813`...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ibe the bug Serving `RedHatAI/gemma-4-31B-it-speculator.dflash` (DFlash draft for Gemma-4) against an AutoRound-Int4 Gemma-4 target on TP=2 fails to initialize on every available Ampere-compatible attention backend. DFl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: rvable on Ampere — non-causal + head_dim=256 has no compatible attention backend ### Your current environment 2× NVIDIA RTX 3090 (Ampere sm_86), CUDA 12.9, vLLM `v0.19.2rc1.dev21+g893611813` (nightly). Full `collect-env...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
