# vllm-project/vllm#9737: [Bug]: "Address already in use" for 1 minute after crash (since 0.6.2)

| 字段 | 值 |
| --- | --- |
| Issue | [#9737](https://github.com/vllm-project/vllm/issues/9737) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: "Address already in use" for 1 minute after crash (since 0.6.2)

### Issue 正文摘录

### 🐛 Describe the bug Since version 0.6.2 (happens also in 0.6.3.post1), after the server dies (due to an exception/crash or hitting ctrl-c), for about a minute, it fails to start again with: ``` Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/home/user/code/debug/.venv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 585, in uvloop.run(run_server(args)) File "/home/user/code/debug/.venv/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run return loop.run_until_complete(wrapper()) File "uvloop/loop.pyx", line 1517, in uvloop.loop.Loop.run_until_complete File "/home/user/code/debug/.venv/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper return await main File "/home/user/code/debug/.venv/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 544, in run_server sock.bind(("", args.port)) OSError: [Errno 98] Address already in use ``` This prolongs recovery from crashes. In example upon crash Kubernetes immediately resta...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: starts the container - previously it would immediately start loading the model again, but now it will do several crash/restart loops until the port is freed. Verified it happens also with `--disable-frontend-multiproces...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Verified it happens also with `--disable-frontend-multiprocessing`. To reproduce it, start vllm with default args, in example: ``` python -m vllm.entrypoints.openai.api_server --model TinyLlama/TinyLlama-1.1B-Chat-v1.0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: for 1 minute after crash (since 0.6.2) bug ### 🐛 Describe the bug Since version 0.6.2 (happens also in 0.6.3.post1), after the server dies (due to an exception/crash or hitting ctrl-c), for about a minute, it fails to s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nyLlama-1.1B-Chat-v1.0 ``` and then send at least one chat or completion request to it (without this it won't reproduce). then hit Ctrl-C to kill the server. starting vllm again should throw the "Address already in use"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
