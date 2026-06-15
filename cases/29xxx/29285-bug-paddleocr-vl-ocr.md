# vllm-project/vllm#29285: [Bug]: 加载PaddleOCR-VL模型进行ocr识别时出错

| 字段 | 值 |
| --- | --- |
| Issue | [#29285](https://github.com/vllm-project/vllm/issues/29285) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 加载PaddleOCR-VL模型进行ocr识别时出错

### Issue 正文摘录

### Your current environment vllm/vllm-openai:v0.11.2 ### 🐛 Describe the bug 调用代码如下： messages = [ { "role": "user", "content": [ {"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{base64_image}"}}, {"type": "text", "text": "OCR"}, ] } ] client = OpenAI( api_key="EMPTY", base_url="http://localhost:18008/v1", timeout=3600 ) response = client.chat.completions.create( model="trs-vl", messages=messages, temperature=0.0, ) 出现的错误信息： (EngineCore_DP0 pid=143) ERROR 11-23 17:06:27 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.11.2) with config: model='/models/PaddleOCR-VL-0.9B', speculative_config=None, tokenizer='/models/PaddleOCR-VL-0.9B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=Fa...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: 加载PaddleOCR-VL模型进行ocr识别时出错 bug;stale ### Your current environment vllm/vllm-openai:v0.11.2 ### 🐛 Describe the bug 调用代码如下： messages = [ { "role": "user", "content": [ {"type": "image_url", "image_url":
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: imeout=3600 ) response = client.chat.completions.create( model="trs-vl", messages=messages, temperature=0.0, ) 出现的错误信息： (EngineCore_DP0 pid=143) ERROR 11-23 17:06:27 [dump_input.py:72] Dumping input data for V1 LLM engi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=trs-vl, enable_prefix_caching=False, enable_chun...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: onfig=None, tokenizer='/models/PaddleOCR-VL-0.9B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=No...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
