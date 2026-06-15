# vllm-project/vllm#41902: Bug report: vLLM gpt-oss-120b returns content=null, reasoning=null with completion_tokens > 0

| 字段 | 值 |
| --- | --- |
| Issue | [#41902](https://github.com/vllm-project/vllm/issues/41902) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Bug report: vLLM gpt-oss-120b returns content=null, reasoning=null with completion_tokens > 0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary Serving `openai/gpt-oss-120b` via vLLM, `/v1/chat/completions` returns `content=null` and `reasoning=null` while `usage.completion_tokens > 0` and `finish_reason="stop"`. The model's final-channel output (the actual answer) is dropped on the way out of vLLM. This breaks any application that expects the OpenAI-compatible response contract, because the response carries no visible text yet bills for the tokens it generated. ## Environment - vLLM: (please fill in `vllm.__version__`) - GPU: NVIDIA Blackwell SM 12.1 (DGX Spark) - CUDA: 13.x - Model: `openai/gpt-oss-120b` (Mixture-of-Experts, harmony output format) - Endpoint: `/v1/chat/completions` - Date observed: 2026-05-06 ## Reproduction ```python import httpx system = ( "You are a precise reasoning assistant. Using the provided context, " "answer the sub-question in 2-4 sentences. Be specific and factual." ) user = ( "Original question (for context only): For what organization does a " "commentator of Press TV serve as associate director?\n\n" "Context: Press TV is an Iranian state media outlet. Some commentators " "have ties to think tanks like the Henry Jackson Societ...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: he tokens it generated. ## Environment - vLLM: (please fill in `vllm.__version__`) - GPU: NVIDIA Blackwell SM 12.1 (DGX Spark) - CUDA: 13.x - Model: `openai/gpt-oss-120b` (Mixture-of-Experts, harmony output format) - En...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: # Environment - vLLM: (please fill in `vllm.__version__`) - GPU: NVIDIA Blackwell SM 12.1 (DGX Spark) - CUDA: 13.x - Model: `openai/gpt-oss-120b` (Mixture-of-Experts, harmony output format) - Endpoint: `/v1/chat/complet...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Bug report: vLLM gpt-oss-120b returns content=null, reasoning=null with completion_tokens > 0 bug ### Your current environment ### 🐛 Describe the bug ## Summary Serving `openai/gpt-oss-120b` via vLLM, `/v1/chat/completi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 12.1 (DGX Spark) - CUDA: 13.x - Model: `openai/gpt-oss-120b` (Mixture-of-Experts, harmony output format) - Endpoint: `/v1/chat/completions` - Date observed: 2026-05-06 ## Reproduction ```python import httpx system = ( "...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: to the caller. ## Workaround applied downstream We added a placeholder fallback in our application: when `_chat()` for the `reasoner` / `synthesizer` role returns empty content with `completion_tokens > 0` even after re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
