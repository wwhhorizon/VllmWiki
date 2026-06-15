# vllm-project/vllm#34322: [Bug]: Qwen3-Coder-Next模型结合qwen3_coder这个tool parser时，报错IndexError: list index out of range

| 字段 | 值 |
| --- | --- |
| Issue | [#34322](https://github.com/vllm-project/vllm/issues/34322) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Coder-Next模型结合qwen3_coder这个tool parser时，报错IndexError: list index out of range

### Issue 正文摘录

### Your current environment v0.15.0 ### 🐛 Describe the bug ``` vllm serve /llm_data2/Qwen3-Coder-Next/ --tensor-parallel-size 4 --served-model-name Qwen3-Coder-Next --trust-remote-code --enable-auto-tool-c hoice --tool-call-parser qwen3_coder --max-model-len auto --max-num-batched-tokens 4096 --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY "}' --gpu-memory-utilization 0.8 ``` ``` (Worker_TP0 pid=109) INFO 02-05 08:06:44 [acl_graph.py:185] Replaying aclgraph (Worker_TP2 pid=111) INFO 02-05 08:06:44 [acl_graph.py:185] Replaying aclgraph (Worker_TP1 pid=110) INFO 02-05 08:06:44 [acl_graph.py:185] Replaying aclgraph (APIServer pid=78) INFO 02-05 08:06:45 [loggers.py:257] Engine 000: Avg prompt throughput: 1852.2 tokens/s, Avg generation throughput: 3.1 tokens /s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 2.3%, Prefix cache hit rate: 0.0% (APIServer pid=78) ERROR 02-05 08:06:47 [serving_chat.py:1343] Error in chat completion stream generator. (APIServer pid=78) ERROR 02-05 08:06:47 [serving_chat.py:1343] Traceback (most recent call last): (APIServer pid=78) ERROR 02-05 08:06:47 [serving_chat.py:1343] File "/vllm-workspace/vllm/vllm/entrypoints/openai/serving_chat...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 型结合qwen3_coder这个tool parser时，报错IndexError: list index out of range bug;unstale ### Your current environment v0.15.0 ### 🐛 Describe the bug ``` vllm serve /llm_data2/Qwen3-Coder-Next/ --tensor-parallel-size 4 --served-mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Coder-Next模型结合qwen3_coder这个tool parser时，报错IndexError: list index out of range bug;unstale ### Your current environment v0.15.0 ### 🐛 Describe the bug ``` vllm serve /llm_data2/Qwen3-Coder-Next/ --tensor-par...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: max-model-len auto --max-num-batched-tokens 4096 --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY "}' --gpu-memory-utilization 0.8 ``` ``` (Worker_TP0 pid=109) INFO 02-05 08:06:44 [acl_graph.py:185] Replaying a...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: eration throughput: 3.1 tokens /s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 2.3%, Prefix cache hit rate: 0.0% (APIServer pid=78) ERROR 02-05 08:06:47 [serving_chat.py:1343] Error in chat completion stream g...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rver pid=78) INFO 02-05 08:06:45 [loggers.py:257] Engine 000: Avg prompt throughput: 1852.2 tokens/s, Avg generation throughput: 3.1 tokens /s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 2.3%, Prefix cache hi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
