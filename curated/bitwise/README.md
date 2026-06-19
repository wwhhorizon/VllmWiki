# Bitwise 确定性与数值等价

状态：curated seed page，基于代表性 raw issue/PR body 生成并持续复核。  
范围：bitwise invariance、deterministic output、batch-size invariance、prefix-cache equivalence，以及可能翻转 greedy decoding 的 numerical drift。

## 核心 Lesson

在 vLLM 中，bitwise issue 很少只是“浮点噪声”。它们通常暴露的是 request state、KV cache identity、backend routing、GEMM tiling、quantization scale/layout 或 kernel launch geometry 之间的契约不一致。单个 kernel test 里 1 ULP 的差异可能看似无害，但一旦写入 KV cache 或 logits，就可能在后续层中放大，并在 `temperature=0` 时翻转 `argmax`。

## 机制页

- [Prefix Cache 等价](prefix_cache_equivalence.md)
- [Batch Invariance 与 Kernel Geometry](batch_invariance_kernel_geometry.md)
- [并发下的 KV Cache Identity](kv_cache_identity_concurrency.md)
- [量化与 Dtype 数值语义](quant_dtype_numerical_semantics.md)
- [Bitwise 工作的验证契约](verification_contracts.md)
- [Deterministic Dispatch 与 Reduction Control](deterministic_dispatch_reduction.md)

本地复核队列 `curated/bitwise_review_queue.*` 属于可再生候选材料，不提交到 GitHub。稳定结论进入本页和六个机制页；待复核 claim 进入 [candidates/bitwise_ledger.csv](../../candidates/bitwise_ledger.csv)。

## 稳定主机制

| 机制 | 修复对象 | 源证据 | Wiki pattern |
| --- | --- | --- | --- |
| 移除不稳定 Triton autotune candidate | `_chunk_cumsum_fwd_kernel` 的 `BLOCK_H=1` 候选会改变数值输出 | [#25194](https://github.com/vllm-project/vllm/issues/25194), [#25197](https://github.com/vllm-project/vllm/pull/25197) | deterministic dispatch |
| 拆分 deterministic 与 fast ROCm skinny GEMM | `atomicAdd` reduction 不是 bitwise stable；store-then-reduce 才能固定累加顺序 | [#35183](https://github.com/vllm-project/vllm/pull/35183) | deterministic reduction |
| 将 `VLLM_BATCH_INVARIANT` 传入 MXFP4 MoE kernel config | tokens-per-expert 与 SM count 改变 `block_m` / `split_k` | [#36488](https://github.com/vllm-project/vllm/pull/36488) | batch invariance; MoE |
| 在 batch-invariant mode 下禁用 cascade attention | 条件性 attention 优化会随同 batch 的其他请求改变 logprob | [#32481](https://github.com/vllm-project/vllm/issues/32481), [#32561](https://github.com/vllm-project/vllm/pull/32561) | batch invariance; attention geometry |
| AWQ 在 BI mode 下绕开 Marlin 自动转换 | 自动路由到 AWQ_Marlin 会绕开 deterministic matmul override | [#29581](https://github.com/vllm-project/vllm/issues/29581), [#38670](https://github.com/vllm-project/vllm/pull/38670) | batch invariance; quantization |
| `TRITON_ATTN` 在 BI mode 下固定 2D kernel | decode path 不能再随 batch shape 在 2D/3D unified attention 间切换 | [#33688](https://github.com/vllm-project/vllm/pull/33688) | batch invariance; backend coverage |
| Cutlass FP8 direct path 使用 fixed-config dispatch | direct FP8 fast path 只有在 config independent of `M` 时才能进入 BI mode | [#40408](https://github.com/vllm-project/vllm/pull/40408) | quantization; batch invariance |
| FP8 MoE LoRA 分离 base activation 与 adapter activation 语义 | 无 active LoRA 的 base batch 不能继承 stale mapping；LoRA kernel 不能直接消费量化后的 base activation | [#42007](https://github.com/vllm-project/vllm/issues/42007), [#42120](https://github.com/vllm-project/vllm/pull/42120) | quantization; LoRA; MoE |
| `torch.compile` 路径显式控制 cuBLAS 行为 | BI mode 需要关闭 reduced-precision / split-K / workspace 相关不稳定选择 | [#27660](https://github.com/vllm-project/vllm/pull/27660) | compile; deterministic dispatch |
| 用 per-layer Q-head 数构建 attention metadata | 非均匀 head 模型不能再用 model-wide head count 做 plan/scratch allocation | [#41651](https://github.com/vllm-project/vllm/issues/41651), [#42650](https://github.com/vllm-project/vllm/pull/42650) | attention metadata; low precision |
| 本地 LoRA cache key 使用稳定 adapter identity | prefix cache hash 不能只看 `lora_name`，要看全局唯一 identity | [#30931](https://github.com/vllm-project/vllm/issues/30931), [#31069](https://github.com/vllm-project/vllm/pull/31069) | KV identity; adapter identity |
| 修复 Mamba prefix-cache metadata persistent buffer | 多个相同 `MambaSpec` cache group 不能复用旧 builder 的 block-index buffer | [#34865](https://github.com/vllm-project/vllm/issues/34865), [#34874](https://github.com/vllm-project/vllm/pull/34874) | prefix cache; metadata identity |
| 清零 hybrid Mamba/attention 共享 block pool 的新 attention KV block | fp32 SSM state stale bits 不能被当成 fp8/fp16 KV 读取 | [#35219](https://github.com/vllm-project/vllm/pull/35219) | KV identity; block zeroing |
| CPU KV offload 先等 compute，再延后提交 store | 高并发 offload 不能在 GPU 计算或 sample-token copy 未完成时搬走 KV | [#31210](https://github.com/vllm-project/vllm/issues/31210), [#31341](https://github.com/vllm-project/vllm/pull/31341) | KV identity; offload ordering |

## 主线核心缺口

- prefix-cache 等价主线仍缺 direct closure：[#42699](https://github.com/vllm-project/vllm/issues/42699)、[#40896](https://github.com/vllm-project/vllm/issues/40896)。
- same-step prefix block 注册与 cache hit 可见性仍在补证：[#37076](https://github.com/vllm-project/vllm/issues/37076)、[#37152](https://github.com/vllm-project/vllm/pull/37152)。
- external KV connector 仍缺稳定的 adapter identity/version schema：[#44250](https://github.com/vllm-project/vllm/issues/44250)。
- runtime same-name LoRA reload 仍缺内容派生的本地 prefix-cache version identity 闭环：[#42125](https://github.com/vllm-project/vllm/issues/42125)。
- loading-lifetime 主线仍缺 direct closure：[#38991](https://github.com/vllm-project/vllm/issues/38991)。

## 辅助边界

- scheduler follow-up、open workaround、support-gate、review-risk 和 test-soundness 项统一维护在 [next.md](next.md)。
- 当前仍在辅助边界队列中的代表项包括：[#42513](https://github.com/vllm-project/vllm/issues/42513) / [#42518](https://github.com/vllm-project/vllm/issues/42518)、[#40179](https://github.com/vllm-project/vllm/pull/40179)、[#42670](https://github.com/vllm-project/vllm/pull/42670)、[#42240](https://github.com/vllm-project/vllm/pull/42240)、[#39849](https://github.com/vllm-project/vllm/pull/39849)、[#43355](https://github.com/vllm-project/vllm/pull/43355)、[#33537](https://github.com/vllm-project/vllm/pull/33537)、[#43317](https://github.com/vllm-project/vllm/pull/43317)。

## 反例 / 排除项

- [#33179](https://github.com/vllm-project/vllm/pull/33179)：closed/unmerged 且被 maintainer 直接反驳的 gfx950 FP8 FNuz 归因，不得继续当作 `#33123` 的 dtype 修复证据。

## 抽取规则

- 始终记录比较契约：bit-identical、`torch.equal`、`assert_close`、logprob tolerance 或 semantic answer equivalence。
- 区分 deterministic numerical drift 与 random nondeterminism；两者都是 correctness bug，但指向不同根因。
- 对 cache 相关 case，比较 full-prefill、prefix-hit、prefix-miss、offload-restore 和 concurrent request path。
- 对 quantized kernel，记录 dtype、scale layout、tile shape、`split_k`、`block_m`、TP/EP shape 和 backend。
- 不要只凭 closed state 把 bitwise issue 判定为 solved；必须有 linked PR、maintainer comment 或 reproduced verification。
