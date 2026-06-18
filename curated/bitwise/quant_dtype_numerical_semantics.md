# 量化与 Dtype 数值语义

状态：curated seed，部分条目仍需 linked fix。  
父页：[Bitwise 确定性与数值等价](README.md)。
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
| [#38991](https://github.com/vllm-project/vllm/issues/38991) | `runai_safetensors_weights_iterator` 产出的 tensors 可能是 shared numpy buffer view；`BaseModelLoader.load_model()` 在 CUDA target device 下初始化参数后，`param.data.copy_(loaded_weight)` 可能成为 CPU -> CUDA cross-device copy。issue body 的定位实验显示：`tensor.clone()`、每次或最终 `torch.cuda.synchronize()`、改变 stream file 顺序都能让问题不复现；但该 issue 仍为 open，且本地 evidence 中没有 comments、timeline、linked PR、changed files 或 maintainer resolution。 | 该条是高价值 loading-lifetime insight，不是已修复结论。clone/sync/sort-file 只能作为定位证据和候选修复方向；缺上游 patch/test 前保持 defer。 |

## 根因机制

低精度路径中的 bitwise 问题常来自“看似实现细节、实际改变数值语义”的地方：dtype guard、scale layout、fusion math dtype、MoE tile config、loading buffer lifetime。它们可能先制造很小的 tensor 差异，再通过 KV cache、MoE routing 或 logits 放大为 token 变化。

## 修复方式

1. 显式记录 weight dtype、activation dtype、KV dtype、scale dtype。
2. 对 scale layout 记录 shape、swizzle、padding、block size、expert routing 和 backend。
3. hardware guard 必须回答“数值语义是否一致”，不是只回答“kernel 能否运行”。
4. 对 async loading 和 streaming buffer 记录 copy completion、buffer lifetime 和 iteration order。
5. 用 exact 或严格 tolerance 测试 fusion path、regular path、LoRA path、base path。
6. 对 loader/streamer 问题，不只记录“加载顺序”，还要记录 tensor 是否是 shared-buffer view、copy 是否跨设备异步、源 buffer 是否可能被 generator 提前复用。
7. 对 `clone()`、`torch.cuda.synchronize()`、排序 stream files 这类定位手段，必须区分“证明竞态存在”和“上游最终修复已合并”；没有 patch/test 前不能写成稳定 fix pattern。

## 验证契约

- dtype/scale 层：记录 dtype、scale layout、backend、hardware guard，并和 reference path 比较。
- loading 层：保证 CPU/GPU copy 完成前 shared buffer 不被复用或覆盖。
- loader/streamer 层：用 `clone()` 与 sync 实验区分 shared-buffer ownership、copy completion 和 generator lifetime；这些实验能支持 root-cause 假设，但不能替代 merged regression test。
- serving 层：LoRA/base、MoE/non-MoE、batch invariant on/off 都要覆盖。
- 对低精度 kernel 可以使用 strict tolerance，但若 claim 是 deterministic/bitwise，就必须额外检查 token/logprob stability。

## 适用边界

- [#38991](https://github.com/vllm-project/vllm/issues/38991) 仍是 defer：当前只有 issue body，没有 linked fix、changed files、comments、timeline 或 maintainer resolution。适用边界也应保留在 issue body 报告的统一内存平台 + FP8/NVFP4 模型；离散 GPU 与 bf16 路径不能直接外推。
- [#36488](https://github.com/vllm-project/vllm/pull/36488) 同时属于 batch invariance 和 quant/dtype 机制，不能只在一个页面维护。
- hardware guard 的结论不能跨 GPU family 外推，尤其是 ROCm gfx950、Blackwell、GB10/GB200/GB300 等低精度路径。

## 仍需补证

- 寻找 `#38991` 的 linked PR/file evidence，确认 `runai_safetensors_weights_iterator` ownership、`BaseModelLoader.load_model()` copy synchronization、shared buffer lifetime 或 regression test 的实际修复方式。
- 继续复核 `#42007/#42120` 的 exact corruption boundary，以及 quantized MoE 在 batch invariant mode 下的 test matrix。
