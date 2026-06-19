# Bitwise 下一轮复核队列

状态：active queue。  
作用：记录下一轮要补证的 bitwise/deterministic 工作项。本文只放队列和缺口，不承载最终机制结论；稳定结论应下沉到 [本专题机制页](README.md)。

## 本页使用方式

- 本页只追踪未闭环项：`defer`、`include_with_boundary`、`unresolved_review_risk` 和 open workaround。
- 稳定结论已下沉到对应机制页和专题入口，不在这里重复维护。
- warmup、test soundness、support gate、selector fallback 默认按边界排队，不在本页写成 landed fix。

## Must Review

| Source | 机制 | 当前状态 | 缺口 | 下一步 |
| --- | --- | --- | --- | --- |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | quant/dtype loading identity | defer | 本地 evidence 只有 open issue body，comments/timeline 均为空；`clone()`、每次或最终 `torch.cuda.synchronize()`、改变 stream file 顺序只是作者定位实验，不能当作 upstream fix。 | 寻找 linked PR/commit/test，重点看 `runai_safetensors_weights_iterator` ownership、`BaseModelLoader.load_model()` copy synchronization、shared buffer lifetime 和 unified-memory 平台回归测试。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | external KV / LoRA identity | defer | 现已抓到 linked PR [#45549](https://github.com/vllm-project/vllm/pull/45549)：它把 `lora_name` 折进 `LMCacheMPConnector` 的 internal cache salt，并补 unit test；issue comment 还指向上游 LMCache `#2962` 的 MP 路径修复。但两边都仍 open，且 `lora_name` 不等于最终稳定 adapter version identity。 | 继续追踪 `#45549` 与 LMCache `#2962` 的合并；确认 MP lookup/store key 与 vLLM vendored connector 同步闭环，并补 same-adapter hit 保留、cross-adapter negative hit 与 version 边界测试。 |
| [#42699](https://github.com/vllm-project/vllm/issues/42699), [#40896](https://github.com/vllm-project/vllm/issues/40896) | prefix cache 等价 | defer | 复现和评论证据支持 prefix 路径可翻转 greedy token；但当前只有 mitigation 线索，没有 root-cause patch、maintainer resolution 或 regression test。 | 寻找 linked fix/docs/test PR；补齐 no-prefix、cold prefix、warm prefix、fp32、`VLLM_BATCH_INVARIANT=1` 的验证矩阵。 |
| [#37076](https://github.com/vllm-project/vllm/issues/37076) | prefix cache / KV block identity | defer | 现已抓到 linked PR [#37152](https://github.com/vllm-project/vllm/pull/37152)：patch 用 `_blocks_registered_this_step` 阻止同一步新注册 block 被 `get_cached_block()` 命中，并在 `new_step_starts()` 清理。但 PR 仍 open/unmerged，只有 reproducer 与两处代码修改，没有 regression test 或 maintainer resolution。 | 继续追踪 `#37152` 的 merge、测试和 maintainer 接受情况；确认 same-step miss gate 生命周期、prefix sharing 性能边界，以及是否补上回归测试。 |
| [#42125](https://github.com/vllm-project/vllm/issues/42125) | runtime LoRA / prefix cache identity | defer | 现已抓到 closed 的 [#42495](https://github.com/vllm-project/vllm/pull/42495) 和更新的 open PR [#45981](https://github.com/vllm-project/vllm/pull/45981)。`#42495` 用 per-load cache key 先解 stale reuse；`#45981` 改为 content-derived `lora_cache_key`，更符合 same-name same-path content change 的根因，但 PR body 明说只部分覆盖 issue，仍不包括 HF Hub、remote path、external KV connector 和 TOCTOU 窗口。 | 继续追踪 `#45981` 的 merge 与后续评论；确认 `lora_cache_key` 是否真正进入 block hash、same-name reload negative tests 是否覆盖 unload/reload 与 same-path content change，并把未覆盖边界继续留在 defer。 |
| [#42513](https://github.com/vllm-project/vllm/issues/42513) | MTP/spec decode kernel selection | defer | issue body 指向 MTP verification batch size=2 与普通 decode batch size=1 引起 cuBLAS algorithm 差异，但没有 comments、linked fix、changed files 或 closure reason。 | 寻找关闭原因和 linked fix；确认 CUDA graph/eager、cuBLAS algorithm lock、KV 放大链路和 regression test。 |

## Strong Include Needs More Detail

| Source | 机制 | 下一步 |
| --- | --- | --- |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | prefix cache 等价 | 继续追踪 follow-up patch：用 `num_computed_tokens` 判断 prefill、用 `(num_prompt_tokens - 1)` 计算 block boundary，并补 resumed request 与 block-aligned prompt 回归测试。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | deterministic reduction | 继续追踪 PR 是否转为 ready/merged，以及上游 AITER 是否落地 deterministic split-K 修复；当前仍按 scoped workaround 维护，不外推到非 128x128 block-scaled shape。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | verification contract | 追踪 FP8 conversion 是否改为 `qk_t`/浮点输入，以及 NHD layout gate、key/value row guard 是否被 maintainer 接受并进入最终合并版本；未闭环前只作为 verification boundary/risk。 |
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | batch invariance support gate | 追踪 PR merge/CI；若继续推进，优先补轻量 selector/support-gate 测试，证明 `VLLM_BATCH_INVARIANT=1` 下 FlashInfer 与 CUTLASS FP4 MoE 不再被 `False` gate 拦截。 |
| [#42120](https://github.com/vllm-project/vllm/pull/42120) | quant/dtype LoRA MoE | 追踪 PR merge；补 wrong-input-dtype regression，以及 routed-expert LoRA weights 非零时的 adapter path 验证。 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325) / [#42379](https://github.com/vllm-project/vllm/pull/42379) | RMSNorm dtype semantics | 若后续 maintainer 重新定义 CUDA reference 为 FP32 multiply，要同步改机制页的 reference boundary。 |
| [#43741](https://github.com/vllm-project/vllm/pull/43741) | recycled KV block zeroing | 追踪 PR merge；若最终 patch 改动，确认 spec gate、`new_block_ids` tracking 和 patched e2e validation 都保留。 |
| [#25603](https://github.com/vllm-project/vllm/pull/25603) | batch-invariant plumbing | 后续检查更多 kernels 是否接入 `VLLM_BATCH_INVARIANT`，尤其是 review 中提到的 multidim `torch.sum` / mean deterministic reduction。 |
| [#34878](https://github.com/vllm-project/vllm/pull/34878) | ROCm beam search verification | 可补到 verification matrix：beam search/ranking 需要 logprob ranking 稳定，`semantic output same` 不够。 |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | cold-start warmup | 只在找到 first-request token/logprob divergence 复现后再提升；否则保持 latency/warmup boundary。 |
| [#32561](https://github.com/vllm-project/vllm/pull/32561) | cascade attention gate | 后续只追踪评论拆出的独立问题：FlashInfer CTA tile/chunked prefill、MLA、MoE router gate、AWQ 长输出；不要把这些缺口归到 cascade attention fix 本身。 |
| [#39849](https://github.com/vllm-project/vllm/pull/39849) | ROCm backend selector workaround | 追踪 PR merge/CI；补 patched Qwen3-VL reranker score regression，并确认 gfx9 gqa_ratio 2/4 以外 shape 未误路由。 |
| [#38670](https://github.com/vllm-project/vllm/pull/38670) | AWQ/Marlin batch invariance | 只在后续出现 deterministic AWQ_Marlin fused path 后再改结论；当前维持“BI mode 绕开 Marlin”的性能换确定性边界。 |
| [#30018](https://github.com/vllm-project/vllm/pull/30018) | FA2/LoRA batch invariance | 查找后续 CUDA graph compatible FA2 BI patch，并补 LoRA landed-code split-K 子路径；未闭环前不要把 `enforce_eager` 测试外推到 CUDA graph serving。 |
| [#33688](https://github.com/vllm-project/vllm/pull/33688) | TRITON_ATTN backend coverage | 追踪 MLA、FlashInfer、chunked prefill 和其他 Triton attention variant 是否进入 decode-invariant backend list。 |
| [#40408](https://github.com/vllm-project/vllm/pull/40408) | Cutlass FP8 fixed-config path | 后续 Cutlass FP8 tuning 改动都要重新检查 config 是否仍 independent of `M`，并跑多 batch-size/M 维测试。 |
| [#40413](https://github.com/vllm-project/vllm/pull/40413) | fused add RMSNorm | 审查其他 fused norm/quant op 是否有同等 BI 证据；没有测试前不要套用该结论。 |
| [#27660](https://github.com/vllm-project/vllm/pull/27660) | torch.compile batch invariance | 如果后续重新允许 AOT compile 或改变 PyTorch/cuBLAS flag，需要重新跑多 batch/M 维 logprob equality；不要把该 PR 外推成所有 compile path 天然稳定。 |
| [#35219](https://github.com/vllm-project/vllm/pull/35219) | hybrid Mamba block zeroing | 后续 Mamba/hybrid 问题要区分 cross-dtype stale NaN、metadata pointer、prefix-cache identity 和 MTP kernel-selection；不要把 narrow hybrid zeroing 写成通用 KV zeroing。 |
| [#42650](https://github.com/vllm-project/vllm/pull/42650) | non-uniform Q-head metadata | 追踪 Gemma4 MTP grouping key 修复；确认 target/draft Q-head 不同的 layers 不再混入同一 attention group。 |
| [#43317](https://github.com/vllm-project/vllm/pull/43317) | decode/prefill test soundness | 追踪 PR 是否合并；如果未合并，所有 decode/prefill logprob mismatch 都要先排除 tokenizer roundtrip 改写 prefix 的误报。 |

## 不应 Promotion 的情况

- 只有关键词命中，没有 issue/PR 正文或评论证据。
- 只有问题描述，没有 linked fix、patch、maintainer resolution 或复现闭环。
- umbrella issue 没有拆到具体 PR 或具体机制。
- 只能证明 semantic answer 相似，不能证明 token/logprob/tensor/KV identity。
