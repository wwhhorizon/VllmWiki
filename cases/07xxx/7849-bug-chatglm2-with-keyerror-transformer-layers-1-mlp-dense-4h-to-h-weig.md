# vllm-project/vllm#7849: [Bug]: Chatglm2 with KeyError: 'transformer.layers.1.mlp.dense_4h_to_h.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#7849](https://github.com/vllm-project/vllm/issues/7849) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Chatglm2 with KeyError: 'transformer.layers.1.mlp.dense_4h_to_h.weight'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have tried to launch the demo of offline inference as followed: ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="/data3/chentower/chatglm2-6b", tokenizer='/data3/chentower/chatglm2-6b', dtype="float16", trust_remote_code=True) ``` But I got the KeyError: 'transformer.layers.1.mlp.dense_4h_to_h.weight' as followed: ``` INFO 08-25 18:29:27 llm_engine.py:184] Initializing an LLM engine (v0.5.5) with config: model='/data3/chentower/chatglm2-6b', speculative_config=None, tokenizer='/data3/chentower/chatglm2-6b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: to launch the demo of offline inference as followed: ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is",...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="/data3/chentower/chatglm2-6b", tokenizer='/data3/chentower/chatglm2-6b', dtype="float16", trust_remote_code=True) ``` But I got the KeyError:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /data3/chentower/chatglm2-6b", tokenizer='/data3/chentower/chatglm2-6b', dtype="float16", trust_remote_code=True) ``` But I got the KeyError: 'transformer.layers.1.mlp.dense_4h_to_h.weight' as followed: ``` INFO 08-25 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, coll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
