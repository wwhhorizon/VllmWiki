# vllm-project/vllm#13285: [Bug]: Qwen2.5-VL broke due to transformers upstream changes

| 字段 | 值 |
| --- | --- |
| Issue | [#13285](https://github.com/vllm-project/vllm/issues/13285) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL broke due to transformers upstream changes

### Issue 正文摘录

### Your current environment Not relevant ### 🐛 Describe the bug When you follow the official docs for `Qwen-2.5-VL`, you get the following error: ``` Traceback (most recent call last): File "/myenv/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/myenv/lib/python3.12/site-packages/vllm/scripts.py", line 204, in main args.dispatch_function(args) File "/myenv/lib/python3.12/site-packages/vllm/scripts.py", line 44, in serve uvloop.run(run_server(args)) File "/myenv/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/root/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/root/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/myenv/lib/python3.12/site-packages/uvloop/__init__.py", line 61, in wrapper return await main ^^^^^^^^^^ File "/myenv/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen2.5-VL broke due to transformers upstream changes bug ### Your current environment Not relevant ### 🐛 Describe the bug When you follow the official docs for `Qwen-2.5-VL`, you get the following error: ``` Tra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vironment Not relevant ### 🐛 Describe the bug When you follow the official docs for `Qwen-2.5-VL`, you get the following error: ``` Traceback (most recent call last): File "/myenv/bin/vllm", line 8, in sys.exit(main())...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ib/python3.12/site-packages/vllm/scripts.py", line 204, in main args.dispatch_function(args) File "/myenv/lib/python3.12/site-packages/vllm/scripts.py", line 44, in serve uvloop.run(run_server(args)) File "/myenv/lib/py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 424, in _init_multimodal_config if ModelRegistry.is_multimodal_model(architectures): ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/myenv/lib/python3.12/site-packages/vllm/model_executor/models/registry.py", li...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
