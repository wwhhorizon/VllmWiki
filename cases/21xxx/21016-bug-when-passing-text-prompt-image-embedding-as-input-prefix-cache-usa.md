# vllm-project/vllm#21016: [Bug]: When passing text prompt + image embedding as Input, prefix cache usage is alway 0%

| 字段 | 值 |
| --- | --- |
| Issue | [#21016](https://github.com/vllm-project/vllm/issues/21016) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When passing text prompt + image embedding as Input, prefix cache usage is alway 0%

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` def call_vllm_api_with_embeds(image_embedding, question="What's in this image?", model="llava-hf/llava-1.5-7b-hf", api_url="http://localhost:8005"): """ Call vLLM API with encoded image embedding Args: image_embedding: PyTorch tensor containing image embeddings question: Question to ask about the image model: Model name to use api_url: API endpoint URL Returns: API response """ # Encode image embedding base64_image_embedding = encode_image_embedding_to_base64(image_embedding) # Prepare the request payload embeds = { "type": "image_embeds", "image_embeds": base64_image_embedding } payload = { "model": model, "messages": [ {"role": "system", "content": "You are a helpful assistant."}, { "role": "user", "content": [ { "type": "text", "text": question, }, embeds ] } ], "max_tokens": 1024, "temperature": 0, "guided_choice": ["yes", "no"] # Add this line } headers = { "Content-Type": "application/json" } try: print(f"Sending request to {api_url}/v1/chat/completions...") response = requests.post( f"{api_url}/v1/chat/completions", headers=headers, data=json.dumps(payload), timeout=120 ) if response.status_code == 200: return response...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: _vllm_api_with_embeds(image_embedding, question="What's in this image?", model="llava-hf/llava-1.5-7b-hf", api_url="http://localhost:8005"): """ Call vLLM API with encoded image embedding Args: image_embedding: PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: xt prompt + image embedding as Input, prefix cache usage is alway 0% bug;stale ### Your current environment ### 🐛 Describe the bug ``` def call_vllm_api_with_embeds(image_embedding, question="What's in this image?", mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding cud...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n in the vllm console output. My command to run the vllm server is: ``` CUDA_VISIBLE_DEVICES="6,7" VLLM_LOGGING_LEVEL=DEBUG python -m vllm.entrypoints.openai.api_server --model /data/models/llava-1.5-7b-hf --trust-remot...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
