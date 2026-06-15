# vllm-project/vllm#22424: [Bug]: Voxtral-Small-24B-2507 Does Not Support Pipeline-Parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#22424](https://github.com/vllm-project/vllm/issues/22424) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Voxtral-Small-24B-2507 Does Not Support Pipeline-Parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug As per the [documentation](https://docs.vllm.ai/en/latest/models/supported_models.html#transcription), Voxtral is indicated to support pipeline-parallel execution. However, when I attempted to launch vllm using the -pp 5 command to enable pipeline parallelism with 5 partitions, I encountered the following error: ``` INFO 08-06 21:09:51 [__init__.py:235] Automatically detected platform cuda. INFO 08-06 21:09:54 [api_server.py:1755] vLLM API server version 0.10.1.dev0+g6d8d0a24c.d20250726 INFO 08-06 21:09:54 [cli_args.py:261] non-default args: {'enable_auto_tool_choice': True, 'tool_call_parser': 'mistral', 'model': 'mistralai/Voxtral-Small-24B-2507', 'tokenizer_mode': 'mistral', 'config_format': 'mistral', 'load_format': 'mistral', 'pipeline_parallel_size': 5} Parse safetensors files: 100%|██████████| 11/11 [00:05 ", line 198, in _run_module_as_main [rank0]: File " ", line 88, in _run_code [rank0]: File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/api_server.py", line 1856, in [rank0]: uvloop.run(run_server(args)) [rank0]: File "/usr/local/lib/python3.12/dist-packages/uvloop/__init__.py", line 109, in run [rank...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: platform cuda. INFO 08-06 21:09:54 [api_server.py:1755] vLLM API server version 0.10.1.dev0+g6d8d0a24c.d20250726 INFO 08-06 21:09:54 [cli_args.py:261] non-default args: {'enable_auto_tool_choice': True, 'tool_call_parse...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: cribe the bug As per the [documentation](https://docs.vllm.ai/en/latest/models/supported_models.html#transcription), Voxtral is indicated to support pipeline-parallel execution. However, when I attempted to launch vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Voxtral-Small-24B-2507 Does Not Support Pipeline-Parallel bug;stale ### Your current environment ### 🐛 Describe the bug As per the [documentation](https://docs.vllm.ai/en/latest/models/supported_models.html#trans...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;speculative_decoding attention;cuda;operator;quantization;triton build_error;crash dtype;env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Voxtral-Small-24B-2507 Does Not Support Pipeline-Parallel bug;stale ### Your current environment ### 🐛 Describe the bug As per the [documentation](https://docs.vllm.ai/en/latest/models/supported_models.html#trans...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
