# vllm-project/vllm#19936: [Usage]: mac run vllm failed by docker 

| 字段 | 值 |
| --- | --- |
| Issue | [#19936](https://github.com/vllm-project/vllm/issues/19936) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: mac run vllm failed by docker 

### Issue 正文摘录

I searched the list of issues but to no avail ### logs ``` WARNING 06-21 08:32:55 arg_utils.py:1145] The model has a long context length (131072). This may cause OOM errors during the initial memory profiling phase, or result in low performance due to small KV cache space. Consider setting --max-model-len to a smaller value. WARNING 06-21 08:32:55 config.py:1148] Possibly too large swap space. 4.00 GiB out of the 7.74 GiB total CPU memory is allocated for the swap space. INFO 06-21 08:33:12 config.py:542] This model supports mult Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 911, in uvloop.run(run_server(args)) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: mac run vllm failed by docker usage;stale I searched the list of issues but to no avail ### logs ``` WARNING 06-21 08:32:55 arg_utils.py:1145] The model has a long context length (131072). This may cause OOM er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: mac run vllm failed by docker usage;stale I searched the list of issues but to no avail ### logs ``` WARNING 06-21 08:32:55 arg_utils.py:1145] The model has a long context length (131072). This may cause OOM er...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: to no avail ### logs ``` WARNING 06-21 08:32:55 arg_utils.py:1145] The model has a long context length (131072). This may cause OOM errors during the initial memory profiling phase, or result in low performance due to s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ls.py:1145] The model has a long context length (131072). This may cause OOM errors during the initial memory profiling phase, or result in low performance due to small KV cache space. Consider setting --max-model-len t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: mac run vllm failed by docker usage;stale I searched the list of issues but to no avail ### logs ``` WARNING 06-21 08:32:55 arg_utils.py:1145] The model has a long context length (131072). This may cause OOM er...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
