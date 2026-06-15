# vllm-project/vllm#17458: [Usage]: How to set max_new_tokens param when use llm.chat?

| 字段 | 值 |
| --- | --- |
| Issue | [#17458](https://github.com/vllm-project/vllm/issues/17458) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to set max_new_tokens param when use llm.chat?

### Issue 正文摘录

```python from vllm import LLM import base64 def encode_image(image_path): with open(image_path, "rb") as image_file: return base64.b64encode(image_file.read()).decode("utf-8") llm = LLM("Qwen/Qwen2.5-VL-7B-Instruct", limit_mm_per_prompt={"image": 20}) video_frames = ["screenshot-20250430-120546.png"] messages = [ { "role": "user", "content": [ {"type": "text", "text": "Describe this set of frames. Consider the frames to be a part of the same video."} ] } ] for frame_path in video_frames: base64_image = encode_image(frame_path) image_content = { "type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"} } messages[0]["content"].append(image_content) outputs = llm.chat(messages, max_new_tokens=1) for o in outputs: generated_text = o.outputs[0].text print(generated_text) ``` I got this error. TypeError: chat() got an unexpected keyword argument 'max_new_tokens'

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: to set max_new_tokens param when use llm.chat? usage ```python from vllm import LLM import base64 def encode_image(image_path): with open(image_path, "rb") as image_file: return base64.b64encode(image_file.read()).decod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: return base64.b64encode(image_file.read()).decode("utf-8") llm = LLM("Qwen/Qwen2.5-VL-7B-Instruct", limit_mm_per_prompt={"image": 20}) video_frames = ["screenshot-20250430-120546.png"] messages = [ { "role": "user", "co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: "rb") as image_file: return base64.b64encode(image_file.read()).decode("utf-8") llm = LLM("Qwen/Qwen2.5-VL-7B-Instruct", limit_mm_per_prompt={"image": 20}) video_frames = ["screenshot-20250430-120546.png"] messages = [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
