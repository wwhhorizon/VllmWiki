# vllm-project/vllm#42363: [Bug]: EngineDeadError with Kimi-K2.6 model using vLLM 0.20.2

| 字段 | 值 |
| --- | --- |
| Issue | [#42363](https://github.com/vllm-project/vllm/issues/42363) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EngineDeadError with Kimi-K2.6 model using vLLM 0.20.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash vllm serve /app/model --trust-remote-code --served-model-name Kimi-K2.6 --trust-remote-code --tensor-parallel-size 4 --attention-config.use_trtllm_ragged_deepseek_prefill=True --tool-call-parser kimi_k2 --enable-auto-tool-choice --reasoning-parser kimi_k2 --gpu-memory-utilization 0.93 --host 0.0.0.0 --port 8000 ``` and log is： ```txt (APIServer pid=1) INFO 05-12 01:46:22 [loggers.py:271] Engine 000: Avg prompt throughput: 75.3 tokens/s, Avg generation throughput: 34.4 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 96.3%, MM cache hit rate: 98.2% (APIServer pid=1) INFO: 10.1.6.81:16983 - "POST /v1/messages?beta=true HTTP/1.1" 200 OK (APIServer pid=1) INFO: 10.1.6.81:16983 - "POST /v1/messages?beta=true HTTP/1.1" 200 OK (APIServer pid=1) INFO: 10.1.6.81:38671 - "GET /metrics HTTP/1.1" 200 OK ... ... ... (APIServer pid=1) INFO 05-12 01:47:42 [loggers.py:271] Engine 000: Avg prompt throughput: 68.4 tokens/s, Avg generation throughput: 58.6 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 33.5%, Prefix cache hit rate: 96.4%, MM cache hit rate: 98.1% (APIServer pid=1)...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: e --tensor-parallel-size 4 --attention-config.use_trtllm_ragged_deepseek_prefill=True --tool-call-parser kimi_k2 --enable-auto-tool-choice --reasoning-parser kimi_k2 --gpu-memory-utilization 0.93 --host 0.0.0.0 --port 8...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding attent...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: EngineDeadError with Kimi-K2.6 model using vLLM 0.20.2 bug ### Your current environment ### 🐛 Describe the bug ```bash vllm serve /app/model --trust-remote-code --served-model-name Kimi-K2.6 --trust-remote-code -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: eration throughput: 34.4 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 96.3%, MM cache hit rate: 98.2% (APIServer pid=1) INFO: 10.1.6.81:16983 - "POST /v1/messages?beta=tru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
