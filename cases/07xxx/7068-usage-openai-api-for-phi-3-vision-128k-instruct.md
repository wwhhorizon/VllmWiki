# vllm-project/vllm#7068: [Usage]: OpenAI API for Phi-3-vision-128k-instruct 

| 字段 | 值 |
| --- | --- |
| Issue | [#7068](https://github.com/vllm-project/vllm/issues/7068) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: OpenAI API for Phi-3-vision-128k-instruct 

### Issue 正文摘录

```text BadRequestError: Error code: 400 - {'object': 'error', 'message': 'Attempted to assign 1 x 2509 = 2509 image tokens to 0 placeholders', 'type': 'BadRequestError', 'param': None, 'code': 400} ``` calling using following function: ```python def prepare_prompts(self, prompts, images): messages = [] #re.sub(r" ", "", ) for i in range(len(prompts)): if i % 2 == 0: content = [ { "type": "text", "text": prompts[i] } ] if images[i]: img_byte_arr = io.BytesIO() images[i].save(img_byte_arr, format='PNG') img_byte_arr = img_byte_arr.getvalue() image_base64 = base64.b64encode(img_byte_arr).decode('utf-8') content.append( { "type": "image_url", "image_url": { "url": f"data:image/jpeg;base64,{image_base64}" } } ) messages.append({"role": "user", "content": content}) else: messages.append({"role": "assistant", "content": prompts[i]}) return messages ``` I tried two format for prompts[i]. 1. "Describe this image" 2. " \n Describe this image" Getting same error for both prompts.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: OpenAI API for Phi-3-vision-128k-instruct usage ```text BadRequestError: Error code: 400 - {'object': 'error', 'message': 'Attempted to assign 1 x 2509 = 2509 image tokens to 0 placeholders', 'type': 'BadReques...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: messages.append({"role": "user", "content": content}) else: messages.append({"role": "assistant", "content": prompts[i]}) return messages ``` I tried two format for prompts[i]. 1. "Describe this image" 2. " \n Describe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: byte_arr = io.BytesIO() images[i].save(img_byte_arr, format='PNG') img_byte_arr = img_byte_arr.getvalue() image_base64 = base64.b64encode(img_byte_arr).decode('utf-8') content.append( {

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
