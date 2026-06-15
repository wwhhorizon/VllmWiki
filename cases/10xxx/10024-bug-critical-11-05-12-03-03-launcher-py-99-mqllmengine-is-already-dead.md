# vllm-project/vllm#10024: [Bug]: CRITICAL 11-05 12:03:03 launcher.py:99] MQLLMEngine is already dead, terminating server process

| 字段 | 值 |
| --- | --- |
| Issue | [#10024](https://github.com/vllm-project/vllm/issues/10024) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CRITICAL 11-05 12:03:03 launcher.py:99] MQLLMEngine is already dead, terminating server process

### Issue 正文摘录

### Your current environment INFO 11-05 12:03:00 engine.py:290] Added request chat-58cc8fe807d34717b775ea663d913bcb. ERROR 11-05 12:03:00 client.py:250] RuntimeError('Engine loop has died') ERROR 11-05 12:03:00 client.py:250] Traceback (most recent call last): ERROR 11-05 12:03:00 client.py:250] File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/client.py", line 150, in run_heartbeat_loop ERROR 11-05 12:03:00 client.py:250] await self._check_success( ERROR 11-05 12:03:00 client.py:250] File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/client.py", line 314, in _check_success ERROR 11-05 12:03:00 client.py:250] raise response ERROR 11-05 12:03:00 client.py:250] RuntimeError: Engine loop has died INFO 11-05 12:03:01 metrics.py:349] Avg prompt throughput: 6.5 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 5.0%, CPU KV cache usage: 0.0%. INFO: 10.12.17.5:58280 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 10.12.17.5:58489 - "GET /v1/models HTTP/1.1" 200 OK CRITICAL 11-05 12:03:03 launcher.py:99] MQLLMEngine is already dead, term...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ncher.py:99] MQLLMEngine is already dead, terminating server process bug;stale ### Your current environment INFO 11-05 12:03:00 engine.py:290] Added request chat-58cc8fe807d34717b775ea663d913bcb. ERROR 11-05 12:03:00 cl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: INFO: Application shutdown complete. ### Model Input Dumps export CUDA_VISIBLE_DEVICES=2 export VLLM_USE_MODELSCOPE= False vllm serve ./Qwen2_5-14B-Instruct-AWQ \ --host 0.0.0.0 \ --port 2015 \ --tensor-parallel-size 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: /chat/completions HTTP/1.1" 200 OK INFO: 10.12.17.5:58489 - "GET /v1/models HTTP/1.1" 200 OK CRITICAL 11-05 12:03:03 launcher.py:99] MQLLMEngine is already dead, terminating server process INFO: 10.12.17.5:58489 - "POST...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ror: Engine loop has died INFO 11-05 12:03:01 metrics.py:349] Avg prompt throughput: 6.5 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 5.0%, CP...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 5.0%, CPU KV cache usage: 0.0%. INFO: 10.12.17.5:58280 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 10.12.17.5:58489 - "GET...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
