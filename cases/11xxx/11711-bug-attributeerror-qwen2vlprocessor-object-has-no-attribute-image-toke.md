# vllm-project/vllm#11711: [Bug]: AttributeError: 'Qwen2VLProcessor' object has no attribute 'image_token'

| 字段 | 值 |
| --- | --- |
| Issue | [#11711](https://github.com/vllm-project/vllm/issues/11711) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Qwen2VLProcessor' object has no attribute 'image_token'

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams from transformers import AutoProcessor if __name__ == '__main__': model = "hf_cache/Qwen2-VL-7B-Instruct" processor = AutoProcessor.from_pretrained(model) messages = [ {"role": "system", "content": "你是一个有用的助手。"}, { "role": "user", "content": [ { "type": "image_url", "image_url": { "url": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png" }, }, {"type": "text", "text": "插图中的文本是什么？"}, ], }, ] prompt = processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model) outputs = llm.generate(prompt, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` I used VLLM to load qwen2-vl-7b for inference, and it can return results normally in VLLM==0.6.3. Post1 version, but this version cannot support qwen2-vl's Lora adapter. Therefore, I upgraded VLLM version to VLLM==0.6.6. Post1. In this version, the model infere...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Model Input Dumps _No response_ ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams from transformers import AutoProcessor if __name__ == '__main__': model = "hf_cache/Qwen2-VL-7B-Instruct" processor = AutoP...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: AttributeError: 'Qwen2VLProcessor' object has no attribute 'image_token' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams from t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: pt = processor.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model) outputs = llm.generate(prompt, sampling_params)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
