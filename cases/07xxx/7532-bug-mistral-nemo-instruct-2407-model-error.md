# vllm-project/vllm#7532: [Bug]: Mistral-Nemo-Instruct-2407 Model Error

| 字段 | 值 |
| --- | --- |
| Issue | [#7532](https://github.com/vllm-project/vllm/issues/7532) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral-Nemo-Instruct-2407 Model Error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am working in a clean Wolfi docker container where I pip installed vllm and didn't do much else in the container. In this container, I can successfully run and ask questions for other models such as Mixtral 8x7B AWQ. I am trying to run the recent Mistral-Nemo-Instruct-2407 model. I am able to successfully start the server, but upon asking a basic question: ``` curl -X 'POST' 'http://localhost:8000/v1/chat/completions' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{ "messages": [ { "content": "Answer as Albert Einstein", "role": "system" }, { "content": "How are you today?", "role": "user" } ], "model": "Mistral-Nemo-Instruct-2407" }' ``` I get this error in the server: ``` Exception in callback _log_task_completion(error_callback= >)( ) at /home/nonroot/.local/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py:37 handle: >)( ) at /home/nonroot/.local/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py:37> Traceback (most recent call last): File "/home/nonroot/.local/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 47, in _log_task_completion return_value = task.resul...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nt environment ### 🐛 Describe the bug I am working in a clean Wolfi docker container where I pip installed vllm and didn't do much else in the container. In this container, I can successfully run and ask questions for o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Mistral-Nemo-Instruct-2407 Model Error bug;stale ### Your current environment ### 🐛 Describe the bug I am working in a clean Wolfi docker container where I pip installed vllm and didn't do much else in the contai...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: File "/home/nonroot/.local/lib/python3.11/site-packages/vllm/attention/backends/xformers.py", line 603, in forward out = PagedAttention.forward_prefix( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/nonroot/.local/lib/pytho...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: an Wolfi docker container where I pip installed vllm and didn't do much else in the container. In this container, I can successfully run and ask questions for other models such as Mixtral 8x7B AWQ. I am trying to run th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Mistral-Nemo-Instruct-2407 Model Error bug;stale ### Your current environment ### 🐛 Describe the bug I am working in a clean Wolfi docker container where I pip installed vllm and didn't do much else in the contai...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
