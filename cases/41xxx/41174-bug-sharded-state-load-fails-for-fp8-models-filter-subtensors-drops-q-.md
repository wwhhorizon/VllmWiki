# vllm-project/vllm#41174: [Bug]: `sharded_state` load fails for FP8 models: `_filter_subtensors` drops `q_scale/k_scale/v_scale/prob_scale` parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#41174](https://github.com/vllm-project/vllm/issues/41174) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `sharded_state` load fails for FP8 models: `_filter_subtensors` drops `q_scale/k_scale/v_scale/prob_scale` parameters

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Environment - vLLM v0.19.1 - Model: Qwen/Qwen3.5-397B-A17B-FP8 (FP8 quantized, TP=8) - Platform: 8x H100 ### What happened Saved a sharded checkpoint using the official save_sharded_state.py example. Loading with --load-format sharded_state fails with: ``` ValueError: Missing keys ('language_model.model.layers.3.self_attn.attn.q_scale', 'language_model.model.layers.3.self_attn.attn.k_scale', 'language_model.model.layers.3.self_attn.attn.v_scale', 'language_model.model.layers.3.self_attn.attn.prob_scale', ...) in loaded state! ``` Full error message: ``` (Worker_TP0 pid=1668288) ERROR 04-28 23:13:07 [multiproc_executor.py:857] raise ValueError(f"Missing keys {tuple(state_dict)} in loaded state!") (Worker_TP0 pid=1668288) ERROR 04-28 23:13:07 [multiproc_executor.py:857] ValueError: Missing keys ('language_model.model.layers.3.self_attn.attn.q_scale', 'language_model.model.layers.3.self_attn.attn.k_scale', 'language_model.model.layers.3.self_attn.attn.v_scale', 'language_model.model.layers.3.self_attn.attn.prob_scale', 'language_model.model.layers.7.self_attn.attn.q_scale', 'language_model.model.layers.7.self_attn.attn.k_scale',...

## 现有链接修复摘要

#41179 Fix sharded_state load for FP8 models with aliased scale keys

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 8x H100 ### What happened Saved a sharded checkpoint using the official save_sharded_state.py example. Loading with --load-format sharded_state fails with: ``` ValueError: Missing keys ('language_model.model.layers.3.se...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: `sharded_state` load fails for FP8 models: `_filter_subtensors` drops `q_scale/k_scale/v_scale/prob_scale` parameters bug ### Your current environment ### 🐛 Describe the bug ### Environment - vLLM v0.19.1 - Model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Model: Qwen/Qwen3.5-397B-A17B-FP8 (FP8 quantized, TP=8) - Platform: 8x H100 ### What happened Saved a sharded checkpoint using the official save_sharded_state.py example. Loading with --load-format sharded_state fails w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: `sharded_state` load fails for FP8 models: `_filter_subtensors` drops `q_scale/k_scale/v_scale/prob_scale` parameters bug ### Your current environment ### 🐛 Describe the bug ### Environment - vLLM v0.19.1 - Model...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s;speculative_decoding attention;cuda;fp8;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency #41179 Fix sharded_state load for FP8 models with aliased scale keys Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41179](https://github.com/vllm-project/vllm/pull/41179) | closes_keyword | 0.95 | Fix sharded_state load for FP8 models with aliased scale keys | Fixes #41174 - `_filter_subtensors` deduplicates tensors sharing storage during save (e.g. `_q_scale` buffer and `q_scale` parameter keep only `_q_scale`). On a fresh model at loa |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
