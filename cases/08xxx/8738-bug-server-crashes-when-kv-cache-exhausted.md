# vllm-project/vllm#8738: [Bug]: Server crashes when kv cache exhausted

| 字段 | 值 |
| --- | --- |
| Issue | [#8738](https://github.com/vllm-project/vllm/issues/8738) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Server crashes when kv cache exhausted

### Issue 正文摘录

### Your current environment GPUs: 8xL4 v0.6.1 (docker) model: neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8-dynamic options: VLLM_ATTENTION_BACKEND=FLASHINFER --tensor-parallel-size 8 --max_model_len 50000 --max-num-batched-tokens 50000 --gpu-memory-utilization 0.90 --enable-chunked-prefill false ### Model Input Dumps _No response_ ### 🐛 Describe the bug The model runs fine when there is not too much load. When the load increases the KV cache eventually reaches 100% and then vllm crashes. ``` Exception in callback functools.partial( , error_callback= >) handle: , error_callback= >)> Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner_base.py", line 112, in _wrapper return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner.py", line 1584, in execute_model model_input.async_callback() File "/usr/local/lib/python3.12/dist-packages/vllm/engine/llm_engine.py", line 1438, in _process_model_outputs self.do_log_stats(scheduler_outputs, outputs, finished_before) File "/usr/local/lib/python3.12/dist-packages/vllm/engine/llm_engine.py", line 1748, in do_log_stats stats = self....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: -num-batched-tokens 50000 --gpu-memory-utilization 0.90 --enable-chunked-prefill false ### Model Input Dumps _No response_ ### 🐛 Describe the bug The model runs fine when there is not too much load. When the load increa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: almagic/Meta-Llama-3.1-70B-Instruct-FP8-dynamic options: VLLM_ATTENTION_BACKEND=FLASHINFER --tensor-parallel-size 8 --max_model_len 50000 --max-num-batched-tokens 50000 --gpu-memory-utilization 0.90 --enable-chunked-pre...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: exhausted bug ### Your current environment GPUs: 8xL4 v0.6.1 (docker) model: neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8-dynamic options: VLLM_ATTENTION_BACKEND=FLASHINFER --tensor-parallel-size 8 --max_model_len 50000...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 2/dist-packages/vllm/engine/llm_engine.py", line 1860, in _get_stats latency = seq_group.get_last_latency(now) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/sequence.py", line 686, i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: kv cache exhausted bug ### Your current environment GPUs: 8xL4 v0.6.1 (docker) model: neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8-dynamic options: VLLM_ATTENTION_BACKEND=FLASHINFER --tensor-parallel-size 8 --max_model_l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
