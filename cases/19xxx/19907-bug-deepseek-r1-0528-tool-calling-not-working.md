# vllm-project/vllm#19907: [Bug]: Deepseek R1 0528 tool calling not working

| 字段 | 值 |
| --- | --- |
| Issue | [#19907](https://github.com/vllm-project/vllm/issues/19907) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek R1 0528 tool calling not working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running DeepSeek R1 0528 on a DGX B200 (all the cards are dedicated to deekseek) on kubernetes. ``` vllm is startted with vllm serve deepseek-ai/DeepSeek-R1-0528 --port 8000 --api-key sk-12345 --enable-reasoning --reasoning-parser deepseek_r1 --trust-remote-code --tensor-parallel-size 8 --enable-chunked-prefill --enable-prefix-caching --tool-call-parser deepseek_v3 --enable-auto-tool --chat-template examples/tool_chat_template_deepseekr1.jinja --uvicorn-log-level info --disable-log-requests ```` Running latest version v0.9.1 Regular chat works OOB but tool calling doesn't trigger tool calling. For instance on librechat it just reply a json and that's all. Had a look at the PR regarding tool calling but nothing works ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: --uvicorn-log-level info --disable-log-requests ```` Running latest version v0.9.1 Regular chat works OOB but tool calling doesn't trigger tool calling. For instance on librechat it just reply a json and that's all. Had...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nvironment ### 🐛 Describe the bug Running DeepSeek R1 0528 on a DGX B200 (all the cards are dedicated to deekseek) on kubernetes. ``` vllm is startted with vllm serve deepseek-ai/DeepSeek-R1-0528 --port 8000 --api-key s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: epseek_r1 --trust-remote-code --tensor-parallel-size 8 --enable-chunked-prefill --enable-prefix-caching --tool-call-parser deepseek_v3 --enable-auto-tool --chat-template examples/tool_chat_template_deepseekr1.jinja --uv...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
