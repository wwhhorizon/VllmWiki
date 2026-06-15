# vllm-project/vllm#21454: [Bug]: Unable to deploy fixie-ai/ultravox-v0_6-gemma-3-27b and fixie-ai/ultravox-v0_6-qwen-3-32b using vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#21454](https://github.com/vllm-project/vllm/issues/21454) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to deploy fixie-ai/ultravox-v0_6-gemma-3-27b and fixie-ai/ultravox-v0_6-qwen-3-32b using vllm serve

### Issue 正文摘录

I am trying to deploy `fixie-ai/ultravox-v0_6-gemma-3-27b` using vllm (vllm/vllm-openai:v0.9.2) in k8s. But, the following error occurs regarding Gemma3 vocab_size. Can anyone help? Saw a related PR [#14687](https://github.com/vllm-project/vllm/issues/14687) but it didn't help ``` INFO 07-23 03:42:46 [__init__.py:244] Automatically detected platform cuda. INFO 07-23 03:42:51 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-23 03:42:51 [cli_args.py:325] non-default args: {'host': '0.0.0.0', 'uvicorn_log_level': 'warning', 'model': '/mnt/models/ultravox-27b', 'trust_remote_code': True, 'max_model_len': 4096, 'served_model_name': ['ultravox-27b'], 'enable_prefix_caching': True} Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 1495, in uvloop.run(run_server(args)) File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run return __asyncio.run( ^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run return runner.run(main) ^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/asyncio/runner...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Unable to deploy fixie-ai/ultravox-v0_6-gemma-3-27b and fixie-ai/ultravox-v0_6-qwen-3-32b using vllm serve bug;stale I am trying to deploy `fixie-ai/ultravox-v0_6-gemma-3-27b` using vllm (vllm/vllm-openai:v0.9.2)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: platform cuda. INFO 07-23 03:42:51 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-23 03:42:51 [cli_args.py:325] non-default args: {'host': '0.0.0.0', 'uvicorn_log_level': 'warning', 'model': '/mnt/models/ult...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `` INFO 07-23 03:42:46 [__init__.py:244] Automatically detected platform cuda. INFO 07-23 03:42:51 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-23 03:42:51 [cli_args.py:325] non-default args: {'host': '0.0...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Unable to deploy fixie-ai/ultravox-v0_6-gemma-3-27b and fixie-ai/ultravox-v0_6-qwen-3-32b using vllm serve bug;stale I am trying to deploy `fixie-ai/ultravox-v0_6-gemma-3-27b` using vllm (vllm/vllm-openai:v0.9.2)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 6-gemma-3-27b and fixie-ai/ultravox-v0_6-qwen-3-32b using vllm serve bug;stale I am trying to deploy `fixie-ai/ultravox-v0_6-gemma-3-27b` using vllm (vllm/vllm-openai:v0.9.2) in k8s. But, the following error occurs rega...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
