# Bitwise 下一轮复核队列

状态：active queue。  
作用：记录下一轮要补证的 bitwise/deterministic 工作项。本文只放队列和缺口，不承载最终机制结论；稳定结论应下沉到 [本专题机制页](README.md)。

维护规则见 [维护规则](../../docs/maintenance.md)；术语定义见 [Glossary](../../docs/glossary.md)。

## 本页使用方式

- 本页只保留当前优先追踪的未闭环项：`defer`、`include_with_boundary`、`unresolved_review_risk` 和 open workaround。
- 稳定结论已下沉到对应机制页和专题入口，不在这里重复维护。
- 本页默认只保留两层：`主线核心缺口` 和 `辅助边界队列`；每轮优先处理前者。
- warmup、test soundness、support gate、selector fallback、review risk、reference boundary 和 contract-only 辅助项统一进入 `辅助边界队列`，不与主线 closure 竞争优先级。
- 已稳定机制的长期 coverage 扩展回到对应机制页和 ledger，不再单独占用本队列。

## 主线核心缺口

| Source | 机制 | 当前状态 | 缺口 | 下一步 |
| --- | --- | --- | --- | --- |
| [#42125](https://github.com/vllm-project/vllm/issues/42125) | runtime LoRA / prefix cache identity | defer | 现已抓到 closed 的 [#42495](https://github.com/vllm-project/vllm/pull/42495) 和更新的 open PR [#45981](https://github.com/vllm-project/vllm/pull/45981)。与早先更激进的 `#42495` 不同，`#45981` 主动把 claim 缩到“本地可读 source 的 loader-effective content identity”：选中的 weight file、canonicalized `adapter_config.json`、`is_3d_lora_weight` 与 tensorizer config 一起进 `lora_cache_key`，并由 serving load path 与 `process_inputs` backstop 共用 `ensure_lora_cache_key` 填充；block-hash extra keys 也拆成 `("lora", name) + ("lora_identity", id)` 两层。结合当前 live patch，这条线其实已经形成 identity 计算、request 传播、block-hash 消费三层闭环；测试除 same-name different-path、same-path different-cache-key、same-content same-key、config/weight 变化改 key 外，还覆盖了 safetensors 优先级、length framing collision、relative path path-only fallback。当前真正剩下的不是 patch 内部机制，而是 PR 自己明确保留的 source/部署边界：HF Hub、relative/remote path、tensorizer/shared-nothing、多节点 rolling-upgrade、external KV connector、TOCTOU；截至 2026-06-21，`#45981` 仍只有作者正文与 bot 活动，reviewers 仍处于 awaiting requested review，尚无 substantive maintainer review。 | 优先追踪 `#45981` 的 merge 与后续 maintainer review；确认 unload/reload、same-path content change、block-hash extra key、path-only warning 与 old EngineCore peer/rolling-upgrade 边界是否保留，并防止方案被回退成 per-process counter 或 path-only identity。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | external KV / LoRA identity | defer | 现已抓到 linked PR [#45549](https://github.com/vllm-project/vllm/pull/45549)：它把 `lora_name` 折进 `LMCacheMPConnector` 的 internal cache salt，并补 unit test；issue comment 还指向上游 LMCache draft PR [#2962](https://github.com/LMCache/LMCache/pull/2962)。新增 insight 是：external KV 的缺口现在不只是“多层 key 还没一起闭环”，还包括 schema single source of truth 仍未定案。`#45549` 只证明了 vLLM vendored MP connector 的 internal salt 层必须带 adapter 维度；LMCache `#2962` 则已经扩到 MP connector、multi-process adapter、chunk-hash / `CacheEngineKey.tags` / L2 object key 多层，但 review 也在明确收敛一个更深的问题：LoRA 维度到底应该统一落在 tags 之类的主 schema 层，还是继续在 request config / token database / cache engine 多处镜像。相比 `#42125`，这条线仍更像“跨仓 schema 还未统一、主键落点也未定”；截至 2026-06-21，`#45549` 与 LMCache `#2962` 都仍 open，且没有新的 maintainer/reviewer acceptance signal。 | 继续追踪 `#45549` 与 LMCache `#2962` 的合并；重点确认 MP lookup/store key、vendored connector、chunk-hash/`CacheEngineKey.tags`/L2 object key 是否真正收敛到统一 schema 入口，并保留 same-adapter hit 与跨 adapter negative regression test。 |

## 辅助边界队列

| Source | 角色 | 下一步 |
| --- | --- | --- |
| [#42699](https://github.com/vllm-project/vllm/issues/42699) / [#40896](https://github.com/vllm-project/vllm/issues/40896) | prefix-cache 默认 exact reproducibility 契约边界 | 继续按“默认 prefix-cache 路径下的 exact reproducibility 契约边界”维护，而不是作为主线 direct-closure 缺口反复追逐：现有评论证据已显示 `fp32` 与 `VLLM_BATCH_INVARIANT=1` 可以让复现收敛，`#40896` maintainer 也明确说 prefix caching determinism 目前还未完全支持。后续只在出现 prefix-cache 专属 linked fix、官方 docs 声明变化、或新的 regression test/changed files 时，再升回主线复核。 |
| [#37076](https://github.com/vllm-project/vllm/issues/37076) / [#37152](https://github.com/vllm-project/vllm/pull/37152) | same-step registration visibility / block lifecycle contested hypothesis | 继续按“same-step registration visibility / block lifecycle 的 contested hypothesis”维护，而不是作为主线 direct-closure 缺口反复追逐：`#37152` 提供了 BlockPool same-step miss gate 与复现实验，但 maintainer 明确指出 same-step KV sharing 按设计允许，因为写 KV 发生在 attention 之前；closed/unmerged 的 [#38715](https://github.com/vllm-project/vllm/pull/38715) 虽补了 regression tests，作者也在收到该反馈后主动撤回 blanket guard。后续只有在出现 runtime instrumentation、maintainer-accepted patch、或新的 lifecycle trace 明确证明设计前提失效时，再升回主线复核。补充：open PR [#42359](https://github.com/vllm-project/vllm/pull/42359) 为这条假说提供了具体 patch 方向——`get_computed_blocks()` 的 `find_longest_cache_hit` 可将同一步内未提交 block 当作 cache hit，MambaManager 已有 `cached_blocks_this_step` guard 但 FullAttention 缺少；若该 PR 合并，可把 same-step visibility 从 contested hypothesis 升级为 landed boundary。 |
| [#42513](https://github.com/vllm-project/vllm/issues/42513) / [#42518](https://github.com/vllm-project/vllm/issues/42518) | eager-vs-BI contract boundary | 继续按 batch-invariant 契约边界维护，而不是作为主线 direct-closure 缺口反复追逐；只有在上游出现 selective fix、官方 eager-vs-BI contract test、文档化声明变化或新的 changed files 时，再升回主线复核。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | prefix-cache follow-up patch / correctness gap | 继续追踪 follow-up patch：`num_computed_tokens` 判断 prefill、`(num_prompt_tokens - 1)` 计算 block boundary，并补 resumed request 与 block-aligned prompt 回归测试。gemini-code-assist 发现两处 correctness gap（resumed request 漏检 + block-aligned final-token 不一致），作者未回复。 | 继续追踪 follow-up patch：用 `num_computed_tokens` 判断 prefill、用 `(num_prompt_tokens - 1)` 计算 block boundary，并补 resumed request 与 block-aligned prompt 回归测试。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | deterministic reduction scoped workaround | 继续追踪 PR 是否转为 ready/merged，以及上游 AITER 是否落地 deterministic split-K 修复；当前仍按 scoped workaround 维护，不外推到非 128x128 block-scaled shape。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | unresolved_review_risk / kv_cache_identity | 三处 bot review 缺陷未处理：CRITICAL FP8 raw_kv_scalar_t 类型转换错误；HIGH HND layout silent corruption；MEDIUM key/value OOB。14 reviewer 无人 approve。merge conflict 持续复现。机制更正为 kv_cache_identity（主）+ deterministic_dispatch_reduction（辅）。 | 2026-05-29 起多次 `needs-rebase`，作者在 2026-05-31/2026-06-12/2026-06-20 多次 force-push 清除后复现，patch 持续演进但截至 2026-06-21 仍无 maintainer approval；继续追踪 FP8 conversion 是否改为 `qk_t`/浮点输入，以及 NHD layout gate、key/value row guard 是否被 maintainer 接受并进入最终合并版本；未闭环前只作为 verification boundary/risk。 |
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | support-gate workaround / batch_invariance | 追踪 PR merge/CI（4 reviewer awaiting review, zero human activity since 2026-05-14）；补轻量 selector/support-gate 测试。SHA256 验证已通过。scope 不覆盖 FlashInferExperts 与非 MiniMax-M2 NVFP4。 | 追踪 PR merge/CI；若继续推进，优先补轻量 selector/support-gate 测试，证明 `VLLM_BATCH_INVARIANT=1` 下 FlashInfer 与 CUTLASS FP4 MoE 不再被 `False` gate 拦截。 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325) / [#42379](https://github.com/vllm-project/vllm/pull/42379) | reference boundary follow-up | 若后续 maintainer 重新定义 CUDA reference 为 FP32 multiply，要同步改机制页的 reference boundary。 |
| [#39849](https://github.com/vllm-project/vllm/pull/39849) | selector fallback workaround | 继续按 selector fallback/workaround 维护，而不是当作主线 closure：追踪 PR merge/CI；补 patched Qwen3-VL reranker score regression，并确认 gfx9 gqa_ratio 2/4 以外 shape 未误路由。 |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | warmup boundary | 只在找到 first-request token/logprob divergence 复现后再提升；否则保持 latency/warmup boundary。 |
| [#43317](https://github.com/vllm-project/vllm/pull/43317) | test soundness boundary | 追踪 PR 是否合并；如果未合并，所有 decode/prefill logprob mismatch 都要先排除 tokenizer roundtrip 改写 prefix 的误报。 |

## 不应 Promotion 的情况

- 只有关键词命中，没有 issue/PR 正文或评论证据。
- 只有问题描述，没有 linked fix、patch、maintainer resolution 或复现闭环。
- umbrella issue 没有拆到具体 PR 或具体机制。
- 只能证明 semantic answer 相似，不能证明 token/logprob/tensor/KV identity。
