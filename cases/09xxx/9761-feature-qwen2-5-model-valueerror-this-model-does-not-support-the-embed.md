# vllm-project/vllm#9761: [Feature]: Qwen2.5 model :  ValueError: This model does not support the 'embedding' task. Supported tasks: {'generate'}

| 字段 | 值 |
| --- | --- |
| Issue | [#9761](https://github.com/vllm-project/vllm/issues/9761) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen2.5 model :  ValueError: This model does not support the 'embedding' task. Supported tasks: {'generate'}

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Using Qwen2.5 model : ValueError: This model does not support the 'embedding' task. Supported tasks: {'generate'} reproduction : `python -m vllm.entrypoints.openai.api_server --served-model-name Qwen2.5-1.5B-Instruct --model Qwen/Qwen2.5-1.5B-Instruct --max_model_len 17000 --dtype float16 --trust_remote_code --host 127.0.0.1 --port 8080 --uvicorn-log-level debug --api-key gUaq3eYuYZjuBfejwH-lVrFAlTbi9g3vQnRZD4jBCYA --task "embedding"` Qwen2.5 model is recognized as "Qwen2ForCausalLM": ("qwen2", "Qwen2ForCausalLM") Qwen2Config { "_name_or_path": "Qwen/Qwen2.5-1.5B-Instruct", "architectures": [ "Qwen2ForCausalLM" ], but in the Embedding model section it is not registred. in config file : vllm/vllm/model_executor/models/registry.py __EMBEDDING_MODELS = { # [Text-only] "BertModel": ("bert", "BertEmbeddingModel"), "Gemma2Model": ("gemma2", "Gemma2EmbeddingModel"), "MistralModel": ("llama", "LlamaEmbeddingModel"), "Qwen2ForRewardModel": ("qwen2_rm", "Qwen2ForRewardModel"), "Qwen2ForSequenceClassification": ( "qwen2_cls", "Qwen2ForSequenceClassification"), # [Multimodal] "LlavaNextForConditionalGeneration": ("llava_next", "LlavaNextForConditionalGe...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Feature]: Qwen2.5 model : ValueError: This model does not support the 'embedding' task. Supported tasks: {'generate'} feature request ### 🚀 The feature, motivation and pitch Using Qwen2.5 model : ValueError: This model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 1.5B-Instruct --model Qwen/Qwen2.5-1.5B-Instruct --max_model_len 17000 --dtype float16 --trust_remote_code --host 127.0.0.1 --port 8080 --uvicorn-log-level debug --api-key gUaq3eYuYZjuBfejwH-lVrFAlTbi9g3vQnRZD4jBCYA --t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: LM") Qwen2Config { "_name_or_path": "Qwen/Qwen2.5-1.5B-Instruct", "architectures": [ "Qwen2ForCausalLM" ], but in the Embedding model section it is not registred. in config file : vllm/vllm/model_executor/models/registr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: # [Text-only] "BertModel": ("bert", "BertEmbeddingModel"), "Gemma2Model": ("gemma2", "Gemma2EmbeddingModel"), "MistralModel": ("llama", "LlamaEmbeddingModel"), "Qwen2ForRewardModel": ("qwen2_rm", "Qwen2ForRewardModel"),...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: not support the 'embedding' task. Supported tasks: {'generate'} feature request ### 🚀 The feature, motivation and pitch Using Qwen2.5 model : ValueError: This model does not support the 'embedding' task. Supported tasks...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
