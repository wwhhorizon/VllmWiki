# vllm-project/vllm#11643: [Bug]: I try to use vllm==0.6.5 for GLM4-9b-chat but error "/usr/bin/ld: cannot find -lcuda"

| 字段 | 值 |
| --- | --- |
| Issue | [#11643](https://github.com/vllm-project/vllm/issues/11643) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: I try to use vllm==0.6.5 for GLM4-9b-chat but error "/usr/bin/ld: cannot find -lcuda"

### Issue 正文摘录

### Your current environment ### Model Input Dumps ``` (glm4-9b-chat-128k-vLLM0_6_5) root@node1:~/ljm/ChatGLM4/GLM-4/api_server_vLLM# python /root/ljm/ChatGLM4/GLM-4/api_server_vLLM/openai_api_server_vLLM_glm4-chat.py INFO 12-31 10:07:32 config.py:478] This model supports multiple tasks: {'reward', 'embed', 'classify', 'score', 'generate'}. Defaulting to 'generate'. WARNING 12-31 10:07:32 arg_utils.py:1096] The model has a long context length (65528). This may cause OOM errors during the initial memory profiling phase, or result in low performance due to small KV cache space. Consider setting --max-model-len to a smaller value. INFO 12-31 10:07:32 llm_engine.py:249] Initializing an LLM engine (v0.6.5) with config: model='/root/ljm/models/glm-4-9b-chat', speculative_config=None, tokenizer='/root/ljm/models/glm-4-9b-chat', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=65528, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtyp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vllm.unified_attention","vllm.unified_attention_with_output"],"candidate_compile_sizes":[],"compile_sizes":[],"capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=65528, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ==0.6.5 for GLM4-9b-chat but error "/usr/bin/ld: cannot find -lcuda" bug;stale ### Your current environment ### Model Input Dumps ``` (glm4-9b-chat-128k-vLLM0_6_5) root@node1:~/ljm/ChatGLM4/GLM-4/api_server_vLLM# python...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: o use vllm==0.6.5 for GLM4-9b-chat but error "/usr/bin/ld: cannot find -lcuda" bug;stale ### Your current environment ### Model Input Dumps ``` (glm4-9b-chat-128k-vLLM0_6_5) root@node1:~/ljm/ChatGLM4/GLM-4/api_server_vL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
