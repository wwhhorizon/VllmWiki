# vllm-project/vllm#16474: [Bug]: Error when running Llama-4-Maverick-17B-128E-Instruct-FP8 on mi300x

| 字段 | 值 |
| --- | --- |
| Issue | [#16474](https://github.com/vllm-project/vllm/issues/16474) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when running Llama-4-Maverick-17B-128E-Instruct-FP8 on mi300x

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’m encountering an issue when running the FP8 version of the meta-llama/Llama-4-Maverick-17B-128E-Instruct model (i.e. meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8) on 4 Mi300x GPUs. According to the [vllm blog](https://blog.vllm.ai/2025/04/05/llama4), it should be possible to run this model on a Mi300x GPU, but the configuration provided in the blog uses a tensor parallelism of 8-GPU . When I set tensor parallel size to 4 but in a fp8 model, I get the following error: ``` VLLM_DISABLE_COMPILE_CACHE=1 vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --tensor-parallel-size 4 --max-model-len 430000 --download-dir /app/data/models/ --kv-cache-dtype fp8 ``` output: ```text INFO 04-11 09:53:14 [__init__.py:239] Automatically detected platform rocm. INFO 04-11 09:53:16 [api_server.py:1034] vLLM API server version 0.8.3rc2.dev77+g2976dc27e.d20250409 INFO 04-11 09:53:16 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=[...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Error when running Llama-4-Maverick-17B-128E-Instruct-FP8 on mi300x bug;rocm ### Your current environment ### 🐛 Describe the bug I’m encountering an issue when running the FP8 version of the meta-llama/Llama-4-Ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Error when running Llama-4-Maverick-17B-128E-Instruct-FP8 on mi300x bug;rocm ### Your current environment ### 🐛 Describe the bug I’m encountering an issue when running the FP8 version of the meta-llama/Llama-4-Ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='meta-llama/Llama-4-Maverick-17B-128E...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: type='auto', kv_cache_dtype='fp8', max_model_len=430000, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### 🐛 Describe the bug I’m encountering an issue when running the FP8 version of the meta-llama/Llama-4-Maverick-17B-128E-Instruct model (i.e. meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8) on 4 Mi300x GPUs. Accordi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
