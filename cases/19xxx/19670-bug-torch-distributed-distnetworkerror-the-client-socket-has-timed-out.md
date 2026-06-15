# vllm-project/vllm#19670: [Bug]: torch.distributed.DistNetworkError: The client socket has timed out after 600000ms while trying to connect to (172.17.0.9, 46229).

| 字段 | 值 |
| --- | --- |
| Issue | [#19670](https://github.com/vllm-project/vllm/issues/19670) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: torch.distributed.DistNetworkError: The client socket has timed out after 600000ms while trying to connect to (172.17.0.9, 46229).

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug INFO 06-16 01:48:43 [multiproc_worker_utils.py:137] Terminating local vLLM worker processes (VllmWorkerProcess pid=4086430) INFO 06-16 01:48:43 [multiproc_worker_utils.py:259] Worker exiting (VllmWorkerProcess pid=4086431) INFO 06-16 01:48:43 [multiproc_worker_utils.py:259] Worker exiting (VllmWorkerProcess pid=4086432) INFO 06-16 01:48:43 [multiproc_worker_utils.py:259] Worker exiting INFO 06-16 01:48:43 [config.py:717] This model supports multiple tasks: {'classify', 'generate', 'reward', 'score', 'embed'}. Defaulting to 'generate'. WARNING 06-16 01:48:43 [arg_utils.py:1525] Chunked prefill is enabled by default for models with max_model_len > 32K. Chunked prefill might not work with some features or models. If you encounter any issues, please disable by launching with --enable-chunked-prefill=False. INFO 06-16 01:48:43 [config.py:1770] Defaulting to use mp for distributed inference INFO 06-16 01:48:43 [config.py:2003] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 06-16 01:48:43 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5.post1) with config: model='work_dirs/llama3_8b_instruct_qlora_alpaca_e3_co...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: out after 600000ms while trying to connect to (172.17.0.9, 46229). bug;unstale ### Your current environment ### 🐛 Describe the bug INFO 06-16 01:48:43 [multiproc_worker_utils.py:137] Terminating local vLLM worker proces...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 8:43 [multiproc_worker_utils.py:259] Worker exiting INFO 06-16 01:48:43 [config.py:717] This model supports multiple tasks: {'classify', 'generate', 'reward', 'score', 'embed'}. Defaulting to 'generate'. WARNING 06-16 0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | gent-r1/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so) frame #4: <unknown function> + 0x63507f4 (0x7fcdd4b4d7f4 in /root/miniconda3/envs/agent-r1/lib/python3.11/site-pack… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | gent-r1/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so) frame #6: c10d::tcpstore::tcpstore(std::string, c10d::tcpstoreoptions const&) + 0x20c (0x7fcdd4b0d14c in /root/mini… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | gent-r1/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so) frame #7: <unknown function> + 0xe486ef (0x7fcde47336ef in /root/miniconda3/envs/agent-r1/lib/python3.11/site-packa… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | me #11: /root/miniconda3/envs/agent-r1/bin/python3() [0x5579ce] frame #12: _pyobject_call + 0x11f (0x54330f in /root/miniconda3/envs/agent-r1/bin/python3) frame #13: /root/minicon… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | t-r1/lib/python3.11/site-packages/torch/lib/libtorch_python.so) frame #16: _pyobject_maketpcall + 0x27c (0x50452c in /root/miniconda3/envs/agent-r1/bin/python3) frame #17: _pyeval… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | me #19: /root/miniconda3/envs/agent-r1/bin/python3() [0x52f30b] frame #20: pyobject_vectorcall + 0x31 (0x51ea31 in /root/miniconda3/envs/agent-r1/bin/python3) frame #21: _pyeval_e… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | + 0x31 (0x51ea31 in /root/miniconda3/envs/agent-r1/bin/python3) frame #21: _pyeval_evalframedefault + 0x6a6 (0x511a76 in /root/miniconda3/envs/agent-r1/bin/python3) frame #22: _py… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | 0x12c (0x5430ac in /root/miniconda3/envs/agent-r1/bin/python3) frame #27: _pyeval_evalframedefault + 0x47c0 (0x515b90 in /root/miniconda3/envs/agent-r1/bin/python3) frame #28: /ro… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | me #28: /root/miniconda3/envs/agent-r1/bin/python3() [0x5581df] frame #29: /root/miniconda3/envs/agent-r1/bin/python3() [0x557a20] frame #30: _pyeval_evalframedefault + 0x47c0 (0x… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | 0x173 (0x539153 in /root/miniconda3/envs/agent-r1/bin/python3) frame #32: pyobject_call + 0x12c (0x5430ac in /root/miniconda3/envs/agent-r1/bin/python3) frame #33: _pyeval_evalfra… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
