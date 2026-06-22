# Prefix Cache 等价

状态：curated。
父页：[Bitwise 确定性与数值等价](README.md)。
范围：full prefill、prefix-cache miss、prefix-cache hit、prefix-cache bypass 之间的 deterministic 输出等价。

## TL;DR

同一个 prompt、同一个模型、同样 deterministic sampling 设置下，cache 状态不应该改变用户可见 token。prefix cache 会改变 prefill 计算几何，也会引入 metadata identity 风险。修复通常不是简单禁用 cache，而是让 cache-miss/cache-hit 的 suffix geometry 或 metadata pointer 保持等价。默认 exact reproducibility 仍有 open 边界，相关队列见 [next.md](next.md)。

## 机制解释

Prefix caching 会让 cache miss 走 full prefill，而 cache hit 只计算未命中的 suffix。不同 `M` 可能触发不同 backend kernel、tiling 或 accumulation order，低精度路径中很小的差异也可能翻转 logits argmax。

另一类问题不是计算几何，而是 metadata 缓存把“值”和“存放值的 persistent buffer 地址”混淆。CUDA graph replay 读取 capture 时的地址；如果 metadata 指向旧 builder，graph 会稳定地读错状态。

<!-- 稳定证据区禁止出现 open/defer/include_with_boundary；此类对象仅可进入"边界与反例"段或 next.md -->

## 稳定证据

- upstream id: [#33123](https://github.com/vllm-project/vllm/issues/33123)
  - upstream status: issue evidence
  - claim level: stable symptom anchor
  - direct evidence: ROCm 上首次 cache miss 与后续 cache hit 输出不同。
  - mechanism: prefix-cache 等价保护的是 token/logprob 语义，不只是 cache 性能。
  - boundary: 具体修复需要结合后续 PR；不能只凭症状归因到 dtype guard。

- upstream id: [#34865](https://github.com/vllm-project/vllm/issues/34865), [#34874](https://github.com/vllm-project/vllm/pull/34874)
  - upstream status: merged PR
  - claim level: stable
  - direct evidence: `update_block_table()` 修正 Mamba metadata，让 block index tensor 指向当前 builder 的 persistent buffer。
  - mechanism: prefix-cache metadata identity 包括 CUDA graph 会读取的 buffer 地址。
  - boundary: 覆盖 Mamba `"all"` mode、多 cache group、CUDA graph；不覆盖所有 hybrid prefix-cache 场景。

- upstream id: [#42699](https://github.com/vllm-project/vllm/issues/42699), [#40896](https://github.com/vllm-project/vllm/issues/40896)
  - upstream status: open issues
  - claim level: boundary
  - direct evidence: 评论显示 `fp32` 或 `VLLM_BATCH_INVARIANT=1` 可让部分 prefix-read/no-prefix-read 差异收敛。
  - mechanism: 默认 prefix-cache exact reproducibility 可能先落在 batch/kernel geometry 契约边界。
  - boundary: 缺 prefix-cache 专属 linked fix、changed files 或 merged regression test。

## 边界与反例

- [#33179](https://github.com/vllm-project/vllm/pull/33179) 是反例：PR body 的 gfx950 FP8 Fnuz 归因被 maintainer 直接反驳，不能作为 `#33123` 的正向修复证据。
- `#40179` 的证据集中在 ROCm/BF16/Tensile 受 GEMM `M` 影响的场景；其他 backend 需要单独验证。
- deterministic prefix caching 可能增加一次 prefill step，这是 reproducibility/latency trade-off。
- upstream id: [#40179](https://github.com/vllm-project/vllm/pull/40179)
  - upstream status: open PR
  - claim level: include with boundary
  - direct evidence: patch 方向是在 scheduler 层把 cache-miss prefill 拆到 cached block boundary，使 suffix GEMM `M` 尽量与 cache-hit path 对齐。
  - mechanism: deterministic prefix caching 需要固定或对齐 cache-hit/cache-miss 的计算几何。
  - boundary: review 暴露 resumed request、block-aligned prompt 和 final-token-aware boundary 风险；未合并前不能写成 landed fix。

- Mamba metadata pointer fix 不能外推到请求重分配、cache eviction、MTP/spec decode 或 kernel-selection 问题。

## Evidence appendix

长证据表、prefix-cache verification matrix 和补证记录见 [evidence_appendix/prefix_cache_equivalence.md](evidence_appendix/prefix_cache_equivalence.md)。
