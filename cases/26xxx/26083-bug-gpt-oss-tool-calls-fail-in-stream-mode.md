# vllm-project/vllm#26083: [Bug]: GPT-OSS Tool Calls Fail in Stream Mode

| 字段 | 值 |
| --- | --- |
| Issue | [#26083](https://github.com/vllm-project/vllm/issues/26083) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS Tool Calls Fail in Stream Mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tool calls work correctly in **non-stream mode** but fail in **stream mode** with GPT-OSS-20B. In stream mode: Tool call tokens are incorrectly identified as reasoning content. ## Root Cause The GPT-OSS-20B model **does not consistently output tool calls with the `commentary` channel**. Instead, it uses the `analysis` channel with a recipient specified via `to=functions.XXX`(mabye a model bug?): ``` analysis to=functions.grep code {...} ``` The stream mode logic in `serving_chat.py:697-745` checks channel type **before** checking recipient, causing tool calls in the `analysis` channel to be misidentified as reasoning content: ```python # Current (incorrect) logic: elif cur_channel == "analysis": # Treats as reasoning, even if cur_recipient = "functions.grep" delta_message = DeltaMessage(reasoning_content=delta_text) elif cur_channel == "commentary" and cur_recipient.startswith("functions."): # Never reaches here for analysis channel ``` In contrast, **non-stream mode correctly identifies tool calls** by checking recipient only, regardless of channel: ```python # openai_tool_parser.py:43 if msg.recipient and msg.recipient.startswi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: `commentary` channel**. Instead, it uses the `analysis` channel with a recipient specified via `to=functions.XXX`(mabye a model bug?): ``` analysis to=functions.grep code {...} ``` The stream mode logic in `serving_chat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: it ok to add VMs without virtual volumes to a snapshot plan?" Need to search guides for snapshot plan and VMs without virtual volumes. Use grep. assistant analysis to=functions.grep code {"pattern":"snapshot plan","glob...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPT-OSS Tool Calls Fail in Stream Mode bug;stale ### Your current environment ### 🐛 Describe the bug Tool calls work correctly in **non-stream mode** but fail in **stream mode** with GPT-OSS-20B. In stream mode:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: GPT-OSS Tool Calls Fail in Stream Mode bug;stale ### Your current environment ### 🐛 Describe the bug Tool calls work correctly in **non-stream mode** but fail in **stream mode** with GPT-OSS-20B. In stream mode:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
