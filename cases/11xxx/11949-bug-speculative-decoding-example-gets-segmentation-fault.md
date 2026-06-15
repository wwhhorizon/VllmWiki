# vllm-project/vllm#11949: [Bug]: Speculative Decoding example gets Segmentation Fault

| 字段 | 值 |
| --- | --- |
| Issue | [#11949](https://github.com/vllm-project/vllm/issues/11949) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative Decoding example gets Segmentation Fault

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to run the speculative decoding example from the docs: https://docs.vllm.ai/en/v0.6.6/usage/spec_decode.html#speculating-with-a-draft-model ```python from vllm import LLM, SamplingParams prompts = [ "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM( model="facebook/opt-6.7b", tensor_parallel_size=1, speculative_model="facebook/opt-125m", num_speculative_tokens=5, ) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Unfortunately, it doesn't seem to work properly. I get `Segmentation fault (core dumped)` without any other information. ``` INFO 01-11 05:31:30 config.py:510] This model supports multiple tasks: {'score', 'embed', 'reward', 'classify', 'generate'}. Defaulting to 'generate'. WARNING 01-11 05:31:30 cuda.py:98] To see benefits of async output processing, enable CUDA graph. Since, enforce-eager is enabled, async output processor cannot be used WARNING 01-11 05:31:30 config.py:64...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Speculative Decoding example gets Segmentation Fault bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to run the speculative decoding example from the docs: h
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: age/spec_decode.html#speculating-with-a-draft-model ```python from vllm import LLM, SamplingParams prompts = [ "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM( model="fac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: example gets Segmentation Fault bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to run the speculative decoding example from the docs: https://docs.vllm.ai/en/v0.6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
