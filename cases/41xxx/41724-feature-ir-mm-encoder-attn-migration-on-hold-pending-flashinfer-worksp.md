# vllm-project/vllm#41724: [Feature]: [IR] mm_encoder_attn migration on hold pending FlashInfer workspace support

| 字段 | 值 |
| --- | --- |
| Issue | [#41724](https://github.com/vllm-project/vllm/issues/41724) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [IR] mm_encoder_attn migration on hold pending FlashInfer workspace support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Summary PR #41613 migrates `mm_encoder_attn` to vLLM IR with three pure backends (`flash_attn`, `triton`, `native`) fully working and tested. Said that, as rightly pointed out by @ProExpertProg, the migration should wait until IR workspace support exists so that all backends including FlashInfer dispatch uniformly via `--kernel-config.ir_op_priority.mm_encoder_attn` ### What's done (in #41613) - IR op definition with native semantics - Provider implementations for flash_attn and triton - Per-platform priority lists (CUDA, ROCm, XPU) - `IrOpPriorityConfig.mm_encoder_attn` field - Test suite: 205 passed, 32 skipped across dtypes, batch sizes, sequence lengths, and head configurations - E2E inference verified on all three backends ### What's blocking: FlashInfer as an IR implementation FlashInfer cannot be a pure functional IR implementation today because it requires: * A workspace buffer, a 128MB persistent GPU allocation (`torch.zeros(128*1024*1024, dtype=uint8, device="cuda")`) passed to every call, with no IR mechanism for persistent allocations across calls * FP8 quantization state, including per-instance mutable scale buffers (`_fp8_q...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Feature]: [IR] mm_encoder_attn migration on hold pending FlashInfer workspace support feature request ### 🚀 The feature, motivation and pitch ### Summary PR #41613 migrates `mm_encoder_attn` to vLLM IR with three pure...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: onfig.mm_encoder_attn` field - Test suite: 205 passed, 32 skipped across dtypes, batch sizes, sequence lengths, and head configurations - E2E inference verified on all three backends ### What's blocking: FlashInfer as a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: implementations for flash_attn and triton - Per-platform priority lists (CUDA, ROCm, XPU) - `IrOpPriorityConfig.mm_encoder_attn` field - Test suite: 205 passed, 32 skipped across dtypes, batch sizes, sequence lengths, a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oder_attn migration on hold pending FlashInfer workspace support feature request ### 🚀 The feature, motivation and pitch ### Summary PR #41613 migrates `mm_encoder_attn` to vLLM IR with three pure backends (`flash_attn`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: including per-instance mutable scale buffers (`_fp8_q/k/v_scale`), amax circular history, and dynamic scale recomputation (`_record_amax_and_update_scales`) that mutates on every forward pass The remaining differences a...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
