# vllm-project/vllm#35847: [Performance]: The checkpoint you are trying to load has model type `qwen3_5` but Transformers does not recognize this architecture.

| 字段 | 值 |
| --- | --- |
| Issue | [#35847](https://github.com/vllm-project/vllm/issues/35847) |
| 状态 | open |
| 标签 | performance |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: The checkpoint you are trying to load has model type `qwen3_5` but Transformers does not recognize this architecture.

### Issue 正文摘录

### Proposal to improve performance raceback (most recent call last): (APIServer pid=184467) File "/home/ubuntu/qwen/qwenvenv/bin/vllm", line 8, in (APIServer pid=184467) sys.exit(main()) (APIServer pid=184467) File "/home/ubuntu/qwen/qwenvenv/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 73, in main (APIServer pid=184467) args.dispatch_function(args) (APIServer pid=184467) File "/home/ubuntu/qwen/qwenvenv/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 111, in cmd (APIServer pid=184467) uvloop.run(run_server(args)) (APIServer pid=184467) File "/home/ubuntu/qwen/qwenvenv/lib/python3.10/site-packages/uvloop/__init__.py", line 69, in run (APIServer pid=184467) return loop.run_until_complete(wrapper()) (APIServer pid=184467) File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete (APIServer pid=184467) File "/home/ubuntu/qwen/qwenvenv/lib/python3.10/site-packages/uvloop/__init__.py", line 48, in wrapper (APIServer pid=184467) return await main (APIServer pid=184467) File "/home/ubuntu/qwen/qwenvenv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 457, in run_server (APIServer pid=184467) await run_server_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: The checkpoint you are trying to load has model type `qwen3_5` but Transformers does not recognize this architecture. performance ### Proposal to improve performance raceback (most recent call last): (API...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: y", line 476, in run_server_worker (APIServer pid=184467) async with build_async_engine_client( (APIServer pid=184467) File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__ (APIServer pid=184467) return awai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ttps://errors.pydantic.dev/2.12/v/value_error ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: trypoints/cli/main.py", line 73, in main (APIServer pid=184467) args.dispatch_function(args) (APIServer pid=184467) File "/home/ubuntu/qwen/qwenvenv/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 111,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: o load has model type `qwen3_5` but Transformers does not recognize this architecture. performance ### Proposal to improve performance raceback (most recent call last): (APIServer pid=184467) File "/home/ubuntu/qwen/qwe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
