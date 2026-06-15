# vllm-project/vllm#7830: [Bug]: vLLM with ray backend and enable nsight can't get perf metrics due to connection issue

| 字段 | 值 |
| --- | --- |
| Issue | [#7830](https://github.com/vllm-project/vllm/issues/7830) |
| 状态 | closed |
| 标签 | bug;ray;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM with ray backend and enable nsight can't get perf metrics due to connection issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug using the code in your repo : benchmark_latency.py, and enable "ray_workers_use_nsight" and 'distributed_executor_backend="ray"'. like below: llm = LLM(model=args.model, tokenizer=args.tokenizer, quantization=args.quantization, tensor_parallel_size=args.tensor_parallel_size, trust_remote_code=args.trust_remote_code, dtype=args.dtype, enforce_eager=args.enforce_eager, kv_cache_dtype=args.kv_cache_dtype, quantization_param_path=args.quantization_param_path, device=args.device, ray_workers_use_nsight=args.ray_workers_use_nsight, enable_chunked_prefill=args.enable_chunked_prefill, download_dir=args.download_dir, block_size=args.block_size, distributed_executor_backend="ray") the *.nsys-rep can be generated but no any CUDA related events. check the logs , here are error : " metric_exporter.cc:105: [1] Export metrics to agent failed: RpcError: RPC Error message: failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:60082: Failed to connect to remote host: Connection refused; RPC Error details: . This won't affect Ray, but you can lose metrics from the cluster." BTW, run "benchmark_latency.py" in a docker container and...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: an lose metrics from the cluster." BTW, run "benchmark_latency.py" in a docker container and try 1 card and 2 cards on 1 node, both has above error and metrics missing in report. Could you instruct me how to set ray clu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: d enable nsight can't get perf metrics due to connection issue bug;ray;unstale ### Your current environment ### 🐛 Describe the bug using the code in your repo : benchmark_latency.py, and enable "ray_workers_use_nsight"...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: nt environment ### 🐛 Describe the bug using the code in your repo : benchmark_latency.py, and enable "ray_workers_use_nsight" and 'distributed_executor_backend="ray"'. like below: llm = LLM(model=args.model, tokenizer=a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: vLLM with ray backend and enable nsight can't get perf metrics due to connection issue bug;ray;unstale ### Your current environment ### 🐛 Describe the bug using the code in your repo : benchmark_latency.py, and e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: (model=args.model, tokenizer=args.tokenizer, quantization=args.quantization, tensor_parallel_size=args.tensor_parallel_size, trust_remote_code=args.trust_remote_code, dtype=args.dtype, enforce_eager=args.enfor

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
