# Prefix Cache 等价

状态：reviewed seed page。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)

## 契约

对同一个可见 prompt 和 deterministic sampling 设置，full-prefill、prefix-cache miss、prefix-cache hit、prefix-read/no-prefix-read 路径应该产生 bit-identical 输出，或明确记录可接受的数值差异。如果用户在 `temperature=0` 下看到不同 greedy answer，这是正确性问题，不是 cache 性能细节。

## 机制

Prefix caching 会改变 compute geometry：

- cache miss 可能一次 prefill 全部 `N` 个 token。
- cache hit 往往只计算未缓存 suffix，常见形态是 `N % block_size`。
- 不同 GEMM `M` 维度可能选择不同 backend kernel 或 tiling。
- 不同累加顺序可能带来 1 ULP 差异。
- 差异一旦写入 KV cache，后续 attention 会把它放大成 logits/token 差异。

## Curated Case

| Case | 观察 | 优化/修复 |
| --- | --- | --- |
| [#33123](https://github.com/vllm-project/vllm/issues/33123) | ROCm MI355X 上首次请求 cache miss 与后续 cache hit 输出不同 | 根机制是 BF16 GEMM tiling 在 full-prefill 与 suffix-prefill 间发散 |
| [#34046](https://github.com/vllm-project/vllm/pull/34046) | 提出 split prefix caching | 在最后 block 边界拆分 cache-miss prefill，使 suffix GEMM geometry 与 cache-hit path 对齐 |
| [#40179](https://github.com/vllm-project/vllm/pull/40179) | 增加 `--deterministic-prefix-caching` | 让 ROCm 和其他 BF16 GEMM-sensitive path 的 cache miss/hit prefill 可复现 |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | gfx950 使用了错误 FP8 dtype | 将 MI325X/MI355X 路由到 `float8_e4m3fnuz`，移除一类 cache 状态发散源 |
| [#42699](https://github.com/vllm-project/vllm/issues/42699) | prefix-read vs no-prefix-read 在 greedy decoding 下翻转词边界 | candidate：仍需 linked fix/comment review |
| [#40896](https://github.com/vllm-project/vllm/issues/40896) | V1 首次请求与后续相同请求不同，禁用 prefix caching 后稳定 | candidate：默认 prefix-caching 语义必须匹配 deterministic decoding 行为 |

## Fix Pattern

1. deterministic mode 下对齐 cache-hit 与 cache-miss compute geometry。
2. 让 dtype/backend dispatch 在不同 cache 状态下保持一致。
3. 用相同 prompt 分别验证 cache miss、cache hit 和 explicit cache bypass。
4. 记录比较契约：bit-identical、logits-close 或 semantic equivalence。

## Open Review Queue

使用 [bitwise_review_queue.csv](../bitwise_review_queue.csv) 中 cluster 为 `prefix_cache_equivalence` 的行。
