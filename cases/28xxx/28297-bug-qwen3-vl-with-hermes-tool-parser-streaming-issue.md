# vllm-project/vllm#28297: [Bug]: Qwen3 VL with hermes tool parser streaming issue

| 字段 | 值 |
| --- | --- |
| Issue | [#28297](https://github.com/vllm-project/vllm/issues/28297) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 VL with hermes tool parser streaming issue

### Issue 正文摘录

### Your current environment ```text My config is the following: "--model", "Qwen/Qwen3-VL-32B-Instruct", "--port", "8000", "--gpu-memory-utilization", "0.9", "--tool-call-parser", "hermes", "--enable-auto-tool-choice", "--limit-mm-per-prompt.video", "0", "--limit-mm-per-prompt.image", "0", "--reasoning-parser", "qwen3", "--async-scheduling", "--enable-log-outputs", "--enable-log-requests" ``` And I'm using version v0.11.0 ### 🐛 Describe the bug When using this model with streaming usage enabled (via Langchain ChatOpenAI, i think it doesn't matter), I receive instead of the correct function call an stream like the following: ```text (streaming delta): output: ' ', output_token_ids: [151657], finish_reason: None (APIServer pid=1) INFO 11-07 04:35:27 [logger.py:71] Generated response chatcmpl-ecb92ec4e7964ddb9f3f9bfabf1fb54c (streaming delta): output: '\n', output_token_ids: [198], finish_reason: None (APIServer pid=1) INFO 11-07 04:35:27 [logger.py:71] Generated response chatcmpl-ecb92ec4e7964ddb9f3f9bfabf1fb54c (streaming delta): output: '{"', output_token_ids: [4913], finish_reason: None (APIServer pid=1) INFO 11-07 04:35:27 [logger.py:71] Generated response chatcmpl-ecb92ec4e796...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3 VL with hermes tool parser streaming issue bug ### Your current environment ```text My config is the following: "--model", "Qwen/Qwen3-VL-32B-Instruct", "--port", "8000", "--gpu-memory-utilization", "0
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "--enable-log-outputs", "--enable-log-requests" ``` And I'm using version v0.11.0 ### 🐛 Describe the bug When using this model with streaming usage enabled (via Langchain ChatOpenAI, i think it doesn't matter), I receiv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ponse chatcmpl-0c816df8c87d4f3e85249380f9a5fa4e: output: '[tool_calls: search_products_general({"description": "PC HP, 16GB RAM", "config": {"thread_id": "12345"}})]', output_token_ids: [151657, 198, 4913, 606, 788, 330...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: "--async-scheduling", "--enable-log-outputs", "--enable-log-requests" ``` And I'm using version v0.11.0 ### 🐛 Describe the bug When using this model with streaming usage enabled (via Langchain ChatOpenAI, i think it doe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
