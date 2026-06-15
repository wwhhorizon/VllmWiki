# vllm-project/vllm#24313: [Bug]: Starting from v0.10.1 model can't be loaded from s3

| 字段 | 值 |
| --- | --- |
| Issue | [#24313](https://github.com/vllm-project/vllm/issues/24313) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Starting from v0.10.1 model can't be loaded from s3

### Issue 正文摘录

### Your current environment production-stack + vllm ### 🐛 Describe the bug The following log is self-describing ``` (APIServer pid=1) INFO 09-05 03:10:33 [api_server.py:1805] vLLM API server version 0.10.1 (APIServer pid=1) INFO 09-05 03:10:33 [utils.py:326] non-default args: {'model_tag': 's3://h2o-models/llmops/h2o-danube3-500m-chat/', 'host': '0.0.0.0', 'model': 's3://h2o-models/llmops/h2o-danube3-500m-chat/', 'trust_remote_code': True, 'load_format': 'runai_streamer', 'gpu_memory_utilization': 0.6, 'enable_prefix_caching': False} (APIServer pid=1) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=1) Traceback (most recent call last): (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/transformers/utils/hub.py", line 479, in cached_files (APIServer pid=1) hf_hub_download( (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/huggingface_hub/utils/_validators.py", line 106, in _inner_fn (APIServer pid=1) validate_repo_id(arg_value) (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/huggingface_hub/utils/_validators.py", line 154, in validate_repo_id (APIServer pid=1) raise H...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Starting from v0.10.1 model can't be loaded from s3 bug ### Your current environment production-stack + vllm ### 🐛 Describe the bug The following log is self-describing ``` (APIServer pid=1) INFO 09-05 03:10:33 [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: PIServer pid=1) INFO 09-05 03:10:33 [api_server.py:1805] vLLM API server version 0.10.1 (APIServer pid=1) INFO 09-05 03:10:33 [utils.py:326] non-default args: {'model_tag': 's3://h2o-models/llmops/h2o-danube3-500m-chat/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: lm/entrypoints/cli/main.py", line 54, in main (APIServer pid=1) args.dispatch_function(args) (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer pid...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nai_streamer', 'gpu_memory_utilization': 0.6, 'enable_prefix_caching': False} (APIServer pid=1) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=1) T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
