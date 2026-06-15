# vllm-project/vllm#9308: [Bug]: Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#9308](https://github.com/vllm-project/vllm/issues/9308) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` vllm serve mistralai/Mistral-Large-Instruct-2407 --tensor-parallel-size 8 --trust-remote-code --gpu_memory_utilization 0.85 --max_model_len 8192 --disable-custom-all-reduce ``` ``` INFO 10-12 13:49:35 config.py:813] Defaulting to use mp for distributed inference INFO 10-12 13:49:35 config.py:911] Chunked prefill is enabled with max_num_batched_tokens=512. INFO 10-12 13:49:35 llm_engine.py:184] Initializing an LLM engine (v0.5.5) with config: model='/share/project/huggingface/models/Mistral-Large-Instruct-2407', speculative_config=None, tokenizer='/share/project/huggingface/models/Mistral-Large-Instruct-2407', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=8, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outl...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: with exception: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` vllm serve mistralai/Mistral-Large-Instruct-2407...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=8, pipeline_parallel_size=1, disable_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ry access was encountered bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` vllm serve mistralai/Mistral-Large-Instruct-2407 --tensor-parallel-size 8 --trust-remote-co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _caching=False) WARNING 10-12 13:49:36 multiproc_gpu_executor.py:59] Reducing Torch parallelism from 64 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this valu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | rness/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0xa0 (0x7f2b54d70600 in /root/miniconda3/envs/harness/li… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | rness/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x7f2b54d796fc in /root/miniconda3/envs/harness/lib/py… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | rness/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdbbf4 (0x7f2ba24c7bf4 in /root/miniconda3/envs/harness/bin/../lib/libstdc++.so.6) fr |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
