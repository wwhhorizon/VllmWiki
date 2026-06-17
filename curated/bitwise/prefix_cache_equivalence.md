# Prefix Cache 等价

状态：curated。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。  
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
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | PR body 明确说明 cache-miss full prefill 的 GEMM `M=N`，cache-hit suffix prefill 的 `M=N % block_size`；不同 `M` 会改变 ROCm/Tensile tiling 和 BF16 accumulation order。changed files 包含 cache config、scheduler split 和 e2e test。 | deterministic mode 下要让 cache miss 与 cache hit 的 suffix GEMM geometry 对齐。 |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | gfx950 FP8 dtype guard 漏掉 MI325X/MI355X，错误使用 `float8_e4m3fn` 而非 `float8_e4m3fnuz`。 | cache 等价还依赖 dtype/backend dispatch 一致。 |
| [#42699](https://github.com/vllm-project/vllm/issues/42699) | prefix-read 与 no-prefix-read 在 greedy decoding 下可能翻转词边界。 | 保持 candidate，需 linked fix/comment 复核。 |
| [#40896](https://github.com/vllm-project/vllm/issues/40896) | V1 首次请求和后续相同请求不同，禁用 prefix caching 后稳定。 | 保持 candidate，作为 prefix-cache 默认语义风险。 |

## 根因机制

Prefix caching 会改变实际计算几何。cache miss 往往对完整 prompt 做 prefill；cache hit 只计算未命中的 suffix。不同 `M` 可能触发不同 backend kernel、tiling 或 accumulation order。低精度路径中，早期层 1 ULP 级差异可能在多层 transformer 中放大，最终翻转 logits argmax。

## 修复方式

1. 在 deterministic mode 下固定或对齐 cache-hit 与 cache-miss 的 prefill kernel geometry。
2. 像 [#40179](https://github.com/vllm-project/vllm/pull/40179) 一样在 scheduler 层把 cache-miss prefill 拆到最后一个 cached block boundary，使 suffix GEMM 的 `M` 与 cache-hit path 对齐。
3. 对 cache miss、cache hit、cache bypass 三种路径都做同 prompt 回归测试。
4. 同时记录 dtype、backend、block size、suffix length、GEMM shape 和硬件架构。

## 验证契约

- 用户可见层：同 prompt 多次请求的 generated token 必须一致。
- kernel 几何层：cache-miss 与 cache-hit 的 suffix GEMM shape 必须一致或被显式解释。
- 回归测试层：覆盖首次请求、后续 cache hit、禁用 prefix cache、非 block-aligned prompt。
- 如果只能证明 strict tolerance，必须继续证明差异不会翻转 token/logprob ranking。

## 适用边界

- [#40179](https://github.com/vllm-project/vllm/pull/40179) 的直接证据集中在 ROCm/BF16/Tensile 受 GEMM `M` 维度影响的场景；其他 backend 需要单独验证。
- deterministic prefix caching 可能增加一次 prefill step，属于可接受的 reproducibility/latency trade-off。
- dtype guard 问题应进入 quant/dtype 机制页交叉复核，不能只归因于 prefix cache。

## 仍需补证

- `#42699`、`#40896` 需要继续确认 linked fix、comment resolution 和测试覆盖。
- 下一轮应从本地 review queue 中筛选 `prefix_cache_equivalence`，但 promotion 前必须阅读 targeted evidence JSON 或上游 issue/PR。
