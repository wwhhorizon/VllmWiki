# vllm-project/vllm#37075: [RFC]: Opt-in Media URL Cache for `MediaConnector`

| 字段 | 值 |
| --- | --- |
| Issue | [#37075](https://github.com/vllm-project/vllm/issues/37075) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | operator |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Opt-in Media URL Cache for `MediaConnector`

### Issue 正文摘录

### Motivation. Every time vLLM processes a request containing a media URL (image, audio, video), `MediaConnector.load_from_url()` performs a fresh HTTP download, even if that exact URL was fetched seconds ago in a previous request. There is no deduplication or caching layer for URL-based media. This creates real problems in two areas: * CI / testing infrastructure: On CI machines with limited or unreliable network access, repeated downloads of the same media across test runs cause flaky tests and inflated runtimes. A single network hiccup can fail an entire test suite. * Production / on-prem deployments: Many organizations run vLLM on infrastructure behind firewalls, in air-gapped environments, or on machines with constrained egress. Repeated identical downloads is likely to result in HTTP conn refusal errors. This is the case in many AMD Ci builds as well. ### Proposed Change. Add an opt-in, URL-level byte cache to `MediaConnector`, controlled by a single environment variable: ``` VLLM_MEDIA_CACHE=/path/to/cache/dir ``` When set, `MediaConnector` will: 1. Hash the URL (SHA-256, truncated) to produce a cache key 2. Check if the file exists on disk before making an HTTP request 3....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: g layer for URL-based media. This creates real problems in two areas: * CI / testing infrastructure: On CI machines with limited or unreliable network access, repeated downloads of the same media across test runs cause...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: harder to share across machines, doesn't work with NFS/pre-warming. 3. **ROCm-specific path**: Would solve the immediate CI problem but fragments the codebase. The feature is hardware-agnostic and useful everywhere. Thi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: AMD CI to eliminate redundant downloads across test runs. That PR covers model weights (HuggingFace, ModelScope), vLLM's own S3 assets (`VLLM_CACHE_ROOT`), and test data (`VLLM_TEST_CACHE`), all through test/infra chang...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: 2. Check if the file exists on disk before making an HTTP request 3. On cache miss, download as usual and write the result to the cache directory 4. On cache hit, read from disk and skip the HTTP request entirely When *...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: he for `MediaConnector` RFC ### Motivation. Every time vLLM processes a request containing a media URL (image, audio, video), `MediaConnector.load_from_url()` performs a fresh HTTP download, even if that exact URL was f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
