# vllm-project/vllm#40628: [RFC][vLLM IR]: Batch Invariance Dispatching in vLLM IR

| 字段 | 值 |
| --- | --- |
| Issue | [#40628](https://github.com/vllm-project/vllm/issues/40628) |
| 状态 | open |
| 标签 | rocm;RFC;vllm-ir |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;fp8;kernel;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC][vLLM IR]: Batch Invariance Dispatching in vLLM IR

### Issue 正文摘录

**Related:** #32358 **Status:** Under Discussion **Written with:** Claude ## Summary This RFC discusses how batch invariance should be handled within the vLLM IR dispatching model. Currently toggled via VLLM\_BATCH\_INVARIANT=1 and primarily affecting rms\_norm, the question is: **should vLLM IR own batch-invariant dispatching as a first-class concern, or should it be handled outside the IR?** ## Background The vLLM IR design introduces a unified dispatching and kernel registration mechanism to replace CustomOp. A key motivation for this replacement is that CustomOp dispatching was opaque and hard to reason about. A clear example is that @yewentao256 did not realize that forward\_native (the torch-native implementation) was being used by default in batch-invariant mode (and I didn't know at all what was happening), meaning the batch-invariant triton kernel was not invoked, as it only existed inside forward\_cuda and forward\_hip. Multiple levels of initialization and dispatching made the actual execution path difficult to trace. Under CustomOp, batch invariance for rms\_norm intersects with three execution paths: * forward\_cuda / forward\_hip — dispatching between the standard CU...

## 现有链接修复摘要

#36816 [DO NOT MERGE][vLLM IR] 2/N batch-invariant-aware dispatching and rms_norm | #40408 [Perf] Batch invariance with Cutlass fp8 support, 28.9% E2E latency improvement | #40413 [Perf] Optimize batch invariant with fused rms norm, 2.1% E2E latency improvement

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: [RFC][vLLM IR]: Batch Invariance Dispatching in vLLM IR rocm;RFC;vllm-ir **Related:** #32358 **Status:** Under Discussion **Written with:** Claude ## Summary This RFC discusses how batch invariance should be handled wit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [RFC][vLLM IR]: Batch Invariance Dispatching in vLLM IR rocm;RFC;vllm-ir **Related:** #32358 **Status:** Under Discussion **Written with:** Claude ## Summary This RFC discusses how batch invariance should be handled wit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: open question. --- ## Proposed Alternatives There are basically two decisions embedded in this: * Do we want to dispatch batch-invariant rms\_norm to native torch ops when compiling the model, or just always use the bat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: es how batch invariance should be handled within the vLLM IR dispatching model. Currently toggled via VLLM\_BATCH\_INVARIANT=1 and primarily affecting rms\_norm, the question is: **should vLLM IR own batch-invariant dis...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: VARIANT=1 vllm bench latency --model=RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8 --attention-backend=TRITON_ATTN --ir-op-priority.rms_norm=triton_batch_invariant --ir-op-priority.fused_add_rms_norm=triton_batch_invariant -c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36816](https://github.com/vllm-project/vllm/pull/36816) | mentioned | 0.45 | [DO NOT MERGE][vLLM IR] 2/N batch-invariant-aware dispatching and rms_norm | ir handles batch-invariant dispatching natively _(original plan, [pr \#36816](https://github.com/vllm-project/vllm/pull/36816))_ batch invariance is a first-class property in the… |
| [#40408](https://github.com/vllm-project/vllm/pull/40408) | mentioned | 0.45 | [Perf] Batch invariance with Cutlass fp8 support, 28.9% E2E latency improvement | g triton\_batch\_invariant and native implementations (this is before #40408 & #40413 which close roughly half of that gap). llama was the easiest to demonstrate this on but this… |
| [#40413](https://github.com/vllm-project/vllm/pull/40413) | mentioned | 0.45 | [Perf] Optimize batch invariant with fused rms norm, 2.1% E2E latency improvement | _batch\_invariant and native implementations (this is before #40408 & #40413 which close roughly half of that gap). llama was the easiest to demonstrate this on but this applies t… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
