# vllm-project/vllm#33507: [Bug]: Startup of the Qwen3-VL model failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#33507](https://github.com/vllm-project/vllm/issues/33507) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Startup of the Qwen3-VL model failed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash vllm serve /home/dev/model/Qwen/Qwen3-VL-30B-A3B-Instruct/ ``` ```bash (APIServer pid=647998) INFO 02-01 17:03:01 [api_server.py:1272] vLLM API server version 0.14.1 (APIServer pid=647998) INFO 02-01 17:03:01 [utils.py:263] non-default args: {'model_tag': '/home/dev/model/Qwen/Qwen3-VL-30B-A3B-Instruct/', 'port': 8083, 'model': '/home/dev/model/Qwen/Qwen3-VL-30B-A3B-Instruct/'} (APIServer pid=647998) WARNING 02-01 17:03:01 [system_utils.py:262] Found ulimit of 4096 and failed to automatically increase with error current limit exceeds maximum limit. This can cause fd limit errors like `OSError: [Errno 24] Too many open files`. Consider increasing with ulimit -n (APIServer pid=647998) Unrecognized keys in `rope_parameters` for 'rope_type'='default': {'mrope_interleaved', 'mrope_section'} (APIServer pid=647998) Unrecognized keys in `rope_parameters` for 'rope_type'='default': {'mrope_interleaved', 'mrope_section'} (APIServer pid=647998) INFO 02-01 17:03:01 [model.py:530] Resolved architecture: Qwen3VLMoeForConditionalGeneration (APIServer pid=647998) INFO 02-01 17:03:01 [model.py:1545] Using max model len 262144 (APIServer p...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ver pid=647998) INFO 02-01 17:03:01 [api_server.py:1272] vLLM API server version 0.14.1 (APIServer pid=647998) INFO 02-01 17:03:01 [utils.py:263] non-default args: {'model_tag': '/home/dev/model/Qwen/Qwen3-VL-30B-A3B-In...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Startup of the Qwen3-VL model failed. bug ### Your current environment ### 🐛 Describe the bug ```bash vllm serve /home/dev/model/Qwen/Qwen3-VL-30B-A3B-Instruct/ ``` ```bash (APIServer pid=647998) INFO 02-01 17:03...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ion'} (APIServer pid=647998) INFO 02-01 17:03:01 [model.py:530] Resolved architecture: Qwen3VLMoeForConditionalGeneration (APIServer pid=647998) INFO 02-01 17:03:01 [model.py:1545] Using max model len 262144 (APIServer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
