# vllm-project/vllm#7681: [Bug]: when `echo=True`, vllm will append chat template(`assistant`) after the last message

| 字段 | 值 |
| --- | --- |
| Issue | [#7681](https://github.com/vllm-project/vllm/issues/7681) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: when `echo=True`, vllm will append chat template(`assistant`) after the last message

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Sometimes we want to guide the model's output by prefilling some of the model responses. However, calling the legacy completions API and manually concatenate the chat template is inconvenient. So I used the `echo=True` parameter of chat completion: ```bash curl -X POST "http://127.0.0.1:8000/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Meta-Llama-3-8B-Instruct", "temperature": 0, "stream": false, "messages": [ { "role": "user", "content": "tell me a common saying" }, { "role": "assistant", "content": "Here is a common saying about apple. An apple a day, keeps" } ], "echo": true, "add_generation_prompt": false }' ``` Response: ```json {"role":"assistant","content":"Here is a common saying about apple. An apple a day, keeps assistant \n\nI think I can finish that one for you!\n\n\"An apple a day keeps the doctor away!\"","tool_calls":[]} ``` But the expectation should be ```json {"role":"assistant","content":"Here is a common saying about apple. An apple a day, keeps the doctor away!\"","tool_calls":[]} ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: apple a day, keeps the doctor away!\"","tool_calls":[]} ``` development ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error env_dependency Your curr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t environment ### 🐛 Describe the bug Sometimes we want to guide the model's output by prefilling some of the model responses. However, calling the legacy completions API and manually concatenate the chat template is inc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ### 🐛 Describe the bug Sometimes we want to guide the model's output by prefilling some of the model responses. However, calling the legacy completions API and manually concatenate the chat template is inconvenient. So...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
