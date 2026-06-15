# vllm-project/vllm#34018: [RFC]: Helix (Context + Tensor) Parallelism for Efficient Long-Context Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#34018](https://github.com/vllm-project/vllm/issues/34018) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cache;moe |
| 症状 | slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Helix (Context + Tensor) Parallelism for Efficient Long-Context Decoding

### Issue 正文摘录

### Motivation. This RFC proposes adding **Helix (Context + Tensor) Parallelism** to vLLM, based on [NVIDIA's Helix paper](https://arxiv.org/abs/2507.07120) (July 2025). Helix enables efficient long-context decoding by combining Context Parallelism (sequence sharding) with Tensor Parallelism (head sharding), eliminating KV cache duplication that occurs in traditional Tensor Parallelism when `TP > num_kv_heads`. **Paper results (NVIDIA):** - Up to **1.5× decode latency reduction** at fixed batch size - Up to **32× more concurrent users** at same latency target - Communication overhead **O(B × H)**, independent of sequence length **Key benefits for vLLM:** - **Eliminates KV cache replication** when TPA > num_kv_heads, improving memory efficiency - **Reduces memory pressure** for long-context workloads (256K+ tokens) - Enables scaling MLA (DeepSeek) and GQA (Llama, Qwen) models more efficiently ## Motivation ### The Problem: KV Cache Duplication Modern LLMs increasingly use **MLA** (Multi-head Latent Attention) or **GQA** (Grouped Query Attention) to reduce KV cache memory. However, these architectures have few KV heads: | Model | Attention | KV Heads | Problem with TP=8 | |-------|-...

## 现有链接修复摘要

#34024 [Core] Add Helix (Context + Tensor) Parallelism

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ntext workloads (256K+ tokens) - Enables scaling MLA (DeepSeek) and GQA (Llama, Qwen) models more efficiently ## Motivation ### The Problem: KV Cache Duplication Modern LLMs increasingly use **MLA** (Multi-head Latent A...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [RFC]: Helix (Context + Tensor) Parallelism for Efficient Long-Context Decoding RFC ### Motivation. This RFC proposes adding **Helix (Context + Tensor) Parallelism** to vLLM, based on [NVIDIA's Helix paper](https://arxi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: --- | | Communication | AllGather Q + ReduceScatter | **All-to-All + LSE** | | Q distribution | AllGather to all ranks | Distributed by TPA | | KV efficiency | Replicates when TPA > K | **No replication** | | GQA at TP=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Helix (Context + Tensor) Parallelism for Efficient Long-Context Decoding RFC ### Motivation. This RFC proposes adding **Helix (Context + Tensor) Parallelism** to vLLM, based on [NVIDIA's Helix paper](https://arxi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ding, TPA = head sharding) FFN Phase: TPF × EP (standard tensor/expert parallelism) ``` ### Key Difference from DCP | Aspect | Standard DCP | Helix | | ----------------- | --------------------------- | -----------------...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34024](https://github.com/vllm-project/vllm/pull/34024) | mentioned | 0.6 | [Core] Add Helix (Context + Tensor) Parallelism | ts 32K-1M - Llama-3.1-8B (GQA): TP=8, DCP=2 **Performance:** See RFC #34018 for benchmark methodology. The NVIDIA Helix paper reports 1.5x decode latency reduction and 32x more co… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
