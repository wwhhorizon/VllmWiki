# vllm-project/vllm#43222: [Bug]: Possible to get GPU OOM for DP/EP

| 字段 | 值 |
| --- | --- |
| Issue | [#43222](https://github.com/vllm-project/vllm/issues/43222) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;moe |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Possible to get GPU OOM for DP/EP

### Issue 正文摘录

### Your current environment - running on `wentao-feature-local-external-dp` ### 🐛 Describe the bug ```bash MODEL := "deepseek-ai/DeepSeek-V2-lite" launch: chg run --gpus 2 -- vllm serve \ {{MODEL}} \ --port 8000 \ --data-parallel-supervisor-port 7999 \ --enable-expert-parallel \ --data-parallel-size 2 \ --data-parallel-size-local 2 \ --data-parallel-start-rank 0 \ --data-parallel-multi-port-external-lb \ --enforce-eager \ --shutdown-timeout 15 eval PORT: lm_eval \ --model local-completions \ --model_args "base_url=http://127.0.0.1:{{PORT}}/v1/completions,model={{MODEL}},num_concurrent=1024,num_retries=0" \ --tasks gsm8k probe_health: curl -vvv GET http://localhost:7999/health ``` run lm_eval a couple times on each port ``` just eval 8000 just eval 8001 ``` ```bash (APIServer_DP1 pid=2646203) INFO: 127.0.0.1:32908 - "GET /health HTTP/1.1" 200 OK (APIServer_DP1 pid=2646203) INFO 05-20 10:42:11 [loggers.py:271] Engine 001: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 2226.2 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 99.1% (APIServer_DP0 pid=2646202) INFO 05-20 10:42:11 [loggers.py:271] Engine 000: Avg prompt throug...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 0 tokens/s, Avg generation throughput: 2226.2 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 99.1% (APIServer_DP0 pid=2646202) INFO 05-20 10:42:11 [loggers.py:271] Engine 00...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r 'CUDA out of memory. Tried to allocate 4.69 GiB. GPU 0 has a total capacity of 79.18 GiB of which 4.48 GiB is free. Including non-PyTorch memory, this process has 74.69 GiB memory in use. Of the allocated memory 71.91...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ns,model={{MODEL}},num_concurrent=1024,num_retries=0" \ --tasks gsm8k probe_health: curl -vvv GET http://localhost:7999/health ``` run lm_eval a couple times on each port ``` just eval 8000 just eval 8001 ``` ```bash (A...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Possible to get GPU OOM for DP/EP bug ### Your current environment - running on `wentao-feature-local-external-dp` ### 🐛 Describe the bug ```bash MODEL := "deepseek-ai/DeepSeek-V2-lite" launch: chg run --gpus 2 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g on `wentao-feature-local-external-dp` ### 🐛 Describe the bug ```bash MODEL := "deepseek-ai/DeepSeek-V2-lite" launch: chg run --gpus 2 -- vllm serve \ {{MODEL}} \ --port 8000 \ --data-parallel-supervisor-port 7999 \ --...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
