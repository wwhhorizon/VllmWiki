# vllm-project/vllm#43457: [deepseek_v4 / DeepGEMM] paged_mqa_logits kernel asserts on next_n=3 → num_speculative_tokens capped at 1 on Hopper

| 字段 | 值 |
| --- | --- |
| Issue | [#43457](https://github.com/vllm-project/vllm/issues/43457) |
| 状态 | open |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention;fp8;kernel;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [deepseek_v4 / DeepGEMM] paged_mqa_logits kernel asserts on next_n=3 → num_speculative_tokens capped at 1 on Hopper

### Issue 正文摘录

## Summary `vllm serve --speculative-config '{"method":"mtp","num_speculative_tokens":2}'` crashes during `profile_cudagraph_memory` on Hopper (H200, sm_90a) with: ``` RuntimeError: Worker failed with error 'Assertion error (/home/ubuntu/src/vllm/.deps/deepgemm-src/csrc/apis/../jit_kernels/impls/smxx_fp8_fp4_paged_mqa_logits.hpp:233): next_n == 1 or next_n == 2' ``` vLLM passes `next_n = num_speculative_tokens + 1` into DeepGemm's `smxx_fp8_fp4_paged_mqa_logits` kernel (k draft + 1 main verifier in the lookahead window). The assertion enforces `num_speculative_tokens 1` is set AND the model uses the paged_mqa_logits kernel path on Hopper, emit a clear error at startup rather than letting the cudagraph capture fail with a confusing assertion message. Option 2 is the cheaper path for vLLM-side. Option 1 unlocks the actual speedup. ## Tracking Filed by the canada-quant team during W4A16+FP8+MTP quantization work. See [`FINDINGS_FOR_SIBLING.md`](https://github.com/canada-quant/dsv4-flash-w4a16-fp8-mtp/blob/main/FINDINGS_FOR_SIBLING.md) §C15 for the full diagnosis. The sibling artifact (B300, NVFP4) is on `arch_major == 10` paths and may hit different assertions; happy to coordinate if...

## 现有链接修复摘要

#43248 [Bugfix][compressed-tensors] Wrap `is_static_input_scheme` with `bool()` for `input_quant=None` schemes | #43288 [Bugfix][DSV4] Default scale_fmt to "ue8m0" instead of hard-subscript | #43290 [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | #43319 [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: e/ubuntu/src/vllm/.deps/deepgemm-src/csrc/apis/../jit_kernels/impls/smxx_fp8_fp4_paged_mqa_logits.hpp:233): next_n == 1 or next_n == 2' ``` vLLM passes `next_n = num_speculative_tokens + 1` into DeepGemm's `smxx_fp8_fp4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ogits kernel asserts on next_n=3 → num_speculative_tokens capped at 1 on Hopper ## Summary `vllm serve --speculative-config '{"method":"mtp","num_speculative_tokens":2}'` crashes during `profile_cudagraph_memory` on Hop...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: o coordinate if there's a cross-arch fix. performance attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;fp8;kernel;quantization b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ative_tokens capped at 1 on Hopper ## Summary `vllm serve --speculative-config '{"method":"mtp","num_speculative_tokens":2}'` crashes during `profile_cudagraph_memory` on Hopper (H200, sm_90a) with: ``` RuntimeError: Wo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eepseek_v4 / DeepGEMM] paged_mqa_logits kernel asserts on next_n=3 → num_speculative_tokens capped at 1 on Hopper ## Summary `vllm serve --speculative-config '{"method":"mtp","num_speculative_tokens":2}'` crashes during...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43248](https://github.com/vllm-project/vllm/pull/43248) | mentioned | 0.45 | [Bugfix][compressed-tensors] Wrap `is_static_input_scheme` with `bool()` for `input_quant=None` schemes | cible on - vllm `~/src/vllm` head `50d9dd902` with cherry-picked prs #43248+#43288+#43290+#43319 - h200 sxm5 (hopper, sm_90a), tp=2 - dsv4-flash w4a16+fp8+mtp artifact (`canada-qu… |
| [#43288](https://github.com/vllm-project/vllm/pull/43288) | mentioned | 0.45 | [Bugfix][DSV4] Default scale_fmt to "ue8m0" instead of hard-subscript | n - vllm `~/src/vllm` head `50d9dd902` with cherry-picked prs #43248+#43288+#43290+#43319 - h200 sxm5 (hopper, sm_90a), tp=2 - dsv4-flash w4a16+fp8+mtp artifact (`canada-quant/dee… |
| [#43290](https://github.com/vllm-project/vllm/pull/43290) | mentioned | 0.45 | [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | lm `~/src/vllm` head `50d9dd902` with cherry-picked prs #43248+#43288+#43290+#43319 - h200 sxm5 (hopper, sm_90a), tp=2 - dsv4-flash w4a16+fp8+mtp artifact (`canada-quant/deepseek-… |
| [#43319](https://github.com/vllm-project/vllm/pull/43319) | mentioned | 0.45 | [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config | rc/vllm` head `50d9dd902` with cherry-picked prs #43248+#43288+#43290+#43319 - h200 sxm5 (hopper, sm_90a), tp=2 - dsv4-flash w4a16+fp8+mtp artifact (`canada-quant/deepseek-v4-flas… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
