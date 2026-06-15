# vllm-project/vllm#27912: [Usage]: How should I use the CPU to deploy QWEN3 VL 30B-A3B?

| 字段 | 值 |
| --- | --- |
| Issue | [#27912](https://github.com/vllm-project/vllm/issues/27912) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How should I use the CPU to deploy QWEN3 VL 30B-A3B?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` (APIServer pid=1033476) Traceback (most recent call last): (APIServer pid=1033476) File "/home/maxgameone/anaconda3/bin/vllm", line 33, in (APIServer pid=1033476) sys.exit(load_entry_point('vllm==0.11.1rc6.dev33+g3a5de7d2d.cpu', 'console_scripts', 'vllm')()) (APIServer pid=1033476) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=1033476) File "/home/maxgameone/anaconda3/lib/python3.12/site-packages/vllm-0.11.1rc6.dev33+g3a5de7d2d.cpu-py3.12-linux-x86_64.egg/vllm/entrypoints/cli/main.py", line 73, in main (APIServer pid=1033476) args.dispatch_function(args) (APIServer pid=1033476) File "/home/maxgameone/anaconda3/lib/python3.12/site-packages/vllm-0.11.1rc6.dev33+g3a5de7d2d.cpu-py3.12-linux-x86_64.egg/vllm/entrypoints/cli/serve.py", line 59, in cmd (APIServer pid=1033476) uvloop.run(run_server(args)) (APIServer pid=1033476) File "/home/maxgameone/.local/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run (APIServer pid=1033476) return __asyncio.run( (APIServer pid=1033476) ^^^^^^^^^^^^^^ (APIServer pid=1033476) File "/home/maxgameone/anac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: /__init__.py", line 109, in run (APIServer pid=1033476) return __asyncio.run( (APIServer pid=1033476) ^^^^^^^^^^^^^^ (APIServer pid=1033476) File "/home/maxgameone/anaconda3/lib/python3.12/asyncio/runners.py", line 194,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How should I use the CPU to deploy QWEN3 VL 30B-A3B? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` (APIServer pid=1033476) Traceback (most recent call last): (APISer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rypoints/cli/main.py", line 73, in main (APIServer pid=1033476) args.dispatch_function(args) (APIServer pid=1033476) File "/home/maxgameone/anaconda3/lib/python3.12/site-packages/vllm-0.11.1rc6.dev33+g3a5de7d2d.cpu-py3....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How should I use the CPU to deploy QWEN3 VL 30B-A3B? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` (APIServer pid=1033476) Traceback (most recent call last): (APISer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
