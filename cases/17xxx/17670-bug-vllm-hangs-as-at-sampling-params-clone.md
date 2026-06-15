# vllm-project/vllm#17670: [Bug]: VLLM hangs as at sampling_params.clone()

| 字段 | 值 |
| --- | --- |
| Issue | [#17670](https://github.com/vllm-project/vllm/issues/17670) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM hangs as at sampling_params.clone()

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Greetings, Everything was fine this morning. But for some reason, VLLM suddenly hangs at `llm.generate`, not returning me anything. I can see the model is loaded into the GPU, but it doesn't compute. I cannot see the progress bar on my screen. I am using `gemma-2-9b-it` with Guided decoding. Everything was fine before. ``` llm = LLM(args.model_name, dtype=dtype, max_model_len=args.max_seq_len, seed=args.seed, max_lora_rank=args.max_lora_rank, enable_lora=args.lora_path is not None, disable_custom_all_reduce=True,) tokenizer = AutoTokenizer.from_pretrained(args.model_name) lora = LoRARequest('test-lora', 1, lora_path=args.lora_path) if args.lora_path is not None else None ``` And here is how I inference it. ``` outputs = llm.generate( input_prompts, sampling_params=SamplingParams(top_k=-1, top_p=1, temperature=0, guided_decoding=GuidedDecodingParams(choice=[' ' + str(i) + ' ' for i in range(0, 11)]))), lora_request=lora_request, ) ``` It seems like it stuck at copying sampling_params: ``` INFO 05-05 16:12:01 __init__.py:207] Automatically detected platform cuda. INFO 05-05 16:12:10 config.py:549] This model supports multiple tasks...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: VLLM hangs as at sampling_params.clone() bug;stale ### Your current environment ### 🐛 Describe the bug Greetings, Everything was fine this morning. But for some reason, VLLM suddenly hangs at `llm.generate`, not...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ed decoding. Everything was fine before. ``` llm = LLM(args.model_name, dtype=dtype, max_model_len=args.max_seq_len, seed=args.seed, max_lora_rank=args.max_lora_rank, enable_lora=args.lora_path is not None, disable_cust...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ddenly hangs at `llm.generate`, not returning me anything. I can see the model is loaded into the GPU, but it doesn't compute. I cannot see the progress bar on my screen. I am using `gemma-2-9b-it` with Guided decoding....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_ti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
