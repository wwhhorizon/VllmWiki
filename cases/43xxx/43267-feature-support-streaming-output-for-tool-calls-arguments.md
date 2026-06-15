# vllm-project/vllm#43267: [Feature]:  Support streaming output for tool_calls arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#43267](https://github.com/vllm-project/vllm/issues/43267) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  Support streaming output for tool_calls arguments

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ... ... (APIServer pid=1) INFO 05-21 00:19:06 [logger.py:92] Generated response chatcmpl-97319e51c49a6410 (streaming delta): output: '[reasoning: get]', output_token_ids: [98628], finish_reason: None (APIServer pid=1) INFO 05-21 00:19:06 [logger.py:92] Generated response chatcmpl-97319e51c49a6410 (streaming delta): output: '[reasoning: data]', output_token_ids: [96902], finish_reason: None (APIServer pid=1) INFO 05-21 00:19:06 [logger.py:92] Generated response chatcmpl-97319e51c49a6410 (streaming delta): output: '[reasoning: 。]', output_token_ids: [1710], finish_reason: None (APIServer pid=1) INFO 05-21 00:19:07 [logger.py:92] Generated response chatcmpl-97319e51c49a6410 (streaming delta): output: '[tool_calls: "content": "Artificial intelligence has rapidly transformed the way we interact with technology. Large language models, in particular, now possess the remarkable ability to understand complex instructions, generate creative content, and seamlessly integrate with external tools through function calling. This evolution allows developers to build dynamic applications that can fetch real-time data, perform calculations, and automate intri...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 19e51c49a6410 (streaming delta): output: '[tool_calls: "content": "Artificial intelligence has rapidly transformed the way we interact with technology. Large language models, in particular, now possess the remarkable ab...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rapidly transformed the way we interact with technology. Large language models, in particular, now possess the remarkable ability to understand complex instructions, generate creative content, and seamlessly integrate w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support streaming output for tool_calls arguments feature request ### 🚀 The feature, motivation and pitch ... ... (APIServer pid=1) INFO 05-21 00:19:06 [logger.py:92] Generated response chatcmpl-97319e51c49a6...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
