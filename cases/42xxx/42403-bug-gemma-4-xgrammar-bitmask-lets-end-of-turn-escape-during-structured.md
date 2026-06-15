# vllm-project/vllm#42403: [Bug]: (Gemma 4) xgrammar bitmask lets <end_of_turn> escape during structured outputs, terminating generation mid-JSON

| 字段 | 值 |
| --- | --- |
| Issue | [#42403](https://github.com/vllm-project/vllm/issues/42403) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: (Gemma 4) xgrammar bitmask lets <end_of_turn> escape during structured outputs, terminating generation mid-JSON

### Issue 正文摘录

### Current environment ### 🐛 Describe the bug When using `structured_outputs` (JSON schema) with Gemma 4, the model occasionally samples ` ` (token id **106**) **while the grammar FSM is still inside a JSON string value**, which terminates generation mid-string and produces an unterminated JSON response. xgrammar's bitmask should forbid ` ` until the grammar reaches its terminal state, but in v0.20.1 it does not. ### Symptom Sometimes Gemma 4 wanders into garbage tokens like `@{!}` mid-string, and then samples ` `. vLLM honors it as a stop signal. A representative truncated response: ```json {"field_a": "...", "field_b": "...", "field_c": "@{!} ``` Returned with: ``` finish_reason: "stop" stop_reason: 106 ← ``` The grammar FSM is clearly **not** at a terminal state here (open string, missing closing `"`, missing fields, missing `}`), yet ` ` was sampled successfully. ### Trigger conditions The bug is reproducible — and high-rate (~20–40% over 10–20 samples) — under this combination: - Gemma 4 31B (dense), specifically the NVFP4 quantized variant. The MoE 26B-A4B is less susceptible (likely because per-token compute uses fewer weights, so quantization noise per sampling step is sm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ` ` was sampled successfully. ### Trigger conditions The bug is reproducible — and high-rate (~20–40% over 10–20 samples) — under this combination: - Gemma 4 31B (dense), specifically the NVFP4 quantized variant. The Mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ples) — under this combination: - Gemma 4 31B (dense), specifically the NVFP4 quantized variant. The MoE 26B-A4B is less susceptible (likely because per-token compute uses fewer weights, so quantization noise per sampli...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ), yet ` ` was sampled successfully. ### Trigger conditions The bug is reproducible — and high-rate (~20–40% over 10–20 samples) — under this combination: - Gemma 4 31B (dense), specifically the NVFP4 quantized variant....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e model occasionally samples ` ` (token id **106**) **while the grammar FSM is still inside a JSON string value**, which terminates generation mid-string and produces an unterminated JSON response. xgrammar's bitmask sh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: (Gemma 4) xgrammar bitmask lets <end_of_turn> escape during structured outputs, terminating generation mid-JSON bug ### Current environment ### 🐛 Describe the bug When using `structured_outputs` (JSON schema) wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
