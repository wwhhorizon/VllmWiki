# vllm-project/vllm#16016: [RFC]: Cache Salting for Secure and Flexible Prefix Caching in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16016](https://github.com/vllm-project/vllm/issues/16016) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Cache Salting for Secure and Flexible Prefix Caching in vLLM

### Issue 正文摘录

### Motivation. vLLM’s prefix caching (APC) improves inference performance by reusing previously computed KV cache accross requests. The prefix cache operates by hashing input in fixed-size blocks (typically 16 tokens), and can use strong hashing (e.g., SHA-256) to guard against hash collisions. However, as demonstrated in [Leaking Secrets from Prefix Caches](https://arxiv.org/html/2411.18191v1), the cache remains vulnerable to timing-based side-channel attacks. An attacker can infer cache reuse by guessing popular inputs and measuring latency — potentially compromising privacy especially in shared or multi-tenant environments. What’s missing in vLLM today is a simple, effective way to **segment cache reuse across groups** while preserving performance. Note that other providers do also limit cache sharing, e.g., OpenAI is [limiting cache sharing to organizations](https://platform.openai.com/docs/guides/prompt-caching). ### Proposed Change. We propose to salt block hashes by introducing an optional top-level field in the request schema, which allows users to set the salts to be used for hashing per request. By sharing the salt, users can enable prefix caching while protecting the p...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: while protecting the user's or subgroups prompts, up to an arbitrary hierarchy of user groups. This includes protecting most sensitive information by keeping salts local without sharing. ## Comparison ### (A) Single-bar...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: hing (APC) improves inference performance by reusing previously computed KV cache accross requests. The prefix cache operates by hashing input in fixed-size blocks (typically 16 tokens), and can use strong hashing (e.g....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: cross requests. The prefix cache operates by hashing input in fixed-size blocks (typically 16 tokens), and can use strong hashing (e.g., SHA-256) to guard against hash collisions. However, as demonstrated in [Leaking Se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rary hierarchy of user groups. This includes protecting most sensitive information by keeping salts local without sharing. ## Comparison ### (A) Single-barrier design - Single salt means only one barrier per request. -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: attacker can infer cache reuse by guessing popular inputs and measuring latency — potentially compromising privacy especially in shared or multi-tenant environments. What’s missing in vLLM today is a simple, effective w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
