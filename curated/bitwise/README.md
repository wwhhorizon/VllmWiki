# Bitwise 确定性与数值等价

状态：curated topic map。
范围：bitwise invariance、deterministic output、batch-size invariance、prefix-cache equivalence，以及可能翻转 greedy decoding 的 numerical drift。

## 核心 Lesson

在当前已复核的代表性 bitwise / deterministic 样本中，许多问题并不只是普通浮点噪声，而是暴露 serving path 中多个隐含契约没有被显式固定。request state、KV cache identity、backend routing、GEMM tiling、quantization scale/layout 和 kernel launch geometry 都可能改变同一请求的 token、logprob、KV 或 metadata identity。

通用术语见 [Glossary](../../docs/glossary.md)；维护规则见 [维护规则](../../docs/maintenance.md)。

## 推荐阅读顺序

1. [Bitwise 工作的验证契约](verification_contracts.md)
2. [Prefix Cache 等价](prefix_cache_equivalence.md)
3. [并发下的 KV Cache Identity](kv_cache_identity_concurrency.md)
4. [Batch Invariance 与 Kernel Geometry](batch_invariance_kernel_geometry.md)
5. [Deterministic Dispatch 与 Reduction Control](deterministic_dispatch_reduction.md)
6. [量化与 Dtype 数值语义](quant_dtype_numerical_semantics.md)
7. [对 Kernel 优化的约束](implications_for_kernels.md)

## 稳定机制族

| 机制族 | 一句话摘要 | 机制页 |
| --- | --- | --- |
| verification contracts | 每条结论必须声明保护对象和比较契约，避免把 semantic answer match 误用为 bitwise 证据。 | [Bitwise 工作的验证契约](verification_contracts.md) |
| prefix-cache equivalence | cache miss、cache hit、cache bypass 与 Mamba metadata replay 要保持 token/logprob/metadata identity。 | [Prefix Cache 等价](prefix_cache_equivalence.md) |
| KV / metadata identity | KV block、block table、persistent buffer、offload store、LoRA adapter 和 external cache key 必须携带足够身份维度。 | [并发下的 KV Cache Identity](kv_cache_identity_concurrency.md) |
| batch / kernel geometry | batch composition 不能改变同一请求的 kernel geometry、attention path、MoE tile 或 quantized matmul config。 | [Batch Invariance 与 Kernel Geometry](batch_invariance_kernel_geometry.md) |
| dispatch / reduction | autotune candidate、split-K、atomic reduction、cuBLAS/workspace 和 backend selector 都必须进入 deterministic contract。 | [Deterministic Dispatch 与 Reduction Control](deterministic_dispatch_reduction.md) |
| quant / dtype semantics | dtype guard、scale layout、fusion math dtype、LoRA activation 和 loading lifetime 都是数值语义的一部分。 | [量化与 Dtype 数值语义](quant_dtype_numerical_semantics.md) |

完整未闭环队列维护在 [next.md](next.md)。

## 维护边界

本页只作为专题地图。完整 defer 队列、open PR/issue 状态、下一步复核计划和辅助边界统一维护在 [next.md](next.md)；候选状态和长文本判断维护在 [bitwise ledger](../../candidates/bitwise_ledger.csv) 与 `candidates/notes/`。