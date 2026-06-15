# vllm-project/vllm#39741: [Bug]: Empty tools array accepted with HTTP 200, should return 400

| 字段 | 值 |
| --- | --- |
| Issue | [#39741](https://github.com/vllm-project/vllm/issues/39741) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Empty tools array accepted with HTTP 200, should return 400

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When sending a request with tools: [] (empty array), vLLM returns HTTP 200. The OpenAI API returns HTTP 400 for the same request with error code "empty_array". **Reproduction** ``` curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": " ", "messages": [{"role": "user", "content": "Hello"}], "tools": [] }' ``` Expected: HTTP 400 Actual: HTTP 200 Happens regardless of tool_choice value — omitted, "auto", or "none". The only exception is tool_choice="required", which is already handled by https://github.com/vllm-project/vllm/pull/21052. **Root Cause** In check_tool_usage() in protocol.py, data.get("tools") returns [] which evaluates to False, so tool_choice is never set to "auto" and stays at the default "none". The method then returns early without validating the empty array: python``` if "tool_choice" not in data and data.get("tools"): # [] evaluates to False, skipped data["tool_choice"] = "auto" ``` python``` if "tool_choice" in data and data["tool_choice"] == "none": return data # exits here, no check for empty tools ``` This was an unintended side effect of https://github.com/vllm...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ### Your current environment ### 🐛 Describe the bug When sending a request with tools: [] (empty array), vLLM returns HTTP 200. The OpenAI API returns HTTP 400 for the same request with error code "empty_array". **Repro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: In check_tool_usage() in protocol.py, data.get("tools") returns [] which evaluates to False, so tool_choice is never set to "auto" and stays at the default "none". The method then returns early without validating the em...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
