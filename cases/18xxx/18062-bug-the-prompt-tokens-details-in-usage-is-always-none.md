# vllm-project/vllm#18062: [Bug]: The `prompt_tokens_details` in `usage` is always `None`.

| 字段 | 值 |
| --- | --- |
| Issue | [#18062](https://github.com/vllm-project/vllm/issues/18062) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The `prompt_tokens_details` in `usage` is always `None`.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The `prompt_tokens_details` in `usage` is always `None`. I'm using the code from the `master` branch, commit: `ee5be834e7dcdea02512cffc125add6961f71b82`. ``` shell vllm serve Qwen/Qwen3-8B --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser hermes --enable-prompt-tokens-details ``` ``` shell # curl -s -X POST http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "messages": [{"role": "user", "content": "Hello, vLLM!"}], "max_tokens": 240 }' |jq { "id": "chatcmpl-c47b4685b8524e778c3da69c27cc32fb", "object": "chat.completion", "created": 1747129556, "model": "Qwen/Qwen3-8B", "choices": [ { "index": 0, "message": { "role": "assistant", "reasoning_content": "\nOkay, the user greeted me with \"Hello, vLLM!\" which is a bit confusing because I'm Qwen. I need to clarify that I'm not vLLM. I should start by politely pointing out the mistake. Then, I should introduce myself as Qwen, explaining my capabilities. It's important to be friendly and invite them to ask any questions. I should keep the tone positive and helpful. Let me make sure the response is clear and not too technical. Also,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: hen, I should introduce myself as Qwen, explaining my capabilities. It's important to be friendly and invite them to ask any questions. I should keep the tone positive and helpful. Let me make sure the response is clear...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ommit: `ee5be834e7dcdea02512cffc125add6961f71b82`. ``` shell vllm serve Qwen/Qwen3-8B --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser hermes --enable-prompt-tokens-details ``` ``` shell # curl -s -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
