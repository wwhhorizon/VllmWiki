# vllm-project/vllm#35569: [Bug]: [ROCm] ROCM_ATTN backend shows ~8.5% systematic score deviation on Qwen3-VL-Reranker pooling

| 字段 | 值 |
| --- | --- |
| Issue | [#35569](https://github.com/vllm-project/vllm/issues/35569) |
| 状态 | open |
| 标签 | bug;rocm;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [ROCm] ROCM_ATTN backend shows ~8.5% systematic score deviation on Qwen3-VL-Reranker pooling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The `ROCM_ATTN` attention backend produces a consistent ~8.5% relative deviation from the expected `text_vs_text` score when running `Qwen/Qwen3-VL-Reranker-2B` through the pooling/score API. This deviation is deterministic. It reproduces identically across all test functions and across multiple runs, indicating a systematic numerical offset rather than random variance. Other ROCm backends (`ROCM_AITER_FA`, `TRITON_ATTN`, `FLEX_ATTENTION`) do not exhibit this behaviour and stay within ~2–3% relative diff under the same conditions. ## Reproduction Related to: - https://github.com/vllm-project/vllm/pull/35571 Run `test_online_score_vision.py` with the `ROCM_ATTN` backend on a ROCm platform: ```bash pytest tests/entrypoints/pooling/score/test_online_score_vision.py \ -k "ROCM_ATTN" -s ``` ## Observed results ``` [ROCM_ATTN] text_vs_text: actual=0.108891 expected=0.100404 diff=0.008488 rel_diff=0.0845 ``` This value (0.1089) is stable across all test functions and runs. ## Expected results The score should be close to 0.1004 (the reference value from `FLASH_ATTN` on CUDA), within ~5% relative tolerance, consistent with other ROCm bac...

## 现有链接修复摘要

#39849 [ROCm] route known-bad gfx9 ROCM_ATTN mfma4 shapes to Triton

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: n/Qwen3-VL-Reranker-2B` through the pooling/score API. This deviation is deterministic. It reproduces identically across all test functions and across multiple runs, indicating a systematic numerical offset rather than...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: [ROCm] ROCM_ATTN backend shows ~8.5% systematic score deviation on Qwen3-VL-Reranker pooling bug;rocm;stale ### Your current environment ### 🐛 Describe the bug The `ROCM_ATTN` attention backend produces a consist...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;kernel;operator;sampling;triton build_err...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: [ROCm] ROCM_ATTN backend shows ~8.5% systematic score deviation on Qwen3-VL-Reranker pooling bug;rocm;stale ### Your current environment ### 🐛 Describe the bug The `ROCM_ATTN` attention backend produces a consist...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Bug]: [ROCm] ROCM_ATTN backend shows ~8.5% systematic score deviation on Qwen3-VL-Reranker pooling bug;rocm;stale ### Your current environment ### 🐛 Describe the bug The `ROCM_ATTN` attention backend produces a consiste...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39849](https://github.com/vllm-project/vllm/pull/39849) | mentioned | 0.6 | [ROCm] route known-bad gfx9 ROCM_ATTN mfma4 shapes to Triton | tention path in V1. Two open ROCm issues point at that same path: - `#35569`: deterministic Qwen3-VL reranker score drift on gfx950 (`head_size=128`, `gqa_ratio=2`) - `#36180`: `m… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
