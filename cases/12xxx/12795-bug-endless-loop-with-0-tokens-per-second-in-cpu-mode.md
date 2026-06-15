# vllm-project/vllm#12795: [Bug]: Endless loop with 0 Tokens per second in CPU mode

| 字段 | 值 |
| --- | --- |
| Issue | [#12795](https://github.com/vllm-project/vllm/issues/12795) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Endless loop with 0 Tokens per second in CPU mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to use 0.65 with bfloat16, but it locks up like the 0.71 release in an endless loop. Please fix your CPU code! ``` vllm serve ~/projects/webui/text-generation-webui/models/gpqt/ --dtype=bfloat16 2025-02-06 00:35:47.383657: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations. To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. No ROCm runtime is found, using ROCM_HOME='/opt/rocm' INFO 02-06 00:35:51 api_server.py:651] vLLM API server version 0.6.5 INFO 02-06 00:35:51 api_server.py:652] args: Namespace(subparser='serve', model_tag='/home/rohezal/projects/webui/text-generation-webui/models/gpqt/', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: . To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. No ROCm runtime is found, using ROCM_HOME='/opt/rocm' INFO 02-06 00:35:51 api_server.py:651]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Endless loop with 0 Tokens per second in CPU mode bug;stale ### Your current environment ### 🐛 Describe the bug I tried to use 0.65 with bfloat16, but it locks up like the 0.71 release in an endless loop. Please...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_paral...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: current environment ### 🐛 Describe the bug I tried to use 0.65 with bfloat16, but it locks up like the 0.71 release in an endless loop. Please fix your CPU code! ``` vllm serve ~/projects/webui/text-generation-webui/mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ix your CPU code! ``` vllm serve ~/projects/webui/text-generation-webui/models/gpqt/ --dtype=bfloat16 2025-02-06 00:35:47.383657: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
