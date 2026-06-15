# vllm-project/vllm#12794: [Bug]: vllm forces float16 to bfloat16 in cpu mode, tensorflow does not support bfloat16 for gptq

| 字段 | 值 |
| --- | --- |
| Issue | [#12794](https://github.com/vllm-project/vllm/issues/12794) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm forces float16 to bfloat16 in cpu mode, tensorflow does not support bfloat16 for gptq

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is stupid. I tried to downgrade to 0.63 to use it without intel ipex. The gptq model fails loading, since you convert all floats in cpu mode to bfloat16. ``` WARNING 02-06 00:09:44 cpu_executor.py:327] float16 is not supported on CPU, casting to bfloat16. ValueError: torch.bfloat16 is not supported for quantization method gptq. Supported dtypes: [torch.float16] ``` Full output. I am just asking myself, if the cpu mode is sometime of April 1st joke. Nothing works in two different releases! ``` vllm serve ~/projects/webui/text-generation-webui/models/gpqt/ INFO 02-06 00:09:26 importing.py:10] Triton not installed; certain GPU-related functions will not be available. 2025-02-06 00:09:28.323160: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations. To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. INFO 02-06 00:09:31 api_server.py:528] vLLM API server version 0.6.3.post1 INFO 02-06 00:09:31 api_server.py:529] args: Namespace(subparser='serve', model_ta...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ~/projects/webui/text-generation-webui/models/gpqt/ INFO 02-06 00:09:26 importing.py:10] Triton not installed; certain GPU-related functions will not be available. 2025-02-06 00:09:28.323160: I tensorflow/core/platform/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: /text-generation-webui/models/gpqt/ INFO 02-06 00:09:26 importing.py:10] Triton not installed; certain GPU-related functions will not be available. 2025-02-06 00:09:28.323160: I tensorflow/core/platform/cpu_feature_guar...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: vllm forces float16 to bfloat16 in cpu mode, tensorflow does not support bfloat16 for gptq bug ### Your current environment ### 🐛 Describe the bug This is stupid. I tried to downgrade to 0.63 to use it without in...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
