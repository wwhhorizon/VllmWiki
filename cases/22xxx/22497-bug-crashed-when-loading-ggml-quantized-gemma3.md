# vllm-project/vllm#22497: [Bug]: Crashed when loading ggml quantized Gemma3

| 字段 | 值 |
| --- | --- |
| Issue | [#22497](https://github.com/vllm-project/vllm/issues/22497) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crashed when loading ggml quantized Gemma3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to serve the ggml quantized gemma-3-27b-it model. ```bash vllm serve gemma-3-27b-it/ggml-model-Q8_0.gguf --hf-config-path gemma-3-27b-it --tokenizer gemma-3-27b-it -tp 2 ``` which encountered `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbd in position 874: invalid start byte` when loading the image processor. Maybe vllm passed wrong arguments to `from_pretrained()` method. Full log output as below: ``` DEBUG 08-08 05:11:30 [__init__.py:30] No plugins for group vllm.platform_plugins found. DEBUG 08-08 05:11:30 [__init__.py:35] Checking if TPU platform is available. DEBUG 08-08 05:11:30 [__init__.py:45] TPU platform is not available because: No module named 'libtpu' DEBUG 08-08 05:11:30 [__init__.py:52] Checking if CUDA platform is available. DEBUG 08-08 05:11:30 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 08-08 05:11:30 [__init__.py:100] Checking if ROCm platform is available. DEBUG 08-08 05:11:30 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi' DEBUG 08-08 05:11:30 [__init__.py:121] Checking if XPU platform is available. DEBUG 08-08 05:11:30 [__init__.py:140] XP...

## 现有链接修复摘要

#27772 [Model] Add Gemma3 GGUF multimodal support

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: Crashed when loading ggml quantized Gemma3 bug;stale ### Your current environment ### 🐛 Describe the bug I tried to serve the ggml quantized gemma-3-27b-it model. ```bash vllm serve gemma-3-27b-it/ggml-model-Q8_0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: Crashed when loading ggml quantized Gemma3 bug;stale ### Your current environment ### 🐛 Describe the bug I tried to serve the ggml quantized gemma-3-27b-it model. ```bash vllm serve gemma-3-27b-it/ggml-model-Q8_0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: lugins to load. INFO 08-08 05:11:33 [api_server.py:1755] vLLM API server version 0.10.0 INFO 08-08 05:11:33 [cli_args.py:261] non-default args: {'model_tag': 'gemma-3-27b-it/ggml-model-Q8_0.gguf', 'model': 'gemma-3-27b-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: module named 'libtpu' DEBUG 08-08 05:11:30 [__init__.py:52] Checking if CUDA platform is available. DEBUG 08-08 05:11:30 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 08-08 05:11:30 [__init__.py:100] Chec...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27772](https://github.com/vllm-project/vllm/pull/27772) | closes_keyword | 0.95 | [Model] Add Gemma3 GGUF multimodal support | Resolves**: #22497 --- ## New Functionality ### 1. **Automatic GGUF Multimodal Detection** The model configuration now automatically detects when a Gemma3 GGUF model has an acc |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
