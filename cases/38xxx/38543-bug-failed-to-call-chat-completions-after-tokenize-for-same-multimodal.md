# vllm-project/vllm#38543: [Bug]: Failed to call /chat/completions after /tokenize for same multimodal query

| 字段 | 值 |
| --- | --- |
| Issue | [#38543](https://github.com/vllm-project/vllm/issues/38543) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failed to call /chat/completions after /tokenize for same multimodal query

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When calling the `/tokenize` endpoint with a multimodal message (e.g. an image), and then calling `/v1/chat/completions` with the **same** message, the chat completion request fails with an internal server error. ### How to reproduce 1. Start a vLLM server with a VLM: ```bash vllm serve Qwen/Qwen2.5-VL-3B-Instruct \ --dtype bfloat16 --max-model-len 4096 --enforce-eager \ --limit-mm-per-prompt '{"image": 1}' ``` 2. Send a `/tokenize` request with an image, then send the exact same payload to `/v1/chat/completions`. The second call fails. ```python def test_tokenize_then_chat_completion_with_image( server: RemoteOpenAIServer, local_asset_server, ): """Tokenize a multimodal message, then send the same message to chat completions. The chat completion must succeed (not 500).""" image_url = local_asset_server.url_for("stop_sign.jpg") messages = [ { "role": "user", "content": [ {"type": "image_url", "image_url": {"url": image_url}}, {"type": "text", "text": "Describe this image briefly."}, ], } ] # Step 1: tokenize (this triggers multimodal processing in the renderer) tok_resp = requests.post( server.url_for("tokenize"), json={"model":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Failed to call /chat/completions after /tokenize for same multimodal query bug ### Your current environment ### 🐛 Describe the bug When calling the `/tokenize` endpoint with a multimodal message (e.g. an image),...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ith a VLM: ```bash vllm serve Qwen/Qwen2.5-VL-3B-Instruct \ --dtype bfloat16 --max-model-len 4096 --enforce-eager \ --limit-mm-per-prompt '{"image": 1}' ``` 2. Send a `/tokenize` request with an image, then send the exa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: chat completion request fails with an internal server error. ### How to reproduce 1. Start a vLLM server with a VLM: ```bash vllm serve Qwen/Qwen2.5-VL-3B-Instruct \ --dtype bfloat16 --max-model-len 4096 --enforce-eager...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ng `/v1/chat/completions` with the **same** message, the chat completion request fails with an internal server error. ### How to reproduce 1. Start a vLLM server with a VLM: ```bash vllm serve Qwen/Qwen2.5-VL-3B-Instruc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: payload to `/v1/chat/completions`. The second call fails. ```python def test_tokenize_then_chat_completion_with_image( server: RemoteOpenAIServer, local_asset_server, ): """Tokenize a multimodal message, then send the s...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
