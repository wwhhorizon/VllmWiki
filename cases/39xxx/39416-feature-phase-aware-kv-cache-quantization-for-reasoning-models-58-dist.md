# vllm-project/vllm#39416: [Feature] Phase-aware KV cache quantization for reasoning models (58% distortion reduction measured)

| 字段 | 值 |
| --- | --- |
| Issue | [#39416](https://github.com/vllm-project/vllm/issues/39416) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Phase-aware KV cache quantization for reasoning models (58% distortion reduction measured)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Summary I would like to propose adding **per-phase KV cache quantization** for reasoning models (DeepSeek-R1, QwQ, o-series). The idea is simple: instead of applying a single `kv_cache_dtype` to all tokens, allow different bit widths for the think-phase and answer-phase tokens based on measured redundancy. I have published a paper with a closed-form theorem and empirical validation showing this approach cuts attention KL divergence by **58%** compared to uniform 3-bit quantization on DeepSeek-R1-Distill-1.5B, with no additional inference-time compute. ## Motivation vLLM currently supports uniform KV cache quantization via `--kv-cache-dtype` (fp8, fp8_e4m3, etc.). This works well for standard LLMs. But reasoning models have a structural asymmetry that uniform quantization ignores: - **Think-phase tokens** (~75% of generation): internal scratchpad, variable redundancy - **Answer-phase tokens** (~25% of generation): final response, different redundancy profile On **distilled** reasoning models (1.5B-7B), the answer phase is actually *more* redundant than the think phase - the opposite of what is reported on the full 671B model. Applying the...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature] Phase-aware KV cache quantization for reasoning models (58% distortion reduction measured) feature request ### 🚀 The feature, motivation and pitch ## Summary I would like to propose adding **per-phase KV cache...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature] Phase-aware KV cache quantization for reasoning models (58% distortion reduction measured) feature request ### 🚀 The feature, motivation and pitch ## Summary I would like to propose adding **per-phase KV cache...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ization for reasoning models (58% distortion reduction measured) feature request ### 🚀 The feature, motivation and pitch ## Summary I would like to propose adding **per-phase KV cache quantization** for reasoning models...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: theorem and empirical validation showing this approach cuts attention KL divergence by **58%** compared to uniform 3-bit quantization on DeepSeek-R1-Distill-1.5B, with no additional inference-time compute. ## Motivation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on distortion. ### Measured Data (DeepSeek-R1-Distill-Qwen-1.5B, n=50, GSM8K) | Metric | Think Phase | Answer Phase | |--------|-------------|--------------| | Pairwise cosine ρ | 0.463 ± 0.040 | 0.544 ± 0.045 | | Fract...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
