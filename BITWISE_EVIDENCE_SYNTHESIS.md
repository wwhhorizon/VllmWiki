# Bitwise 证据炼化：第一轮

状态：基于 targeted GitHub evidence 的第一轮 source-backed 综合。  
输入证据：`E:\Vllm-Issue\all\data\targeted\bitwise`。  
机器索引：本地生成文件 `evidence/bitwise_sources.csv`、`evidence/bitwise_sources.md`。这些文件属于可再生证据索引，不提交到 GitHub。

## 本轮补齐了什么

本轮抓取后，bitwise/deterministic 主线不再只依赖本地 issue body：

| 证据层 | 覆盖 |
| --- | ---: |
| Issue evidence JSON | 785 |
| PR evidence JSON | 242 |
| 带已抓评论的 issue | 676 |
| 带 changed files 的 PR | 240 |
| 统一 evidence index 行数 | 1,027 |

每个 issue JSON 包含 issue body、comments 和 timeline。每个 PR JSON 包含 PR body、changed files、review comments、reviews、commits 和 PR discussion comments。后续 curated claim 应优先引用本地 targeted evidence JSON 与 `bitwise_sources.csv`，再回链到 GitHub URL。

## 已经变硬的机制

### 1. Prefix cache hit/miss 必须对齐 prefill 几何

强证据链：

- Issue [#33123](https://github.com/vllm-project/vllm/issues/33123)：ROCm 上首次请求 cache miss 与后续 cache hit 在 greedy/确定性设置下输出不同。
- PR [#40179](https://github.com/vllm-project/vllm/pull/40179)：新增 `--deterministic-prefix-caching`，并在 PR body 与测试中明确 cache-miss full prefill 与 cache-hit suffix prefill 的 GEMM `M` 维度不同会改变 ROCm/Tensile tiling 和 BF16 accumulation order。
- PR [#33179](https://github.com/vllm-project/vllm/pull/33179)：gfx950 FP8 dtype guard 错误会在 cache miss/full prefill 与 cache hit/partial prefill 之间制造数值发散。

炼化结论：prefix caching 不是纯性能开关。只要 cache 状态改变了 prefill 的 kernel shape、dtype dispatch 或 accumulation order，它就进入 correctness contract。deterministic mode 下应让 cache-miss 与 cache-hit 的 suffix 计算几何一致，或在文档和测试中显式声明差异边界。

### 2. KV cache identity 是并发确定性的硬契约

强证据链：

- Issue [#39589](https://github.com/vllm-project/vllm/issues/39589)：不同 prompt length 的并发 prefill 在 `temperature=0` 下产生非确定输出，且 `VLLM_BATCH_INVARIANT=1` 与禁用 prefix cache 不能解释该问题。
- PR [#39591](https://github.com/vllm-project/vllm/pull/39591)：修复 `BlockTable` row tail 未清零导致 stale block id 泄漏；测试直接覆盖 concurrent variable-length prefill determinism。
- Issue [#39146](https://github.com/vllm-project/vllm/issues/39146) 与 PR [#43741](https://github.com/vllm-project/vllm/pull/43741)：recycled KV cache blocks 未清零会让标准 attention 在 `temperature=0` 下出现非确定输出。
- Issue [#30931](https://github.com/vllm-project/vllm/issues/30931)、PR [#31069](https://github.com/vllm-project/vllm/pull/31069)、Issue [#44250](https://github.com/vllm-project/vllm/issues/44250)：LoRA/external KV cache key 必须纳入 adapter identity，否则不同 adapter 可能共享错误 KV。

炼化结论：KV cache 的 identity 维度至少包括 prompt/token range、model、adapter/LoRA identity、dtype/layout、cache group、block ownership 和 backend-specific metadata。只要任一维度被省略或复用时未清理，就不是“数值抖动”，而是读取了错误语义的 KV。

### 3. Deterministic dispatch 要控制 autotune、split-K 和 atomic reduction

强证据链：

- Issue [#25194](https://github.com/vllm-project/vllm/issues/25194)、PR [#25197](https://github.com/vllm-project/vllm/pull/25197)：Triton `_chunk_cumsum_fwd_kernel` 的 `BLOCK_H=1` candidate 会产生不同数值输出；修复方式是移除该 autotune candidate。
- PR [#35183](https://github.com/vllm-project/vllm/pull/35183)：ROCm skinny GEMM 拆分 deterministic store-then-reduce 与 fast `atomicAdd` path，默认走 deterministic path，fast path 需要显式 opt-in。
- Issue [#25404](https://github.com/vllm-project/vllm/issues/25404)、PR [#25603](https://github.com/vllm-project/vllm/pull/25603)：提供 kernel-level deterministic override plumbing，让后续 kernel 可以按需接入 deterministic launch。
- PR [#42240](https://github.com/vllm-project/vllm/pull/42240)：AITER FP8 block-scaled GEMM 强制 `splitK=0`，绕开 split-K atomic reduction 带来的非确定累加。

炼化结论：设置 seed 不足以定义 deterministic execution。必须枚举并约束 dispatcher 仍能改变的路径：autotune candidate、backend fallback、split-K、atomic reduction、JIT/graph warmup 和 hardware-specific CSV dispatcher。

### 4. Batch invariance 要锁定 kernel config，而不只是锁定请求语义

强证据链：

- Issue [#27433](https://github.com/vllm-project/vllm/issues/27433)：batch invariant 是 umbrella issue，包含多个实际机制，不能单独作为 curated measure。
- PR [#36488](https://github.com/vllm-project/vllm/pull/36488)：MXFP4 MoE `matmul_ogs` 会根据 tokens-per-expert 和 SM count 动态选择 `block_m`/`split_k`；传入 `enforce_bitwise_invariance` 后固定 config。
- PR [#42670](https://github.com/vllm-project/vllm/pull/42670)：FlashInfer + CUTLASS FP4 MoE 已有 batch-invariant path，但 support gate 未暴露，导致 `VLLM_BATCH_INVARIANT=1` 不可达。
- Issue [#39096](https://github.com/vllm-project/vllm/issues/39096)：torch.compile/CUDA graphs 与 SM<90 组合会打破 batch invariance，仍需继续审计 linked PR 和 exact config。
- PR [#33537](https://github.com/vllm-project/vllm/pull/33537)：batch invariant mode 下真实请求前需要 warmup，以稳定 CUDA graph、Triton JIT 和 allocator/cache 状态。

炼化结论：batch invariance 的实质不是“同一个请求在不同 batch 中看起来一样”，而是同一请求的 kernel config、graph/capture 状态、reduction geometry 和 cache warmup 状态都要被稳定下来。

### 5. Quant/dtype 语义会放大 bitwise 问题

强证据链：

- PR [#33179](https://github.com/vllm-project/vllm/pull/33179)：gfx950 dtype guard 错误让 MI325X/MI355X 使用错误 FP8 dtype，导致 cache miss/hit 之间数值发散。
- PR [#36488](https://github.com/vllm-project/vllm/pull/36488)：MXFP4 MoE 的 batch-invariant flag 没有传入 integration layer，导致低精度 MoE 在不同 batch composition 下改变 `block_m`/`split_k`。
- Issue [#42007](https://github.com/vllm-project/vllm/issues/42007)、PR [#42120](https://github.com/vllm-project/vllm/pull/42120)：MoE FP8 LoRA/base model response corruption 与 LoRA path、precision hidden state 保存有关。
- Issue [#38991](https://github.com/vllm-project/vllm/issues/38991)：FP8 inference 中权重迭代顺序非确定，仍需要 linked fix 或 file evidence 才能 promotion。

炼化结论：低精度路径的 bitwise 复核必须记录 weight dtype、activation dtype、KV dtype、scale layout、swizzle/padding、expert routing、MoE tile config 和 loading buffer lifetime。

### 6. Verification contract 必须区分 exact equality、strict tolerance 和 token equality

强证据链：

- PR [#29086](https://github.com/vllm-project/vllm/pull/29086)：将 `torch.allclose` revert 回 `torch.equal`，因为 draft/target model layer identity 不能用近似相等替代。
- PR [#43355](https://github.com/vllm-project/vllm/pull/43355)：fused RoPE + KV cache write 增加 bit-identical 测试，使用 `rtol=0, atol=0` 并约束 slot mapping。
- PR [#40179](https://github.com/vllm-project/vllm/pull/40179)、PR [#39591](https://github.com/vllm-project/vllm/pull/39591)：分别把 cache miss/hit equality 和 concurrent prefill determinism 写成回归测试。

炼化结论：bitwise 主线不能只说“输出接近”。每条机制都要声明验证对象：tensor bit equality、KV identity、logits/token equality、strict numeric tolerance，还是 semantic answer equivalence。只有前几类能支持 deterministic/bitwise claim。

## 仍然不能直接 curated 的内容

- `patterns/bitwise_determinism_equivalence.md` 和 `curated/bitwise_review_queue.csv` 中很多命中只是关键词候选，不能直接当作机制结论。
- `evidence/bitwise_sources.csv` 的 `mechanism_guess` 是自动分类，只能做导航；promotion 必须阅读对应 JSON 的 issue body、comments、PR body 和 patch。
- `#27433` 是 umbrella issue，适合做索引，不适合单独 promotion。
- `#38991` 有强问题描述，但当前仍缺 linked fix/file evidence，应该保持 `defer`。
- `#39096` 已有评论和 timeline，但 linked PR 与 exact failing config 仍需要人工复核。

## 下一轮优先队列

1. 把 `#33123/#40179/#33179` 写成 prefix-cache 等价的完整 curated case。
2. 把 `#39589/#39591/#39146/#43741/#30931/#31069/#44250` 合并为 KV identity 机制页的强证据链。
3. 把 `#25194/#25197/#35183/#42240/#25404/#25603` 合并为 deterministic dispatch/reduction 的强证据链。
4. 把 `#36488/#42670/#33537/#39096` 拆成 batch invariance 的 kernel config、support gate、warmup 三类子机制。
5. 把 `#29086/#43355/#40179/#39591` 抽成 verification contract matrix。
