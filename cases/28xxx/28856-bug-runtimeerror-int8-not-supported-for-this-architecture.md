# vllm-project/vllm#28856: [Bug]: RuntimeError: Int8 not supported for this architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#28856](https://github.com/vllm-project/vllm/issues/28856) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;gemm;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Int8 not supported for this architecture

### Issue 正文摘录

### Your current environment When I used the GPQT method of the llmcompressor library to perform int8 quantization on Qwen3-VL-4B with an RTX 5090 graphics card, and ran inference using vllm version 0.11.0, the following error occurred: RuntimeError: Int8 not supported for this architecture. However, it works normally on an RTX 4090 graphics card. ### 🐛 Describe the bug ```bash python3 -m vllm.entrypoints.openai.api_server --model /workspace/Qwen2.5-VL-7B-Instruct-20250829-quantized.w8a8 --served-model-name base_model --port 9001 --tensor-parallel-size 1 --dtype auto --enable-prefix-caching --enable-chunked-prefill --max-model-len 8000 --max-num-batched-tokens 15360 --limit-mm-per-prompt '{"image":30}' --compilation-config '{"level": 3,"compilation_mode":"default","compiler":"vllm-compiler","configs":{"model":{"vision_language":{"enable":true,"vision_encoder_compilation_mode":"disable","llm_compilation_mode":"enable"}}}}' --gpu-memory-utilization 0.7 ``` ```bash root@ms-22309-server-5090test-1-1114131839-67558b84b-mmsnq:/workspace# python3 -m vllm.entrypoints.openai.api_server --model /workspace/Qwen2.5-VL-7B-Instruct-20250829-quantized.w8a8 --served-model-name base_model --port 9...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: GPQT method of the llmcompressor library to perform int8 quantization on Qwen3-VL-4B with an RTX 5090 graphics card, and ran inference using vllm version 0.11.0, the following error occurred: RuntimeError: Int8 not supp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: e, 'compilation_config': {"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":null,"use_inductor":true,"compile_sizes":null,"inductor_compile_config":{"enable_auto_functionalized_v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Qwen3-VL-4B with an RTX 5090 graphics card, and ran inference using vllm version 0.11.0, the following error occurred: RuntimeError: Int8 not supported for this architecture. However, it works normally on an RTX 4090 gr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: When I used the GPQT method of the llmcompressor library to perform int8 quantization on Qwen3-VL-4B with an RTX 5090 graphics card, and ran inference using vllm version 0.11.0, the following error occurred: RuntimeErro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: RuntimeError: Int8 not supported for this architecture bug;stale ### Your current environment When I used the GPQT method of the llmcompressor library to perform int8 quantization on Qwen3-VL-4B with an RTX 5090...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
