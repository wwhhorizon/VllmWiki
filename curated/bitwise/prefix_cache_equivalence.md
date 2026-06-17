# Prefix Cache 等价

状态：curated。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。

## 契约

同一个 prompt、同一个模型、同样 deterministic sampling 设置下，full prefill、prefix-cache miss、prefix-cache hit、prefix-cache bypass 不应该产生不同的可见 token。若 backend 只能保证近似数值一致，必须明确写出 tolerance 与适用边界；不能把 `temperature=0` 下的 greedy token 翻转当作普通性能差异。

## 机制

Prefix caching 会改变实际计算几何。cache miss 往往对完整 prompt 做 prefill，GEMM 的 `M=N`；cache hit 只计算未命中的 suffix，常见 `M=N % block_size`。不同 `M` 会触发不同 backend kernel、tiling 或 accumulation order。低精度路径中，1 ULP 的早期层差异可能在多层 transformer 中放大，最后翻转 logits argmax。

## Source Evidence

| Source | 证据 | 炼化结论 |
| --- | --- | --- |
| [#33123](https://github.com/vllm-project/vllm/issues/33123) | ROCm 上首次请求 cache miss 与后续 cache hit 输出不同；本地已抓取 18 条评论和 55 条 timeline event。 | 这是 prefix-cache 语义问题，不只是 cache 性能问题。 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | PR body 明确说明 cache-miss full prefill 与 cache-hit suffix prefill 的 GEMM `M` 维度不同会改变 ROCm/Tensile tiling 和 BF16 accumulation order；changed files 增加 `--deterministic-prefix-caching`、cache config、scheduler split 和 e2e test。 | deterministic mode 下要让 cache miss 与 cache hit 的 suffix GEMM geometry 对齐。 |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | gfx950 FP8 dtype guard 漏掉 MI325X/MI355X，错误使用 `float8_e4m3fn` 而非 `float8_e4m3fnuz`，会在 cache miss/full prefill 与 cache hit/partial prefill 间制造发散。 | cache 等价还依赖 dtype/backend dispatch 一致。 |
| [#42699](https://github.com/vllm-project/vllm/issues/42699) | prefix-read 与 no-prefix-read 在 greedy decoding 下可能翻转词边界。 | 保持 candidate，需 linked fix/comment 复核。 |
| [#40896](https://github.com/vllm-project/vllm/issues/40896) | V1 首次请求和后续相同请求不同，禁用 prefix caching 后稳定。 | 保持 candidate，作为 prefix-cache 默认语义风险。 |

## Fix Pattern

1. 在 deterministic mode 下固定或对齐 cache-hit 与 cache-miss 的 prefill kernel geometry。
2. 对 cache miss、cache hit、cache bypass 三种路径都做同 prompt 回归测试。
3. 同时记录 dtype、backend、block size、suffix length、GEMM shape 和硬件架构。
4. 如果必须接受近似数值差异，应证明不会翻转 token/logprob ranking。
5. 对 ROCm/Tensile、CUDA/cuBLAS、FlashInfer 等 backend 分别记录边界，避免把一个 backend 的结论泛化到所有硬件。

## Open Review Queue

继续从 [bitwise_review_queue.csv](../bitwise_review_queue.csv) 中筛选 `prefix_cache_equivalence`，但 promotion 前必须阅读本地 targeted evidence JSON 或上游 issue/PR。
