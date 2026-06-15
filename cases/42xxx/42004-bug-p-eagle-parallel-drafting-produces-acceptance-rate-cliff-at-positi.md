# vllm-project/vllm#42004: [Bug]: P-EAGLE / parallel drafting produces acceptance-rate cliff at position 1 on google/gemma-4-31B-it

| 字段 | 值 |
| --- | --- |
| Issue | [#42004](https://github.com/vllm-project/vllm/issues/42004) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: P-EAGLE / parallel drafting produces acceptance-rate cliff at position 1 on google/gemma-4-31B-it

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary Parallel drafting (p-eagle, `parallel_drafting: true`) on `google/gemma-4-31B-it` produces a severe acceptance-rate cliff at position 1 when running with constrained decoding (JSON schema via xgrammar). Filing per discussion with @benchislett - he's tracking gemma-4-specific issues. ## Observed behavior On `google/gemma-4-31B-it` with a p-eagle head in parallel mode, `num_speculative_tokens=5`, on a constrained-decoding workload (JSON schema via xgrammar): | Position | Accepted / Drafts | Rate | |---|---:|:---:| | 0 | 111 / 192 | 57.8% | | 1 | 11 / 192 | **5.8%** ← cliff | | 2 | 0 / 192 | 0% | | 3 | 0 / 192 | 0% | | 4 | 0 / 192 | 0% | **Overall: 122/488 = 25%. Mean accepted per draft: 1.64.** Position 0 is reasonable; position 1 collapses by >50 percentage points; positions 2–4 accept zero tokens across the entire run. The cliff is immediate and complete, not a gradual degradation. ## Expected behavior Smooth decay across positions (geometric or near-geometric), not an abrupt collapse at position 1. ## Environment - **Target model:** `google/gemma-4-31B-it` - **Hardware:** 2× H200, TP=2 - **vLLM:** main branch - **Work...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: P-EAGLE / parallel drafting produces acceptance-rate cliff at position 1 on google/gemma-4-31B-it bug ### Your current environment ### 🐛 Describe the bug ## Summary Parallel drafting (p-eagle, `parallel_drafting:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: mar). Filing per discussion with @benchislett - he's tracking gemma-4-specific issues. ## Observed behavior On `google/gemma-4-31B-it` with a p-eagle head in parallel mode, `num_speculative_tokens=5`, on a constrained-d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: parallel drafting produces acceptance-rate cliff at position 1 on google/gemma-4-31B-it bug ### Your current environment ### 🐛 Describe the bug ## Summary Parallel drafting (p-eagle, `parallel_drafting: true`) on `googl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: mmediate and complete, not a gradual degradation. ## Expected behavior Smooth decay across positions (geometric or near-geometric), not an abrupt collapse at position 1. ## Environment - **Target model:** `google/gemma-...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: cuit correctly, and positions with real token IDs are rejected on target-mismatch as expected. - **Reducing K to 2 does not change mean accepted length.** Re-running at `num_speculative_tokens: 2` yields the same mean o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
