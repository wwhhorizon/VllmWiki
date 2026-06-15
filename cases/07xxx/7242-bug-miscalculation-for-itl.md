# vllm-project/vllm#7242: [Bug]: Miscalculation for ITL

| 字段 | 值 |
| --- | --- |
| Issue | [#7242](https://github.com/vllm-project/vllm/issues/7242) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Miscalculation for ITL

### Issue 正文摘录

### Your current environment This bug is irrelevant to environment. ### 🐛 Describe the bug Thanks for open source such a excellent project! I found it possibly misses an "else" in the async_request_openai_completions function of 'benchmarks /backend_request_func.py'. ``` if data["choices"][0]["text"]: timestamp = time.perf_counter() # First token if ttft == 0.0: ttft = time.perf_counter() - st output.ttft = ttft # Decoding phase # Missing 'else:' here !!!! output.itl.append(timestamp - most_recent_timestamp) most_recent_timestamp = timestamp generated_text += data["choices"][0]["text"] ``` It cause the function incorrectly append TTFT into ITL list. Curiously, I saw others request function in the file have this conditional statement. By the way, I found most of articles said TPOT is same as ITL. Could you tell me what's the difference between TPOT and ITL in the benchmark of vllm? Thanks a lot.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ly misses an "else" in the async_request_openai_completions function of 'benchmarks /backend_request_func.py'. ``` if data["choices"][0]["text"]: timestamp = time.perf_counter() # First token
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: "else" in the async_request_openai_completions function of 'benchmarks /backend_request_func.py'. ``` if data["choices"][0]["text"]: timestamp = time.perf_counter() # First token
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: or open source such a excellent project! I found it possibly misses an "else" in the async_request_openai_completions function of 'benchmarks /backend_request_func.py'. ``` if data["choices"][0]["text"]: timestamp = tim...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: h a excellent project! I found it possibly misses an "else" in the async_request_openai_completions function of 'benchmarks /backend_request_func.py'. ``` if data["choices"][0]["text"]: timestamp = time.perf_counter()

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
