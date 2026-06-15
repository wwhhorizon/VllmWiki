# vllm-project/vllm#38195: [Bug]: Qwen3.5-dense wfp8afp8 w: per-tensor a: per-tensor Output garbled text, but in sglang is norm

| 字段 | 值 |
| --- | --- |
| Issue | [#38195](https://github.com/vllm-project/vllm/issues/38195) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | activation;cuda;fp8;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-dense wfp8afp8 w: per-tensor a: per-tensor Output garbled text, but in sglang is norm

### Issue 正文摘录

### Your current environment sglang 0.5.9 vllm 0.17.1 transformers: 5.3.0 ### 🐛 Describe the bug ## sglang qwen3.5-dense wfp8afp8 dynamic(a: per-token, w: per-channel) ✅ qwen3.5-dense wfp8afp8 static(a: per-tensor, w: per-tensor)✅ ## vllm qwen3.5-dense wfp8afp8 dynamic(a: per-token, w: per-channel) ✅ qwen3.5-dense wfp8afp8 static(a: per-tensor, w: per-channel)✅ qwen3.5-dense wfp8afp8 static(a: per-tensor, w: per-tensor)❌ Output garbled text **With the same model and FP8 static quantization (per-tensor for both activations and weights), the output is normal in SGLang but garbled in vLLM** ### sglang ### vllm config.json ``` { "architectures": [ "Qwen3_5ForConditionalGeneration" ], "dtype": "bfloat16", "image_token_id": 248056, "model_type": "qwen3_5", "quantization_config": { "config_groups": { "group_0": { "input_activations": { "dynamic": false, "group_size": -1, "num_bits": 8, "strategy": "tensor", "type": "float" }, "output_activations": null, "targets": [ "Linear" ], "weights": { "dynamic": false, "group_size": -1, "num_bits": 8, "strategy": "tensor", "type": "float" } } }, "format": "float-quantized", "ignore": [ "lm_head", "re:.*embed_tokens$", "re:.*conv1d$", "re:.*in_proj_...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Qwen3.5-dense wfp8afp8 w: per-tensor a: per-tensor Output garbled text, but in sglang is norm bug ### Your current environment sglang 0.5.9 vllm 0.17.1 transformers: 5.3.0 ### 🐛 Describe the bug ## sglang qwen3.5...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: "vocab_size": 248320 }, "tie_word_embeddings": true, "transformers_version": "5.3.0", "video_token_id": 248057, "vision_config": { "deepstack_visual_indexes": [], "depth": 12, "dtype": "bfloat16", "hidden_act": "gelu_py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3.5-dense wfp8afp8 w: per-tensor a: per-tensor Output garbled text, but in sglang is norm bug ### Your current environment sglang 0.5.9 vllm 0.17.1 transformers: 5.3.0 ### 🐛 Describe the bug ## sglang qwen3.5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ng but garbled in vLLM** ### sglang ### vllm config.json ``` { "architectures": [ "Qwen3_5ForConditionalGeneration" ], "dtype": "bfloat16", "image_token_id": 248056, "model_type": "qwen3_5", "quantization_config": { "co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ware_porting;model_support;quantization activation;cuda;fp8;quantization;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
