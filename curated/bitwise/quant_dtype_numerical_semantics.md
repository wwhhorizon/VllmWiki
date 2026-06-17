# 量化与 Dtype 数值语义

状态：curated seed，部分条目仍需 linked fix。  
父页：[Bitwise 确定性与数值等价](../bitwise_determinism.md)。  
范围：FP8/FP4/NVFP4/MXFP4、scale layout、dtype dispatch、LoRA path、fusion path 和 weight loading lifetime。

## 问题定义

量化和 dtype dispatch 必须保持语义稳定：同一个模型权重、scale layout、backend 和 cache dtype 不应因为硬件 guard、load order、LoRA path 或 fusion path 不同而改变 deterministic 输出。

## 典型触发条件

- FP8/FP4/NVFP4/MXFP4 dtype guard 选错数值格式。
- scale layout、swizzle、padding、block size 或 expert routing 不一致。
- fused kernel 与 regular kernel dtype 规则混用。
- async loading buffer lifetime 破坏权重。
- MoE routing 改变 tile/reduction order，低精度累加放大差异。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | gfx950 FP8 dtype guard 漏掉 MI325X/MI355X，导致错误使用 `float8_e4m3fn` 而非 `float8_e4m3fnuz`。 | hardware guard 必须约束数值语义，而不只是可运行性。 |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE integration 未传入 batch-invariant flag，导致低精度 MoE 随 batch composition 改变 `block_m`/`split_k`。 | quant kernel config 是 bitwise contract 的一部分。 |
| [#42007](https://github.com/vllm-project/vllm/issues/42007), [#42120](https://github.com/vllm-project/vllm/pull/42120) | MoE FP8 LoRA/base response corruption 与 LoRA path、precision hidden state 保存、early exit 有关。 | LoRA + MoE + FP8 要同时验证 base path 和 adapter path。 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325) | RMSNorm FP8 fusion 与 regular RMSNorm dtype 语义混淆。 | fusion path 需要独立记录 multiply dtype 和 reference boundary。 |
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | `runai_safetensors_weights_iterator` 产出的 tensors 是 shared numpy buffer view；加载到 CUDA 参数时 `copy_()` 可能是异步 cross-device copy，统一内存平台上 buffer lifetime/迭代顺序可能破坏 FP8/NVFP4 权重。 | 强问题描述，但缺 linked fix/file evidence，保持 defer。 |

## 根因机制

低精度路径中的 bitwise 问题常来自“看似实现细节、实际改变数值语义”的地方：dtype guard、scale layout、fusion math dtype、MoE tile config、loading buffer lifetime。它们可能先制造很小的 tensor 差异，再通过 KV cache、MoE routing 或 logits 放大为 token 变化。

## 修复方式

1. 显式记录 weight dtype、activation dtype、KV dtype、scale dtype。
2. 对 scale layout 记录 shape、swizzle、padding、block size、expert routing 和 backend。
3. hardware guard 必须回答“数值语义是否一致”，不是只回答“kernel 能否运行”。
4. 对 async loading 和 streaming buffer 记录 copy completion、buffer lifetime 和 iteration order。
5. 用 exact 或严格 tolerance 测试 fusion path、regular path、LoRA path、base path。

## 验证契约

- dtype/scale 层：记录 dtype、scale layout、backend、hardware guard，并和 reference path 比较。
- loading 层：保证 CPU/GPU copy 完成前 shared buffer 不被复用或覆盖。
- serving 层：LoRA/base、MoE/non-MoE、batch invariant on/off 都要覆盖。
- 对低精度 kernel 可以使用 strict tolerance，但若 claim 是 deterministic/bitwise，就必须额外检查 token/logprob stability。

## 适用边界

- [#38991](https://github.com/vllm-project/vllm/issues/38991) 仍是 defer：当前只有 issue body，没有 linked fix、changed files 或 maintainer resolution。
- [#36488](https://github.com/vllm-project/vllm/pull/36488) 同时属于 batch invariance 和 quant/dtype 机制，不能只在一个页面维护。
- hardware guard 的结论不能跨 GPU family 外推，尤其是 ROCm gfx950、Blackwell、GB10/GB200/GB300 等低精度路径。

## 仍需补证

- 寻找 `#38991` 的 linked PR/file evidence，确认 buffer lifetime、copy synchronization 或 iterator order 的实际修复方式。
- 继续复核 `#42007/#42120` 的 exact corruption boundary，以及 quantized MoE 在 batch invariant mode 下的 test matrix。
