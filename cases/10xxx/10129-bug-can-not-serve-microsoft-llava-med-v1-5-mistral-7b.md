# vllm-project/vllm#10129: [Bug]: can not serve microsoft/llava-med-v1.5-mistral-7b

| 字段 | 值 |
| --- | --- |
| Issue | [#10129](https://github.com/vllm-project/vllm/issues/10129) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can not serve microsoft/llava-med-v1.5-mistral-7b

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can successfully use `python -m vllm.entrypoints.openai.api_server --model llava-hf/llava-1.5-7b-hf --chat-template /condo/wanglab/shared/xyw/vllm/examples/template_llava.jinja` , but can not use 'microsoft/llava-med-v1.5-mistral-7b', which is supported by vLLM and I can not use this model just using `vllm serve "microsoft/llava-med-v1.5-mistral-7b"` this model can be loaded in transformer: `from llava.model.builder import load_pretrained_model model_path='microsoft/llava-med-v1.5-mistral-7b' model_base=None model_name='llava-med-v1.5-mistral-7b' tokenizer, model, image_processor, context_len = load_pretrained_model(model_path, model_base, model_name, load_8bit=False, load_4bit=False, device="cuda")` I don't know how to use it in vllm `python -m vllm.entrypoints.openai.api_server --model microsoft/llava-med-v1.5-mistral-7b --chat-template /condo/wanglab/shared/xyw/vllm/examples/template_llava.jinja` INFO 11-07 14:36:42 api_server.py:528] vLLM API server version 0.6.3.post1 INFO 11-07 14:36:42 api_server.py:529] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: osoft/llava-med-v1.5-mistral-7b bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I can successfully use `python -m vllm.entrypoints.openai.api_server --model llava-hf/llava-1.5...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -mistral-7b"` this model can be loaded in transformer: `from llava.model.builder import load_pretrained_model model_path='microsoft/llava-med-v1.5-mistral-7b' model_base=None model_name='llava-med-v1.5-mistral-7b' token...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: = load_pretrained_model(model_path, model_base, model_name, load_8bit=False, load_4bit=False, device="cuda")` I don't know how to use it in vllm `python -m vllm.entrypoints.openai.api_server --model microsoft/llava-med-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
