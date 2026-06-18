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

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#33123](https://github.com/vllm-project/vllm/issues/33123) | ROCm 上首次请求 cache miss 与后续 cache hit 输出不同；本地已抓取评论和 timeline。 | 这是 prefix-cache 语义问题，不只是 cache 性能问题。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | PR body 明确说明 cache-miss full prefill 的 GEMM `M=N`，cache-hit suffix prefill 的 `M=N % block_size`；不同 `M` 会改变 ROCm/Tensile tiling 和 BF16 accumulation order。changed files 包含 cache config、scheduler split 和 e2e test。深读 patch 后，review comment 直接命中当前实现：`request.num_output_tokens > 0` 会让 resumed request 早退，`remainder == 0` 会让 block-aligned prompt 早退，而 vLLM 至少要计算 final token，cache-hit path 不会真正命中完整 prompt。 | deterministic mode 下要让 cache miss 与 cache hit 的 suffix GEMM geometry 对齐；但当前 PR 只能作为机制方向和测试样例，不能作为完整 scheduler fix，promotion 需要覆盖 preemption/resume、block-aligned prompt 和 final-token 约束。 |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | gfx950 FP8 dtype guard 漏掉 MI325X/MI355X，错误使用 `float8_e4m3fn` 而非 `float8_e4m3fnuz`。 | cache 等价还依赖 dtype/backend dispatch 一致。 |
| [#42699](https://github.com/vllm-project/vllm/issues/42699) | prefix-read 与 no-prefix-read 在 greedy decoding 下翻转词边界；复现评论显示同一现象可在 v0.20.0、RTX 3090、Qwen2-0.5B、BF16 上复现，`fp32` 或 `VLLM_BATCH_INVARIANT=1` 后 hit/control 收敛。 | 这更像 batch/kernel geometry 导致的 BF16 reduction order 差异，而不是已定位的 prefix-cache 状态机 bug；缺 linked fix PR，保持 defer。 |
| [#40896](https://github.com/vllm-project/vllm/issues/40896) | V1 首次请求和后续相同请求不同，禁用 prefix caching 后稳定；H100 + Qwen3-0.6B 的 reduced repro 显示 warmed prefix cache 输出从 `7577` 变为 `5777`。评论指出 prefix caching determinism 尚未完全支持，并建议尝试 `VLLM_BATCH_INVARIANT=1`。 | 作为 prefix-cache 默认语义风险和 batch-invariant mitigation 证据；缺 root-cause patch/test 闭环，保持 defer。 |

## 根因机制

Prefix caching 会改变实际计算几何。cache miss 往往对完整 prompt 做 prefill；cache hit 只计算未命中的 suffix。不同 `M` 可能触发不同 backend kernel、tiling 或 accumulation order。低精度路径中，早期层 1 ULP 级差异可能在多层 transformer 中放大，最终翻转 logits argmax。

## 修复方式

1. 在 deterministic mode 下固定或对齐 cache-hit 与 cache-miss 的 prefill kernel geometry。
2. 像 [#40179](https://github.com/vllm-project/vllm/pull/40179) 一样在 scheduler 层把 cache-miss prefill 拆到最后一个 cached block boundary，使 suffix GEMM 的 `M` 与 cache-hit path 对齐。
3. 对 cache miss、cache hit、cache bypass 三种路径都做同 prompt 回归测试。
4. 同时记录 dtype、backend、block size、suffix length、GEMM shape 和硬件架构。
5. 对被 preempt 后 resume 的请求、prompt 长度刚好 block-aligned 的请求，也要走同一 split 判定，不能只处理普通首次 prefill。
6. split boundary 应基于 `num_computed_tokens` 与 `(num_prompt_tokens - 1)` 的最后一个 block boundary，而不是只看 `request.num_output_tokens` 或 `num_prompt_tokens % block_size`；否则 final-token logits 约束会让 block-aligned prompt 仍出现 cache-state-dependent GEMM shape。
7. 对 prefix-read/no-prefix-read 或 cold/warm cache 差异，先用 `fp32` 与 `VLLM_BATCH_INVARIANT=1` 做归因分流：若二者能收敛输出，优先归为 batch/kernel geometry 的数值稳定性边界，而不是直接归为 KV cache state corruption。

## 验证契约

- 用户可见层：同 prompt 多次请求的 generated token 必须一致。
- kernel 几何层：cache-miss 与 cache-hit 的 suffix GEMM shape 必须一致或被显式解释。
- 回归测试层：覆盖首次请求、后续 cache hit、禁用 prefix cache、非 block-aligned prompt。
- 调度边界层：覆盖 resumed request、block-aligned prompt、至少计算 final token 的 vLLM scheduler 约束；只测重复同 prompt 的 happy path 不足以证明 scheduler split 完整。
- 数值边界层：对 BF16 prefix 路径差异同时跑 fp32、batch-invariant mode、禁用 prefix cache、cold/warm prefix cache 四组对照。
- 如果只能证明 strict tolerance，必须继续证明差异不会翻转 token/logprob ranking。

## 适用边界

- [#40179](https://github.com/vllm-project/vllm/pull/40179) 的直接证据集中在 ROCm/BF16/Tensile 受 GEMM `M` 维度影响的场景；其他 backend 需要单独验证。
- deterministic prefix caching 可能增加一次 prefill step，属于可接受的 reproducibility/latency trade-off。
- review comment 暴露的 resumed/block-aligned 风险是实现边界，不等价于 PR 已完全失效；但在当前 patch 中这两个早退条件仍存在，且 PR 仍 open/dirty、有 merge conflict 提醒，因此只能写成 include-with-boundary。
- [#42699](https://github.com/vllm-project/vllm/issues/42699) 与 [#40896](https://github.com/vllm-project/vllm/issues/40896) 是 open issue：评论提供复现和 mitigation 线索，但没有 linked fix、changed files 或 maintainer resolution，不能写成已解决结论。
- dtype guard 问题应进入 quant/dtype 机制页交叉复核，不能只归因于 prefix cache。

## 仍需补证

- `#42699`、`#40896` 需要继续确认 linked fix、comment resolution 和测试覆盖；特别是 batch-invariant mode 是否被文档化为 prefix-cache reproducibility 的推荐设置。
- 下一轮应从本地 review queue 中筛选 `prefix_cache_equivalence`，但 promotion 前必须阅读 targeted evidence JSON 或上游 issue/PR。
- 继续追踪 `#40179` 是否出现 follow-up patch：用 `num_computed_tokens` 判断 prefill、用 `(num_prompt_tokens - 1)` 计算 final-token-aware block boundary，并补 resumed/block-aligned 回归测试。
