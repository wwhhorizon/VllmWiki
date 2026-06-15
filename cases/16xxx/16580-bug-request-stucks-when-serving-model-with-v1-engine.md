# vllm-project/vllm#16580: [Bug]: Request stucks when serving model with v1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#16580](https://github.com/vllm-project/vllm/issues/16580) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Request stucks when serving model with v1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to serve `ibm-research/PowerMoE-3b` model with the following command: `VLLM_USE_V1=1 vllm serve ibm-research/PowerMoE-3b --trust-remote-code --load-format dummy --tensor-parallel-size=1 --data-parallel-size=2 --gpu-memory-utilization=0.9 --disable-log-requests 2>&1 | tee -a dp_2_lite.log` But when making a request the following request: ``` curl http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{ "model": "ibm-research/PowerMoE-3b", "prompt": [ "You are a helpful assistant. Who won the world series in 2020?" ], "max_tokens": 2 }' ``` I can't receive any response, it stucks. The log appears as following: ``` INFO 04-14 08:14:07 [launcher.py:34] Route: /v1/rerank, Methods: POST INFO 04-14 08:14:07 [launcher.py:34] Route: /v2/rerank, Methods: POST INFO 04-14 08:14:07 [launcher.py:34] Route: /invocations, Methods: POST INFO: Started server process [2459897] INFO: Waiting for application startup. INFO: Application startup complete. [1;36m(EngineCore_1 pid=2461252)[0;0m DEBUG 04-14 08:14:10 [core.py:445] EngineCore starting idle loop. [1;36m(EngineCore_1 pid=2461252)[0;0m DEBUG 04-14 08:14:10...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Request stucks when serving model with v1 engine bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to serve `ibm-research/PowerMoE-3b` model with the following command: `VLLM_USE_V1=1 vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding cache;cuda;operator;triton build_e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt environment ### 🐛 Describe the bug I am trying to serve `ibm-research/PowerMoE-3b` model with the following command: `VLLM_USE_V1=1 vllm serve ibm-research/PowerMoE-3b --trust-remote-code --load-format dummy --tensor...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% INFO 04-14 08:14:17 [loggers.py:87] Engine 001: Avg prompt throughput: 0.0 tokens/s, Avg generat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Request stucks when serving model with v1 engine bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to serve `ibm-research/PowerMoE-3b` model with the following command: `VLLM_USE_V1=1 vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
