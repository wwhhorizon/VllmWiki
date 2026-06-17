# 量化与 Dtype 数值语义

状态：curated seed，部分条目仍需 linked fix。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。

## 契约

量化和 dtype dispatch 必须保持语义稳定：同一个模型权重、scale layout、backend 和 cache dtype 不应因为硬件 guard、load order、LoRA path 或 fusion path 不同而改变 deterministic 输出。

## 机制

低精度路径中的 bitwise 问题常来自 FP8/FP4/NVFP4/MXFP4 dtype 选择错误、scale layout/swizzle/padding 不一致、fused kernel 与 regular kernel dtype 规则混用、async loading buffer lifetime 破坏权重、MoE routing 改变 tile/reduction order。

## Source Evidence

| Source | 证据 | 炼化结论 |
| --- | --- | --- |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | gfx950 FP8 dtype guard 漏掉 MI325X/MI355X，导致错误使用 `float8_e4m3fn` 而非 `float8_e4m3fnuz`。 | hardware guard 必须约束数值语义，而不只是可运行性。 |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE integration 未传入 batch-invariant flag，导致低精度 MoE 随 batch composition 改变 `block_m`/`split_k`。 | quant kernel config 是 bitwise contract 的一部分。 |
| [#42007](https://github.com/vllm-project/vllm/issues/42007), [#42120](https://github.com/vllm-project/vllm/pull/42120) | MoE FP8 LoRA/base response corruption 与 LoRA path、precision hidden state 保存、early exit 有关。 | LoRA + MoE + FP8 要同时验证 base path 和 adapter path。 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325) | RMSNorm FP8 fusion 与 regular RMSNorm dtype 语义混淆。 | fusion path 需要独立记录 multiply dtype 和 reference boundary。 |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | FP8 inference 中权重迭代顺序非确定，可能与 streaming buffer lifetime/corruption 相关。 | 强问题描述，但缺 linked fix/file evidence，保持 defer。 |

## Fix Pattern

1. 显式记录 weight dtype、activation dtype、KV dtype、scale dtype。
2. 对 scale layout 记录 shape、swizzle、padding、block size、expert routing 和 backend。
3. hardware guard 必须回答“数值语义是否一致”，不是只回答“kernel 能否运行”。
4. 对 async loading 和 streaming buffer 记录 copy completion、buffer lifetime 和 iteration order。
5. 用 exact 或严格 tolerance 测试 fusion path、regular path、LoRA path、base path。

## Open Review Queue

优先继续复核 `#38991` 的 linked fix、`#42007/#42120` 的 exact corruption boundary，以及 quantized MoE 在 batch invariant mode 下的 test matrix。
