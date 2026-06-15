# vllm-project/vllm#30599: [Bug]: Qwen3-30B-A3B on vLLM-OpenAI v0.12.0 “hangs” in thinking mode: keeps reasoning until token cap

| 字段 | 值 |
| --- | --- |
| Issue | [#30599](https://github.com/vllm-project/vllm/issues/30599) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-30B-A3B on vLLM-OpenAI v0.12.0 “hangs” in thinking mode: keeps reasoning until token cap

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running Qwen/Qwen3-30B-A3B via vLLM OpenAI v0.12.0 with thinking enabled, the model often gets stuck producing/maintaining a long internal reasoning trace instead of converging to an answer/tool call. --- From vLLM server logs we see: 1. One request stays Running: 1 for minutes. 2. KV cache usage slowly grows (e.g. 0.3% → ~4%). 3. Generation throughput gradually decreases over time (e.g. ~181 tok/s → ~158 tok/s). 4. The server then shows the same pattern again with KV cache restarting from a low value (a fresh attempt of the same prompt). It looks like the model is “thinking” until it hits the token budget. Additionally, if we limit output (max_tokens=512), tool-call related parsing fails because the response contains ... where valid JSON is expected. --- --- If we set max_tokens = 512: HTTP 400 (tool-call args not valid JSON) ```text ModelHTTPError: status_code: 400 ... Invalid JSON ... input_value=' \nOkay, let's ta...' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: AI v0.12.0 “hangs” in thinking mode: keeps reasoning until token cap bug;stale ### Your current environment ### 🐛 Describe the bug When running Qwen/Qwen3-30B-A3B via vLLM OpenAI v0.12.0 with thinking enabled, the model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: LM OpenAI v0.12.0 with thinking enabled, the model often gets stuck producing/maintaining a long internal reasoning trace instead of converging to an answer/tool call. --- From vLLM server logs we see: 1. One request st...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-30B-A3B on vLLM-OpenAI v0.12.0 “hangs” in thinking mode: keeps reasoning until token cap bug;stale ### Your current environment ### 🐛 Describe the bug When running Qwen/Qwen3-30B-A3B via vLLM OpenAI v0.12.0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: minutes. 2. KV cache usage slowly grows (e.g. 0.3% → ~4%). 3. Generation throughput gradually decreases over time (e.g. ~181 tok/s → ~158 tok/s). 4. The server then shows the same pattern again with KV cache restarting...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
