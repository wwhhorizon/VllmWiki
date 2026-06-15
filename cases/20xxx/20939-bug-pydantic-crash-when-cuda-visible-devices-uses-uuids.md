# vllm-project/vllm#20939: [Bug]: pydantic crash when CUDA_VISIBLE_DEVICES uses UUIDs

| 字段 | 值 |
| --- | --- |
| Issue | [#20939](https://github.com/vllm-project/vllm/issues/20939) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: pydantic crash when CUDA_VISIBLE_DEVICES uses UUIDs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With the CUDA_VISIBLE_DEVICES environment variable containing one GPU UUID. I got the following from `kubectl logs` of the Pod. ``` INFO 07-11 12:19:33 [__init__.py:244] Automatically detected platform cuda. WARNING 07-11 12:19:37 [api_server.py:913] SECURITY WARNING: Development endpoints are enabled! This should NOT be used in production! INFO 07-11 12:19:37 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-11 12:19:37 [cli_args.py:325] non-default args: {'host': '0.0.0.0', 'model': 'ibm-granite/granite-3.3-2b-instruct', 'enable_sleep_mode': True} INFO 07-11 12:19:43 [config.py:841] This model supports multiple tasks: {'generate', 'classify', 'reward', 'embed'}. Defaulting to 'generate'. Traceback (most recent call last): File "/usr/local/bin/vllm", line 10, in sys.exit(main()) ^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 65, in main args.dispatch_function(args) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 55, in cmd uvloop.run(run_server(args)) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run return __a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: in production! INFO 07-11 12:19:37 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-11 12:19:37 [cli_args.py:325] non-default args: {'host': '0.0.0.0', 'model': 'ibm-granite/granite-3.3-2b-instruct', 'enable_s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 07-11 12:19:37 [cli_args.py:325] non-default args: {'host': '0.0.0.0', 'model': 'ibm-granite/granite-3.3-2b-instruct', 'enable_sleep_mode': True} INFO 07-11 12:19:43 [config.py:841] This model supports multiple tasks: {...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: pydantic crash when CUDA_VISIBLE_DEVICES uses UUIDs bug;stale ### Your current environment ### 🐛 Describe the bug With the CUDA_VISIBLE_DEVICES environment variable containing one GPU UUID. I got the following fr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2/dist-packages/vllm/entrypoints/cli/main.py", line 65, in main args.dispatch_function(args) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 55, in cmd uvloop.run(run_server(args)) Fil...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 78' [type=value_error, input_value=ArgsKwargs((), {'model': ...attention_dtype': None}), input_type=ArgsKwargs] For further information visit https://errors.pydantic.dev/2.11/v/value_error ``` I found Issue #6551 and PR...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
