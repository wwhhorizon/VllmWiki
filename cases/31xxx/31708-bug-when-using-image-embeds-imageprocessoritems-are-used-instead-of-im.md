# vllm-project/vllm#31708: [Bug]: When using image_embeds, ImageProcessorItems are used instead of ImageEmbeddingItems, causing an out-of-bounds array error.

| 字段 | 值 |
| --- | --- |
| Issue | [#31708](https://github.com/vllm-project/vllm/issues/31708) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using image_embeds, ImageProcessorItems are used instead of ImageEmbeddingItems, causing an out-of-bounds array error.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To achieve EPD separation, I need to use vllm to input image_embeds. Refer to https://vllm.hyper.ai/docs/inference-and-serving/multimodal_inputs/ Reference code: ```python image_embedding = torch.load(...) grid_thw = torch.load(...) # Required by Qwen/Qwen2-VL-2B-Instruct buffer = io.BytesIO() torch.save(image_embedding, buffer) buffer.seek(0) binary_data = buffer.read() base64_image_embedding = base64.b64encode(binary_data).decode('utf-8') client = OpenAI( # defaults to os.environ.get("OPENAI_API_KEY") api_key=openai_api_key, base_url=openai_api_base, ) model = "llava-hf/llava-1.5-7b-hf" embeds = { "type": "image_embeds", "image_embeds": f"{base64_image_embedding}" } model = "Qwen/Qwen2-VL-2B-Instruct" embeds = { "type": "image_embeds", "image_embeds": { "image_embeds": f"{base64_image_embedding}" , # Required "image_grid_thw": f"{base64_image_grid_thw}" # Required by Qwen/Qwen2-VL-2B-Instruct }, } model = "openbmb/MiniCPM-V-2_6" embeds = { "type": "image_embeds", "image_embeds": { "image_embeds": f"{base64_image_embedding}" , # Required "image_sizes": f"{base64_image_sizes}" # Required by openbmb/MiniCPM-V-2_6 }, } chat_complet...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: image_embeds. Refer to https://vllm.hyper.ai/docs/inference-and-serving/multimodal_inputs/ Reference code: ```python image_embedding = torch.load(...) grid_thw = torch.load(...) # Required by Qwen/Qwen2-VL-2B-Instruct b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: a)` returns False, and ultimately returns `ImageProcessorItems`. Q: In version 0.10.2, I was able to solve the problem by forcibly converting `image_embeds` into a list and modifying the code under `ImageProcessorItems`...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: a = buffer.read() base64_image_embedding = base64.b64encode(binary_data).decode('utf-8') client = OpenAI( # defaults to os.environ.get("OPENAI_API_KEY") api_key=openai_api_key, base_url=openai_api_base, ) model = "llava...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 778 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r) image_embedding = torch.load('/tensor_example.pt', weights_only=False) # shape torch.Size([416, 1024]) print(image_embedding.shape) image_embedding = image_embedding.unsqueeze(0) # torch.Size([1, 416, 1024]) buffer =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
