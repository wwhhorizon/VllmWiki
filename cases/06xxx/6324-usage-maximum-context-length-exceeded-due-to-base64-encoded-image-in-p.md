# vllm-project/vllm#6324: [Usage]: Maximum Context Length Exceeded Due to Base64-Encoded Image in Prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#6324](https://github.com/vllm-project/vllm/issues/6324) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Maximum Context Length Exceeded Due to Base64-Encoded Image in Prompt

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm # Example Code llm = VLLMOpenAI( openai_api_key="EMPTY", openai_api_base=api_base, model_name="microsoft/Phi-3-vision-128k-instruct", model_kwargs={"stop": ["."]} ) image_path = "invoice_data_images/Screenshot 2024-05-02 160946_page_1.png" with open(image_path, "rb") as image_file: image_base64 = base64.b64encode(image_file.read()).decode("utf-8") prompt_1 = "Give me the invoice date from the given image." messages = [ HumanMessage( content=[ {"type": "text", "text": prompt_1}, {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}} ] ) ] response = llm.invoke(messages) print(response) # Error Message { "name": "BadRequestError", "message": "Error code: 400 - {'object': 'error', 'message': 'This model's maximum context length is 8192 tokens. However, you requested 254457 tokens (254201 in the messages, 256 in the completion). Please reduce the length of the messages or completion.', 'type': 'BadRequestError', 'param': None, 'code': 400}" } # Description I hosted VLLM on an EC2 instance to extract text data from images using the Phi-3 Vision...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: "rb") as image_file: image_base64 = base64.b64encode(image_file.read()).decode("utf-8") prompt_1 = "Give me the invoice date from the given image." messages = [ HumanMessage( content=[ {"type": "text", "text": prompt_1}...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 8000 --model microsoft/Phi-3-vision-128k-instruct --trust-remote-code --dtype=half --max_model_len=8192 When running the code, I encounter a BadRequestError due to exceeding the maximum context length. The error message...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Code llm = VLLMOpenAI( openai_api_key="EMPTY", openai_api_base=api_base, model_name="microsoft/Phi-3-vision-128k-instruct", model_kwargs={"stop": ["."]} ) image_path = "invoice_data_images/Screenshot 2024-05-02 160946_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
