# vllm-project/vllm#22783: [Bug]: Can't run Qwen3-32B NVFP4 model

| 字段 | 值 |
| --- | --- |
| Issue | [#22783](https://github.com/vllm-project/vllm/issues/22783) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't run Qwen3-32B NVFP4 model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_id = "RedHatAI/Qwen3-32B-NVFP4" sampling_params = SamplingParams(temperature=0.6, top_p=0.9, max_tokens=256) tokenizer = AutoTokenizer.from_pretrained(model_id) messages = [ {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"}, {"role": "user", "content": "Who are you?"}, ] prompts = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False) llm = LLM(model=model_id, enforce_eager=True) outputs = llm.generate(prompts, sampling_params) generated_text = outputs[0].outputs[0].text print(generated_text) ``` Output: ``` INFO 08-12 22:05:53 [utils.py:326] non-default args: {'model': 'RedHatAI/Qwen3-32B-NVFP4', 'disable_log_stats': True, 'enforce_eager': True} INFO 08-12 22:05:54 [__init__.py:702] Resolved architecture: Qwen3ForCausalLM INFO 08-12 22:05:54 [__init__.py:1739] Using max model len 40960 INFO 08-12 22:05:54 [scheduler.py:237] Chunked prefill is enabled with max_num_batched_tokens=8192. (EngineCore_0 pid=12806) INFO 08-12 22:05:55 [core.py:619] Waiting for init message...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Can't run Qwen3-32B NVFP4 model bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_id = "RedHatAI/Qwen3-32B-N...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_id = "RedHatAI/Qwen3-32B-NVFP4" sampling_params = SamplingParams(temperature=0....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Can't run Qwen3-32B NVFP4 model bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_id = "RedHatAI/Qwen3-32B-N...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: e, 'enforce_eager': True} INFO 08-12 22:05:54 [__init__.py:702] Resolved architecture: Qwen3ForCausalLM INFO 08-12 22:05:54 [__init__.py:1739] Using max model len 40960 INFO 08-12 22:05:54 [scheduler.py:237] Chunked pre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
