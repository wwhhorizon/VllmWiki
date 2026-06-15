# vllm-project/vllm#43304: [Bug] DSV4 MTP draft model inherits main quantization scheme; can't load artifacts with BF16 MTP block

| 字段 | 值 |
| --- | --- |
| Issue | [#43304](https://github.com/vllm-project/vllm/issues/43304) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;moe;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;fp8;moe;quantization |
| 症状 | crash;mismatch |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] DSV4 MTP draft model inherits main quantization scheme; can't load artifacts with BF16 MTP block

### Issue 正文摘录

## Summary When serving a DSV4-class quantized artifact with `--speculative-config '{"method":"mtp","num_speculative_tokens":N}'`, vLLM constructs the MTP draft model (`DeepSeekV4MTP` / `DeepseekV4MTPModel` / `DeepSeekV4MultiTokenPredictorLayer`) by passing the SAME `vllm_config` as the main model — including its `quant_config`. That means the MTP block's `DeepseekV4DecoderLayer` constructs its `DSV4MoE` FFN and `DSV4Attention` with the main model's quantization scheme. For artifacts whose MTP block was intentionally left unquantized on disk — a common pattern because of `vllm-project/llm-compressor#2745` (the `Inplace update to inference tensor` crash that fires at MTP qparam writeback during calibration) — the resulting mismatch between the draft model's expected parameter names (`w13_weight_packed`, `weight_scale_inv`, etc.) and the on-disk parameter names (`w1.weight`, `w2.weight`, no scales) means weight load fails with `KeyError` or the attention forward fails with `AttributeError: ColumnParallelLinear has no attribute weight_scale`. ## Reproducer Take any DSV4 artifact whose calibration recipe excluded MTP modules — e.g. an `llm-compressor` recipe with `ignore=[..., r"re:.*...

## 现有链接修复摘要

#43290 [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | #43319 [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug] DSV4 MTP draft model inherits main quantization scheme; can't load artifacts with BF16 MTP block ## Summary When serving a DSV4-class quantized artifact with `--speculative-config '{"method":"mtp","num_speculative...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug] DSV4 MTP draft model inherits main quantization scheme; can't load artifacts with BF16 MTP block ## Summary When serving a DSV4-class quantized artifact with `--speculative-config '{"method":"mtp","num_speculative...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug] DSV4 MTP draft model inherits main quantization scheme; can't load artifacts with BF16 MTP block ## Summary When serving a DSV4-class quantized artifact with `--speculative-config '{"method":"mtp","num_speculative...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: h that fires at MTP qparam writeback during calibration) — the resulting mismatch between the draft model's expected parameter names (`w13_weight_packed`, `weight_scale_inv`, etc.) and the on-disk parameter names (`w1.w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: that fires at MTP qparam writeback during calibration) — the resulting mismatch between the draft model's expected parameter names (`w13_weight_packed`, `weight_scale_inv`, etc.) and the on-disk parameter names (`w1.wei...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43290](https://github.com/vllm-project/vllm/pull/43290) | mentioned | 0.45 | [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | ressor#2745` — the upstream cause that forces mtp exclusion - vllm pr #43290 (this org) — `weight_scale_inv`/`weight_scale` fallback at attention.py:334; partial unblock for the a… |
| [#43319](https://github.com/vllm-project/vllm/pull/43319) | closes_keyword | 0.95 | [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config | fix for the AttributeError variant when wo_a has no scale_inv but has scale - vLLM issue #43304 — this PR addresses fix option (1) - vLLM PRs #43248, #43288 (this org) — same code- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
