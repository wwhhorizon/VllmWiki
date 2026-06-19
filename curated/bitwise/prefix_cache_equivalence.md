# Prefix Cache 等价

状态：curated。  
父页：[Bitwise 确定性与数值等价](README.md)。
范围：full prefill、prefix-cache miss、prefix-cache hit、prefix-cache bypass 之间的 deterministic 输出等价。

## 问题定义

同一个 prompt、同一个模型、同样 deterministic sampling 设置下，cache 状态不应该改变用户可见 token。若 backend 只能保证近似数值一致，必须明确 tolerance 与适用边界；不能把 `temperature=0` 下的 greedy token 翻转当作普通性能差异。

## 典型触发条件

- prefix cache 首次请求 miss，后续相同请求 hit。
- prompt 长度不是 block size 的整数倍，cache-hit 只计算 suffix。
- ROCm/Tensile、CUDA/cuBLAS、FlashInfer 等 backend 因 GEMM shape 改变 tiling 或 accumulation order。
- FP8/BF16 等低精度路径中，dtype guard 或 backend dispatch 与 cache 状态一起变化。
- Mamba `"all"` mode 在多 KV cache group + CUDA graph 下复用 metadata，但没有把 block index 写入当前 builder 的 persistent buffer。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#33123](https://github.com/vllm-project/vllm/issues/33123) | ROCm 上首次请求 cache miss 与后续 cache hit 输出不同；本地已抓取评论和 timeline。 | 这是 prefix-cache 语义问题，不只是 cache 性能问题。 |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | PR body 试图把 `#33123` 归因到 gfx950 FP8 dtype guard，并把 gfx950 加入 `is_fp8_fnuz()`；但 maintainer 评论明确指出该前提错误：Fnuz 只支持 gfx942，MI355/gfx950 使用 CUDA-like FP8 format。PR closed/unmerged。 | 这是一条反例：prefix-cache divergence 不能只凭 PR body 归因到 dtype guard；硬件 dtype 结论必须有 maintainer resolution 和 merged patch。 |
| [#34865](https://github.com/vllm-project/vllm/issues/34865), [#34874](https://github.com/vllm-project/vllm/pull/34874) | Nemotron hybrid 模型的 `mamba_cache_mode="all"` 启用 prefix caching 后出现 NaN logprobs 和垃圾 token；merged PR 定位到多个 KV cache group 共享相同 `MambaSpec` 时，metadata caching 用 `(kv_cache_spec, type(builder))` 复用 shallow copy。`update_block_table()` 只把 `state_indices_tensor` 复制到当前 builder 的 CUDA graph persistent buffer，却让 `block_idx_last_scheduled_token` / `block_idx_last_computed_token` 继续指向第一个 builder 的 buffer。 | prefix cache metadata 的 identity 不只是 block table 值，还包括 CUDA graph 捕获的 persistent buffer 地址；多 cache group 复用 metadata 时，所有 graph replay 会读取的指针都必须切到当前 builder。 |

## 根因机制

Prefix caching 会改变实际计算几何。cache miss 往往对完整 prompt 做 prefill；cache hit 只计算未命中的 suffix。不同 `M` 可能触发不同 backend kernel、tiling 或 accumulation order。低精度路径中，早期层 1 ULP 级差异可能在多层 transformer 中放大，最终翻转 logits argmax。

`#34865/#34874` 展示的是另一类 prefix-cache 等价：不是计算几何变了，而是 metadata 缓存把“值”和“存放值的 persistent buffer 地址”混淆了。CUDA graph capture 后 kernel 读的是当前 builder 的地址；如果 `update_block_table()` 只返回指向旧 builder buffer 的 shallow metadata，graph replay 看到的就是未更新的 block index，进而读错 Mamba state。

## 修复方式

1. 在 deterministic mode 下固定或对齐 cache-hit 与 cache-miss 的 prefill kernel geometry。
2. 像 [#40179](https://github.com/vllm-project/vllm/pull/40179) 一样在 scheduler 层把 cache-miss prefill 拆到最后一个 cached block boundary，使 suffix GEMM 的 `M` 与 cache-hit path 对齐。
3. 对 cache miss、cache hit、cache bypass 三种路径都做同 prompt 回归测试。
4. 同时记录 dtype、backend、block size、suffix length、GEMM shape 和硬件架构。
5. 对被 preempt 后 resume 的请求、prompt 长度刚好 block-aligned 的请求，也要走同一 split 判定，不能只处理普通首次 prefill。
6. split boundary 应基于 `num_computed_tokens` 与 `(num_prompt_tokens - 1)` 的最后一个 block boundary，而不是只看 `request.num_output_tokens` 或 `num_prompt_tokens % block_size`；否则 final-token logits 约束会让 block-aligned prompt 仍出现 cache-state-dependent GEMM shape。
7. 对 prefix-read/no-prefix-read 或 cold/warm cache 差异，先用 `fp32` 与 `VLLM_BATCH_INVARIANT=1` 做归因分流：若二者能收敛输出，优先归为 batch/kernel geometry 的数值稳定性边界，而不是直接归为 KV cache state corruption。
8. 对 Mamba `"all"` mode，`update_block_table()` 必须把 `block_idx_last_scheduled_token` 与 `block_idx_last_computed_token` 复制进当前 builder 的 persistent buffer，并让新 metadata 指向当前 builder 的 slice；不能只更新 `state_indices_tensor`。

## 验证契约

- 用户可见层：同 prompt 多次请求的 generated token 必须一致。
- kernel 几何层：cache-miss 与 cache-hit 的 suffix GEMM shape 必须一致或被显式解释。
- 回归测试层：覆盖首次请求、后续 cache hit、禁用 prefix cache、非 block-aligned prompt。
- 调度边界层：覆盖 resumed request、block-aligned prompt、至少计算 final token 的 vLLM scheduler 约束；只测重复同 prompt 的 happy path 不足以证明 scheduler split 完整。
- 数值边界层：对 BF16 prefix 路径差异同时跑 fp32、batch-invariant mode、禁用 prefix cache、cold/warm prefix cache 四组对照。
- Mamba metadata 层：构造至少两个共享同一 `MambaSpec` 的 builder，断言 `update_block_table()` 返回的 block index tensor 与当前 builder 的 persistent buffer 共享 storage，且不再指向旧 builder；测试模型必须有至少两个相关 cache group，单 Mamba 层 tiny model 不会触发该路径。
- 如果只能证明 strict tolerance，必须继续证明差异不会翻转 token/logprob ranking。

## 适用边界

- [#40179](https://github.com/vllm-project/vllm/pull/40179) 的直接证据集中在 ROCm/BF16/Tensile 受 GEMM `M` 维度影响的场景；其他 backend 需要单独验证。
- deterministic prefix caching 可能增加一次 prefill step，属于可接受的 reproducibility/latency trade-off。
- review comment 暴露的 resumed/block-aligned 风险是实现边界，不等价于 PR 已完全失效；但在当前 patch 中这两个早退条件仍存在，且 PR 仍 open/dirty、有 merge conflict 提醒，因此只能写成 include-with-boundary。
- [#42699](https://github.com/vllm-project/vllm/issues/42699) 与 [#40896](https://github.com/vllm-project/vllm/issues/40896) 是 open issue：评论提供复现和 mitigation 线索，但没有 prefix-cache 专属 linked fix、changed files 或 merged regression test。当前最佳证据更支持把它们视为“默认 prefix-cache 路径下的 exact reproducibility 契约边界”: `#42699` 评论显示 `fp32` 与 `VLLM_BATCH_INVARIANT=1` 都可让 prefix-read/no-prefix-read 收敛，并把该缓解指向已合并的 [#40193](https://github.com/vllm-project/vllm/pull/40193)；`#40896` maintainer 则明确说 prefix caching determinism 目前还未完全支持。因此它们暂不进入代表证据，也不再作为独立 direct-closure 主线维护。
- dtype guard 问题应进入 quant/dtype 机制页交叉复核，不能只归因于 prefix cache。`#33179` 已被 maintainer 评论排除，不能继续作为 `#33123` 的正向修复证据。
- [#34874](https://github.com/vllm-project/vllm/pull/34874) 已 merged，结论覆盖 `mamba_cache_mode="all"`、CUDA graph、多个相同 `MambaSpec` cache group 的 metadata buffer 问题；不代表所有 Mamba prefix-cache 模式、所有 hybrid speculative/MTP 场景都已稳定。

## 仍需补证

- `#42699`、`#40896` 当前更适合作为 batch-invariant / kernel geometry 的分流证据维护：继续确认 batch-invariant mode 是否被文档化为 prefix-cache reproducibility 的推荐设置，以及后续是否出现 prefix-cache 专属 regression test 或 docs patch。
- `#37076/#37152` 需要继续确认 same-step prefix block 注册可见性是否有 merged regression test；当前 open PR 只证明 miss gate 方向和最小 patch，不足以 promotion 为 landed fix。
- 下一轮应从本地 review queue 中筛选 `prefix_cache_equivalence`，但 promotion 前必须阅读 targeted evidence JSON 或上游 issue/PR。
- 继续追踪 `#40179` 是否出现 follow-up patch：用 `num_computed_tokens` 判断 prefill、用 `(num_prompt_tokens - 1)` 计算 final-token-aware block boundary，并补 resumed/block-aligned 回归测试。
- 复核后续 Mamba + prefix caching + MTP/spec decode 问题时，不要把 `#34874` 外推；它只修复 metadata persistent-buffer 指针，不覆盖请求重分配、cache eviction 或 speculative verification 的 kernel geometry。
