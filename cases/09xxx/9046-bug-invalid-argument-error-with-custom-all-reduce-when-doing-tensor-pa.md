# vllm-project/vllm#9046: [Bug]: 'invalid argument' Error with custom_all_reduce when doing tensor parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#9046](https://github.com/vllm-project/vllm/issues/9046) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'invalid argument' Error with custom_all_reduce when doing tensor parallelism

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I built vllm from source with nightly PyTorch as documented [here](https://docs.vllm.ai/en/latest/getting_started/installation.html#build-from-source-with-compilation) then I try ```bash NCCL_DEBUG=TRACE python3 benchmarks/benchmark_latency.py -tp 4 ``` ```bash Namespace(model='facebook/opt-125m', speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_size=None, tokenizer=None, quantization=None, tensor_parallel_size=4, input_len=32, output_len=128, batch_size=8, n=1, use_beam_search=False, num_iters_warmup=10, num_iters=30, trust_remote_code=False, max_model_len=None, dtype='auto', enforce_eager=False, kv_cache_dtype='auto', quantization_param_path=None, profile=False, profile_result_dir=None, device='auto', block_size=16, enable_chunked_prefill=False, enable_prefix_caching=False, use_v2_block_manager=False, ray_workers_use_nsight=False, download_dir=None, output_json=None, gpu_memory_utilization=0.9, load_format='auto', distributed_executor_backend=None, otlp_traces_endpoint=None) INFO 10-03 11:23:18 config.py:899] Defaulting to use mp for distributed inference...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: argument' Error with custom_all_reduce when doing tensor parallelism bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I built vllm from source with nightly PyTorch as doc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: orch as documented [here](https://docs.vllm.ai/en/latest/getting_started/installation.html#build-from-source-with-compilation) then I try ```bash NCCL_DEBUG=TRACE python3 benchmarks/benchmark_latency.py -tp 4 ``` ```bas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: doing tensor parallelism bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I built vllm from source with nightly PyTorch as documented [here](https://docs.vllm.ai/en/lates...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: urce with nightly PyTorch as documented [here](https://docs.vllm.ai/en/latest/getting_started/installation.html#build-from-source-with-compilation) then I try ```bash NCCL_DEBUG=TRACE python3 benchmarks/benchmark_latenc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: okens=None, speculative_draft_tensor_parallel_size=None, tokenizer=None, quantization=None, tensor_parallel_size=4, input_len=32, output_len=128, batch_size=8, n=1, use_beam_search=False, num_iters_warmup=10, num_iters=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
