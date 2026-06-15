# vllm-project/vllm#39061: [Bug]: Gemma4 vision encoder crashes with ValueError: Expected hidden_size to be 5376, but found: 72

| 字段 | 值 |
| --- | --- |
| Issue | [#39061](https://github.com/vllm-project/vllm/issues/39061) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | activation;cuda |
| 症状 | crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4 vision encoder crashes with ValueError: Expected hidden_size to be 5376, but found: 72

### Issue 正文摘录

## Your current environment - **vLLM version**: main (commit approx. 2025-04-05) - **Model**: `google/gemma-4-27b-it` (or any Gemma4 multimodal model) - **Python**: 3.12 - **CUDA**: 13.x - **Transformers**: installed via pip in `.vllm` venv ## 🐛 Describe the bug Starting vLLM with a Gemma4 multimodal model (e.g. `google/gemma-4-27b-it`) fails during engine core initialization with: ``` ValueError: Expected hidden_size to be 5376, but found: 72 ``` Full traceback (abbreviated): ``` File ".../vllm/v1/worker/gpu_model_runner.py", line 5761, in profile_run dummy_encoder_outputs = self.model.embed_multimodal(...) File ".../vllm/model_executor/models/transformers/multimodal.py", line 350, in embed_multimodal vision_embeddings = self.model.get_image_features(...) File ".../transformers/models/gemma4/modeling_gemma4.py", line 905, in forward value_states = self.v_norm(value_states) File ".../vllm/model_executor/layers/layernorm.py", line 241, in forward_static raise ValueError( ValueError: Expected hidden_size to be 5376, but found: 72 ``` ## Root Cause When vLLM's `TransformersModelBase._recursive_replace` walks the model graph and replaces norm modules, it calls: ```python # base.py:442...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma4 vision encoder crashes with ValueError: Expected hidden_size to be 5376, but found: 72 ## Your current environment - **vLLM version**: main (commit approx. 2025-04-05) - **Model**: `google/gemma-4-27b-it`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: den_size to be 5376, but found: 72 ## Your current environment - **vLLM version**: main (commit approx. 2025-04-05) - **Model**: `google/gemma-4-27b-it` (or any Gemma4 multimodal model) - **Python**: 3.12 - **CUDA**: 13...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /gemma-4-27b-it` (or any Gemma4 multimodal model) - **Python**: 3.12 - **CUDA**: 13.x - **Transformers**: installed via pip in `.vllm` venv ## 🐛 Describe the bug Starting vLLM with a Gemma4 multimodal model (e.g. `googl...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: se` does not store `dim` as an attribute. Fix 1 is necessary. ## How to Reproduce ```bash vllm serve google/gemma-4-27b-it --trust-remote-code ``` Engine crashes before serving any requests. ## Expected behavior Engine...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: `` Gemma4's vision encoder `v_norm` is `Gemma4RMSNorm(head_dim=72, with_scale=False)`. With `with_scale=False`, no `weight` is registered, so `hidden_size` stays at 5376. The resulting `RMSNorm(hidden_size=5376, has_wei...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
