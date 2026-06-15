# vllm-project/vllm#9284: May I ask what is the image parameter of vllm's api about blip2, and I have an error here，INFO: 127.0.0.1:40608 - "POST /v1/completions HTTP/1.1" 400 Bad Request

| 字段 | 值 |
| --- | --- |
| Issue | [#9284](https://github.com/vllm-project/vllm/issues/9284) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> May I ask what is the image parameter of vllm's api about blip2, and I have an error here，INFO: 127.0.0.1:40608 - "POST /v1/completions HTTP/1.1" 400 Bad Request

### Issue 正文摘录

def send_request_to_model(api_url, model_name, question, image_path, max_tokens, temperature): prompt = f"Question: {question} Answer:" encoded_image = encode_image_to_base64(image_path) data = { "model": model_name, "prompt": prompt, "multi_modal_data": { "image": encoded_image }, "max_tokens": max_tokens, "temperature": temperature, "stop_token_ids" : None } headers = { "Content-Type": "application/json" } try: response = requests.post(api_url, headers=headers, json=data) if response.status_code == 200: response_json = response.json() print("API：", response_json) # 查看详细的返回数据结构 return response_json.get("choices", [{}])[0].get("text", "No answer found.") else: print(f": {response.status_code}") print(f": {response.text}") return None except requests.exceptions.RequestException as e: print(f": {e}") return None May I ask what is the image parameter of vllm's api about blip2, and I have an error here，INFO: 127.0.0.1:40608 - "POST /v1/completions HTTP/1.1" 400 Bad Request data = { "model": model_name, "prompt": prompt, "multi_modal_data":{"image": encoded_image}, "max_tokens": max_tokens, "temperature": temperature, "stop_token_ids" : None } "multi_modal_data":{"image": encoded_image...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: se_json.get("choices", [{}])[0].get("text", "No answer found.") else: print(f": {response.status_code}") print(f": {response.text}") return None except requests.exceptions.RequestException as e: print(f": {e}") return N...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: POST /v1/completions HTTP/1.1" 400 Bad Request usage def send_request_to_model(api_url, model_name, question, image_path, max_tokens, temperature): prompt = f"Question: {question} Answer:" encoded_image = encode_image_t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ror here，INFO: 127.0.0.1:40608 - "POST /v1/completions HTTP/1.1" 400 Bad Request usage def send_request_to_model(api_url, model_name, question, image_path, max_tokens, temperature): prompt = f"Question: {question} Answe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
