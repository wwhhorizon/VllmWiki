# vllm-project/vllm#42400: [Bug]: GLM-5.1 tool call parsing fails intermittently when used as backend for Claude Code

| 字段 | 值 |
| --- | --- |
| Issue | [#42400](https://github.com/vllm-project/vllm/issues/42400) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-5.1 tool call parsing fails intermittently when used as backend for Claude Code

### Issue 正文摘录

### Your current environment ```text vLLM version: v0.20.1 (vllm-openai:v0.20.1) Model: GLM-5.1-FP8 (max_model_len: 202752) Tool call parser: glm47 Reasoning parser: glm45 Speculative decoding: MTP (num_speculative_tokens=3) ``` ### 🐛 Describe the bug When deploying GLM-5.1 with vLLM and connecting it as a custom model provider in **Claude Code** (Anthropic's CLI agent), tool calls intermittently fail to parse. Claude Code reports: > The model's tool call could not be parsed (retry also failed). **Key observations:** 1. The issue only manifests when the context window is nearly full (~200k tokens, approaching the model's 202752 max_model_len limit). With short-to-moderate contexts, tool calls parse correctly in both streaming and non-streaming modes. 2. **The failure typically occurs when Claude Code enters planning mode** — the model must produce a structured Plan tool call with detailed content at long context. This combination of near-max context + complex tool call output appears to be the trigger. ### Reproduction 1. Deploy GLM-5.1 with vLLM: ```bash vllm serve /xxxxx/GLM-5.1-FP8 \ --trust-remote-code \ --chat-template-content-format=string \ --tensor-parallel-size 8 \ --tool...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: current environment ```text vLLM version: v0.20.1 (vllm-openai:v0.20.1) Model: GLM-5.1-FP8 (max_model_len: 202752) Tool call parser: glm47 Reasoning parser: glm45 Speculative decoding: MTP (num_speculative_tokens=3) ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: GLM-5.1 tool call parsing fails intermittently when used as backend for Claude Code ### Your current environment ```text vLLM version: v0.20.1 (vllm-openai:v0.20.1) Model: GLM-5.1-FP8 (max_model_len: 202752) Tool...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed as backend for Claude Code ### Your current environment ```text vLLM version: v0.20.1 (vllm-openai:v0.20.1) Model: GLM-5.1-FP8 (max_model_len: 202752) Tool call parser: glm47 Reasoning parser: glm45 Speculative decod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ment ```text vLLM version: v0.20.1 (vllm-openai:v0.20.1) Model: GLM-5.1-FP8 (max_model_len: 202752) Tool call parser: glm47 Reasoning parser: glm45 Speculative decoding: MTP (num_speculative_tokens=3) ``` ### 🐛 Describe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: (max_model_len: 202752) Tool call parser: glm47 Reasoning parser: glm45 Speculative decoding: MTP (num_speculative_tokens=3) ``` ### 🐛 Describe the bug When deploying GLM-5.1 with vLLM and connecting it as a custom mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
