# vllm-project/vllm#2692: server crash while running models on multiple GPU but not on single

| 字段 | 值 |
| --- | --- |
| Issue | [#2692](https://github.com/vllm-project/vllm/issues/2692) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> server crash while running models on multiple GPU but not on single

### Issue 正文摘录

Hello, I have server on Ubutu 22.04 with 3 A6000 I have a very strange bug, I'm able to run https://huggingface.co/TheBloke/Nous-Hermes-2-Mixtral-8x7B-DPO-AWQ on a single GPU using async. While I try to switch to multigpu with same configuration (only --tensor-parallel-size 2) my server is crashing (shutting and restart) with enforce_eager=True without any explicit message : log at /var/log/syslog : Jan 31 18:00:57 thot python3.10[2761]: INFO 01-31 18:00:57 llm_engine.py:877] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 9.7 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0% Jan 31 18:01:02 thot python3.10[2761]: INFO 01-31 18:01:02 llm_engine.py:877] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 11.3 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0% Jan 31 18:04:25 thot systemd-modules-load[1291]: Inserted module 'lp' Any help would be appreciated.. Edit : the issue seems to be on all models (quntized or not )running on multi-gpu

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: server crash while running models on multiple GPU but not on single Hello, I have server on Ubutu 22.04 with 3 A6000 I have a very strange bug, I'm able to run https://huggingface.co/TheBloke/Nous-Hermes-2-Mixtral-8x7B-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: crashing (shutting and restart) with enforce_eager=True without any explicit message : log at /var/log/syslog : Jan 31 18:00:57 thot python3.10[2761]: INFO 01-31 18:00:57 llm_engine.py:877] Avg prompt throughput: 0.0 to...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 9.7 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0% Jan 31 18:01:02 thot python3.10[2761]: INFO 01-31 18:01:02 llm_engine.py:877] Avg prompt throughput...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: thot python3.10[2761]: INFO 01-31 18:00:57 llm_engine.py:877] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 9.7 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
