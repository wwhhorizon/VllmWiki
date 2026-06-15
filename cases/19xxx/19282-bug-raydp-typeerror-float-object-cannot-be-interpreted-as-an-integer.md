# vllm-project/vllm#19282: [Bug]: RayDP: TypeError: 'float' object cannot be interpreted as an integer

| 字段 | 值 |
| --- | --- |
| Issue | [#19282](https://github.com/vllm-project/vllm/issues/19282) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RayDP: TypeError: 'float' object cannot be interpreted as an integer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve /data/deepseek-ai/DeepSeek-R1 -tp 4 -pp 4 --data-parallel-size 4 --data-parallel-size-local 0 --data-parallel-address 10.254.20.30 --data-parallel-rpc-port 5555 --data-parallel-backend ray ``` ``` Traceback (most recent call last): File "/data/kebe/conda/envs/vllm-dev/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/data/kebe/vllm/vllm/entrypoints/cli/main.py", line 59, in main args.dispatch_function(args) File "/data/kebe/vllm/vllm/entrypoints/cli/serve.py", line 58, in cmd uvloop.run(run_server(args)) File "/data/kebe/conda/envs/vllm-dev/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/data/kebe/conda/envs/vllm-dev/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/data/kebe/conda/envs/vllm-dev/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/data/kebe/conda/envs/vllm-dev/lib/python3.12/site-packages/uvloop/__init__.py", line 61, in wrapp...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: allel-address 10.254.20.30 --data-parallel-rpc-port 5555 --data-parallel-backend ray ``` ``` Traceback (most recent call last): File "/data/kebe/conda/envs/vllm-dev/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/data/kebe/conda/envs/vllm-dev/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: run_server_worker async with build_async_engine_client(args, client_config) as engine_client: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/kebe/conda/envs/vllm-dev/lib/python3.12/contextlib.py", line 210,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
