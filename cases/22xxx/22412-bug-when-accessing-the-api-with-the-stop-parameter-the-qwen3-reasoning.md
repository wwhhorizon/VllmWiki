# vllm-project/vllm#22412: [Bug]: When accessing the API with the 'stop' parameter, the 'qwen3-reasoning-parser' fails to function correctly.

| 字段 | 值 |
| --- | --- |
| Issue | [#22412](https://github.com/vllm-project/vllm/issues/22412) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When accessing the API with the 'stop' parameter, the 'qwen3-reasoning-parser' fails to function correctly.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When accessing the API with the 'stop' parameter, the ‘think’ and ‘ ’ tags output by the model are split into multiple tokens, causing the 'qwen3 reasoning parser' to be unable to parse the thinking content properly.Is there any good way to solve this problem at present?The log is as follows: INFO 08-06 10:16:27 [qwen3_reasoning_parser.py:85] mydebug:delta_text=邀请用户进一步交 INFO 08-06 10:16:27 [qwen3_reasoning_parser.py:85] mydebug:delta_text=流。 INFO 08-06 10:16:27 [qwen3_reasoning_parser.py:85] mydebug:delta_text= INFO 08-06 10:16:27 [qwen3_reasoning_parser.py:85] INFO 08-06 10:16:27 [qwen3_reasoning_parser.py:85] mydebug:delta_text= INFO 08-06 10:16:27 [qwen3_reasoning_parser.py:85] INFO 08-06 10:16:27 [qwen3_reasoning_parser.py:85] mydebug:delta_text= INFO 08-06 10:16:27 [qwen3_reasoning_parser.py:85] 你 INFO 08-06 10:16:27 [qwen3_reasoning_parser.py:85] mydebug:delta_text=好！ INFO 08-06 10:16:27 [qwen3_reasoning_parser.py:85] mydebug:delta_text=很高兴 The parsed content is as follows： ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner o...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency You...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: When accessing the API with the 'stop' parameter, the 'qwen3-reasoning-parser' fails to function correctly. bug;stale ### Your current environment ### 🐛 Describe the bug When accessing the API with the 'stop' par...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: parameter, the 'qwen3-reasoning-parser' fails to function correctly. bug;stale ### Your current environment ### 🐛 Describe the bug When accessing the API with the 'stop' parameter, the ‘think’ and ‘ ’ tags output by the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
