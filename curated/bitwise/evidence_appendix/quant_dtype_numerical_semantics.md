# 量化与 Dtype 数值语义 Evidence Appendix

状态：curated public evidence summary。
父页：[../quant_dtype_numerical_semantics.md](../quant_dtype_numerical_semantics.md)。

本文只保存机制页之外的长证据摘要、case 表格、验证矩阵、详细边界和补证记录；通用问题定义、机制解释和修复模式以父页为准。

## 代表证据

| Source | 证据事实 | 炼化结论 |
| --- | --- | --- |
| [#33179](https://github.com/vllm-project/vllm/pull/33179) | PR body 声称 MI325X/MI355X(gfx950) 应使用 `float8_e4m3fnuz`，并修改 `is_fp8_fnuz()` 匹配 `gfx95`；但 maintainer 评论明确反驳：Fnuz 只支持 gfx942，MI325 与 MI300 同为 gfx942，MI355/gfx950 使用 CUDA-like FP8 format。PR closed/unmerged。 | hardware guard 结论必须先被硬件/maintainer 事实校验；这条应作为 exclude 反例，而不是 dtype 修复手段。 |
| [#36488](https://github.com/vllm-project/vllm/pull/36488) | MXFP4 MoE integration 未传入 batch-invariant flag，导致低精度 MoE 随 batch composition 改变 `block_m`/`split_k`。 | quant kernel config 是 bitwise contract 的一部分。 |
| [#42007](https://github.com/vllm-project/vllm/issues/42007), [#42120](https://github.com/vllm-project/vllm/pull/42120) | `#42120` 已于 2026-06-19 合并。它把 FP8 W8A8 MoE + LoRA 的两类问题同时收口：一是 `no_lora_flag_cpu` 早退，防止没有 active LoRA 的 base batch 继续沿用 stale LoRA mapping 写坏输出；二是为 LoRA shrink path保留 `original_hidden_states`，在 DP/EP all2all 场景下延后 activation quantization，让 base GEMM 用量化副本、LoRA kernel 用原始 BF16/FP16 activation。review 要求的“stash 必须清理”和“stash 应在 `_prepare()` 前保存”都已进入最终 patch；Blackwell 上的实际验证也确认了 LoRA crash 消失、no-LoRA FP8 MoE 路径无回归、base-after-adapter byte-identical。 | LoRA + MoE + FP8 的稳定性不是单个 kernel dtype 对不对，而是 base path、adapter path 和 token mapping 生命周期必须同时闭环。`#42120` 已形成稳定主机制：无 active LoRA 时必须早退，active LoRA 时必须把原始精度 activation 送到 LoRA kernel，而不能直接重用量化后的 base activation。 |
| [#42325](https://github.com/vllm-project/vllm/issues/42325), [#42379](https://github.com/vllm-project/vllm/pull/42379) | RMSNorm regression 将 weight 先 upcast 到 FP32 再乘，导致 BF16 weight 场景与 native-dtype reference 最大差异约 `3.125e-02`；merged PR 在 regular RMSNorm、fused add RMSNorm、static FP8 quant RMSNorm 等 6 个 kernel site 恢复 `static_cast<scalar_t>(x * s_variance) * weight`，并让 fused quant path 与 non-fused composite path 对齐。PR 测试显示 core layernorm 865 项、IR layernorm 1442 项通过，并补充 TinyLlama/H100 `lm_eval` 无回归；后续评论指出 Python IR 不应默认充当 CUDA spec。 | fusion path 需要独立记录 multiply dtype 和 reference boundary。结论应写成“已合并的 native-dtype 行为及其验证”，同时保留 spec 争议边界：不能把 Python IR 自动等同于所有 CUDA kernel 的规范。 |
| [#29581](https://github.com/vllm-project/vllm/issues/29581), [#38670](https://github.com/vllm-project/vllm/pull/38670) | AWQ 模型默认可自动转换到 AWQ_Marlin kernel；issue 复现集中在 Qwen3-30B-AWQ 和 SM120/SM90 支持边界。merged PR 在 BI mode 下阻止 AWQ_Marlin override，并强制 AWQ dequant + `torch.matmul`，同时修 float16 BI kernel 的 shared-memory block size 和 `_half_to_float` log_softmax。 | quantization method selection 是数值语义的一部分；BI mode 下可以牺牲 fused Marlin 性能，换取受控 matmul path。 |
| [#40408](https://github.com/vllm-project/vllm/pull/40408) | merged PR 为 Cutlass FP8 scaled-mm 在 sm89/sm90/sm100/sm120 增加 batch-invariant dispatch：BI mode 下 direct FP8 path 可绕过 BF16 dequant，但要求 CUTLASS config independent of `M`；新增 `test_cutlass_fp8_batch_invariant_fixed_config` 覆盖多 weight shape 与 batch size/M 维。 | 低精度 fast path 可以被纳入 BI，但必须证明 config 不随 batch M 维改变；否则 tuning 会重新引入 batch-dependent rounding/reduction。 |
| [#40413](https://github.com/vllm-project/vllm/pull/40413) | merged PR 去掉 BI mode 下 fused add RMSNorm 强制走 Triton `rms_norm_batch_invariant` 的分支，因为 `fused_add_rms_norm` 自身已是 batch invariant；新增测试覆盖 residual path、hidden size、FP16/BF16，并在 `_custom_ops.py` 标注该 op batch invariant。 | 不应因为进入 BI mode 就盲目替换所有 fused op；如果 fused op 本身已有 batch-invariant 证据，保留原 op 可以减少 dtype/path drift 和性能损失。 |
| [#41651](https://github.com/vllm-project/vllm/issues/41651), [#42650](https://github.com/vllm-project/vllm/pull/42650) | Laguna XS.2 FP8 + FP8 KV cache 在 sm120 上表现为 random output/garbage logits；PR #42650 将 FlashInfer/Triton metadata builder 的 Q-head source 从 model-wide config 改为 served `Attention` layer 的 `impl.num_heads`。这修复了非均匀 per-layer head count 下 plan-time 48 heads 与 runtime 64 heads 不一致导致的 FlashInfer tail zero 与 Triton scratch 越界。 | FP8 KV 问题不总是 scale/dtype 本身错误，也可能是 low-precision path 的 metadata shape 错误；head count、scratch shape 和 KV dtype 必须一起进入数值语义边界。 |

## Source-Adjacent 摘要

- `#33179` 是反例锚点：它把 MI355/gfx950 的 FP8 format 判断成 `float8_e4m3fnuz`，但 maintainer 评论直接给出硬件事实——Fnuz 只支持 gfx942，gfx950 用 CUDA-like FP8。因此这条 closed/unmerged PR 只能作为“hardware guard 必须先被 maintainer/硬件事实校验”的负向证据，不能进入 dtype 修复链。
- `#42120` 的 patch 落点很具体：它同时改了 `no_lora_flag_cpu` 早退和 LoRA shrink path 的 `original_hidden_states` stash，让 base GEMM 吃量化 activation、LoRA kernel 吃原始 BF16/FP16 activation；review 要求的“stash 清理”和“stash 在 `_prepare()` 前保存”都已进最终 patch。这说明 LoRA + FP8 MoE 的稳定性是一个“base path / adapter path / token mapping 生命周期同时闭环”的机制，不是单点 dtype 判断。
- `#42379` 的 reference boundary 更值得写准：patch 在 6 个 kernel site 恢复 `static_cast<scalar_t>(x * s_variance) * weight`，把 fused quant path 与 non-fused composite path 对齐；它的验证是 core layernorm 865 项 + IR layernorm 1442 项 + TinyLlama/H100 `lm_eval` 无回归。但 `#42325` 后续评论明确质疑“Python IR 不应默认充当 CUDA spec”，所以这条只能写成“已合并的 native-dtype 行为及其验证”，不能写成“Python IR = 所有 CUDA kernel 规范”。
- `#38991/#43163/#43464` 这条 family 的 source-adjacent 事实很硬：`#43464` 的回归测试不是泛泛断言数值正确，而是显式把 `RUNAI_STREAMER_MEMORY_LIMIT=0` 压到会复用内部 buffer 的状态，再验证不同 yielded tensor 不再共享 data pointer；上游接受的修法是在 `runai_safetensors_weights_iterator` 边界 `clone()` yielded tensor。`#44645` 又把 `clone()` 的 host-RAM 回归收口成 Llama4 loader 的 streaming 改造，而不是回退 `clone()`。因此这条线已分成两层：iterator-side `clone()` = correctness closure，streaming loader = memory/perf closure。

## 适用边界

- [#38991](https://github.com/vllm-project/vllm/issues/38991) 仍是 defer，但它当前的未闭环点已经可以写得更窄：同宗已合并修复线 [#43163](https://github.com/vllm-project/vllm/issues/43163) 与 merged PR [#43464](https://github.com/vllm-project/vllm/pull/43464) 已把 iterator-side `clone()` 收敛成 reusable-buffer loader 的上游 accepted correctness fix，而且测试显式强制 RunAI 内部 buffer 复用；结合当前 main 代码路径，原始 shared-buffer alias 链在默认加载路径上也已被 iterator-side `clone()` 机械切断。closed issue [#44430](https://github.com/vllm-project/vllm/issues/44430) 与 merged PR [#44645](https://github.com/vllm-project/vllm/pull/44645) 又说明 `clone()` 的 host-RAM 回归应由 streaming loader 吸收，而不是回退 correctness fix，但这条 landed 证据直接覆盖的是 Llama4 weight-loading 路径，应把它写成 family-level 样例，不外推成所有模型 loader 已统一完成 streaming 化；issue 提交者已在 2026-06-15 确认修复。本轮之后，`#38991` 继续 defer 的原因不再是“是否真有 shared-buffer lifetime 根因”，也不再默认是“也许还需要另一条 sync/ownership 修法”，而是它本身仍 open、缺 direct linked fix / maintainer closure，而且 exact unified-memory + `BaseModelLoader.load_model()` async copy 路径还没有自己的正式 regression test。
- [#36488](https://github.com/vllm-project/vllm/pull/36488) 同时属于 batch invariance 和 quant/dtype 机制，不能只在一个页面维护。
- [#42120](https://github.com/vllm-project/vllm/pull/42120) 已于 2026-06-19 合并，因此“base batch stale mapping”与“LoRA kernel 错吃量化 activation”这两条主机制已经闭环。但边界仍要保留：PR body 明说 wrong input dtype 缺专门单测，第三方 Blackwell 验证的 adapter 没有 routed-expert LoRA 权重，所以不要把它外推成“所有 FP8 MoE + LoRA 变体都已完全验证”。
- [#42379](https://github.com/vllm-project/vllm/pull/42379) 已 merged，但 `#42325` 后续评论对“Python IR 是否是 CUDA spec”提出异议；wiki 结论应约束在该 PR 接受并合并的 native-dtype behavior 与已跑测试，不把 Python IR 扩展成通用规范。
- [#38670](https://github.com/vllm-project/vllm/pull/38670) 已 merged，但只是让 AWQ 在 BI mode 下回到 dequant + `torch.matmul`；不能宣称 AWQ_Marlin fused kernel 本身已 deterministic。
- [#40408](https://github.com/vllm-project/vllm/pull/40408) 已 merged，证据覆盖当前 Cutlass FP8 fixed-config path；后续如果 Cutlass tuning 重新依赖 `M`，需要重新验证。
- [#40413](https://github.com/vllm-project/vllm/pull/40413) 已 merged，但结论只覆盖 `fused_add_rms_norm` residual path 的 batch-invariant property，不等于所有 fused norm/quant op 都可直接保留。
- [#42650](https://github.com/vllm-project/vllm/pull/42650) 已 merged，但 `#41651` 的完整症状还包含独立的 TRITON_ATTN FP8 scale 问题；wiki 只把它写成非均匀 per-layer Q-head metadata fix，不写成所有 FP8 KV Blackwell random output 的完整修复。
- hardware guard 的结论不能跨 GPU family 外推，尤其是 ROCm gfx950、Blackwell、GB10/GB200/GB300 等低精度路径。`#33179` 显示 PR body 里的硬件格式假设可能反过来是错的；closed/unmerged PR 和 maintainer 反驳应进入 exclude，而非 promotion。

## 仍需补证

- 对 `#38991`，下一轮不再从零开始找“是否存在 buffer-reuse family”，也不再把“是否应该 clone”或“是否应该回退 clone”当成开放问题。这条已经被 `#43163/#43464` 补成上游 accepted correctness fix，`#44430/#44645` 也说明 memory regression 的正确收口是 loader streaming，而不是撤回 `clone()`；但要继续区分“Llama4 已 landed 的 streaming 样例”和“其他模型路径是否也已完成同类收口”。结合当前 main 代码路径，默认加载链上的 alias 已经被切断。现在真正要补的是 exact unified-memory + `BaseModelLoader.load_model()` async copy 场景是否已被 dedicated regression 证明，以及 issue 本体能否获得 direct attribution / maintainer closure。
- 对 `#42120`，合并状态已闭环；下一轮只需继续补 wrong input dtype 的可维护测试，并确认 routed-expert LoRA weights 非零时的 adapter path 也稳定。
- 对 `#42325/#42379` 继续记录 spec 讨论结果：如果未来 CUDA 侧改回 FP32，应同步更新 reference boundary，而不是只看某一侧实现。
- 追踪 AWQ_Marlin 是否未来提供 deterministic fused path；追踪 Cutlass FP8 tuning 和 fused norm 优化是否保持 batch-invariant tests。
- `#42580` 已于 2026-05-21 被作者关闭，原因是 concurrent fix [#42080](https://github.com/vllm-project/vllm/pull/42080) 已于 2026-05-19 合并，为 Triton attention backend 添加了 FP8 per-tensor Q scale 支持。因此 TRITON_ATTN FP8 `k_scale/v_scale` 边界已由 `#42080` 收口，不再单独追踪 `#42580`；`#42650` 的 metadata head-count 修复与 `#42080` 的 FP8 scale 修复仍是两条独立机制，不合并。

## Verification matrices

### Quant / Dtype 最小验证矩阵

| Source | 保护对象 | 最小验证矩阵 | 合格契约 | 不能被什么替代 |
| --- | --- | --- | --- | --- |
| [#42120](https://github.com/vllm-project/vllm/pull/42120) | FP8 W8A8 MoE + LoRA 的 base/adapter activation 生命周期 | active LoRA、无 active LoRA、adapter batch 后 base batch、DP/EP all2all、`original_hidden_states` stash 前后对照、wrong input dtype 单测 | base path 与 adapter path byte-identical；无 stale LoRA mapping 写坏 base batch | 只测 early exit；只测 happy-path adapter；把第三方 Blackwell 验证外推到 routed-expert LoRA |
| [#42325](https://github.com/vllm-project/vllm/issues/42325), [#42379](https://github.com/vllm-project/vllm/pull/42379) | RMSNorm / fused quant RMSNorm 的 multiply dtype 与 reference boundary | regular RMSNorm、fused add RMSNorm、static FP8 quant RMSNorm、non-fused composite path 对照、BF16 weight 场景、TinyLlama/H100 `lm_eval` | native-dtype multiply behavior 与 fused path 对齐；无 `lm_eval` 回归 | 只看 Python IR；只测单一 norm site；把 IR 默认当 CUDA spec |
| [#38991](https://github.com/vllm-project/vllm/issues/38991), [#43163](https://github.com/vllm-project/vllm/issues/43163), [#43464](https://github.com/vllm-project/vllm/pull/43464) | weight loader 的 tensor ownership / buffer lifetime | shared-buffer view source、`param.data.copy_()` async、iterator-side `clone()`、`RUNAI_STREAMER_MEMORY_LIMIT=0` 强制复用、data pointer 不共享断言 | yielded tensor 不共享 backing storage；clone 后数值正确 | 只测数值；不强制 buffer 复用；把 Llama4 streaming 样例外推成所有 loader |
| [#40408](https://github.com/vllm-project/vllm/pull/40408) | Cutlass FP8 scaled-mm 的 batch-invariant fixed-config dispatch | sm89/sm90/sm100/sm120、多 weight shape、`test_cutlass_fp8_batch_invariant_fixed_config`、CUTLASS config independent of `M` | BI mode 下 direct FP8 path 输出稳定，不随 `M` 改变 config | 只测单一 shape；不验证 config 是否依赖 `M`；把当前 tuning 外推到未来 |

