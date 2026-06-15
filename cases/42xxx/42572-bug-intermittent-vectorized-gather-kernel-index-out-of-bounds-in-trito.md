# vllm-project/vllm#42572: [Bug]: Intermittent `vectorized_gather_kernel index out of bounds` in `triton_reshape_and_cache_flash` (KV-cache update) during Gemma 4 31B + MTP K=3 inference — both FP8-block and NVFP4

| 字段 | 值 |
| --- | --- |
| Issue | [#42572](https://github.com/vllm-project/vllm/issues/42572) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Intermittent `vectorized_gather_kernel index out of bounds` in `triton_reshape_and_cache_flash` (KV-cache update) during Gemma 4 31B + MTP K=3 inference — both FP8-block and NVFP4

### Issue 正文摘录

### Your current environment Below I've described the result from the B300 node, I'm currently testing on. But I've seen the same error on H100 and H200 nodes as well. ### 🐛 Describe the bug ## Summary Running Gemma 4 31B (both `RedHatAI/gemma-4-31B-it-FP8-block` and `nvidia/Gemma-4-31B-IT-NVFP4`) with **MTP speculative decoding (K=3)** and **single-image multimodal inputs** in vLLM V1 on B300 (Blackwell, sm_103) intermittently crashes mid-inference with a PyTorch `vectorized_gather_kernel index out of bounds` device-side assertion. The crash surfaces inside `unified_kv_cache_update` → `triton_reshape_and_cache_flash` (i.e. in the KV cache *write* path, not the spec-decode dispatch itself), suggesting the scheduler/spec-decode layer is producing a slot mapping that contains an out-of-range block index for the new K/V tokens. Observed crash rate across our recent sweeps: **5 out of ~60 captioner runs (~8%)**, distributed across different cells / GPUs / quantizations / image batches — strongly looks like a non-deterministic edge case, not a config-specific failure. This appears to be the same family as the closed [#28785](https://github.com/vllm-project/vllm/issues/28785) (Qwen3-VL...

## 现有链接修复摘要

#42638 [Bugfix][Spec Decode][CPU] Fix expand_batch_to_tokens on CPU

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: e_flash` (KV-cache update) during Gemma 4 31B + MTP K=3 inference — both FP8-block and NVFP4 bug ### Your current environment Below I've described the result from the B300 node, I'm currently testing on. But I've seen t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: of bounds` in `triton_reshape_and_cache_flash` (KV-cache update) during Gemma 4 31B + MTP K=3 inference — both FP8-block and NVFP4 bug ### Your current environment Below I've described the result from the B300 node, I'm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: /gemma-4-31B-it-FP8-block` and `nvidia/Gemma-4-31B-IT-NVFP4`) with **MTP speculative decoding (K=3)** and **single-image multimodal inputs** in vLLM V1 on B300 (Blackwell, sm_103) intermittently crashes mid-inference wi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: ent cells / GPUs / quantizations / image batches — strongly looks like a non-deterministic edge case, not a config-specific failure. This appears to be the same family as the closed [#28785](https://github.com/vllm-proj...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ode dispatch itself), suggesting the scheduler/spec-decode layer is producing a slot mapping that contains an out-of-range block index for the new K/V tokens. Observed crash rate across our recent sweeps: **5 out of ~60...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42638](https://github.com/vllm-project/vllm/pull/42638) | mentioned | 0.6 | [Bugfix][Spec Decode][CPU] Fix expand_batch_to_tokens on CPU | on-greedy request *after* warmup succeeds. - **Related open issue**: [#42572](https://github.com/vllm-project/vllm/issues/42572) reports a similar "index out of bounds" symptom on… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
