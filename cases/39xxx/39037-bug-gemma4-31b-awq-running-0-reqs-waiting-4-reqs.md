# vllm-project/vllm#39037: [Bug]: gemma4-31B-AWQ Running: 0 reqs, Waiting: 4 reqs

| 字段 | 值 |
| --- | --- |
| Issue | [#39037](https://github.com/vllm-project/vllm/issues/39037) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;gemm;quantization |
| 症状 | crash;import_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gemma4-31B-AWQ Running: 0 reqs, Waiting: 4 reqs

### Issue 正文摘录

### Your current environment 4090 vllm 0.19.0 transformer 5.5.0 Driver Version: 570.211.01 CUDA Version: 12.8 ### 🐛 Describe the bug Apr 05 18:07:38 gpu4090d bash[59857]: (APIServer pid=59857) INFO 04-05 18:07:38 [loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 4 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, MM cache hit rate: 30.3% 模型： cyankiwi/gemma-4-31B-it-AWQ-4bit Running: 0 reqs, Waiting: 4 reqs，vLLM日志不再定时打印(APIServer pid=xxxxx) INFO，期间GPU零负载，过很长很长时间之后能恢复。 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ### Your current environment 4090 vllm 0.19.0 transformer 5.5.0 Driver Version: 570.211.01 CUDA Version: 12.8 ### 🐛 Describe the bug Apr 05 18:07:38 gpu4090d bash[59857]: (APIServer pid=59857) INFO 04-05 18:07:38 [logge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nment 4090 vllm 0.19.0 transformer 5.5.0 Driver Version: 570.211.01 CUDA Version: 12.8 ### 🐛 Describe the bug Apr 05 18:07:38 gpu4090d bash[59857]: (APIServer pid=59857) INFO 04-05 18:07:38 [loggers.py:259] Engine 000:...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 4 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, MM cache hit rate: 30.3% 模型： cyankiwi/gemma-4-31B-it-AWQ-4bit Running: 0 reqs, Waiting: 4 reqs，...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: gemma4-31B-AWQ Running: 0 reqs, Waiting: 4 reqs bug ### Your current environment 4090 vllm 0.19.0 transformer 5.5.0 Driver Version: 570.211.01 CUDA Version: 12.8 ### 🐛 Describe the bug Apr 05 18:07:38 gpu4090d ba...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r pid=59857) INFO 04-05 18:07:38 [loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 4 reqs, GPU KV cache usage: 0.0%, Prefix cache hit ra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
