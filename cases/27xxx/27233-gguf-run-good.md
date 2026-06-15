# vllm-project/vllm#27233: gguf run good

| 字段 | 值 |
| --- | --- |
| Issue | [#27233](https://github.com/vllm-project/vllm/issues/27233) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;quantization;sampling |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> gguf run good

### Issue 正文摘录

### Your current environment from vllm import LLM, SamplingParams gguf_path = "/home/m/Desktop/vllm/vllm/examples/offline_inference/basic/Qwen3-1.7B-GGUF/Qwen3-1.7B-Q6_K.gguf" llm = LLM( gguf_path, tokenizer="Qwen/Qwen3-1.7B" ) params = SamplingParams( temperature=0.8, top_p=0.9, top_k=40, max_tokens=200, ) outputs = llm.generate(["Who is Napoleon Bonaparte?"], params) print(outputs[0].outputs[0].text) ### How would you like to use vllm I want to run inferevenv) m@m-HP-Z440-Workstation:~/Desktop/vllm/vllm/examples/offline_inference/basic$ (venv) m@m-HP-Z440-Workstation:~/Desktop/vllm/vllm/examples/offline_inference/basic$ python3 Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> from vllm import LLM, SamplingParams INFO 10-21 03:05:39 [__init__.py:216] Automatically detected platform cuda. >>> >>> gguf_path = "/home/m/Desktop/vllm/vllm/examples/offline_inference/basic/Qwen3-1.7B-GGUF/Qwen3-1.7B-Q6_K.gguf" >>> >>> llm = LLM( ... gguf_path, ... tokenizer="Qwen/Qwen3-1.7B" ... ) INFO 10-21 03:05:41 [utils.py:233] non-de...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: gguf run good usage;stale ### Your current environment from vllm import LLM, SamplingParams gguf_path = "/home/m/Desktop/vllm/vllm/examples/offline_inference/basic/Qwen3-1.7B-GGUF/Qwen3-1.7B-Q6_K.gguf" llm = LLM( gguf_p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: gguf run good usage;stale ### Your current environment from vllm import LLM, SamplingParams gguf_path = "/home/m/Desktop/vllm/vllm/examples/offline_inference/basic/Qwen3-1.7B-GGUF/Qwen3-1.7B-Q6_K.gguf" llm = LLM( gguf_p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 1 03:06:14 [model.py:547] Resolved architecture: Qwen3ForCausalLM `torch_dtype` is deprecated! Use `dtype` instead! ERROR 10-21 03:06:14 [config.py:278] Error retrieving safetensors: Repo id must be in the form 'repo_na...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: gguf_path = "/home/m/Desktop/vllm/vllm/examples/offline_inference/basic/Qwen3-1.7B-GGUF/Qwen3-1.7B-Q6_K.gguf" llm = LLM( gguf_path, tokenizer="Qwen/Qwen3-1.7B" ) params = SamplingParams( temperature=0.8, top_p=0.9, top_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
