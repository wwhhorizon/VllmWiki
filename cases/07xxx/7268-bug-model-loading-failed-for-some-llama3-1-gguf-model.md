# vllm-project/vllm#7268: [Bug]: model loading failed for some Llama3.1 GGUF model

| 字段 | 值 |
| --- | --- |
| Issue | [#7268](https://github.com/vllm-project/vllm/issues/7268) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: model loading failed for some Llama3.1 GGUF model

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug **Brief description** - This issue is used to track the llama3.1 gguf weight loading bug reported in #5191 for clarity. **Bug description** - Some Llama3.1 GGUF model which using the new `llama.cpp` conversion script updated in [llama.cpp PR-8676](https://github.com/ggerganov/llama.cpp/pull/8676) will contain a `rope_freqs.weight` tensor. - The extra rope_freqs weight cause a weight loading error as reported in #5191. - Note that the `rope_freqs.weight` is a tensor only used for `llama.cpp` inference speedup, and it's not a exact weight of source model. **Reproduce code** ```python from huggingface_hub import hf_hub_download from vllm import LLM, SamplingParams def run_gguf_inference(model_path): PROMPT_TEMPLATE = " system \n" \ "{system_message} \n" \ " user \n" \ "{prompt} \n" \ " assistant " # PROMPT_TEMPLATE = " \n{system_message} \n \n{prompt} \n \n" # noqa: E501 system_message = "You are a helpful assistant." # noqa: E501 # Sample prompts. prompts = [ "How many helicopters can a human eat in one sitting?", "What's the future of AI?", ] prompts = [ PROMPT_TEMPLATE.format(syst...

## 现有链接修复摘要

#5191 [Core] Support loading GGUF model | #7269 [Bugfix] Fix new Llama3.1 GGUF model loading

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: model loading failed for some Llama3.1 GGUF model bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug **Brief description** - This issue is used to track the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: cription** - Some Llama3.1 GGUF model which using the new `llama.cpp` conversion script updated in [llama.cpp PR-8676](https://github.com/ggerganov/llama.cpp/pull/8676) will contain a `rope_freqs.weight` tensor. - The e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.GGUF, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None), seed=0, served_model_name=/root/.cache/huggingface/hub/m...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: es, please disable chunked prefill by setting --enable-chunked-prefill=False. INFO 08-07 14:20:20 config.py:853] Chunked prefill is enabled with max_num_batched_tokens=512. INFO 08-07 14:20:20 llm_engine.py:176] Initial...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5191](https://github.com/vllm-project/vllm/pull/5191) | mentioned | 0.45 | [Core] Support loading GGUF model | e extra rope_freqs weight cause a weight loading error as reported in #5191. - note that the `rope_freqs.weight` is a tensor only used for `llama.cpp` inference speedup, and it's… |
| [#7269](https://github.com/vllm-project/vllm/pull/7269) | closes_keyword | 0.95 | [Bugfix] Fix new Llama3.1 GGUF model loading | FIX #7268 (*link existing issues this PR will resolve*) - After the investigation about [llama.cpp PR-8676](https://github.com/ggerganov/llama.cpp/pull/8676), which introduced the |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
