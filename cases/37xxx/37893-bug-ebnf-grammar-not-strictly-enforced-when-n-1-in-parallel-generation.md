# vllm-project/vllm#37893: [Bug]: EBNF grammar not strictly enforced when n > 1 in parallel generation

| 字段 | 值 |
| --- | --- |
| Issue | [#37893](https://github.com/vllm-project/vllm/issues/37893) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EBNF grammar not strictly enforced when n > 1 in parallel generation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary I found a grammar-enforcement issue when using structured output with an EBNF whitelist grammar. The same grammar works correctly when `n=1` (100% compliance), but when `n>1` (for example `n=5`), some outputs contain out-of-vocabulary words that should have been forbidden by the grammar. This does **not** look like a full syntax collapse: - the outer JSON shell is usually still valid, - the separator pattern is usually still preserved, - but some `word` slots contain invalid tokens / OOV words not present in the whitelist. So the issue appears as a **token-level whitelist leak under parallel structured decoding**, rather than a complete grammar failure. ## Environment - Backend: `vLLM` structured outputs - Grammar backend: `XGrammar` - Model: Qwen3-4B-based model - Decoding mode: - `n=1`: works as expected - `n=5`: issue appears - Task type: whitelist-constrained text generation - Output format: JSON object with a slash-separated sequence inside a `translation` field ## Minimal Grammar Shape The grammar is essentially a whitelist over allowed words: ```ebnf root ::= json json ::= "{\"translation\": \"" glosses "\"}" gl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: under parallel decoding, since it never reproduces when n=1. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nt - Backend: `vLLM` structured outputs - Grammar backend: `XGrammar` - Model: Qwen3-4B-based model - Decoding mode: - `n=1`: works as expected - `n=5`: issue appears - Task type: whitelist-constrained text generation -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: d decoding**, rather than a complete grammar failure. ## Environment - Backend: `vLLM` structured outputs - Grammar backend: `XGrammar` - Model: Qwen3-4B-based model - Decoding mode: - `n=1`: works as expected - `n=5`:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: puts as a deployment-grade hard constraint. In this setting, even a very small OOV leak makes the constrained decoding unsafe for production use. The output may look structurally valid while still violating the whitelis...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ic between vLLM sampling and the XGrammar backend. Since the issue never reproduces for n=1, it seems more likely to be in the parallel decoding path than in the core grammar definition itself. If Needed I can provide:...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
