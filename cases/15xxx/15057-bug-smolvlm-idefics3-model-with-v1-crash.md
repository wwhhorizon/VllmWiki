# vllm-project/vllm#15057: [Bug]: SmolVLM / Idefics3 model with V1 crash

| 字段 | 值 |
| --- | --- |
| Issue | [#15057](https://github.com/vllm-project/vllm/issues/15057) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SmolVLM / Idefics3 model with V1 crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using v0.8.0rc2 built for CPU only, I started the service with the following to test `HuggingFaceTB/SmolVLM-500M-Instruct` with vLLM V1: ```bash VLLM_TRACE_FUNCTION=1 VLLM_ENABLE_V1_MULTIPROCESSING=0 VLLM_USE_V1=1 python3.10 -m vllm.entrypoints.openai.api_server --model HuggingFaceTB/SmolVLM-500M-Instruct --task generate --limit-mm-per-prompt image=1 --dtype=bfloat16 --allowed-local-media-path /data --mm-processor-kwargs '{"size": {"longest_edge": 512}}' --device cpu ``` The service failed to start but didn't seem to include a stacktrace as it should have. The full output is here: ``` root@911975c7b272:/workspace# VLLM_TRACE_FUNCTION=1 VLLM_ENABLE_V1_MULTIPROCESSING=0 VLLM_USE_V1=1 python3.10 -m vllm.entrypoints.openai.api_server --model HuggingFaceTB/SmolVLM-500M-Instruct --task generate --limit-mm-per-prompt image=1 --dtype=bfloat16 --allowed-local-media-path /data --mm-processor-kwargs '{"size": {"longest_edge": 512}}' --device cpu DEBUG 03-18 17:27:09 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 03-18 17:27:09 [__init__.py:35] Checking if TPU platform is available. DEBUG 03-18 17:27:09 [__init__.py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: l_plugins found. INFO 03-18 17:27:13 [api_server.py:972] vLLM API server version 0.8.0rc2 INFO 03-18 17:27:13 [api_server.py:973] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: SmolVLM / Idefics3 model with V1 crash bug ### Your current environment ### 🐛 Describe the bug Using v0.8.0rc2 built for CPU only, I started the service with the following to test `HuggingFaceTB/SmolVLM-500M-Inst...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='HuggingFaceTB/SmolVLM-500M-Instruct'...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: TB/SmolVLM-500M-Instruct --task generate --limit-mm-per-prompt image=1 --dtype=bfloat16 --allowed-local-media-path /data --mm-processor-kwargs '{"size": {"longest_edge": 512}}' --device cpu ``` The service failed to sta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: SmolVLM / Idefics3 model with V1 crash bug ### Your current environment ### 🐛 Describe the bug Using v0.8.0rc2 built for CPU only, I started the service with the following to test `HuggingFaceTB/SmolVLM-500M-Inst...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
