# vllm-project/vllm#21776: [Bug]: vLLM v0.10.0 vllm.ray package is being imported instead of the actual Ray library

| 字段 | 值 |
| --- | --- |
| Issue | [#21776](https://github.com/vllm-project/vllm/issues/21776) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM v0.10.0 vllm.ray package is being imported instead of the actual Ray library

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Vllm startup failed (see Error log) due to naming conflict after upgrading to v0.10.0. ``` Exception has occurred: AttributeError (note: full exception trace is shown but execution is paused at: _run_module_as_main) module 'ray' has no attribute 'is_initialized' File "/opt/pytorch/lib/python3.12/site-packages/vllm/utils/__init__.py", line 2872, in is_in_ray_actor return (ray.is_initialized() ^^^^^^^^^^^^^^^^^^ File "/opt/pytorch/lib/python3.12/site-packages/vllm/engine/arg_utils.py", line 1067, in create_engine_config if is_in_ray_actor(): ^^^^^^^^^^^^^^^^^ File "/opt/pytorch/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client_from_engine_args vllm_config = engine_args.create_engine_config(usage_context=usage_context) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/contextlib.py", line 210, in __aenter__ return await anext(self.gen) ^^^^^^^^^^^^^^^^^^^^^ File "/opt/pytorch/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 158, in build_async_engine_client engine_args, args.disable_frontend_multiprocessing,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: vLLM v0.10.0 vllm.ray package is being imported instead of the actual Ray library bug;ray ### Your current environment ### 🐛 Describe the bug Vllm startup failed (see Error log) due to naming conflict after upgra...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: .12/site-packages/vllm/engine/arg_utils.py", line 1067, in create_engine_config if is_in_ray_actor(): ^^^^^^^^^^^^^^^^^ File "/opt/pytorch/lib/python3.12/site-packages/vllm/entrypoints/openai/api_server.py", line 180, i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2/site-packages/vllm/entrypoints/cli/main.py", line 54, in main args.dispatch_function(args) File "/opt/pytorch/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/usr/local/lib/python3.12/runpy.py", line 88, in _run_c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
