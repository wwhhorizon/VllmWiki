# vllm-project/vllm#10970: 🤗 Support request for a new model from huggingface: embedding model with rotary embeddings not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#10970](https://github.com/vllm-project/vllm/issues/10970) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> 🤗 Support request for a new model from huggingface: embedding model with rotary embeddings not supported

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ## problem I'm unable to use the `jinaai/jina-embeddings-v3` embedding model with vllm. When run using OpenAI style OpenAIServingEmbedding it throws an error `No CUDA GPUs are available`. I also tried to run it using LLM class and it gives the error described below. Does this mean the model is not yet supported or a different issue? ## code ``` from vllm import LLM # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create an LLM. model = LLM(model="jinaai/jina-embeddings-v3", enforce_eager=True, trust_remote_code=True) # Generate embedding. The output is a list of PoolingRequestOutputs. outputs = model.encode(prompts) # Print the outputs. for output in outputs: print(output.outputs.embedding) # list of 4096 floats ``` ## error ``` WARNING 12-06 23:15:27 config.py:503] To see benefits of async output processing, enable CUDA graph. Since, enforce-eager is enabled, async output processor cannot be used INFO 12-06 23:15:27 llm_engine.py:249] Initializing an LLM engine (v0.6.4.post1) with config: model='j...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 🤗 Support request for a new model from huggingface: embedding model with rotary embeddings not supported bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ## problem I'm unable...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: model is not yet supported or a different issue? ## code ``` from vllm import LLM # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=8194, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 🤗 Support request for a new model from huggingface: embedding model with rotary embeddings not supported bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ## problem I'm unable...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
