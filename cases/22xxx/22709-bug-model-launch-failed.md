# vllm-project/vllm#22709: [Bug]: Model launch failed

| 字段 | 值 |
| --- | --- |
| Issue | [#22709](https://github.com/vllm-project/vllm/issues/22709) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Model launch failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm version: 0.9.2 vllm serve nanonets/Nanonets-OCR-s --host 0.0.0.0 --port 10000 INFO 08-12 06:14:08 [cli_args.py:325] non-default args: {'host': '0.0.0.0', 'port': 10000, 'model': 'Nanonets-OCR'} Traceback (most recent call last): File "/root/miniconda3/envs/vllm/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/cli/main.py", line 65, in main args.dispatch_function(args) File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 55, in cmd uvloop.run(run_server(args)) File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run return runner.run(wrapper()) ^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/vllm/lib/python3.11/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper return await main ^^^^^^^^^^ File "/root/miniconda3/envs/vllm/l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: failed bug ### Your current environment ### 🐛 Describe the bug vllm version: 0.9.2 vllm serve nanonets/Nanonets-OCR-s --host 0.0.0.0 --port 10000 INFO 08-12 06:14:08 [cli_args.py:325] non-default args: {'host': '0.0.0.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Model launch failed bug ### Your current environment ### 🐛 Describe the bug vllm version: 0.9.2 vllm serve nanonets/Nanonets-OCR-s --host 0.0.0.0 --port 10000 INFO 08-12 06:14:08 [cli_args.py:325] non-default args
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 1/site-packages/vllm/entrypoints/cli/main.py", line 65, in main args.dispatch_function(args) File "/root/miniconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 55, in cmd uvloop.run(run_s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [type=assertion_error, input_value=ArgsKwargs((), {'model': ...attention_dtype': None}), input_type=ArgsKwargs] For further information visit https://errors.pydantic.dev/2.11/v/assertion_error ### Before submitting a ne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ror ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
