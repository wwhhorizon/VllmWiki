# vllm-project/vllm#35550: [RFC]: Batch-Aware Expert Pruning for MoE Decode (XShare)

| 字段 | 值 |
| --- | --- |
| Issue | [#35550](https://github.com/vllm-project/vllm/issues/35550) |
| 状态 | open |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;moe;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Batch-Aware Expert Pruning for MoE Decode (XShare)

### Issue 正文摘录

### Motivation During MoE decode, each forward pass loads expert weights from HBM for every activated expert. Each token routes to only k experts (e.g., k=6), but the union of activated experts across a batch grows with batch size. The XShare paper ([Section 3](https://arxiv.org/abs/2602.07265)) measures this on DeepSeek-R1 (256 experts, k=8): at batch=32, 163/256 experts are activated; at batch=64, 243/256. The key observation is that expert demand is highly skewed: a small subset captures most of the aggregate routing score. [XShare](https://arxiv.org/abs/2602.07265) proposes **batch-aware expert selection**: before top-k routing, aggregate expert demand across the batch and mask low-scoring experts. The fused MoE kernel then skips loading masked experts entirely, reducing HBM reads proportional to the pruning ratio. We propose adding this as a configurable optimization in vLLM. Our implementation delivers **+53% throughput** at concurrency 32 on GPT-OSS-120B (128 experts, budget=24) with **no measurable quality degradation** on MMLU-Pro or GSM-8K across multiple pruning configurations. This is a routing-level optimization, complementary to EP ([#20323](https://github.com/vllm-p...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #35551 feat: batch-aware expert pruning (XShare) for MoE models

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Batch-Aware Expert Pruning for MoE Decode (XShare) stale ### Motivation During MoE decode, each forward pass loads expert weights from HBM for every activated expert. Each token routes to only k experts (e.g., k=...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [RFC]: Batch-Aware Expert Pruning for MoE Decode (XShare) stale ### Motivation During MoE decode, each forward pass loads expert weights from HBM for every activated expert. Each token routes to only k experts (e.g., k=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: t demand is highly skewed: a small subset captures most of the aggregate routing score. [XShare](https://arxiv.org/abs/2602.07265) proposes **batch-aware expert selection**: before top-k routing, aggregate expert demand...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ts. The fused MoE kernel then skips loading masked experts entirely, reducing HBM reads proportional to the pruning ratio. We propose adding this as a configurable optimization in vLLM. Our implementation delivers **+53...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 16 | 1,342 | 1,835 | **+37%** | | 32 | 1,996 | 3,054 | **+53%** | Gains scale with batch size. Similar pattern on GPT-OSS-20B (32 experts, +18% at c=32). Full benchmark tables, rate-limited serving results, and the 32-e...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | ting"] --> f["fused moe kernel"] style xshare fill:#ebf5fb,stroke:#4a90d9,stroke-width:2px ``` before top-k routing, router logits are summed per expert across the batch. the to |
| [#35551](https://github.com/vllm-project/vllm/pull/35551) | mentioned | 0.45 | feat: batch-aware expert pruning (XShare) for MoE models | for moe inference](https://arxiv.org/abs/2602.07265) - **draft pr:** [#35551](https://github.com/vllm-project/vllm/pull/35551) (includes implementation, full benchmark data, quali… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
