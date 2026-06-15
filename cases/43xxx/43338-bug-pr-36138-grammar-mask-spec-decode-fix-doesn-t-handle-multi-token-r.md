# vllm-project/vllm#43338: [Bug] PR #36138 grammar-mask spec-decode fix doesn't handle multi-token reasoning boundaries (gpt-oss/openai_gptoss still bleeds; Qwen3 fixed)

| 字段 | 值 |
| --- | --- |
| Issue | [#43338](https://github.com/vllm-project/vllm/issues/43338) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] PR #36138 grammar-mask spec-decode fix doesn't handle multi-token reasoning boundaries (gpt-oss/openai_gptoss still bleeds; Qwen3 fixed)

### Issue 正文摘录

## Symptom PR #36138 ("Grammar was ignored when reasoning ended within speculated tokens") fixes the spec-decode × structured-output bypass for reasoning parsers whose end marker is a **single token** (e.g., the `qwen3` parser's ` ` — tested by the PR with Qwen/Qwen3-8B and confirmed by me with Qwen/Qwen3.6-35B-A3B-FP8). It does **not** fix parsers whose end marker is **multi-token** — most notably `gpt-oss` (`openai_gptoss`), where the boundary is ` final ` (3-4 tokens after tokenization). Effect in practice: a vLLM build at PR #36138's HEAD SHA (`94f4dc2e98d63dc1a3ff7cca2b35a9235df667e1`) serving `openai/gpt-oss-120b` with EAGLE3 + `response_format: {type: "json_schema", strict: true}` still produces ~27% of responses with garbage-prefix-before-JSON (e.g. `**Best{...}`, `(no{...}`, `chunk_0{...}`) — identical pattern to pre-patch behavior. By contrast, Qwen3.6-35B-A3B-FP8 (using the `qwen3` reasoning parser) + MTP + the same patched vLLM shows **0% prefix-bleed**. ## Reproducer (gpt-oss, fails) ``` vllm serve openai/gpt-oss-120b \ --tensor-parallel-size 2 \ --reasoning-parser openai_gptoss \ --max-model-len 131072 \ --enable-prefix-caching \ --speculative-config '{"model":" ","n...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ar-mask spec-decode fix doesn't handle multi-token reasoning boundaries (gpt-oss/openai_gptoss still bleeds; Qwen3 fixed) ## Symptom PR #36138 ("Grammar was ignored when reasoning ended within speculated tokens") fixes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s ` final ` (3-4 tokens after tokenization). Effect in practice: a vLLM build at PR #36138's HEAD SHA (`94f4dc2e98d63dc1a3ff7cca2b35a9235df667e1`) serving `openai/gpt-oss-120b` with EAGLE3 + `response_format: {type: "js...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug] PR #36138 grammar-mask spec-decode fix doesn't handle multi-token reasoning boundaries (gpt-oss/openai_gptoss still bleeds; Qwen3 fixed) ## Symptom PR #36138 ("Grammar was ignored when reasoning ended within specu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: * fully contained in a 2-5 token spec batch. `is_reasoning_end_streaming(small_prefix)` falls back to the base `is_reasoning_end(small_prefix)` which scans the prefix in isolation — never finds the boundary. `is_reasoni...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ing parser) + MTP + the same patched vLLM shows **0% prefix-bleed**. ## Reproducer (gpt-oss, fails) ``` vllm serve openai/gpt-oss-120b \ --tensor-parallel-size 2 \ --reasoning-parser openai_gptoss \ --max-model-len 1310...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
