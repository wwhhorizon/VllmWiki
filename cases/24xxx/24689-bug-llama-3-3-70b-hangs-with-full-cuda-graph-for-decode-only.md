# vllm-project/vllm#24689: [Bug]: Llama 3.3 70B hangs with full cuda graph for decode-only

| 字段 | 值 |
| --- | --- |
| Issue | [#24689](https://github.com/vllm-project/vllm/issues/24689) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama 3.3 70B hangs with full cuda graph for decode-only

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the following vllm server command: ``` vllm serve meta-llama/Llama-3.3-70B-Instruct \ --no-enable-prefix-caching \ --tensor-parallel-size 4 \ -O '{"cudagraph_mode": "FULL_DECODE_ONLY"}' ``` And then running the client like this: ``` python /data/vllm-community-homes/vllm-user-8/code/vllm/benchmarks/benchmark_serving.py --port 8123 --model meta-llama/Llama-3.3-70B-Instruct --dataset-name random --max-concurrency 32 --random-input-len 1 --random-output-len 1024 --num-prompts 160 --seed 1757539087 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 90,95,99 --ignore-eos ``` The server hangs during the sample iteration, after the following server log messages appear: ``` (APIServer pid=3789507) INFO: 127.0.0.1:45082 - "POST /v1/completions HTTP/1.1" 200 OK (VllmWorker TP3 pid=3790676) WARNING 09-10 13:35:53 [flashinfer.py:220] Using TRTLLM attention (auto-detected). (VllmWorker TP0 pid=3790673) WARNING 09-10 13:35:53 [flashinfer.py:220] Using TRTLLM attention (auto-detected). (VllmWorker TP1 pid=3790674) WARNING 09-10 13:35:53 [flashinfer.py:220] Using TRTLLM attention (auto-detected). (VllmWorker TP2 pid=379067...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: like this: ``` python /data/vllm-community-homes/vllm-user-8/code/vllm/benchmarks/benchmark_serving.py --port 8123 --model meta-llama/Llama-3.3-70B-Instruct --dataset-name random --max-concurrency 32 --random-input-len...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Llama 3.3 70B hangs with full cuda graph for decode-only bug;stale ### Your current environment ### 🐛 Describe the bug When running the following vllm server command: ``` vllm serve meta-llama/Llama-3.3-70B-Instr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Llama 3.3 70B hangs with full cuda graph for decode-only bug;stale ### Your current environment ### 🐛 Describe the bug When running the following vllm server command: ``` vllm serve meta-llama/Llama-3.3-70B-Instr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ns HTTP/1.1" 200 OK (VllmWorker TP3 pid=3790676) WARNING 09-10 13:35:53 [flashinfer.py:220] Using TRTLLM attention (auto-detected). (VllmWorker TP0 pid=3790673) WARNING 09-10 13:35:53 [flashinfer.py:220] Using TRTLLM at...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
