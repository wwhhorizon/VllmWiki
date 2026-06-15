# vllm-project/vllm#23837: [Bug]: gpt-oss Intermittent 500 Internal Server Error with empty response body when using strict JSON “function router” system prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#23837](https://github.com/vllm-project/vllm/issues/23837) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: gpt-oss Intermittent 500 Internal Server Error with empty response body when using strict JSON “function router” system prompt

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Serving gpt-oss-20b via vLLM’s OpenAI-compatible Chat Completions intermittently returns HTTP 500 with no response body (Content-Length: 0). This occurs for a minimal request using a strict JSON “function router” system prompt (below) ```text { "model": "gpt-oss-20b", "max_tokens": 128, "messages": [ { "role": "system", "content": "Objective: Answer weather-related user queries by using previously called functions when possible, and only call a new function if it is strictly required.\n\nAvailable Data:\nNo previous functions called\n\nInstructions:\n1. **Strictly Use JSON**: Respond only in JSON format with no extra text, explanations, or notes.\n2. **Use Prior Data First**: Treat the results from all previously called functions as **fully available** for answering the query. Do not re-call a function if its data is already provided.\n3. **Only Call the Next Required Function**:\n - Select the next function only if specific data needed for the query is missing from the available data.\n - If all necessary data exists, return `no-function-needed`.\n\nResponse Format:\n- Use the following formats based on the query requirements:\n...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the Next Required Function**:\n - Select the next function only if specific data needed for the query is missing from the available data.\n - If all necessary data exists, return `no-function-needed`.\n\nResponse Format...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ce! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gpt-oss Intermittent 500 Internal Server Error with empty response body when using strict JSON “function router” system prompt bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug Serving gpt-oss...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: response body when using strict JSON “function router” system prompt bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug Serving gpt-oss-20b via vLLM’s OpenAI-compatible Chat Completions intermittently...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23860: Should have ROCm label: NO (0 matches) #23837: Should have ROCm label: NO (0 matches) #23834: Should have ROCm label: NO (0 matches) #23832: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
