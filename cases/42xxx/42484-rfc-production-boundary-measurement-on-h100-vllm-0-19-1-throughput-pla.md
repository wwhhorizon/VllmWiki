# vllm-project/vllm#42484: [RFC] Production-boundary measurement on H100 + vLLM 0.19.1: throughput plateau at c=4→16, methodology critique invited

| 字段 | 值 |
| --- | --- |
| Issue | [#42484](https://github.com/vllm-project/vllm/issues/42484) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;fp8;operator |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] Production-boundary measurement on H100 + vLLM 0.19.1: throughput plateau at c=4→16, methodology critique invited

### Issue 正文摘录

> **Updated 2026-05-13 after Lambda H100 SXM5 cross-provider replication.** Original framing preserved in GitHub edit history (click the "edited" link next to the timestamp). Major changes: ctx 8K c=4/c=16 reproduces across providers under fresh-server conditions; warm-vs-fresh server state introduces a separate observation; fairness 4.3× number is environment-specific (Lambda shows 1.08× at 90/10 mix under n=100). ## Motivation Single-stream benchmarks dominate published LLM serving numbers, but production traffic is concurrent. This RFC documents a measurement protocol applied to vLLM 0.19.1 on H100 SXM5, with a cross-provider follow-up that reproduces the structural boundary across two providers under matched fresh-server conditions. I am posting this as an RFC for methodology critique because: 1. The boundary shape was sharper than I expected and I want to confirm I am not misinterpreting a vLLM scheduler behavior or a benchmark artifact. 2. If the shape is real, it has implications for how operators should pick concurrency under similar production load — the decision is currently driven by intuition, not measurement. 3. After the original Spheron run I extended with a Lambda...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [RFC] Production-boundary measurement on H100 + vLLM 0.19.1: throughput plateau at c=4→16, methodology critique invited RFC > **Updated 2026-05-13 after Lambda H100 SXM5 cross-provider replication.** Original framing pr...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: n v3 | | Model | `RedHatAI/Meta-Llama-3.1-70B-Instruct-FP8` | (same) | | KV cache dtype | FP8 | FP8 | | vLLM args | `--max-num-seqs 64 --max-model-len 32768 --gpu-memory-utilization 0.95 --kv-cache-dtype fp8` | (same) |...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ** Original framing preserved in GitHub edit history (click the "edited" link next to the timestamp). Major changes: ctx 8K c=4/c=16 reproduces across providers under fresh-server conditions; warm-vs-fresh server state...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: cenario logs, vLLM server logs, pip freeze, nvidia-smi dump, environment metadata, and analysis scripts: `https://github.com/jacob-sunho-kim/llm-boundary-research` (cross-provider sprint at `findings/cross_provider_lamb...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: sed Change No vLLM code change is proposed. The "change" requested is informational: I would value pointers on whether (a) the boundary shape generalizes, (b) the methodology has gaps, (c) the warm-server observation is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
