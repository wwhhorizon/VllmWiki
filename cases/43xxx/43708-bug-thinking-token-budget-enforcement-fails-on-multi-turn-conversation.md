# vllm-project/vllm#43708: [Bug]: `thinking_token_budget` enforcement fails on multi-turn conversations when `max_completion_tokens` >> `thinking_token_budget` with ignore_eos:true

| 字段 | 值 |
| --- | --- |
| Issue | [#43708](https://github.com/vllm-project/vllm/issues/43708) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | cold_start |
| Operator 关键词 | fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `thinking_token_budget` enforcement fails on multi-turn conversations when `max_completion_tokens` >> `thinking_token_budget` with ignore_eos:true

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description When using Qwen3.5-27B-FP8 with `--reasoning-parser qwen3` in vLLM 0.21.0, the `thinking_token_budget` parameter is not enforced on turns where the gap between `max_completion_tokens` and `thinking_token_budget` is large (1000+ tokens). On those turns, the model produces a `None` content response with `finish_reason=length`, and the returned `completion_tokens` equals the `max_completion_tokens` limit Configure turn parameters as follows: - **Turn 0**: `max_completion_tokens=900`, `thinking_token_budget=800` (gap: 100) - **Turn 1**: `max_completion_tokens=1800`, `thinking_token_budget=800` (gap: 1000) - **Turn 2**: `max_completion_tokens=2800`, `thinking_token_budget=800` (gap: 2000) ## Environment - **vLLM version**: 0.21.0 - **Model**: Qwen3.5-27B-FP8 (quantized) - **Deployment**: Kubernetes with KServe (ClusterServingRuntime + InferenceService) - **GPU**: 1 * RTX 6000 PRO - **Other server args**: - `--enable-prefix-caching True` --reasoning-parser qwen3 --reasoning-config ReasoningConfig(reasoning_start_str=' ', reasoning_end_str='think quota done! ') ## Steps to Reproduce 1. Deploy Qwen3.5-27B-FP8 on vLLM 0.21....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: urrent environment ### 🐛 Describe the bug ## Description When using Qwen3.5-27B-FP8 with `--reasoning-parser qwen3` in vLLM 0.21.0, the `thinking_token_budget` parameter is not enforced on turns where the gap between `m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: =2800`, `thinking_token_budget=800` (gap: 2000) ## Environment - **vLLM version**: 0.21.0 - **Model**: Qwen3.5-27B-FP8 (quantized) - **Deployment**: Kubernetes with KServe (ClusterServingRuntime + InferenceService) - **...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: onment ### 🐛 Describe the bug ## Description When using Qwen3.5-27B-FP8 with `--reasoning-parser qwen3` in vLLM 0.21.0, the `thinking_token_budget` parameter is not enforced on turns where the gap between `max_completio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: .0 with the reasoning config above (pod logs attached) 2. Run multi-turn benchmark (aiperf 0.8.0) with 50 concurrent conversations × 3 turns per conversation 2.1 Install aiperf 0.8.0 2.2 rename the attached call_center_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es with KServe (ClusterServingRuntime + InferenceService) - **GPU**: 1 * RTX 6000 PRO - **Other server args**: - `--enable-prefix-caching True` --reasoning-parser qwen3 --reasoning-config ReasoningConfig(reasoning_start...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
