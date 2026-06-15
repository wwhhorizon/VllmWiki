# vllm-project/vllm#40689: [Bug]: Max token length incorrect when /nothink tag on Qwen3.5-4B

| 字段 | 值 |
| --- | --- |
| Issue | [#40689](https://github.com/vllm-project/vllm/issues/40689) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Max token length incorrect when /nothink tag on Qwen3.5-4B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running Qwen3.5-4B with vLLM and the flag `{"enable_thinking": False}`. When I set max_tokens to a specific number, the loop does not stop early enough, potentially because the /nothink (added from `{"enable_thinking": False}`) flag is not considered. The resulting number of tokens is always 1 more than the maximum context length I set when I deploy. The error is below: ``` ERROR 04-22 14:48:25 [serving.py:311] vllm.exceptions.VLLMValidationError: You passed 1193 input tokens and requested 7000 output tokens. However, the model's context length is only 8192 tokens, resulting in a maximum input length of 1192 tokens. Please reduce the length of the input prompt. (parameter=input_tokens, value=1193) ``` Here, I have a max context length of 8192 and set max_tokens to 7000, but since /nothink is added to the input, the input which was clipped at 1192 becomes 1193. If I change max_tokens to 5000, the input will be clipped at 3192, but with /nothink is 3193, again giving me 1 token over the maximum context. I am using `vllm:0.17.1-gpu-py312-cu129-ubuntu22.04-sagemaker` ### Before submitting a new issue... - [x] Make sure you alrea...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Max token length incorrect when /nothink tag on Qwen3.5-4B bug ### Your current environment ### 🐛 Describe the bug I am running Qwen3.5-4B with vLLM and the flag `{"enable_thinking": False}`. When I set max_token...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and the flag `{"enable_thinking": False}`. When I set max_tokens to a specific number, the loop does not stop early enough, potentially because the /nothink (added from `{"enable_thinking": False}`) flag is not consider...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g I am running Qwen3.5-4B with vLLM and the flag `{"enable_thinking": False}`. When I set max_tokens to a specific number, the loop does not stop early enough, potentially because the /nothink (added from `{"enable_thin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 1] vllm.exceptions.VLLMValidationError: You passed 1193 input tokens and requested 7000 output tokens. However, the model's context length is only 8192 tokens, resulting in a maximum input length of 1192 tokens. Please...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
