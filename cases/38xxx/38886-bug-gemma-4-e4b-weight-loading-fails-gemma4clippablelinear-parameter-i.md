# vllm-project/vllm#38886: [Bug]: Gemma 4 E4B weight loading fails `Gemma4ClippableLinear` parameter `input_max` not recognized

| 字段 | 值 |
| --- | --- |
| Issue | [#38886](https://github.com/vllm-project/vllm/issues/38886) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 E4B weight loading fails `Gemma4ClippableLinear` parameter `input_max` not recognized

### Issue 正文摘录

### Your current environment PyTorch version : 2.8.0+cu128 vLLM Version : 0.18.0 transformers : 5.4.x (bundled in vllm/vllm-openai:v0.18.0) ### 🐛 Describe the bug When loading `google/gemma-4-e4b-it` on vLLM **v0.18.0**, the model resolves to `TransformersMultiModalForCausalLM` (fallback path, no native Gemma 4 implementation) and fails during weight loading with a `ValueError` on the audio tower's `Gemma4ClippableLinear` layer. The `input_max` parameter in the checkpoint is not recognized by the fallback weight mapper because `Gemma4ClippableLinear` wraps a standard `Linear` layer with an extra `input_max` buffer that the generic loader does not expect. ``` (EngineCore pid=322) INFO 04-03 03:39:22 [base.py:115] Using Transformers modeling backend. (EngineCore pid=322) WARNING 04-03 03:38:21 [utils.py:187] TransformersMultiModalForCausalLM has no vLLM implementation, falling back to Transformers implementation. (EngineCore pid=322) ValueError: There is no module or parameter named 'model.audio_tower.layers.0.feed_forward1.ffw_layer_1.input_max' in TransformersMultiModalForCausalLM. The available parameters belonging to model.audio_tower.layers.0.feed_forward1.ffw_layer_1 (Gemma4Cl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma 4 E4B weight loading fails `Gemma4ClippableLinear` parameter `input_max` not recognized bug ### Your current environment PyTorch version : 2.8.0+cu128 vLLM Version : 0.18.0 transformer
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: **v0.18.0**, the model resolves to `TransformersMultiModalForCausalLM` (fallback path, no native Gemma 4 implementation) and fails during weight loading with a `ValueError` on the audio tower's `Gemma4ClippableLinear` l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e/gemma-4-e4b-it` on vLLM **v0.18.0**, the model resolves to `TransformersMultiModalForCausalLM` (fallback path, no native Gemma 4 implementation) and fails during weight loading with a `ValueError` on the audio tower's...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ter `input_max` not recognized bug ### Your current environment PyTorch version : 2.8.0+cu128 vLLM Version : 0.18.0 transformers : 5.4.x (bundled in vllm/vllm-openai:v0.18.0) ### 🐛 Describe the bug When loading `google/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma 4 E4B weight loading fails `Gemma4ClippableLinear` parameter `input_max` not recognized bug ### Your current environment PyTorch version : 2.8.0+cu128 vLLM Version : 0.18.0 transformer

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
