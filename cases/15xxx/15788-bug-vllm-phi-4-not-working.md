# vllm-project/vllm#15788: [Bug]: vllm phi-4 not working

| 字段 | 值 |
| --- | --- |
| Issue | [#15788](https://github.com/vllm-project/vllm/issues/15788) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | debug |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm phi-4 not working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am following the instructions here to run phi-4: https://docs.vllm.ai/en/latest/getting_started/examples/openai_chat_completion_client_for_multimodal.html Here is the code: ``` import subprocess cmd = [ "vllm", "serve", "--uvicorn-log-level=info", "microsoft/Phi-4-multimodal-instruct", "--host", "0.0.0.0", "--port", str(VLLM_PORT), "--api-key", API_KEY, "--trust-remote-code", "--disable-sliding-window", "--enable-lora", "--dtype", "auto", "--max-model-len", "131072", "--lora-extra-vocab-size", "0", "--max-loras", "2", "--max-lora-rank", "256", "--lora-modules", "speech=/root/.cache/huggingface/hub/models--microsoft--Phi-4-multimodal-instruct/snapshots/0ae13bd0f508a906f8b8288fc5e36b01b903c132/speech-lora/", "vision=/root/.cache/huggingface/hub/models--microsoft--Phi-4-multimodal-instruct/snapshots/0ae13bd0f508a906f8b8288fc5e36b01b903c132/vision-lora/", ] subprocess.Popen(" ".join(cmd), shell=True) ``` I am getting the following error: ``` INFO 03-31 03:34:00 __init__.py:207] Automatically detected platform cuda. INFO 03-31 03:34:03 api_server.py:912] vLLM API server version 0.7.3 INFO 03-31 03:34:03 api_server.py:913] args: Name...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: .ai/en/latest/getting_started/examples/openai_chat_completion_client_for_multimodal.html Here is the code: ``` import subprocess cmd = [ "vllm", "serve", "--uvicorn-log-level=info", "microsoft/Phi-4-multimodal-instruct"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: _chat_completion_client_for_multimodal.html Here is the code: ``` import subprocess cmd = [ "vllm", "serve", "--uvicorn-log-level=info", "microsoft/Phi-4-multimodal-instruct", "--host", "0.0.0.0", "--port", str(VLLM_P
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: vllm phi-4 not working bug;stale ### Your current environment ### 🐛 Describe the bug I am following the instructions here to run phi-4: https://docs.vllm.ai/en/latest/getting_started/examples/openai_chat_completi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: "--disable-sliding-window", "--enable-lora", "--dtype", "auto", "--max-model-len", "131072", "--lora-extra-vocab-size", "0", "--max-loras", "2", "--max-lora-rank", "256", "--lora-modules",
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ype='auto', kv_cache_dtype='auto', max_model_len=131072, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
