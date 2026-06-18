# Bitwise 下一轮复核队列

状态：active queue。  
作用：记录下一轮要补证的 bitwise/deterministic 工作项。本文只放队列和缺口，不承载最终机制结论；稳定结论应下沉到 [本专题机制页](README.md)。

## 已完成本轮推进

| Source | 状态 | 本轮结论 |
| --- | --- | --- |
| [#39096](https://github.com/vllm-project/vllm/issues/39096) / [#38938](https://github.com/vllm-project/vllm/pull/38938) | include | 已确认 batch invariance regression 至少包含两个具体机制：`ParallelLMHead` 的 `UnquantizedEmbeddingMethod.apply` 未走 deterministic Triton persistent kernel，以及 SM<90 下 `torch.compile` + CUDA graphs 组合需要边界处理。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | include + boundary | scheduler split 是核心机制方向；本轮确认 review comment 直接命中当前 patch：`request.num_output_tokens > 0` 与 `remainder == 0` 两个早退会漏掉 resumed request、block-aligned prompt 和 final-token scheduler 约束。 |
| [#39591](https://github.com/vllm-project/vllm/pull/39591) | include + invariant | `BlockTable` 的稳定契约不是“写入当前 slice”，而是 `num_blocks_per_row` 之后 tail 必须为零；本轮确认 `move_row` 整行复制是性能/简化建议，不是 correctness 阻塞。 |
| [#42240](https://github.com/vllm-project/vllm/pull/42240) | include + workaround | `splitK=0` 是 scoped workaround，绕过 CK/CK-Tile split-K atomic reduction；本轮确认 128x128 weight group guard 已进入 `can_implement` 和 call-site assert，env opt-out 也被删除。 |
| [#43355](https://github.com/vllm-project/vllm/pull/43355) | include + risk | PR 的 bit-identical test 有价值；本轮深读修正了风险状态：HND/NHD layout gate 与 key/value row guard 已在 patch 中出现，FP8 `scaled_convert` 仍使用 `raw_kv_scalar_t`，且 PR 仍 open/unmerged、有 merge conflict 提醒。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | strong defer | issue body 和评论已足以支持 external KV key 缺 adapter identity 的 root-cause 方向；但评论中的 `lora_name` patch 只是本地对照实验，未证明上游 MP connector、vLLM vendored connector 和 regression test 已闭环。 |
| [#42699](https://github.com/vllm-project/vllm/issues/42699) / [#40896](https://github.com/vllm-project/vllm/issues/40896) | defer | prefix-read/no-prefix-read 与 cold/warm prefix cache 的 greedy token 差异更像 BF16 batch/kernel geometry 边界：评论显示 `fp32` 或 `VLLM_BATCH_INVARIANT=1` 可让输出收敛，但缺 linked fix PR 和 regression test。 |
| [#42670](https://github.com/vllm-project/vllm/pull/42670) | include + boundary | FlashInfer/CUTLASS FP4 MoE 已有 batch-invariant code path，但 support gate 继承 base-class `False`，导致 `VLLM_BATCH_INVARIANT=1` 不可达；PR 用两个 capability override 暴露路径，并以 MiniMax-M2 NVFP4 并发复现的相同 sha256 证明 workaround 有效。仍 open，且模型级复现不适合 CI。 |
| [#42007](https://github.com/vllm-project/vllm/issues/42007) / [#42120](https://github.com/vllm-project/vllm/pull/42120) | include + boundary | FP8 MoE LoRA corruption 拆成两个契约：LoRA kernel 需要原始 BF16/FP16 activation，而 base GEMM 需要量化 activation；无 active LoRA 的 base batch 必须按 `no_lora_flag` 早退，避免 stale mapping 写坏输出。PR 有 approval 和 Blackwell 验证，但仍 open，且 wrong input dtype 单测欠缺。 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325) / [#42379](https://github.com/vllm-project/vllm/pull/42379) | include | RMSNorm native-dtype multiply fix 已 merged，并同步 regular/fused quant path；但后续评论对 Python IR 是否是 CUDA spec 有争议，因此结论边界写成“已合并 native-dtype behavior + 现有测试覆盖”，不把某一侧实现扩展成通用规范。 |
| [#39146](https://github.com/vllm-project/vllm/issues/39146) / [#39283](https://github.com/vllm-project/vllm/pull/39283) / [#43741](https://github.com/vllm-project/vllm/pull/43741) | include + boundary | recycled KV block zeroing 需要两个 gate：`needs_kv_cache_zeroing` 覆盖 FullAttentionSpec family，manager 用 `isinstance` 把所有 FullAttentionSpec 子类的新 block id 送进 zeroing pipeline。`#43741` 仍 open，unit tests 强但 patched e2e 还要追踪。 |
| [#25404](https://github.com/vllm-project/vllm/issues/25404) / [#25603](https://github.com/vllm-project/vllm/pull/25603) | include | merged PR 提供 batch-invariant mode 的首批 C++/Python/env hook 和 kernel override plumbing；review 后把命名从 deterministic 收敛为 batch invariant，并补 logprob bit equality。结论边界是“plumbing 已有”，不是“所有 kernel 已覆盖”。 |
| [#34878](https://github.com/vllm-project/vllm/pull/34878) | include | ROCm beam search failure 是 test-harness geometry 问题：batch-size-dependent attention/GEMM reduction 的 `1e-5` 级 logprob 差异能翻转 beam ranking。merged PR 在 ROCm test 中固定 async scheduling、CUDA graph、prefix caching、batch size 和 skinny GEMM，非 ROCm 不变。 |
| [#33537](https://github.com/vllm-project/vllm/pull/33537) | include + boundary | warmup automation 合理覆盖 cold-start serving-state，但本地 evidence 主要证明 TRITON_MLA 首请求 latency 稳定；缺 token/logprob bitwise divergence 的 before/after 复现，且 PR stale，所以只作为 boundary。 |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | exclude | 本轮纠错：PR body 声称 gfx950 应使用 FP8 FNuz，但 maintainer 明确指出 Fnuz 只支持 gfx942，MI355/gfx950 使用 CUDA-like FP8 format；该 PR closed/unmerged，不能再作为 `#33123` 的 dtype/prefix-cache 修复证据。 |
| [#32481](https://github.com/vllm-project/vllm/issues/32481) / [#32561](https://github.com/vllm-project/vllm/pull/32561) | include + boundary | merged PR 在 `VLLM_BATCH_INVARIANT=1` 下禁用 cascade attention，并用 logprob batch-invariance test 从 34/128 prompts fail 到通过验证；边界是 FlashInfer/chunked prefill、MLA、MoE/AWQ 长输出 failure 已在评论中拆成后续问题。 |
| [#35569](https://github.com/vllm-project/vllm/issues/35569) / [#39849](https://github.com/vllm-project/vllm/pull/39849) | include + boundary | ROCM_ATTN 对 Qwen3-VL reranker 的 score drift 可先通过 selector workaround 管控：open PR 把 gfx9 上 gqa_ratio 2/4 的 native `mfma4` path 路由回 Triton；缺 merge 与 patched reranker e2e score regression。 |
| [#42125](https://github.com/vllm-project/vllm/issues/42125) | strong defer | same-name runtime LoRA A->B reload 的复现矩阵强，no-prefix、`cache_salt`、first-block change、cold B、unique-name controls 都指向 adapter-version cache identity；但缺 linked PR、changed files、maintainer resolution 和 regression test。 |
| [#42513](https://github.com/vllm-project/vllm/issues/42513) | defer | MTP eager vs non-MTP 的 batch-size/kernel-selection 链路有 insight，但本地 evidence 只有 issue body；closed state 缺 closure reason、linked fix 和测试，不能 promotion。 |
| [#29581](https://github.com/vllm-project/vllm/issues/29581) / [#38670](https://github.com/vllm-project/vllm/pull/38670) | include | AWQ batch invariance 的关键不是修 sampler，而是在 BI mode 下阻止 AWQ 自动转换到不可控的 AWQ_Marlin fused kernel，回到 dequant + `torch.matmul`，让 BI override 接管；merged PR 有 AWQ before/after、H200 验证和 approval。 |
| [#30018](https://github.com/vllm-project/vllm/pull/30018) | include + boundary | FA2 split 有直接 patch 证据；LoRA 有 PR body、测试矩阵和 review 支持，1000 请求并发测试 distinct outputs 收敛到 1；但 landed-code 子路径仍需复核，且本地评论明确不支持 CUDA graph，测试依赖 `enforce_eager`。 |
| [#33688](https://github.com/vllm-project/vllm/pull/33688) | include | TRITON_ATTN 通过强制 2D Triton unified attention path 成为 decode-invariant backend；B200 和 GPT-OSS/Qwen logprob test 从 128/128 prompts fail 到通过。 |
| [#40408](https://github.com/vllm-project/vllm/pull/40408) | include | Cutlass FP8 direct path 可以进入 BI mode，但前提是 config independent of `M`；merged PR 为 sm89/sm90/sm100/sm120 增加 fixed-config dispatch 和多 batch size/M 维测试。 |
| [#40413](https://github.com/vllm-project/vllm/pull/40413) | include | fused add RMSNorm 已有 batch-invariant 证据，BI mode 下不应无谓改走 Triton RMSNorm；merged PR 保留 fused op，并补 residual path FP16/BF16 测试。 |
| [#27660](https://github.com/vllm-project/vllm/pull/27660) | include + boundary | batch-invariant mode 可以与 `torch.compile` 组合，但前提是显式控制 cuBLAS reduced-precision/split-K/workspace 行为；PR 同时保留 PyTorch 版本差异和 AOT compile 边界，DeepSeek V3.1 logprob BI test 通过。 |
| [#34865](https://github.com/vllm-project/vllm/issues/34865) / [#34874](https://github.com/vllm-project/vllm/pull/34874) | include | Mamba `"all"` mode prefix-cache bug 是 CUDA graph persistent-buffer identity 问题：多个相同 `MambaSpec` cache group 复用 metadata 时，`block_idx_last_*` 必须复制到当前 builder buffer。 |
| [#35219](https://github.com/vllm-project/vllm/pull/35219) | include + boundary | hybrid Mamba/attention 共享 block pool 会把 fp32 SSM state stale bits 复用成 fp8/fp16 attention KV NaN；merged PR 只在 hybrid 模型下清新分配的 `FullAttentionSpec` block，不清 prefix-cache hit 或非 hybrid 部署。 |
| [#41651](https://github.com/vllm-project/vllm/issues/41651) / [#42650](https://github.com/vllm-project/vllm/pull/42650) | include + boundary | 非均匀 per-layer Q-head 模型需要 attention metadata 从实际 served layer 取 `num_heads`；#42650 修 FlashInfer/Triton plan/scratch head-count mismatch，但不覆盖独立的 TRITON_ATTN FP8 scale fix，也暴露 Gemma4 MTP grouping 后续风险。 |
| [#43317](https://github.com/vllm-project/vllm/pull/43317) | defer | decode/prefill consistency test 不能用文本 `decode -> encode` roundtrip 重建 token prefix；open PR 改为 token-id prefix，但未合并，只能作为测试 soundness 风险。 |

## Must Review

| Source | 机制 | 当前状态 | 缺口 | 下一步 |
| --- | --- | --- | --- | --- |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | quant/dtype loading identity | defer | 本地 evidence 只有 open issue body，comments/timeline 均为空；`clone()`、每次或最终 `torch.cuda.synchronize()`、改变 stream file 顺序只是作者定位实验，不能当作 upstream fix。 | 寻找 linked PR/commit/test，重点看 `runai_safetensors_weights_iterator` ownership、`BaseModelLoader.load_model()` copy synchronization、shared buffer lifetime 和 unified-memory 平台回归测试。 |
| [#44250](https://github.com/vllm-project/vllm/issues/44250) | external KV / LoRA identity | defer | 已有端到端 cross-adapter 命中、key schema 代码证据、unpatched/patched connector 对照；但缺 linked fix PR、changed files、maintainer resolution 和 regression test。`lora_name` 对照 patch 只能证明缺 adapter 维度，不能证明最终 external cache key schema。 | 继续抓取或等待 linked fix PR；重点看 MP lookup/store key 是否纳入稳定 LoRA identity/version，并同时覆盖 LMCache MP connector、vLLM vendored connector、同 adapter hit 保留与跨 adapter negative test。 |
| [#42699](https://github.com/vllm-project/vllm/issues/42699), [#40896](https://github.com/vllm-project/vllm/issues/40896) | prefix cache 等价 | defer | 复现和评论证据支持 prefix 路径可翻转 greedy token；但当前只有 mitigation 线索，没有 root-cause patch、maintainer resolution 或 regression test。 | 寻找 linked fix/docs/test PR；补齐 no-prefix、cold prefix、warm prefix、fp32、`VLLM_BATCH_INVARIANT=1` 的验证矩阵。 |
| [#37076](https://github.com/vllm-project/vllm/issues/37076) | prefix cache / KV block identity | defer | issue 与评论给出强 root-cause 假设：同一步 `cache_full_blocks` 在 GPU forward 前把新分配 block 注册到 prefix-cache hash，后续请求可命中并读取未初始化 GPU memory；但本地缺 linked PR `#37152` 的 changed files/test。 | 抓取 `#37152`；确认 `_blocks_registered_this_step`、`get_cached_block` miss gate、`new_step_starts` 清理和 regression test 是否闭环。 |
| [#31210](https://github.com/vllm-project/vllm/issues/31210) | KV offload identity | defer | CPU offload 高并发下同 prompt 输出错误/乱码；maintainer 评论称 `#31341` patch 可复现修复，用户确认生产环境不再发生。但本地缺 `#31341` PR JSON，不能确认 copy/ownership/root cause 与测试。 | 抓取 `#31341`；确认 OffloadingConnector restore/copy length、block ownership、high-concurrency regression 和用户确认对应到最终 patch。 |
| [#42125](https://github.com/vllm-project/vllm/issues/42125) | runtime LoRA / prefix cache identity | defer | 复现矩阵强，但仍只有 issue body 和一条待复现评论；缺 linked fix PR、changed files、maintainer resolution 和 regression test。 | 寻找 runtime load/unload fix；确认同名 adapter reload 是否触发 prefix-cache eviction，或 key 是否纳入 adapter content/version/generation，并覆盖 same-name reload negative test。 |
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
