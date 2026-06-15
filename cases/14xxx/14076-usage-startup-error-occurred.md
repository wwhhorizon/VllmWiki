# vllm-project/vllm#14076: [Usage]: Startup error occurred

| 字段 | 值 |
| --- | --- |
| Issue | [#14076](https://github.com/vllm-project/vllm/issues/14076) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Startup error occurred

### Issue 正文摘录

### Your current environment INFO 03-01 15:15:27 [parallel_state.py:948] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0 Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00 sys.exit(load_entry_point('vllm==0.7.4.dev119+gca377cf1.cpu', 'console_scripts', 'vllm')()) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/vllm_env/lib/python3.12/site-packages/vllm-0.7.4.dev119+gca377cf1.cpu-py3.12-linux-x86_64.egg/vllm/entrypoints/cli/main.py", line 73, in main args.dispatch_function(args) File "/opt/vllm_env/lib/python3.12/site-packages/vllm-0.7.4.dev119+gca377cf1.cpu-py3.12-linux-x86_64.egg/vllm/entrypoints/cli/serve.py", line 34, in cmd uvloop.run(run_server(args)) File "/opt/vllm_env/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 194, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ere appear to be %d ' (vllm_env) bouyei@bouyei-ai-1:/opt$ vllm serve "./models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B" --max-model-len=1024 --sarved-model-name DeepSeek-R1-Distill-Qwen-14B INFO 03-01 15:51:57 [__init_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: inux-x86_64.egg/vllm/entrypoints/cli/main.py", line 73, in main args.dispatch_function(args) File "/opt/vllm_env/lib/python3.12/site-packages/vllm-0.7.4.dev119+gca377cf1.cpu-py3.12-linux-x86_64.egg/vllm/entrypoints/cli/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 024 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
