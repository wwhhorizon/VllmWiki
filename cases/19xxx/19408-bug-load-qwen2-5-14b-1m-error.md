# vllm-project/vllm#19408: [Bug]: load Qwen2.5-14B-1M error

| 字段 | 值 |
| --- | --- |
| Issue | [#19408](https://github.com/vllm-project/vllm/issues/19408) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: load Qwen2.5-14B-1M error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug i have an error when i load qwen2.5-14B-Instruct-1M INFO 06-10 16:32:52 [core.py:159] init engine (profile, create kv cache, warmup model) took 7.68 seconds INFO 06-10 16:32:52 [core_client.py:439] Core engine process 0 ready. Processed prompts: 0%| | 0/1 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]ERROR 06-10 16:33:51 [core.py:398] EngineCore encountered a fatal error. ERROR 06-10 16:33:51 [core.py:398] Traceback (most recent call last): ERROR 06-10 16:33:51 [core.py:398] File "/home/brain/anaconda3/envs/tk_longcontext/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 181, in collective_rpc ERROR 06-10 16:33:51 [core.py:398] status, result = w.worker_response_mq.dequeue( ERROR 06-10 16:33:51 [core.py:398] File "/home/brain/anaconda3/envs/tk_longcontext/lib/python3.10/site-packages/vllm/distributed/device_communicators/shm_broadcast.py", line 479, in dequeue ERROR 06-10 16:33:51 [core.py:398] with self.acquire_read(timeout, cancel) as buf: ERROR 06-10 16:33:51 [core.py:398] File "/home/brain/anaconda3/envs/tk_longcontext/lib/python3.10/contextlib.py", line 135, in enter ERROR 06-10...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: load Qwen2.5-14B-1M error bug ### Your current environment ### 🐛 Describe the bug i have an error when i load qwen2.5-14B-Instruct-1M INFO 06-10 16:32:52 [core.py:159] init engine (profile, create kv cache, warmu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ROR 06-10 16:33:51 [core.py:398] status, result = w.worker_response_mq.dequeue( ERROR 06-10 16:33:51 [core.py:398] File "/home/brain/anaconda3/envs/tk_longcontext/lib/python3.10/site-packages/vllm/distributed/device_com...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: qwen2.5-14B-Instruct-1M INFO 06-10 16:32:52 [core.py:159] init engine (profile, create kv cache, warmup model) took 7.68 seconds INFO 06-10 16:32:52 [core_client.py:439] Core engine process 0 ready. Processed prompts: 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d ' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: truct-1M INFO 06-10 16:32:52 [core.py:159] init engine (profile, create kv cache, warmup model) took 7.68 seconds INFO 06-10 16:32:52 [core_client.py:439] Core engine process 0 ready. Processed prompts: 0%| | 0/1 [00:00...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
