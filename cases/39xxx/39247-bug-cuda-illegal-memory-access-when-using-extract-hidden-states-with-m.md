# vllm-project/vllm#39247: [Bug]: CUDA illegal memory access when using extract_hidden_states with multiple generate() calls

| 字段 | 值 |
| --- | --- |
| Issue | [#39247](https://github.com/vllm-project/vllm/issues/39247) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access when using extract_hidden_states with multiple generate() calls

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using speculative decoding infrastructure to get hidden states with repeated `LLM.generate()` calls, a CUDA illegal memory access occurs after 2-5 iterations. Importantly, I've also only observed this happening when continuing to generate after the initial prefill stage (i.e. `max_tokens > 1`). I've written a small script (posted in [this gist](https://gist.github.com/noahrossi/4f0cb75386646edadbd20c073162dd54)) that minimally reproduces the problem on my system. I pointed Claude at the problem, and it produced [this small fix](https://github.com/vllm-project/vllm/compare/main...noahrossi:vllm:fix/extract-hidden-states-invalid-draft-tokens). On the face of it, it looks reasonable, and Claude says that it mirrors the same way that the Eagle codepath sanitizes token IDs. However, I'm unfamiliar with vLLM's codebase and inference optimization in general, and I didn't want to create a PR solely based on generated code. My quick testing over a few prompts seems to show that generation still works the same, but I didn't run anything comprehensive. ### Before submitting a new issue... - [x] Make sure you already searched for releva...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rate()` calls, a CUDA illegal memory access occurs after 2-5 iterations. Importantly, I've also only observed this happening when continuing to generate after the initial prefill stage (i.e. `max_tokens > 1`). I've writ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA illegal memory access when using extract_hidden_states with multiple generate() calls bug ### Your current environment ### 🐛 Describe the bug When using speculative decoding infrastructure to get hidden stat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: bug ### Your current environment ### 🐛 Describe the bug When using speculative decoding infrastructure to get hidden states with repeated `LLM.generate()` calls, a CUDA illegal memory access occurs after 2-5 iterations....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t.github.com/noahrossi/4f0cb75386646edadbd20c073162dd54)) that minimally reproduces the problem on my system. I pointed Claude at the problem, and it produced [this small fix](https://github.com/vllm-project/vllm/compar...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
