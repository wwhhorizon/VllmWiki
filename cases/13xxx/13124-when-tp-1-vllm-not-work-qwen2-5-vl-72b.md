# vllm-project/vllm#13124: When tp>1 vllm not work （Qwen2.5-VL-72B）

| 字段 | 值 |
| --- | --- |
| Issue | [#13124](https://github.com/vllm-project/vllm/issues/13124) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When tp>1 vllm not work （Qwen2.5-VL-72B）

### Issue 正文摘录

Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/home/lzh/anaconda3/envs/qwen25vl/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 911, in uvloop.run(run_server(args)) File "/home/lzh/anaconda3/envs/qwen25vl/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/home/lzh/anaconda3/envs/qwen25vl/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/home/lzh/anaconda3/envs/qwen25vl/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/home/lzh/anaconda3/envs/qwen25vl/lib/python3.12/site-packages/uvloop/__init__.py", line 61, in wrapper return await main ^^^^^^^^^^ File "/home/lzh/anaconda3/envs/qwen25vl/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 875, in run_server async with build_async_engine_client(args) as engine_client: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/lzh/anaconda3/envs/qwen25vl/lib/pytho...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/home/lzh/anaconda3/envs/qwen25vl/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: When tp>1 vllm not work （Qwen2.5-VL-72B） stale Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/home/lzh/anaconda3/envs/qwen25vl/lib/python3.12/site-pa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: When tp>1 vllm not work （Qwen2.5-VL-72B） stale Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/home/lzh/anaconda3/envs/qwen25vl/lib/python3.12/site-pa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
