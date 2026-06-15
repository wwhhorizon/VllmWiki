# VllmWiki

VllmWiki 是从本地 `vllm-project/vllm` issue 与 PR 数据炼化出的 source-backed wiki。
当前版本刻意采用证据优先：每个生成的 case 页都会指回原始 issue 正文、候选 PR 证据和抽取状态。

## 数据快照

- 原始 issue JSONL 行数：16,243
- 按编号去重后的原始 issue 数：15,818
- Operator/kernel 候选 case 行数：7,344
- Operator/kernel 候选 issue 去重数：7,239
- 原始 PR JSONL 行数：28,120
- PR 表按编号去重行数：8,931
- 本地存在 issue-PR 链接的 issue 数：1,275
- 本地缺失评论正文但有评论计数的 issue 数：14,271
- Issue 状态：closed=13,816, open=2,002
- Case 分类：correctness=3,748, performance=1,962, development=1,529

## 导航

- [方法论](METHODOLOGY.md)
- [Wiki 实现说明](WIKI_IMPLEMENTATION.md)
- [无限迭代协议](ITERATION_PROTOCOL.md)
- [KDA 风格优化流程](OPTIMIZATION_FLOW.md)
- [KDA 调研笔记](KDA_RESEARCH_NOTES.md)
- [质量门](QUALITY_GATE.md)
- [Curated：Bitwise 确定性与数值等价](curated/bitwise_determinism.md)
- [Bitwise 候选 ledger](candidates/bitwise_ledger.csv)
- [Schema](data/schemas.yaml)、[标签](data/tags.yaml)、[别名](data/aliases.yaml)、[版本声明](data/version-claims.yaml)
- [Issue 索引](indexes/issues.csv)
- [PR 索引](indexes/prs.csv)
- [Pattern 证据 ledger](evidence/pattern_evidence.csv)
- [构建 manifest](audit/manifest.md)

## 领域

- [模型支持](domains/model_support.md): 6,450 个候选 case
- [CI、构建与打包](domains/ci_build.md): 5,949 个候选 case
- [分布式与并行](domains/distributed_parallel.md): 5,324 个候选 case
- [前端与 Serving API](domains/frontend_api.md): 5,021 个候选 case
- [硬件适配](domains/hardware_porting.md): 4,914 个候选 case
- [采样与 Logits](domains/sampling_logits.md): 4,029 个候选 case
- [投机解码](domains/speculative_decoding.md): 3,599 个候选 case
- [量化与低精度](domains/quantization.md): 3,249 个候选 case
- [Attention 与 KV Cache](domains/attention_kv_cache.md): 2,561 个候选 case
- [调度与内存](domains/scheduler_memory.md): 1,527 个候选 case
- [GEMM 与 Linear Kernel](domains/gemm_linear.md): 1,391 个候选 case
- [MoE](domains/moe.md): 1,201 个候选 case
- [多模态与 VLM](domains/multimodal_vlm.md): 741 个候选 case
- [激活与归一化](domains/activation_norm.md): 381 个候选 case
- [未分类](domains/uncategorized.md): 57 个候选 case

## 优化模式

- [Bitwise 确定性与数值等价](patterns/bitwise_determinism_equivalence.md): 2,872 个 issue 命中，1,981 个 PR 命中
- [Backend 路由与 Fallback](patterns/backend_routing_fallback.md): 6,908 个 issue 命中，4,183 个 PR 命中
- [Metadata 与 Layout 契约](patterns/metadata_layout_contract.md): 6,519 个 issue 命中，3,521 个 PR 命中
- [Dtype、量化与 Scale 路径](patterns/dtype_quantization_path.md): 6,113 个 issue 命中，4,141 个 PR 命中
- [KV Cache 容量、压缩与 Offload](patterns/kv_cache_capacity_offload.md): 3,087 个 issue 命中，1,808 个 PR 命中
- [MoE、GEMM 与 Expert Routing](patterns/moe_gemm_routing.md): 4,034 个 issue 命中，3,801 个 PR 命中
- [Scheduler 与请求状态生命周期](patterns/scheduler_request_lifecycle.md): 11,857 个 issue 命中，5,143 个 PR 命中
- [硬件架构 Guard](patterns/hardware_arch_guard.md): 13,162 个 issue 命中，6,890 个 PR 命中
- [构建、依赖与打包](patterns/build_dependency_packaging.md): 11,884 个 issue 命中，7,338 个 PR 命中
- [模型格式与 Adapter 路径](patterns/model_format_adapter.md): 13,023 个 issue 命中，7,709 个 PR 命中
- [验证与 Benchmark](patterns/verification_benchmarking.md): 12,558 个 issue 命中，7,021 个 PR 命中

## 优先焦点：Bitwise 与数值等价

Bitwise/determinism case 应该先于宽泛的 performance-only case 复核，因为它们经常暴露更深的契约：cache-hit 与 cache-miss 等价、batch-size invariance、backend-specific 累加顺序、BF16/FP8 scale 语义，以及 prefix-cache 状态生命周期。
从 [Bitwise 确定性与数值等价](patterns/bitwise_determinism_equivalence.md) 开始，再沿着代表性 issue 和 PR 证据继续阅读。
curated 路径是 [Bitwise 确定性与数值等价](curated/bitwise_determinism.md)，包含严格的 [Bitwise 复核队列](curated/bitwise_review_queue.md)，以及 prefix cache 等价、batch invariance、KV identity、quant/dtype 语义、deterministic dispatch/reduction、verification contract 等机制页。

## 查询工具

可使用 KernelWiki 风格的访问工具：

```powershell
python VllmWiki\scripts\query_vllmwiki.py bitwise --kind issue --limit 5
python VllmWiki\scripts\get_page.py 33123 --follow-sources
python VllmWiki\scripts\grep_wiki.py "deterministic prefix" --only wiki
python VllmWiki\scripts\validate_vllmwiki.py
```

## 如何阅读这个 Wiki

1. 已知子系统时，从领域页开始。
2. 想找可复用优化经验时，使用 pattern 页。
3. 在信任结论前，打开代表性 case 页阅读源证据。
4. 在源证据完成复核前，把 `root_cause_hint`、`work_area` 和 pattern match 只当作导航提示。
