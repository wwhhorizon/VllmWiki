# vllm-project/vllm#35665: [Bug]: Multimodal Requests Fail on /v1/chat/completions/render Endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#35665](https://github.com/vllm-project/vllm/issues/35665) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Multimodal Requests Fail on /v1/chat/completions/render Endpoint

### Issue 正文摘录

### Your current environment latest vllm 0.16.0 ### 🐛 Describe the bug Vision-enabled models failed to process the completion request when an `image_url` was included in the messages. Additionally, the `/v1/chat/completions/render` endpoint returns various internal data structures and does not conform to the RFC discussed here: https://github.com/vllm-project/vllm/issues/22817 ```python @pytest.mark.asyncio async def test_chat_completion_render_with_base64_image_url( vision_client, local_asset_server, ): """Render a multimodal chat request and verify that tokens are returned.""" image = local_asset_server.get_image_asset("RGBA_comp.png") data_url = encode_image_url(image, format="PNG") assert data_url.startswith("data:image/") assert ";base64," in data_url response = await vision_client.post( "/v1/chat/completions/render", json={ "model": VISION_MODEL_NAME, "messages": [ { "role": "user", "content": [ {"type": "image_url", "image_url": {"url": data_url}}, {"type": "text", "text": "What's in this image?"}, ], } ], }, ) # Expect a successful render response assert response.status_code == 200 ``` Another issue is that the legacy `/tokenize` endpoint is ineffective for multimodal requ...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Multimodal Requests Fail on /v1/chat/completions/render Endpoint bug ### Your current environment latest vllm 0.16.0 ### 🐛 Describe the bug Vision-enabled models failed to process the completion request when an `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ://github.com/vllm-project/vllm/issues/22817 ```python @pytest.mark.asyncio async def test_chat_completion_render_with_base64_image_url( vision_client, local_asset_server, ): """Render a multimodal chat request and veri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Multimodal Requests Fail on /v1/chat/completions/render Endpoint bug ### Your current environment latest vllm 0.16.0 ### 🐛 Describe the bug Vision-enabled models failed to process the completion request when an `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: /v1/chat/completions/render Endpoint bug ### Your current environment latest vllm 0.16.0 ### 🐛 Describe the bug Vision-enabled models failed to process the completion request when an `image_url` was included in the mess...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
