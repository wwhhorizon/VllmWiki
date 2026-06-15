# vllm-project/vllm#31319: [Bug]: GLM-4.7-FP8 missing beginning <think> tag 

| 字段 | 值 |
| --- | --- |
| Issue | [#31319](https://github.com/vllm-project/vllm/issues/31319) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.7-FP8 missing beginning <think> tag 

### Issue 正文摘录

### Your current environment I am on docker nightly vLLM API server version 0.14.0rc1.dev104+g8ee90c83f ### 🐛 Describe the bug I hosted the model via vllm and already without reasoning_parser, I found the model output with directly output without but having close tag later. ``` root@iv-ydzbs5zshss6ipm6s5gu /h/n/d/ark_http_proxy# curl --location 'http://localhost/v1/chat/completions' \ --header 'Authorization: Bearer YOUR_API_KEY' \ --header 'Content-Type: application/json' \ --data '{ "model": "GLM-4.7-FP8", "stream": true, "messages": [ { "role": "user", "content": "what is cryptography" } ],"chat_template_kwargs": {"enable_thinking": true}, "skip_special_tokens": false, "thinking": { "type": "enabled" }, "max_tokens": 1024, "temperature": 1.0 }' data: {"id":"chatcmpl-9fbc092d919f9e51","object":"chat.completion.chunk","created":1766599479,"model":"GLM-4.7-FP8","choices":[{"index":0,"delta":{"role":"assistant","content":"","reasoning_content":null},"logprobs":null,"finish_reason":null}],"prompt_token_ids":null} data: {"id":"chatcmpl-9fbc092d919f9e51","object":"chat.completion.chunk","created":1766599479,"model":"GLM-4.7-FP8","choices":[{"index":0,"delta":{"content":"1","reasoning_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: missing beginning <think> tag bug ### Your current environment I am on docker nightly vLLM API server version 0.14.0rc1.dev104+g8ee90c83f ### 🐛 Describe the bug I hosted the model via vllm and already without reasoning_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: GLM-4.7-FP8 missing beginning <think> tag bug ### Your current environment I am on docker nightly vLLM API server version 0.14.0rc1.dev104+g8ee90c83f ### 🐛 Describe the bug I hosted the model via vllm and already...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: at_template_kwargs": {"enable_thinking": true}, "skip_special_tokens": false, "thinking": { "type": "enabled" },
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ersion 0.14.0rc1.dev104+g8ee90c83f ### 🐛 Describe the bug I hosted the model via vllm and already without reasoning_parser, I found the model output with directly output without but having close tag later. ``` root@iv-y...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
