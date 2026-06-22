# Deterministic Dispatch 与 Reduction Control

状态：curated。
父页：[Bitwise 确定性与数值等价](README.md)。
范围：autotune candidate、backend dispatch、split-K、atomic reduction、fast/deterministic path、compile/cuBLAS 和 metadata launch contract。

## TL;DR

deterministic mode 必须控制 kernel/backend dispatch 和 reduction geometry。只设置随机种子不够；autotune candidate、split-K、atomic reduction、backend fallback、cuBLAS workspace、warmup 状态和 attention metadata 都可能改变 bitwise 输出。fast path 可以存在，但不能借用 deterministic path 的 correctness claim。open workaround 保留在 [next.md](next.md)。

## 机制解释

这类问题来自“可变但未被 deterministic contract 管住”的执行路径。dispatcher、autotuner、CSV heuristic、graph warmup 或 metadata builder 为了性能选择不同 kernel；这些 kernel 在数学上近似等价，但在浮点累加顺序、atomic interleaving、低精度 rounding 或 launch geometry 上不 bitwise 等价。

compile path 也不是简单的 compile/eager 二选一。需要显式控制 cuBLAS reduced-precision、split-K、workspace/algorithm，并避免 Dynamo trace 进入 runtime capability query。

## 稳定证据

- upstream id: [#25194](https://github.com/vllm-project/vllm/issues/25194), [#25197](https://github.com/vllm-project/vllm/pull/25197)
- upstream status: merged PR
- claim level: stable
- direct evidence: `_chunk_cumsum_fwd_kernel` 的 `BLOCK_H=1` 与 `BLOCK_H>1` 输出不同；PR 移除不稳定 autotune config。
- mechanism: autotune candidate 必须先证明数值等价。
- boundary: 只覆盖该 kernel candidate，不代表全部 autotune 空间已验证。

- upstream id: [#35183](https://github.com/vllm-project/vllm/pull/35183)
- upstream status: merged PR
- claim level: stable
- direct evidence: ROCm skinny GEMM 拆成 deterministic store-then-reduce 与 fast `atomicAdd` path。
- mechanism: deterministic 与 fast path 应显式拆开。
- boundary: fast path 是性能 opt-in，不承诺 bitwise。

- upstream id: [#34878](https://github.com/vllm-project/vllm/pull/34878)
- upstream status: merged PR
- claim level: stable boundary
- direct evidence: ROCm beam search test 固定 async scheduling、eager、prefix cache、batch size 和 skinny GEMM path。
- mechanism: verification harness 自身也要固定 batch/reduction geometry。
- boundary: 这是 test placement，不代表生产 ROCm path 默认全 bitwise。

- upstream id: [#27660](https://github.com/vllm-project/vllm/pull/27660)
- upstream status: merged PR
- claim level: stable
- direct evidence: BI mode 为 `torch.compile` 路径补 cuBLAS reduced-precision/workspace 控制，并关闭未验证的 AOT compile 组合。
- mechanism: compile path determinism 需要控制 cuBLAS 和 Dynamo trace side effect。
- boundary: 不覆盖所有 AOT compile 或未来 PyTorch flag 行为。

- upstream id: [#41651](https://github.com/vllm-project/vllm/issues/41651), [#42650](https://github.com/vllm-project/vllm/pull/42650)
- upstream status: merged PR
- claim level: stable
- direct evidence: FlashInfer/Triton metadata builder 从 model-wide head count 改为 served layer 的 `impl.num_heads`。
- mechanism: plan-time allocation、scratch shape 和 runtime tensor shape 必须来自同一 source of truth。
- boundary: 不等于所有 TRITON_ATTN FP8 KV 问题都由该 PR 修复。

## 边界与反例

- `#42240` 是 open scoped workaround：强制 `splitK=0` 绕过 AITER split-K reduction，直到上游修复；不能外推到所有 shape。
- `#39849` 是 open selector fallback：证明 known-bad shape 可改道，但还缺 patched e2e numeric regression。
- `#25603` 是第一批 BI plumbing，不代表全 serving path 已 batch invariant。
- `#40408` 证明当前 Cutlass FP8 fixed-config path 可进入 BI；后续 tuning 若重新依赖 `M`，需要重跑验证。
- `#44115` 是 open dispatch fallback 边界：FlashInfer MoE internal router 与 CUDA graph capture 仍需 upstream closure。

## Evidence appendix

长证据表、dispatch/reduction matrix 和补证记录见 [evidence_appendix/deterministic_dispatch_reduction.md](evidence_appendix/deterministic_dispatch_reduction.md)。
