# vllm-project/vllm#20404: [Usage]: Does vLLM support accept text embedding and image embedding inputs at the same time?

| 字段 | 值 |
| --- | --- |
| Issue | [#20404](https://github.com/vllm-project/vllm/issues/20404) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vLLM support accept text embedding and image embedding inputs at the same time?

### Issue 正文摘录

### Your current environment vllm 0.9.1 ### How would you like to use vllm ``` image_embedding = torch.load(...) grid_thw = torch.load(...) # Required by Qwen/Qwen2-VL-2B-Instruct buffer = io.BytesIO() torch.save(image_embedding, buffer) buffer.seek(0) binary_data = buffer.read() base64_image_embedding = base64.b64encode(binary_data).decode('utf-8') client = OpenAI( # defaults to os.environ.get("OPENAI_API_KEY") api_key=openai_api_key, base_url=openai_api_base, ) model = "llava-hf/llava-1.5-7b-hf" embeds = { "type": "image_embeds", "image_embeds": f"{base64_image_embedding}" } model = "Qwen/Qwen2-VL-2B-Instruct" embeds = { "type": "image_embeds", "image_embeds": { "image_embeds": f"{base64_image_embedding}" , # Required "image_grid_thw": f"{base64_image_grid_thw}" # Required by Qwen/Qwen2-VL-2B-Instruct }, } model = "openbmb/MiniCPM-V-2_6" embeds = { "type": "image_embeds", "image_embeds": { "image_embeds": f"{base64_image_embedding}" , # Required "image_sizes": f"{base64_image_sizes}" # Required by openbmb/MiniCPM-V-2_6 }, } chat_completion = client.chat.completions.create( messages=[ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": [ { "...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: age_embedding = torch.load(...) grid_thw = torch.load(...) # Required by Qwen/Qwen2-VL-2B-Instruct buffer = io.BytesIO() torch.save(image_embedding, buffer) buffer.seek(0) binary_data = buffer.read() base64_image_embedd...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: accept text embedding and image embedding inputs at the same time? usage;stale ### Your current environment vllm 0.9.1 ### How would you like to use vllm ``` image_embedding = torch.load(...) grid_thw = torch.load(...)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: According to the document: [multimodalInput](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html#image-embedding-inputs) vllm supports image embedding input. But what if I want the text type input is also a t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
