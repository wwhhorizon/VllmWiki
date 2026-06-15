# vllm-project/vllm#26329: [Bug]: OffloadingConnector instability with increasing --num-prompts vllm bench values

| 字段 | 值 |
| --- | --- |
| Issue | [#26329](https://github.com/vllm-project/vllm/issues/26329) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OffloadingConnector instability with increasing --num-prompts vllm bench values

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While evaluating performance of kvcache CPU offloading using 'vllm bench' we observe an inflection point with increasing --num-prompts where vllm becomes unstable and consistently crashes. An example command line showing the issue (on the setup shown in attached python collect_env.py output): ``` vllm bench throughput --model Qwen/Qwen3-0.6B --tensor-parallel-size 2 --dataset-name sharegpt --dataset-path /source/dataset/ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 565 --kv-transfer-config '{"kv_connector":"OffloadingConnector","kv_role":"kv_both","kv_connector_extra_config":{"num_cpu_blocks":5000,"cpu_block_size":256}}' ``` With --num-prompts at 550 all is well, but at ~565 and anything greater it crashes with the stack trace below. The failure pattern is always the same - a series of offloading_connector.py WARNINGs ('Cannot store blocks') , followed by the core.py ERRORs exception ('IndexError: list index out of range'). As a comparison point, in the same hardware setup if I swap in 'LMCacheConnectorV1' in place of 'OffloadingConnector', the setup is stable - I've tested up to --num-samples 10000 without any issues....

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: er=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen3-0.6B, enable_prefix_caching=True, chu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 02:50:07 [model.py:1510] Using max model len 40960 INFO 10-07 02:50:07 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 10-07 02:50:11 [__init__.py:216] Automatically detected platfor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 7 02:50:07 [model.py:547] Resolved architecture: Qwen3ForCausalLM `torch_dtype` is deprecated! Use `dtype` instead! INFO 10-07 02:50:07 [model.py:1510] Using max model len 40960 INFO 10-07 02:50:07 [scheduler.py:205] Ch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ' INFO 10-07 02:49:55 [__init__.py:216] Automatically detected platform cuda. /source/vllm/vllm/benchmarks/throughput.py:610: UserWarning: --random-range-ratio will be ignored since --dataset-name is not 'random'. valid...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
