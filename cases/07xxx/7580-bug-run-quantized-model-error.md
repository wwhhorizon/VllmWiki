# vllm-project/vllm#7580: [Bug]: run quantized model error

| 字段 | 值 |
| --- | --- |
| Issue | [#7580](https://github.com/vllm-project/vllm/issues/7580) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: run quantized model error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug my codes: ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="/home/sky/.xinference/cache/internlm2_5-7b-chat-4bit",trust_remote_code=True,max_model_len=2048) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` and i got this error: ``` python test.py INFO 08-16 13:29:04 awq_marlin.py:89] The model is convertible to awq_marlin during runtime. Using awq_marlin kernel. INFO 08-16 13:29:04 llm_engine.py:174] Initializing an LLM engine (v0.5.4) with config: model='/home/sky/.xinference/cache/internlm2_5-7b-chat-4bit', speculative_config=None, tokenizer='/home/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment ### 🐛 Describe the bug my codes: ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: run quantized model error bug;stale ### Your current environment ### 🐛 Describe the bug my codes: ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: run quantized model error bug;stale ### Your current environment ### 🐛 Describe the bug my codes: ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of th
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: run quantized model error bug;stale ### Your current environment ### 🐛 Describe the bug my codes: ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None), seed=0, served_model_name=/home/sky/.xinference/cache/in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
