# vllm-project/vllm#17170: [Bug]: HIP error: invalid device function

| 字段 | 值 |
| --- | --- |
| Issue | [#17170](https://github.com/vllm-project/vllm/issues/17170) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: HIP error: invalid device function

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(max_tokens=8192, temperature=0.8, top_p=0.95) if __name__ == "__main__": model_name = "/home/zz/mistralai/mistralhf-gptq/" # Create an LLM. llm = LLM(model=model_name) #quantization="fp8" tensor_parallel_size=4 # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") When running the simple quick start code, the following error was reported: INFO 04-25 08:04:59 [__init__.py:239] Automatically detected platform rocm. INFO 04-25 08:05:18 [config.py:713] This model supports multiple tasks: {'embed', 'classify', 'score', 'generate', 'reward'}. Defaulting to 'generate'. WARNING 04-25 08:05:27 [config.py:792] gptq quant...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: n bug ### Your current environment ### 🐛 Describe the bug from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: HIP error: invalid device function bug ### Your current environment ### 🐛 Describe the bug from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the Unite
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: tokens=8192, temperature=0.8, top_p=0.95) if __name__ == "__main__": model_name = "/home/zz/mistralai/mistralhf-gptq/" # Create an LLM. llm = LLM(model=model_name) #quantization="fp8" tensor_parallel_size=4 # Generate t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: stralai/mistralhf-gptq/" # Create an LLM. llm = LLM(model=model_name) #quantization="fp8" tensor_parallel_size=4 # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
