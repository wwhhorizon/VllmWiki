# vllm-project/vllm#17242: [Bug]: "Fatal Python error: Segmentation fault" when running DeepSeek TP16 using v0.8.4 v1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#17242](https://github.com/vllm-project/vllm/issues/17242) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "Fatal Python error: Segmentation fault" when running DeepSeek TP16 using v0.8.4 v1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run the distribute inference in ray with vllm v0.8.4 and v1 engine on two nodes of 16*H20 and failed with the following "Segmentation fault". However, v0 engine doesn't have this problem with same commands. ```bash export VLLM_LOGGING_LEVEL=DEBUG export VLLM_USE_V1=1 python /workspace/vllm/benchmarks/benchmark_latency.py \ --trust-remote-code \ --max-num-batched-tokens 138 \ --max-model-len 138 \ --model /data/deepseek-ai/DeepSeek-R1/ \ --num-iters-warmup 1 \ --num-iters 1 \ --dtype bfloat16 \ --input-len 128 \ --output-len 10 \ -tp 16 \ --batch-size 1 \ --max-num-seqs 1 \ --distributed-executor-backend ray \ --gpu-memory-utilization 0.7 ``` ``` INFO 04-27 02:51:57 [kv_cache_utils.py:634] GPU KV cache size: 335,360 tokens INFO 04-27 02:51:57 [kv_cache_utils.py:637] Maximum concurrency for 138 tokens per request: 2430.14x INFO 04-27 02:51:57 [kv_cache_utils.py:634] GPU KV cache size: 335,360 tokens INFO 04-27 02:51:57 [kv_cache_utils.py:637] Maximum concurrency for 138 tokens per request: 2430.14x INFO 04-27 02:51:57 [kv_cache_utils.py:634] GPU KV cache size: 335,168 tokens INFO 04-27 02:51:57 [kv_cache_utils.py:637...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: egmentation fault" when running DeepSeek TP16 using v0.8.4 v1 engine bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to run the distribute inference in ray with vllm v0.8.4 and v1 engine on two...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: id=376230, ip=10.10.10.61)[0m INFO 04-27 02:51:55 [monitor.py:33] torch.compile takes 9.36 s in total[32m [repeated 15x across cluster][0m INFO 04-27 02:52:25 [core.py:163] init engine (profile, create kv cache, warm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ort VLLM_LOGGING_LEVEL=DEBUG export VLLM_USE_V1=1 python /workspace/vllm/benchmarks/benchmark_latency.py \ --trust-remote-code \ --max-num-batched-tokens 138 \ --max-model-len 138 \ --model /data/deepseek-ai/DeepSeek-R1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: k-ai/DeepSeek-R1/ \ --num-iters-warmup 1 \ --num-iters 1 \ --dtype bfloat16 \ --input-len 128 \ --output-len 10 \ -tp 16 \ --batch-size 1 \ --max-num-seqs 1 \ --distributed-executor-backend ray \ --gpu-memory-utilizatio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: local/lib/python3.10/dist-packages/vllm/distributed/device_communicators/cuda_communicator.py", line 63 in all_reduce [36m(RayWorkerWrapper pid=376235, ip=10.10.10.61)[0m File "/usr/local/lib/python3.10/dist-packages/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
