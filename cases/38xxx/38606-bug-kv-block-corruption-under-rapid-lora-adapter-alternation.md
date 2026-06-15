# vllm-project/vllm#38606: [Bug]: KV block corruption under rapid LoRA adapter alternation

| 字段 | 值 |
| --- | --- |
| Issue | [#38606](https://github.com/vllm-project/vllm/issues/38606) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error;nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV block corruption under rapid LoRA adapter alternation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Possibily Related to:** #37076 When fuzzing vllm 0.18.0 with **lora**, I found an independent trigger for KV cache block corruption, specific to multi-adapter deployments. Rapidly alternating between two LoRA adapters while long-prefix requests are mid-prefill causes non-deterministic output at `temperature=0`. Confirmed **10/10 runs** on a single minimal trace. The same trace reproduces at **5/10** on a base-model server without `--enable-lora`, but the LoRA-aware KV cache manager doubles the reproduction rate, pointing to an additional aliasing surface in the per-adapter block namespace. The divergence is not cancel-induced: the corrupted request (`thrash_9`) completes at **72ms**, and the first cancel in the trace does not occur until **225ms**. ### Why a different issue from #37076: **#37076 / PR #37164** fixes a TOCTOU race where request B steals a cached block between `get_computed_blocks()` and `allocate_slots()`. The fix pre-pins blocks immediately after lookup. This issue looks different and is most likely not patched by that fix. **The cancel-induced path** (reported separately) triggers corruption when a cancelled re...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: ween two LoRA adapters while long-prefix requests are mid-prefill causes non-deterministic output at `temperature=0`. Confirmed **10/10 runs** on a single minimal trace. The same trace reproduces at **5/10** on a base-m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lora**, I found an independent trigger for KV cache block corruption, specific to multi-adapter deployments. Rapidly alternating between two LoRA adapters while long-prefix requests are mid-prefill causes non-determinis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: red prefix forces the cache manager to resolve cross-adapter block ownership at every scheduler step. The same trace confirms at only 5/10 on a base server — the adapter-namespace multiplexing is an amplifying factor th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: KV block corruption under rapid LoRA adapter alternation bug ### Your current environment ### 🐛 Describe the bug **Possibily Related to:** #37076 When fuzzing vllm 0.18.0 with **lora**, I found an independent tri...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: oyments. Rapidly alternating between two LoRA adapters while long-prefix requests are mid-prefill causes non-deterministic output at `temperature=0`. Confirmed **10/10 runs** on a single minimal trace. The same trace re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
