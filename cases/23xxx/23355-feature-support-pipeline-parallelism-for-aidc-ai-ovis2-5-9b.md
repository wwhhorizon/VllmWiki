# vllm-project/vllm#23355: [Feature]: Support pipeline parallelism for AIDC-AI/Ovis2.5-9B

| 字段 | 值 |
| --- | --- |
| Issue | [#23355](https://github.com/vllm-project/vllm/issues/23355) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support pipeline parallelism for AIDC-AI/Ovis2.5-9B

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Can we add support for pipeline parallelism for this model? ``` (APIServer pid=42) INFO 08-21 10:25:00 [__init__.py:742] Resolved architecture: Ovis2_5 (APIServer pid=42) INFO 08-21 10:25:00 [__init__.py:1774] Using max model len 40960 (APIServer pid=42) INFO 08-21 10:25:01 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=42) Traceback (most recent call last): (APIServer pid=42) File "/usr/local/bin/vllm", line 10, in (APIServer pid=42) sys.exit(main()) (APIServer pid=42) ^^^^^^ (APIServer pid=42) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 54, in main (APIServer pid=42) args.dispatch_function(args) (APIServer pid=42) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer pid=42) uvloop.run(run_server(args)) (APIServer pid=42) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run (APIServer pid=42) return __asyncio.run( (APIServer pid=42) ^^^^^^^^^^^^^^ (APIServer pid=42) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=42) return runner.run(main) (AP...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Support pipeline parallelism for AIDC-AI/Ovis2.5-9B feature request ### 🚀 The feature, motivation and pitch Can we add support for pipeline parallelism for this model? ``` (APIServer pid=42) INFO 08-21 10:25:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vloop/__init__.py", line 109, in run (APIServer pid=42) return __asyncio.run( (APIServer pid=42) ^^^^^^^^^^^^^^ (APIServer pid=42) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=42) retur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Support pipeline parallelism for AIDC-AI/Ovis2.5-9B feature request ### 🚀 The feature, motivation and pitch Can we add support for pipeline parallelism for this model? ``` (APIServer pid=42) INFO 08-21 10:25:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tivation and pitch Can we add support for pipeline parallelism for this model? ``` (APIServer pid=42) INFO 08-21 10:25:00 [__init__.py:742] Resolved architecture: Ovis2_5 (APIServer pid=42) INFO 08-21 10:25:00 [__init__...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: m/entrypoints/cli/main.py", line 54, in main (APIServer pid=42) args.dispatch_function(args) (APIServer pid=42) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer pi...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
