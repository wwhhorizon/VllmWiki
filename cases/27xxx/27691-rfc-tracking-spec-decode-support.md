# vllm-project/vllm#27691: [RFC]: Tracking Spec Decode Support

| 字段 | 值 |
| --- | --- |
| Issue | [#27691](https://github.com/vllm-project/vllm/issues/27691) |
| 状态 | open |
| 标签 | RFC;speculative-decoding |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;moe;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;fp8;kernel;moe |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Tracking Spec Decode Support

### Issue 正文摘录

### Motivation. I've started to try to understand how spec decode composes with other features. Each row represents one combination, and the status column indicates whether this combination runs without issues. This issue will track the status for now. | Model | Hardware | Spec Decode | TP Size | DP Size | EP Enabled? | CUDA Graph Mode | DCP Size | DBO Enabled? | KV Cache DType | Attn Backend | Runs? | GSM8K Score | Notes | | ---------- | -------- | ----------- | ------- | ------- | ----------- | -------------------- | -------- | ------------ | -------------- | ----------------- | ----- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | L3-8B | H100 | - | 1 | 1 | N | `FULL_AND_PIECEWISE` | 1 | N | `auto` | `FLASH_ATTN` | ✅ | 0.64 | | | L3-8B | H100 | EAGLE | 1 | 1 | N | `FULL_AND_PIECEWISE` | 1 | N | `auto` | `FLASH_ATTN` | ✅ | 0.65 | | | L3-8B | H100 | EAGLE | 2 | 1 | N | `FULL_AND_PIECEWISE` | 1 | N | `auto` | `FLASH_ATTN` | ✅ | 0.65 | | | L3-8B | H100 | - | 2 | 1 | N | `FULL_AND_PIECEWISE` | 1 | N | `auto` | `TRITON_ATTN` | ✅ | 0.64 | | | L3...

## 现有链接修复摘要

#27837 [Spec Decode] Fix spec decode + DP bug

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Model | Hardware | Spec Decode | TP Size | DP Size | EP Enabled? | CUDA Graph Mode | DCP Size | DBO Enabled? | KV Cache DType | Attn Backend | Runs? | GSM8K Score | Notes
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [RFC]: Tracking Spec Decode Support RFC;speculative-decoding ### Motivation. I've started to try to understand how spec decode composes with other features. Each row represents one combination, and the status column ind...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: | CUDA Graph Mode | DCP Size | DBO Enabled? | KV Cache DType | Attn Backend | Runs? | GSM8K Score | Notes | | ---------
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ing benchmark (10 prompts works, 1000 fails) (memory leak?) Also hits `recompile_limit reached with fullgraph=True` GSM8K with 32 concurrent requests works | | L3-8B | H100 | - | 1 | 2 | N | `FULL_AND_PIECEWISE` | 1 | N...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: EP Enabled? | CUDA Graph Mode | DCP Size | DBO Enabled? | KV Cache DType | Attn Backend | Runs? | GSM8K Score | Notes

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27837](https://github.com/vllm-project/vllm/pull/27837) | closes_keyword | 0.95 | [Spec Decode] Fix spec decode + DP bug | Fix spec decode + DP bug ## Purpose Spec decode + DP is currently broken because `coordinate_batch_across_dp` causes a hang for the drafter (see #27691). This PR addresses this as |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
