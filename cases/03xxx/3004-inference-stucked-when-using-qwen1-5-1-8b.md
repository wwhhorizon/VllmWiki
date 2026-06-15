# vllm-project/vllm#3004: inference stucked when using qwen1.5-1.8b

| 字段 | 值 |
| --- | --- |
| Issue | [#3004](https://github.com/vllm-project/vllm/issues/3004) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> inference stucked when using qwen1.5-1.8b

### Issue 正文摘录

start openai api server with ``` python -m vllm.entrypoints.openai.api_server --model Qwen1.5-1.8B-Chat --tensor-parallel-size 2 ``` and call api server with ``` client = OpenAI() client.chat.completions.create(...) ``` and GPU: 2\*A800 80G BUT the log is below ``` INFO 02-23 14:22:58 llm_engine.py:877] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 20 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 5.8%, CPU KV cache usage: 0.0% [33m(raylet)[0m [2024-02-23 14:23:05,101 E 2215919 2215949] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2024-02-23_14-03-32_516162_2215629 is over 95% full, available space: 22462472192; capacity: 470171115520. Object creation will fail if spilling is required. INFO 02-23 14:23:08 llm_engine.py:877] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 20 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 5.8%, CPU KV cache usage: 0.0% [33m(raylet)[0m [2024-02-23 14:23:15,104 E 2215919 2215949] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2024-02-23_14-03-32_516162_2215629 is over 95% full, available space: 22462230528; capacity: 4701711155...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: inference stucked when using qwen1.5-1.8b start openai api server with ``` python -m vllm.entrypoints.openai.api_server --model Qwen1.5-1.8B-Chat --tensor-parallel-size 2 ``` and call api server with ``` client = OpenAI...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 03-32_516162_2215629 is over 95% full, available space: 22462472192; capacity: 470171115520. Object creation will fail if spilling is required. INFO 02-23 14:23:08 llm_engine.py:877] Avg prompt throughput: 0.0 tokens/s,...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t: 0.0 tokens/s, Running: 20 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 5.8%, CPU KV cache usage: 0.0% [33m(raylet)[0m [2024-02-23 14:23:05,101 E 2215919 2215949] (raylet) file_system_monitor.cc:111:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: the log is below ``` INFO 02-23 14:22:58 llm_engine.py:877] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 20 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 5.8%, CPU...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
