# vllm-project/vllm#41430: fused_add_rms_norm does not branch on has_weight=False (TODO(luka)); FlashNorm weightless RMSNorm cannot realize a speedup on the GPU path

| 字段 | 值 |
| --- | --- |
| Issue | [#41430](https://github.com/vllm-project/vllm/issues/41430) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | activation;attention;cuda;kernel;operator |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> fused_add_rms_norm does not branch on has_weight=False (TODO(luka)); FlashNorm weightless RMSNorm cannot realize a speedup on the GPU path

### Issue 正文摘录

## Summary `vllm/model_executor/layers/layernorm.py` already supports `RMSNorm(..., has_weight=False)` (added in [#40117](https://github.com/vllm-project/vllm/pull/40117) for the Gemma-4 KV-shared `k_norm`). When `has_weight=False` is set, `RMSNorm.weight` becomes a buffer of ones (not a registered Parameter) and `forward_native` correctly passes `weight=None` into `vllm.ir.ops.rms_norm`, which has the `if weight is not None: x *= weight` branch and skips the per-channel multiply. However, the **fused CUDA kernel** path used by `forward_cuda` (`vllm._custom_ops.fused_add_rms_norm` and `rms_norm`) does not branch on `has_weight=False`. It always multiplies by the weight tensor, even when that tensor is the buffer of ones. The mathematics are preserved (multiply by ones is a no-op) but the kernel work is identical to the weighted case, so any speedup expected from `has_weight=False` is not realized on the GPU path. An adjacent `TODO(luka)` marker at `vllm/model_executor/layers/layernorm.py:240` (inside `forward_native`, where weight=None is already passed correctly) acknowledges the broader weight=None passing inconsistency. The actual shim that prevents a speedup on CUDA today is i...

## 现有链接修复摘要

#22486 [Transform] [Quantization] Add transforms to compressed tensors | #44109 [Kernel] Add weightless RMSNorm CUDA kernels for has_weight=False (#41430)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: tless RMSNorm cannot realize a speedup on the GPU path ## Summary `vllm/model_executor/layers/layernorm.py` already supports `RMSNorm(..., has_weight=False)` (added in [#40117](https://github.com/vllm-project/vllm/pull/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: weight` branch and skips the per-channel multiply. However, the **fused CUDA kernel** path used by `forward_cuda` (`vllm._custom_ops.fused_add_rms_norm` and `rms_norm`) does not branch on `has_weight=False`. It always m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ch this issue asks vLLM to implement): - Hardware: NVIDIA A100 (40 GB), bf16, 256-token greedy decode, 20 trials with 3 warmup, eager attention. - Same model class as is typically deployed via vLLM (`Llama-3.2-1B-Instru...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: fused_add_rms_norm does not branch on has_weight=False (TODO(luka)); FlashNorm weightless RMSNorm cannot realize a speedup on the GPU path ## Summary `vllm/model_executor/layers/layernorm.py` already supports `RMSNorm(....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: to implement): - Hardware: NVIDIA A100 (40 GB), bf16, 256-token greedy decode, 20 trials with 3 warmup, eager attention. - Same model class as is typically deployed via vLLM (`Llama-3.2-1B-Instruct`, `open-machine/Llama...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#22486](https://github.com/vllm-project/vllm/pull/22486) | mentioned | 0.45 | [Transform] [Quantization] Add transforms to compressed tensors | ght: optional[tensor]` as the signaling mechanism). - llama.cpp issue #22486 (`feature request: support weightless rmsnorm for flashnorm weight folding trick`): the equivalent ask… |
| [#44109](https://github.com/vllm-project/vllm/pull/44109) | closes_keyword | 0.95 | [Kernel] Add weightless RMSNorm CUDA kernels for has_weight=False (#41430) | fixes GPU-path gap in [#41430](https://github.com/vllm-project/vllm/issues/41430) for `RMSNorm(has_weight=False)` / FlashNorm-folded checkpoints. - [x] The test plan — pytest comm |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
