# vllm-project/vllm#6301: [Usage]: In phi3 vision maximum context length issue

| 字段 | 值 |
| --- | --- |
| Issue | [#6301](https://github.com/vllm-project/vllm/issues/6301) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 | crash;oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: In phi3 vision maximum context length issue

### Issue 正文摘录

### Your current environment llm = VLLMOpenAI( openai_api_key="EMPTY", openai_api_base=api_base, model_name="microsoft/Phi-3-vision-128k-instruct", model_kwargs={"stop": ["."]} ) image_path = "invoice_data_images/Screenshot 2024-05-02 160946_page_1.png" with open(image_path, "rb") as image_file: image_base64 = base64.b64encode(image_file.read()).decode("utf-8") prompt_1 = "Give me the invoice date from the given image." messages = [ HumanMessage( content=[ {"type": "text", "text": prompt_1}, {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}} ] ) ] response = llm.invoke(messages) print(response) # Error { "name": "BadRequestError", "message": "Error code: 400 - {'object': 'error', 'message': \"This model's maximum context length is 3744 tokens. However, you requested 254457 tokens (254201 in the messages, 256 in the completion). Please reduce the length of the messages or completion.\", 'type': 'BadRequestError', 'param': None, 'code': 400}", "stack": "--------------------------------------------------------------------------- BadRequestError Traceback (most recent call last) Cell In[96], line 26 16 messages = [ 17 HumanMessage( 18 content=[ (...)...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: s\"), 350 tags=config.get(\"tags\"), 351 metadata=config.get(\"metadata\"), 352 run_name=config.get(\"run_name\"), 353 run_id=config.pop(\"run_id\", None), 354 **kwargs, 355 ) 356 .generati
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: LLMOpenAI( openai_api_key="EMPTY", openai_api_base=api_base, model_name="microsoft/Phi-3-vision-128k-instruct", model_kwargs={"stop": ["."]} ) image_path = "invoice_data_images/Screenshot 2024-05-02 160946_page_1.png" w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ") as image_file: image_base64 = base64.b64encode(image_file.read()).decode("utf-8") prompt_1 = "Give me the invoice date from the given image." messages = [ HumanMessage( content=[ {"type": "text", "text": prompt_1}, {...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: completion_with_retry(llm, run_manager, **kwargs) 117 \"\"\"Use tenacity to retry the completion call.\"\"\" 118 if is_openai_v1(): --> 119 return llm.client.create(**kwargs) 121 retry_decorator = _create_retry_decorato...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 8000 --model microsoft/Phi-3-vision-128k-instruct --trust-remote-code --dtype=half --max_model_len=8192 However, when I increase max_model_len, I get a CUDA out of memory error. When I use microsoft/Phi-3-vision-128k-in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
