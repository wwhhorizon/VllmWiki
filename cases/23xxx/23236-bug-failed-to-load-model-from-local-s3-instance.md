# vllm-project/vllm#23236: [Bug]: Failed to load model from local s3 instance

| 字段 | 值 |
| --- | --- |
| Issue | [#23236](https://github.com/vllm-project/vllm/issues/23236) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to load model from local s3 instance

### Issue 正文摘录

### Your current environment docker image `vllm-openai` version v1.10.1 ### 🐛 Describe the bug Loading a model from local s3 causes the following error on version v1.10.1: ``` INFO 08-19 23:09:31 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1) INFO 08-19 23:09:34 [api_server.py:1805] vLLM API server version 0.10.1 (APIServer pid=1) INFO 08-19 23:09:34 [utils.py:326] non-default args: {'model_tag': 's3://ai-prod.models/Qwen2.5-14B-Instruct', 'host': '0.0.0.0', 'enable_auto_tool_choice': True, 'tool_call_parser': 'hermes', 'model': 's3://ai-prod.models/Qwen2.5-14B-Instruct', 'dtype': 'bfloat16', 'served_model_name': ['Qwen/Qwen2.5-14B-Instruct'], 'load_format': 'runai_streamer', 'enable_prefix_caching': False} (APIServer pid=1) Traceback (most recent call last): (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/transformers/utils/hub.py", line 479, in cached_files (APIServer pid=1) hf_hub_download( (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/huggingface_hub/utils/_validators.py", line 106, in _inner_fn (APIServer pid=1) validate_repo_id(arg_value) (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/huggingface_h...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Failed to load model from local s3 instance bug ### Your current environment docker image `vllm-openai` version v1.10.1 ### 🐛 Describe the bug Loading a model from local s3 causes the following error on version v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d to load model from local s3 instance bug ### Your current environment docker image `vllm-openai` version v1.10.1 ### 🐛 Describe the bug Loading a model from local s3 causes the following error on version v1.10.1: ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: parser': 'hermes', 'model': 's3://ai-prod.models/Qwen2.5-14B-Instruct', 'dtype': 'bfloat16', 'served_model_name': ['Qwen/Qwen2.5-14B-Instruct'], 'load_format': 'runai_streamer', 'enable_prefix_caching': False} (APIServe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `` INFO 08-19 23:09:31 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1) INFO 08-19 23:09:34 [api_server.py:1805] vLLM API server version 0.10.1 (APIServer pid=1) INFO 08-19 23:09:34 [utils.py:32...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s/vllm/entrypoints/cli/main.py", line 54, in main (APIServer pid=1) args.dispatch_function(args) (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
