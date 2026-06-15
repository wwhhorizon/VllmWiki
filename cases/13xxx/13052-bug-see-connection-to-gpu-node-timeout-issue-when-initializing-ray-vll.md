# vllm-project/vllm#13052: [Bug]: see connection to gpu node timeout issue when initializing ray vllm multi-node serving

| 字段 | 值 |
| --- | --- |
| Issue | [#13052](https://github.com/vllm-project/vllm/issues/13052) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: see connection to gpu node timeout issue when initializing ray vllm multi-node serving

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am setting up serving Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 model for inference using two g6.2xlarge instances (each node has one 1gpu). I created placement group like this: Placement Group Bundles: [{'CPU': 1.0}, {'GPU': 1.0, 'CPU': 1.0, 'memory': 9000000000.0}, {'memory': 9000000000.0, 'CPU': 1.0, 'GPU': 1.0}], and configured it to the serve deployment actor. ```python infer_ray_actor_options = { "num_gpus": 0, "num_cpus": 1, } handle = serve.run(InferActor.options(ray_actor_options=infer_ray_actor_options, placement_group_bundles=placement_group_bundles, placement_group_strategy=placement_group_strategy, max_ongoing_requests=512, autoscaling_config=autoscale_config) .bind(model_cache_deployment), route_prefix=None, name=deployment_name) ``` The AsyncEngineArgs is using tensor_parallel_size=1, pipeline_parallel_size=2. Other args can be seen in the logs below. But I can also attach relevant python code. Errors ``` :job_id:01000000 :actor_name:ServeReplica:hugging-quants2-Meta-Llama-3.1-70B-Instruct-GPTQ-INT4@infer_actor:InferActor INFO 2025-02-10 09:26:45,197 hugging-quants2-Meta-Llama-3.1-70B-Instruct-GPTQ-INT4@infer_actor_I...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: node timeout issue when initializing ray vllm multi-node serving bug;ray;stale ### Your current environment ### 🐛 Describe the bug I am setting up serving Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 model for inference using...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: e=None, tokenizer='/tmp/tmpojalf_6s', task='auto', skip_tokenizer_init=False, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path='', download_dir=None, load_format= , config_format= , dtype='auto',...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ent environment ### 🐛 Describe the bug I am setting up serving Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 model for inference using two g6.2xlarge instances (each node has one 1gpu). I created placement group like this: Plac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype='auto', seed=0, max_model_len=1024, distributed_executor_backend='ray', pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loading_workers=None, block_size=None, enable_prefix_caching=False, d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: scribe the bug I am setting up serving Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 model for inference using two g6.2xlarge instances (each node has one 1gpu). I created placement group like this: Placement Group Bundles: [{'...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | aconda3/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #4: <unknown function> + 0x602a3a4 (0x7fe5817973a4 in /home/ray/anaconda3/lib/python3.10/site-packages/torch/… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | aconda3/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #6: c10d::tcpstore::tcpstore(std::string, c10d::tcpstoreoptions const&) + 0x20c (0x7fe581757f7c in /home/ray/… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | aconda3/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #7: <unknown function> + 0xd9acdd (0x7fe59113acdd in /home/ray/anaconda3/lib/python3.10/site-packages/torch/l… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | 0x147296 (0x5610a9ba7296 in /home/ray/anaconda3/bin/python3.10) frame #12: pyvectorcall_call + 0xc9 (0x5610a9ba7cc9 in /home/ray/anaconda3/bin/python3.10) frame #13: <unknown func… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | nda3/lib/python3.10/site-packages/torch/lib/libtorch_python.so) frame #16: _pyobject_maketpcall + 0x2d3 (0x5610a9b94a03 in /home/ray/anaconda3/bin/python3.10) frame #17: _pyeval_e… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | + 0x309 (0x5610a9b8bda9 in /home/ray/anaconda3/bin/python3.10) frame #20: _pyfunction_vectorcall + 0x6c (0x5610a9b9bb7c in /home/ray/anaconda3/bin/python3.10) frame #21: _pyeval_e… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | l + 0x6c (0x5610a9b9bb7c in /home/ray/anaconda3/bin/python3.10) frame #21: _pyeval_evalframedefault + 0x309 (0x5610a9b8bda9 in /home/ray/anaconda3/bin/python3.10) frame #22: _pyfu… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | l + 0x6c (0x5610a9b9bb7c in /home/ray/anaconda3/bin/python3.10) frame #27: _pyeval_evalframedefault + 0x49b7 (0x5610a9b90457 in /home/ray/anaconda3/bin/python3.10) frame #28: _pyf… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | l + 0x6c (0x5610a9b9bb7c in /home/ray/anaconda3/bin/python3.10) frame #29: _pyeval_evalframedefault + 0x309 (0x5610a9b8bda9 in /home/ray/anaconda3/bin/python3.10) frame #30: _pyob… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | d + 0x69 (0x5610a9ba55b9 in /home/ray/anaconda3/bin/python3.10) frame #32: <unknown function> + 0x205f29 (0x5610a9c65f29 in /home/ray/anaconda3/bin/python3.10) frame #33: pyobject… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | t-gptq-int4@infer_actor:inferactor.initialize_and_get_metadata) frame #53: _pyobject_maketpcall + 0x2eb (0x5599cf9a9a1b in ray::1-70b-instruct-gptq-int4@infer_actor:inferactor.ini… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
