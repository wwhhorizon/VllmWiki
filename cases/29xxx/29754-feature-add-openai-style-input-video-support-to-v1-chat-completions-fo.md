# vllm-project/vllm#29754: [Feature]: Add OpenAI-style `input_video` support to `/v1/chat/completions` for multimodal models (e.g., Qwen3-VL)

| 字段 | 值 |
| --- | --- |
| Issue | [#29754](https://github.com/vllm-project/vllm/issues/29754) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add OpenAI-style `input_video` support to `/v1/chat/completions` for multimodal models (e.g., Qwen3-VL)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### **Feature Request: OpenAI-compatible `input_video` support for vLLM’s Chat Completions and Responses API** First, thank you for the incredible work on multimodal support and the recent EVS improvements for Qwen3-VL. At the moment, vLLM fully supports video inside the *Python API* for models like Qwen3-VL, but the **OpenAI-compatible `/v1/chat/completions` and `/v1/responses` endpoints do not expose any way to pass video inputs**, even though the backend model executor now handles video embeddings. This makes it impossible to perform video inference using vLLM via HTTP, because the HTTP parser does not convert input_video items into VideoItem, so the multimodal pipeline is never invoked. --- ## **Current Behavior** The vLLM OpenAI server currently supports: **`/v1/chat/completions`:** * `{"type": "text"}` * `{"type": "image_url"}` — for images provided as URLs or data URLs **`/v1/responses`:** * `{"type": "input_text"}` * `{"type": "input_image"}` — also URL/data URL or file ID However, **neither endpoint accepts any form of video input**. The following OpenAI-style content blocks are rejected: **Chat Completions (expected analogue to `im...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e]: Add OpenAI-style `input_video` support to `/v1/chat/completions` for multimodal models (e.g., Qwen3-VL) feature request ### 🚀 The feature, motivation and pitch ### **Feature Request: OpenAI-compatible `input_video`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: g path for video inference today is the Python API: ```python from vllm import LLM llm.generate(...) ``` This requires running models locally and bypasses HTTP entirely, preventing remote or OpenAI-compatible deployment...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: endpoints do not expose any way to pass video inputs**, even though the backend model executor now handles video embeddings. This makes it impossible to perform video inference using vLLM via HTTP, because the HTTP pars...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nt accepts any form of video input**. The following OpenAI-style content blocks are rejected: **Chat Completions (expected analogue to `image_url`):** ```json { "type": "video_url", "video_url": { "url": "data:video/mp4...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
