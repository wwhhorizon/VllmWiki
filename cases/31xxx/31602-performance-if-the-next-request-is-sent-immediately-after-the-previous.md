# vllm-project/vllm#31602: [Performance]: If the next request is sent immediately after the previous one finishes, its TTFT will be relatively small; if the next request is sent 10 seconds after the previous one ends, its TTFT will be relatively large.

| 字段 | 值 |
| --- | --- |
| Issue | [#31602](https://github.com/vllm-project/vllm/issues/31602) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: If the next request is sent immediately after the previous one finishes, its TTFT will be relatively small; if the next request is sent 10 seconds after the previous one ends, its TTFT will be relatively large.

### Issue 正文摘录

### Question **If I send requests continuously (one after another), TTFT keeps dropping and soon stays flat. If I insert a gap of only a few seconds (e.g. 10 s) between requests, every request suffers a large TTFT again.** --- **I start the server with** ` - python -m vllm.entrypoints.openai.api_server \ - --model /workspace/models/Qwen3-4B-AWQ \ - --served-model-name Qwen3-4B-AWQ \ - --host 0.0.0.0 \ - --port 8000 ` --- **Below are the logs after I started the service：** ` root@localhost:/workspace# python -m vllm.entrypoints.openai.api_server \ --model /workspace/models/Qwen3-4B-AWQ \ --served-model-name Qwen3-4B-AWQ \ --host 0.0.0.0 \ --port 8000 - INFO 01-01 16:09:47 [init.py:216] Automatically detected platform cuda. - (APIServer pid=180) INFO 01-01 16:09:48 [api_server.py:1842] vLLM API server version 0.11.0+582e4e37.nv25.11 - (APIServer pid=180) INFO 01-01 16:09:48 [utils.py:233] non-default args: {'host': '0.0.0.0', 'model': '/workspace/models/Qwen3-4B-AWQ', 'served_model_name': ['Qwen3-4B-AWQ']} - (APIServer pid=180) INFO 01-01 16:09:48 [model.py:547] Resolved architecture: Qwen3ForCausalLM - (APIServer pid=180) torch_dtype is deprecated! Use dtype instead! - (APIServer p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Performance]: If the next request is sent immediately after the previous one finishes, its TTFT will be relatively small; if the next request is sent 10 seconds after the previous one ends, its TTFT will be relatively...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Server pid=180) INFO 01-01 16:09:48 [api_server.py:1842] vLLM API server version 0.11.0+582e4e37.nv25.11 - (APIServer pid=180) INFO 01-01 16:09:48 [utils.py:233] non-default args: {'host': '0.0.0.0', 'model': '/workspac...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 547] Resolved architecture: Qwen3ForCausalLM - (APIServer pid=180) torch_dtype is deprecated! Use dtype instead! - (APIServer pid=180) INFO 01-01 16:09:48 [model.py:1510] Using max model len 40960 - (APIServer pid=180)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: he server with** ` - python -m vllm.entrypoints.openai.api_server \ - --model /workspace/models/Qwen3-4B-AWQ \ - --served-model-name Qwen3-4B-AWQ \ - --host 0.0.0.0 \ - --port 8000 ` --- **Below are the logs after I sta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
