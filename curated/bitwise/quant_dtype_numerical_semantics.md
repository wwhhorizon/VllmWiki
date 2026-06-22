# 量化与 Dtype 数值语义

状态：curated。
父页：[Bitwise 确定性与数值等价](README.md)。
范围：FP8/FP4/NVFP4/MXFP4、scale layout、dtype dispatch、LoRA path、fusion path 和 weight loading lifetime。

## TL;DR

低精度路径中的 bitwise 问题常来自 dtype guard、scale layout、fusion math dtype、MoE tile config、LoRA activation 和 loading buffer lifetime。它们不是普通实现细节，而是数值语义的一部分。merged 修复可以稳定下沉，但 hardware guard、loader lifetime 和 fused fast path 都必须保留适用边界。`#38991` 这类仍缺 direct closure 的项继续留在 [next.md](next.md) 和 candidate note。

## 机制解释

量化和 dtype dispatch 必须保持语义稳定：同一个模型权重、scale layout、backend 和 cache dtype 不应因为硬件 guard、load order、LoRA path 或 fusion path 不同而改变 deterministic 输出。

LoRA + FP8 MoE 展示的是 activation identity：base GEMM 需要量化 activation，LoRA delta 需要原始精度 activation。RMSNorm 展示的是 reference boundary：native dtype、FP32 和 composite path 不能被混写。weight loading lifetime 展示的是 tensor ownership：iterator 复用 backing storage 时，异步 copy 可能读到被改写的数据。

<!-- 稳定证据区禁止出现 open/defer/include_with_boundary；此类对象仅可进入"边界与反例"段或 next.md -->

## 稳定证据

- upstream id: [#33179](https://github.com/vllm-project/vllm/pull/33179)
  - upstream status: closed/unmerged PR
  - claim level: exclude / counterexample
  - direct evidence: maintainer 反驳 gfx950 FP8 Fnuz 前提，说明 Fnuz 只支持 gfx942。
  - mechanism: hardware dtype guard 必须被硬件/maintainer 事实校验。
  - boundary: 这是反例，不进入 dtype 修复链。

- upstream id: [#42120](https://github.com/vllm-project/vllm/pull/42120)
  - upstream status: merged PR
  - claim level: stable
  - direct evidence: PR 同时修 `no_lora_flag_cpu` 早退和 `original_hidden_states` stash，避免 stale LoRA mapping 与 LoRA kernel 错吃量化 activation。
  - mechanism: FP8 MoE + LoRA 需要同时维护 base path、adapter path 和 token mapping 生命周期。
  - boundary: wrong input dtype 和 routed-expert LoRA 权重仍是测试覆盖边界。

- upstream id: [#42325](https://github.com/vllm-project/vllm/issues/42325), [#42379](https://github.com/vllm-project/vllm/pull/42379)
  - upstream status: merged PR
  - claim level: stable
  - direct evidence: regular RMSNorm、fused add RMSNorm、static FP8 quant RMSNorm 等 kernel site 恢复 native-dtype multiply，并跑 core/IR tests 与 `lm_eval`。
  - mechanism: fusion path 必须声明 multiply dtype 和 reference boundary。
  - boundary: 不能把 Python IR 自动当成所有 CUDA kernel 规范。

- upstream id: [#38670](https://github.com/vllm-project/vllm/pull/38670), [#40408](https://github.com/vllm-project/vllm/pull/40408), [#40413](https://github.com/vllm-project/vllm/pull/40413)
  - upstream status: merged PRs
  - claim level: stable family
  - direct evidence: BI mode 下 AWQ_Marlin 被绕开，Cutlass FP8 direct path 通过 fixed-config test，fused add RMSNorm 因已有 BI 证据不再被替换。
  - mechanism: fused/fast kernel 要逐个判断：不可控的绕开，可证明 fixed-config 的保留。
  - boundary: 不外推到所有 fused norm/quant op 或未来 Cutlass tuning。

- upstream id: [#38991](https://github.com/vllm-project/vllm/issues/38991), [#43163](https://github.com/vllm-project/vllm/issues/43163), [#43464](https://github.com/vllm-project/vllm/pull/43464), [#44645](https://github.com/vllm-project/vllm/pull/44645)
  - upstream status: family evidence, partial merged closure
  - claim level: defer with narrowed proof gap
  - direct evidence: `#43464` 在 iterator 边界 clone yielded tensor，并用 forced buffer reuse test 证明不共享 data pointer；`#44645` 用 Llama4 streaming loader 吸收 clone 的 host-RAM 代价。
  - mechanism: iterator-side `clone()` 是 correctness closure，streaming loader 是 memory/perf closure。
  - boundary: `#38991` 本体仍缺 direct linked closure 和 exact unified-memory regression。

## 边界与反例

- hardware guard 结论不能跨 GPU family 外推，尤其是 ROCm gfx950、Blackwell、GB10/GB200/GB300。
- `#36488` 同时属于 batch invariance 和 quant/dtype；不要只在一个页面维护。
- `#42120` 已合并，但不能宣称所有 FP8 MoE + LoRA 变体都完整验证。
- `#38670` 只是让 AWQ 在 BI mode 下回到受控 matmul path，不证明 AWQ_Marlin 本身 deterministic。
- `#42650` 是非均匀 per-layer Q-head metadata fix，不等于所有 FP8 KV Blackwell random output 完整修复。

## Evidence appendix

长证据表、quant/dtype verification matrix 和补证记录见 [evidence_appendix/quant_dtype_numerical_semantics.md](evidence_appendix/quant_dtype_numerical_semantics.md)。
