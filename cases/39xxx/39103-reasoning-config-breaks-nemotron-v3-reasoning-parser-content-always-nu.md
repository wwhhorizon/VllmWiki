# vllm-project/vllm#39103: `--reasoning-config` breaks Nemotron v3 reasoning parser (content always null, thinking unbounded)

| 字段 | 值 |
| --- | --- |
| Issue | [#39103](https://github.com/vllm-project/vllm/issues/39103) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> `--reasoning-config` breaks Nemotron v3 reasoning parser (content always null, thinking unbounded)

### Issue 正文摘录

**Summary** When running Nemotron-3-Super with `--reasoning-parser nemotron_v3`, adding `--reasoning-config` causes all responses to have `content: null`, while all generated tokens go into the reasoning trace. Without `--reasoning-config`, the parser works, but there's no way to cap thinking tokens, so short `max_tokens` calls can be completely consumed by thinking. This looks like an interaction/compatibility bug between `--reasoning-config` and the `nemotron_v3` reasoning parser. --- ### Environment - vLLM version: 0.19.1rc1.dev35+g968ed02ac (cu130-nightly) - Backend: NVIDIA GB10 (DGX Spark, SM121) - Model: `NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` - Launch flags (repro case): ```bash python -m vllm.entrypoints.openai.api_server \ --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 \ --reasoning-parser nemotron_v3 \ # variant A (works, but no thinking cap) # [no --reasoning-config] # variant B (broken; used for repro) --reasoning-config '{"reasoning_start_str":" ","reasoning_end_str":" "}' ``` Client: OpenAI-compatible `/v1/chat/completions` (via LiteLLM proxy, but behavior confirmed directly against vLLM as well). --- ### Expected behavior - With `--reasoning-parser nemotro...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: g` and the `nemotron_v3` reasoning parser. --- ### Environment - vLLM version: 0.19.1rc1.dev35+g968ed02ac (cu130-nightly) - Backend: NVIDIA GB10 (DGX Spark, SM121) - Model: `NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` - La...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: IDIA GB10 (DGX Spark, SM121) - Model: `NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` - Launch flags (repro case): ```bash python -m vllm.entrypoints.openai.api_server \ --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `--reasoning-config` breaks Nemotron v3 reasoning parser (content always null, thinking unbounded) **Summary** When running Nemotron-3-Super with `--reasoning-parser nemotron_v3`, adding `--reasoning-config` causes all...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nvironment - vLLM version: 0.19.1rc1.dev35+g968ed02ac (cu130-nightly) - Backend: NVIDIA GB10 (DGX Spark, SM121) - Model: `NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` - Launch flags (repro case): ```bash python -m vllm.entr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: et params. 3. **LiteLLM proxy** — Verified not the root cause; behavior reproduced calling vLLM directly. --- ### Hypothesis There is a **double-parsing / conflicting logic** between: - The per-model reasoning parser `n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
