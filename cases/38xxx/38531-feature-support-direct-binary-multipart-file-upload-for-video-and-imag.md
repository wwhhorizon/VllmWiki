# vllm-project/vllm#38531: [Feature]: Support direct binary/multipart file upload for video and image in OpenAI-compatible API

| 字段 | 值 |
| --- | --- |
| Issue | [#38531](https://github.com/vllm-project/vllm/issues/38531) |
| 状态 | open |
| 标签 | feature request;multi-modality |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support direct binary/multipart file upload for video and image in OpenAI-compatible API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Feature Request ### Summary Allow clients to upload video/image files directly via the API (multipart or binary), similar to how SGLang and LMDeploy handle local media, instead of requiring base64 encoding or a reachable URL. ### Current Behavior The `/v1/chat/completions` endpoint only accepts media via: - Public/accessible URL (`video_url.url = "https://..."`) - Base64 data URI (`video_url.url = "data:video/mp4;base64,..."`) - `file://` URI (requires `--allowed-local-media-path` server flag + file must be on server) ### Problem - Base64 encoding 18MB video → ~24MB payload → exceeds shell ARG_MAX (`Argument list too long`) - `file://` requires server restart with `--allowed-local-media-path` and file must exist on the server machine, not the client - Forces users to run a separate HTTP server just to pass local files ### Proposed Solution Support a `/v1/files` upload endpoint or multipart form upload in `/v1/chat/completions` so clients can send raw binary files directly: ```bash curl http://localhost:8000/v1/chat/completions \ -F "file=@/local/video.mp4" \ -F 'payload={"model":"...","messages":[...]}' ``` Or alternatively, a pre-upload...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 00/v1/chat/completions \ -F "file=@/local/video.mp4" \ -F 'payload={"model":"...","messages":[...]}' ``` Or alternatively, a pre-upload endpoint: ```bash # Upload file first, get a reference ID curl http://localhost:800...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Avoids memory/shell limits from base64 encoding large video files - Especially painful for multimodal workflows with large video files ### Environment - vLLM version: latest - Model: Qwen3.5-35B-A3B-FP8 (multimodal MoE)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: o files ### Environment - vLLM version: latest - Model: Qwen3.5-35B-A3B-FP8 (multimodal MoE) - Use case: local video inference via OpenAI-compatible API ### Alternatives _No response_ ### Additional context _No response...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ironment - vLLM version: latest - Model: Qwen3.5-35B-A3B-FP8 (multimodal MoE) - Use case: local video inference via OpenAI-compatible API ### Alternatives _No response_ ### Additional context _No response_ ### Before su...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
