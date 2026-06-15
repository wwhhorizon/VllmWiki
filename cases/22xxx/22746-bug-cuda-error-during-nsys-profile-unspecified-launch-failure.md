# vllm-project/vllm#22746: [Bug]: CUDA error during nsys profile : unspecified launch failure

| 字段 | 值 |
| --- | --- |
| Issue | [#22746](https://github.com/vllm-project/vllm/issues/22746) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA error during nsys profile : unspecified launch failure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug nsys --version NVIDIA Nsight Systems version 2025.3.1.90-253135822126v0 command ''' nsys profile -f true -o qwen32b.nsys-rep --trace-fork-before-exec=true --cuda-graph-trace=node python3 ~/code/vllm/benchmarks/benchmark_latency.py --model /data01/model/Qwen/Qwen3-32B-FP8 --num-iters-warmup 5 --num-iters 1 --batch-size 1 --input-len 1024 --output-len 1024 --tensor-parallel-size 2 ''' error message ''' DEBUG 08-12 08:45:18 [utils.py:741] Waiting for 1 local, 0 remote core engine proc(s) to start. ^[[1;36m(VllmWorker rank=0 pid=13543)^[[0;0m INFO 08-12 08:45:18 [custom_all_reduce.py:196] Registering 8643 cuda graph addresses ^[[1;36m(VllmWorker rank=1 pid=13550)^[[0;0m INFO 08-12 08:45:18 [gpu_model_runner.py:2485] Graph capturing finished in 9 secs, took 1.30 GiB ^[[1;36m(VllmWorker rank=0 pid=13543)^[[0;0m INFO 08-12 08:45:18 [gpu_model_runner.py:2485] Graph capturing finished in 9 secs, took 1.30 GiB INFO 08-12 08:45:18 [core.py:193] init engine (profile, create kv cache, warmup model) took 41.76 seconds DEBUG 08-12 08:45:18 [utils.py:822] READY from local core engine process 0. DEBUG 08-12 08:45:18 [core.py:660] EngineCore waiti...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: CUDA error during nsys profile : unspecified launch failure bug ### Your current environment ### 🐛 Describe the bug nsys --version NVIDIA Nsight Systems version 2025.3.1.90-253135822126v0 command ''' nsys profile...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: CUDA error during nsys profile : unspecified launch failure bug ### Your current environment ### 🐛 Describe the bug nsys --version NVIDIA Nsight Systems version 2025.3.1.90-253135822126v0 command ''' nsys profile...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: gnu/libc.so.6) terminate called after throwing an instance of 'c10::DistBackendError' what(): [PG ID 2 PG GUID 3 Rank 1] Process group watchdog thread terminated with exception: CUDA error: unspecified launch failure CU...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: llm/benchmarks/benchmark_latency.py --model /data01/model/Qwen/Qwen3-32B-FP8 --num-iters-warmup 5 --num-iters 1 --batch-size 1 --input-len 1024 --output-len 1024 --tensor-parallel-size 2 ''' error message ''' DEBUG 08-1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA error during nsys profile : unspecified launch failure bug ### Your current environment ### 🐛 Describe the bug nsys --version NVIDIA Nsight Systems version 2025.3.1.90-253135822126v0 command ''' nsys profile...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0xdc253 (0x7fdd7574b253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #5: <unkn… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | t-systems-cli/2025.3.1/target-linux-x64/libtoolsinjection64.so) frame #6: <unknown function> + 0x94ac3 (0x7fdd7d851ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #7: <unknown f… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 0x94ac3 (0x7fdd7d851ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #7: <unknown function> + 0x126850 (0x7fdd7d8e3850 in /usr/lib/x86_64-linux-gnu/libc.so.6) error 08-12 08:45:33 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
