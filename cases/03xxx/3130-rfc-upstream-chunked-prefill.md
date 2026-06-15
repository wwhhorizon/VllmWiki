# vllm-project/vllm#3130: [RFC] Upstream Chunked Prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#3130](https://github.com/vllm-project/vllm/issues/3130) |
| 状态 | closed |
| 标签 |  |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | slowdown |
| 根因提示 | memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC] Upstream Chunked Prefill

### Issue 正文摘录

# Progress - 2D -> 1D query refactoring https://github.com/vllm-project/vllm/issues/3130 - Sequence group metadata API update https://github.com/vllm-project/vllm/pull/3538/files - Scheduler refactoring https://github.com/vllm-project/vllm/pull/3550 - Chunked prefill scheduler https://github.com/vllm-project/vllm/pull/3853 - Chunked prefill attention update https://github.com/vllm-project/vllm/pull/3884 - logprob fix https://github.com/vllm-project/vllm/pull/4309 - Enable cuda-graph on prefill path -> Won't do **Future Extension (not a scope of this RFC)** - Make it work with sliding window attention - Use same mechanism for prefix caching - Use better kernel than context attention forward (ideally flash infer) Chunked prefill chunks prefill requests into multiple chunks and batch them with decoding requests. Since prefill requests are compute-bound and decoding requests are memory-bound, it can greatly improve system efficiency by overlapping these two. See the linked papers for more details. - https://arxiv.org/pdf/2401.08671.pdf - https://arxiv.org/pdf/2308.16369.pdf We are planning to upstream chunked prefill internally used at Anyscale to OSS Vllm repo. We turned on this feat...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 84 - logprob fix https://github.com/vllm-project/vllm/pull/4309 - Enable cuda-graph on prefill path -> Won't do **Future Extension (not a scope of this RFC)** - Make it work with sliding window attention - Use same mech...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: toring https://github.com/vllm-project/vllm/issues/3130 - Sequence group metadata API update https://github.com/vllm-project/vllm/pull/3538/files - Scheduler refactoring https://github.com/vllm-project/vllm/pull/3550 -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC] Upstream Chunked Prefill # Progress - 2D -> 1D query refactoring https://github.com/vllm-project/vllm/issues/3130 - Sequence group metadata API update https://github.com/vllm-project/vllm/pull/3538/files - Schedul...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nd decoding requests are memory-bound, it can greatly improve system efficiency by overlapping these two. See the linked papers for more details. - https://arxiv.org/pdf/2401.08671.pdf - https://arxiv.org/pdf/2308.16369...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: repo. We turned on this feature in the Anyscale production endpoint. # Benchmark Result See https://github.com/vllm-project/vllm/issues/3130#issuecomment-2011281519 The following diagram is the benchmark result of Llama...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
