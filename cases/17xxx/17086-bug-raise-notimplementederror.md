# vllm-project/vllm#17086: [Bug]: raise NotImplementedError

| 字段 | 值 |
| --- | --- |
| Issue | [#17086](https://github.com/vllm-project/vllm/issues/17086) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: raise NotImplementedError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/workspace/alg/vllm_source/vllm/entrypoints/openai/api_server.py", line 1130, in uvloop.run(run_server(args)) File "/opt/conda/envs/llm-bench/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/opt/conda/envs/llm-bench/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/opt/conda/envs/llm-bench/lib/python3.12/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete File "/opt/conda/envs/llm-bench/lib/python3.12/site-packages/uvloop/__init__.py", line 61, in wrapper return await main ^^^^^^^^^^ File "/workspace/alg//vllm_source/vllm/entrypoints/openai/api_server.py", line 1078, in run_server async with build_async_engine_client(args) as engine_client: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/envs/llm-bench/lib/python3.12/contextlib.py", line 210, in __aenter__ return awai...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: .12/site-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/opt/conda/envs/llm-bench/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: er.py", line 166, in build_async_engine_client_from_engine_args vllm_config = engine_args.create_engine_config(usage_context=usage_context) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/workspace/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cpu ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: raise NotImplementedError bug;stale ### Your current environment ### 🐛 Describe the bug Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/workspa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;import_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
