# 量化与 Dtype 数值语义

状态：reviewed seed page。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)

## 契约

量化和 dtype dispatch 必须保持语义稳定：同一个模型权重、scale layout、backend 和 cache dtype 不应因为硬件 guard、load order 或 fusion path 不同而改变 deterministic 输出。

## 机制

低精度路径中的 bitwise 问题常来自：

- FP8/FP4/NVFP4/MXFP4 dtype 选择错误。
- scale factor layout、swizzle、padding 或 block-scale index 不一致。
- fused kernel 重用普通 kernel 的 dtype 规则，或反过来。
- async weight loading / streaming buffer lifetime 破坏权重。
- quantized MoE routing 改变 tile/reduction order。

## Curated Case

| Case | 观察 | 优化/修复 |
| --- | --- | --- |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | ROCm gfx950 FP8 dtype 错误 | MI325X/MI355X 使用 `float8_e4m3fnuz` |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE batch composition 改变 config | 传递 batch invariant flag，固定 kernel 参数 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325) | RMSNorm FP8 fusion 与 regular RMSNorm dtype 语义混淆 | 区分 fusion path 与 regular path 的 multiply dtype |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | FP8/NVFP4 weight loading order/lifetime 可疑 | candidate：需要 fix PR/file evidence |
| [#42007](https://github.com/vllm-project/vllm/issues/42007), [#42120](https://github.com/vllm-project/vllm/pull/42120) | quant/load-order gap | candidate：需要 source review |
| [#23256](https://github.com/vllm-project/vllm/issues/23256) | quant 相关候选 | candidate：需要确认是否 bitwise family |

## Fix Pattern

1. 显式记录 dtype：weight dtype、activation dtype、KV cache dtype、scale dtype。
2. 对 scale layout 记录 shape、swizzle、padding、block size 与 backend。
3. hardware guard 不只判断可运行，还要判断数值语义是否一致。
4. 对 async loading 记录 buffer lifetime 与 copy completion。
5. 用 exact 或严格 tolerance 测试 fusion path 与 reference path。

## Open Review Queue

使用 [bitwise_review_queue.csv](../bitwise_review_queue.csv) 中 cluster 为 `quant_dtype_semantics` 的行。
