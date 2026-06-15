# vllm-project/vllm#24587: [Bug]: use disagg_example_p2p_nccl_xpyd.sh, 每次pd 分离的实例，p和d 只能启动成功一个，另一个就报下面的错，大佬帮忙看看

| 字段 | 值 |
| --- | --- |
| Issue | [#24587](https://github.com/vllm-project/vllm/issues/24587) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: use disagg_example_p2p_nccl_xpyd.sh, 每次pd 分离的实例，p和d 只能启动成功一个，另一个就报下面的错，大佬帮忙看看

### Issue 正文摘录

### Your current environment @KuntaiDu 大佬瞅一眼， [Bug]: use disagg_example_p2p_nccl_xpyd.sh, 每次pd 分离的实例，p和d 只能启动成功一个，另一个就报下面的错，大佬帮忙看看 INFO 09-10 21:20:09 [__init__.py:1152] Found nccl from library libnccl.so.2 Traceback (most recent call last): File "/opt/ac2/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/opt/ac2/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 65, in main args.dispatch_function(args) File "/opt/ac2/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 55, in cmd uvloop.run(run_server(args)) File "/opt/ac2/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/opt/ac2/lib/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/opt/ac2/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/opt/ac2/lib/python3.12/site-packages/uvloop/__init__.py", line 61, in wrapper return await main ^^^^^^^^^^ File "/opt/ac2/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 14...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/opt/ac2/lib/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/opt/ac2/li...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2/site-packages/vllm/entrypoints/cli/main.py", line 65, in main args.dispatch_function(args) File "/opt/ac2/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 55, in cmd uvloop.run(run_server(args)) File...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: no ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: run_server_worker async with build_async_engine_client(args, client_config) as engine_client: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/ac2/lib/python3.12/contextlib.py", line 210, in __aenter__ return a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g_example_p2p_nccl_xpyd.sh, 每次pd 分离的实例，p和d 只能启动成功一个，另一个就报下面的错，大佬帮忙看看 bug;stale ### Your current environment @KuntaiDu 大佬瞅一眼， [Bug]: use disagg_example_p2p_nccl_xpyd.sh, 每次pd 分离的实例，p和d 只能启动成功一个，另一个就报下面的错，大佬帮忙看看 INFO 09-1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
