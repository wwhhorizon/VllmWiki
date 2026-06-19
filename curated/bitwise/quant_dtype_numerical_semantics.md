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
- quantization auto-conversion 将模型路由到不受 batch-invariant override 控制的 fused kernel。
- FP8 KV 与非均匀 per-layer Q-head 模型组合时，metadata plan/scratch shape 使用错误 head count。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | PR body 声称 MI325X/MI355X(gfx950) 应使用 `float8_e4m3fnuz`，并修改 `is_fp8_fnuz()` 匹配 `gfx95`；但 maintainer 评论明确反驳：Fnuz 只支持 gfx942，MI325 与 MI300 同为 gfx942，MI355/gfx950 使用 CUDA-like FP8 format。PR closed/unmerged。 | hardware guard 结论必须先被硬件/maintainer 事实校验；这条应作为 exclude 反例，而不是 dtype 修复手段。 |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE integration 未传入 batch-invariant flag，导致低精度 MoE 随 batch composition 改变 `block_m`/`split_k`。 | quant kernel config 是 bitwise contract 的一部分。 |
| [#42007](https://github.com/vllm-project/vllm/issues/42007), [#42120](https://github.com/vllm-project/vllm/pull/42120) | FP8 W8A8 MoE + LoRA adapter 输出乱码：MoE `_prepare()` 已把 hidden states 量化成 `torch.float8_e4m3fn`，但 LoRA shrink/expand 仍需要原始 BF16/FP16 activation。PR 同时修两个路径：无 active LoRA 的 base batch 通过 `no_lora_flag` 早退，避免 stale mapping 写坏 base output；LoRA active 时 stash/传递 `original_hidden_states`，并在 DP/EP all2all 下延后 activation quantization，让 base GEMM 用量化副本、LoRA kernel 用未量化输入。review comment 要求清理 stash、把 stash 提前到 `_prepare()` 前，后续 patch 已响应；另有 Blackwell 验证确认 LoRA crash 消失、no-LoRA FP8 MoE 路径无回归、base-after-adapter byte-identical。 | LoRA + MoE + FP8 要同时验证 base path、adapter path、DP/EP all2all、stale mapping 与 dtype 输入；PR 已有强机制证据和 maintainer approval，但仍 open，且 PR body 明确未覆盖 wrong input dtype 的单元测试，因此保持 include-with-boundary。 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325), [#42379](https://github.com/vllm-project/vllm/pull/42379) | RMSNorm regression 将 weight 先 upcast 到 FP32 再乘，导致 BF16 weight 场景与 native-dtype reference 最大差异约 `3.125e-02`；merged PR 在 regular RMSNorm、fused add RMSNorm、static FP8 quant RMSNorm 等 6 个 kernel site 恢复 `static_cast<scalar_t>(x * s_variance) * weight`，并让 fused quant path 与 non-fused composite path 对齐。PR 测试显示 core layernorm 865 项、IR layernorm 1442 项通过，并补充 TinyLlama/H100 `lm_eval` 无回归；后续评论指出 Python IR 不应默认充当 CUDA spec。 | fusion path 需要独立记录 multiply dtype 和 reference boundary。结论应写成“已合并的 native-dtype 行为及其验证”，同时保留 spec 争议边界：不能把 Python IR 自动等同于所有 CUDA kernel 的规范。 |
| [#29581](https://github.com/vllm-project/vllm/issues/29581), [#38670](https://github.com/vllm-project/vllm/pull/38670) | AWQ 模型默认可自动转换到 AWQ_Marlin kernel；issue 复现集中在 Qwen3-30B-AWQ 和 SM120/SM90 支持边界。merged PR 在 BI mode 下阻止 AWQ_Marlin override，并强制 AWQ dequant + `torch.matmul`，同时修 float16 BI kernel 的 shared-memory block size 和 `_half_to_float` log_softmax。 | quantization method selection 是数值语义的一部分；BI mode 下可以牺牲 fused Marlin 性能，换取受控 matmul path。 |
| [#40408](https://github.com/vllm-project/vllm/pull/40408) | merged PR 为 Cutlass FP8 scaled-mm 在 sm89/sm90/sm100/sm120 增加 batch-invariant dispatch：BI mode 下 direct FP8 path 可绕过 BF16 dequant，但要求 CUTLASS config independent of `M`；新增 `test_cutlass_fp8_batch_invariant_fixed_config` 覆盖多 weight shape 与 batch size/M 维。 | 低精度 fast path 可以被纳入 BI，但必须证明 config 不随 batch M 维改变；否则 tuning 会重新引入 batch-dependent rounding/reduction。 |
| [#40413](https://github.com/vllm-project/vllm/pull/40413) | merged PR 去掉 BI mode 下 fused add RMSNorm 强制走 Triton `rms_norm_batch_invariant` 的分支，因为 `fused_add_rms_norm` 自身已是 batch invariant；新增测试覆盖 residual path、hidden size、FP16/BF16，并在 `_custom_ops.py` 标注该 op batch invariant。 | 不应因为进入 BI mode 就盲目替换所有 fused op；如果 fused op 本身已有 batch-invariant 证据，保留原 op 可以减少 dtype/path drift 和性能损失。 |
| [#41651](https://github.com/vllm-project/vllm/issues/41651), [#42650](https://github.com/vllm-project/vllm/pull/42650) | Laguna XS.2 FP8 + FP8 KV cache 在 sm120 上表现为 random output/garbage logits；PR #42650 将 FlashInfer/Triton metadata builder 的 Q-head source 从 model-wide config 改为 served `Attention` layer 的 `impl.num_heads`。这修复了非均匀 per-layer head count 下 plan-time 48 heads 与 runtime 64 heads 不一致导致的 FlashInfer tail zero 与 Triton scratch 越界。 | FP8 KV 问题不总是 scale/dtype 本身错误，也可能是 low-precision path 的 metadata shape 错误；head count、scratch shape 和 KV dtype 必须一起进入数值语义边界。 |

## 根因机制

低精度路径中的 bitwise 问题常来自“看似实现细节、实际改变数值语义”的地方：dtype guard、scale layout、fusion math dtype、MoE tile config、loading buffer lifetime。它们可能先制造很小的 tensor 差异，再通过 KV cache、MoE routing 或 logits 放大为 token 变化。

`#42120` 展示的是 activation identity 问题：base MoE GEMM 需要量化后的 activation，但 LoRA delta 计算需要原始精度 activation。把同一个 `hidden_states` 同时当作两种语义使用，会让 LoRA correction 基于缺 scale compensation 的 FP8 值，或者让无 LoRA 的 base batch 继承上一批 LoRA mapping。

`#42379` 展示的是 reference boundary 问题：regular RMSNorm 与 fused quant RMSNorm 必须声明“最终乘法在哪个 dtype 中发生”。即使某个 FP32 路径看起来更高精度，只要它改变了既有 native-dtype 行为，就可能在多层 norm 后累积成可见输出差异。

`#38670/#40408/#40413` 补充了 BI mode 下的低精度路径选择原则：不是所有 fused/fast kernel 都必须禁用，也不是所有 fused/fast kernel 都能保留。AWQ_Marlin 因绕开 BI override 被禁用；Cutlass FP8 因补了 fixed-config BI dispatch 可以保留；fused add RMSNorm 因已有 batch-invariant 测试，不应被替换成另一条 Triton path。

`#42650` 展示的是低精度 metadata shape 问题：FP8 KV cache 让错误 head-count metadata 的后果更快变成 garbage output，但根因不是 FP8 格式本身，而是 FlashInfer/Triton 的 plan-time allocation 与 runtime Q-head 维度不一致。

## 修复方式

1. 显式记录 weight dtype、activation dtype、KV dtype、scale dtype。
2. 对 scale layout 记录 shape、swizzle、padding、block size、expert routing 和 backend。
3. hardware guard 必须回答“数值语义是否一致”，不是只回答“kernel 能否运行”。
4. 对 async loading 和 streaming buffer 记录 copy completion、buffer lifetime 和 iteration order。
5. 用 exact 或严格 tolerance 测试 fusion path、regular path、LoRA path、base path。
6. 对 loader/streamer 问题，不只记录“加载顺序”，还要记录 tensor 是否是 shared-buffer view、copy 是否跨设备异步、源 buffer 是否可能被 generator 提前复用。
7. 对 `clone()`、`torch.cuda.synchronize()`、排序 stream files 这类定位手段，必须区分“证明竞态存在”和“上游最终修复已合并”；没有 patch/test 前不能写成稳定 fix pattern。
8. 对 MoE LoRA，分开保存 base GEMM 的量化 activation 与 LoRA kernel 的原始精度 activation；无 active LoRA 时必须早退，不能让 stale mapping 继续写入 output。
9. 对 RMSNorm/fused quant，明确 native-dtype multiply、FP32 multiply 与 composite reference 的关系；修 fused path 时要同时修 regular path，避免两条路径互相漂移。
10. 对 BI mode 下的 quantization selector，逐个判断 fused kernel：不可控的要绕开，可证明 fixed-config 的可以保留，已有 BI 证据的 fused op 不应无谓替换。
11. 对 FP8 KV + attention backend，除了 scale/k/v dtype，还要记录 per-layer Q-head、KV-head、scratch shape、plan-time metadata 和 runtime tensor shape 是否一致。

## 验证契约

- dtype/scale 层：记录 dtype、scale layout、backend、hardware guard，并和 reference path 比较。
- loading 层：保证 CPU/GPU copy 完成前 shared buffer 不被复用或覆盖。
- loader/streamer 层：用 `clone()` 与 sync 实验区分 shared-buffer ownership、copy completion 和 generator lifetime；这些实验能支持 root-cause 假设，但不能替代 merged regression test。
- serving 层：LoRA/base、MoE/non-MoE、batch invariant on/off 都要覆盖。
- 对低精度 kernel 可以使用 strict tolerance，但若 claim 是 deterministic/bitwise，就必须额外检查 token/logprob stability。
- MoE LoRA 层：覆盖 active LoRA、无 active LoRA、adapter batch 后的 base batch、DP/EP all2all、one-shot/small-batch/legacy kernel fallback；只测 early exit 不足以覆盖 wrong input dtype。
- Norm/fusion 层：同时比较 regular RMSNorm、fused add RMSNorm、static FP8 quant RMSNorm 与 non-fused composite path；如果选择 Python/IR reference，必须记录 maintainer 是否接受该 reference boundary。
- Quant selector 层：比较原 quant method、BI fallback method、硬件能力、dtype 和性能代价；若保留 direct FP8/Cutlass path，必须覆盖多 batch size/M 维。
- FP8 KV metadata 层：覆盖非均匀 per-layer head 模型、长 prompt、CUDA graphs/compile、FlashInfer native path、TRITON_ATTN path；并将 scale bug 与 metadata bug拆开验证。

## 适用边界

- [#38991](https://github.com/vllm-project/vllm/issues/38991) 仍是 defer：当前只有 issue body，没有 linked fix、changed files、comments、timeline 或 maintainer resolution。适用边界也应保留在 issue body 报告的统一内存平台 + FP8/NVFP4 模型；离散 GPU 与 bf16 路径不能直接外推。它是 loading-lifetime 风险，不进入代表证据。
- [#36488](https://github.com/vllm-project/vllm/pull/36488) 同时属于 batch invariance 和 quant/dtype 机制，不能只在一个页面维护。
- [#42120](https://github.com/vllm-project/vllm/pull/42120) 当前本地 evidence 中仍 open/unmerged，虽然已有 maintainer approval 和 Blackwell 验证；wrong input dtype 缺专门单测，第三方验证的 adapter 没有 routed-expert LoRA 权重，因此不能写成所有 FP8 MoE LoRA 数值都已闭环。
- [#42379](https://github.com/vllm-project/vllm/pull/42379) 已 merged，但 `#42325` 后续评论对“Python IR 是否是 CUDA spec”提出异议；wiki 结论应约束在该 PR 接受并合并的 native-dtype behavior 与已跑测试，不把 Python IR 扩展成通用规范。
- [#38670](https://github.com/vllm-project/vllm/pull/38670) 已 merged，但只是让 AWQ 在 BI mode 下回到 dequant + `torch.matmul`；不能宣称 AWQ_Marlin fused kernel 本身已 deterministic。
- [#40408](https://github.com/vllm-project/vllm/pull/40408) 已 merged，证据覆盖当前 Cutlass FP8 fixed-config path；后续如果 Cutlass tuning 重新依赖 `M`，需要重新验证。
- [#40413](https://github.com/vllm-project/vllm/pull/40413) 已 merged，但结论只覆盖 `fused_add_rms_norm` residual path 的 batch-invariant property，不等于所有 fused norm/quant op 都可直接保留。
- [#42650](https://github.com/vllm-project/vllm/pull/42650) 已 merged，但 `#41651` 的完整症状还包含独立的 TRITON_ATTN FP8 scale 问题；wiki 只把它写成非均匀 per-layer Q-head metadata fix，不写成所有 FP8 KV Blackwell random output 的完整修复。
- hardware guard 的结论不能跨 GPU family 外推，尤其是 ROCm gfx950、Blackwell、GB10/GB200/GB300 等低精度路径。`#33179` 显示 PR body 里的硬件格式假设可能反过来是错的；closed/unmerged PR 和 maintainer 反驳应进入 exclude，而非 promotion。

## 仍需补证

- 寻找 `#38991` 的 linked PR/file evidence，确认 `runai_safetensors_weights_iterator` ownership、`BaseModelLoader.load_model()` copy synchronization、shared buffer lifetime 或 regression test 的实际修复方式。
- 追踪 `#42120` 是否合并，并补齐 wrong input dtype 的可维护测试；确认 routed-expert LoRA weights 非零时的 adapter path 也稳定。
- 对 `#42325/#42379` 继续记录 spec 讨论结果：如果未来 CUDA 侧改回 FP32，应同步更新 reference boundary，而不是只看某一侧实现。
- 追踪 AWQ_Marlin 是否未来提供 deterministic fused path；追踪 Cutlass FP8 tuning 和 fused norm 优化是否保持 batch-invariant tests。
- 追踪 `#42580` 是否提供 TRITON_ATTN FP8 `k_scale/v_scale` 的独立闭环；不要把它并入 `#42650`。
