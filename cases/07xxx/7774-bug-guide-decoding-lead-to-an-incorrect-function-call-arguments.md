# vllm-project/vllm#7774: [Bug]: guide decoding lead to an incorrect function call arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#7774](https://github.com/vllm-project/vllm/issues/7774) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: guide decoding lead to an incorrect function call arguments

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug while i test the function call of openai api base on internlm model, i got the incorrect parameters like this: ``` {"location":": "} ``` but if i reset the guideline guided_decode_logits_processor in serving_chat.py to None and skip_special_tokens to false, it will get the correct parameters. ``` {"name": "get_current_weather", "parameters": {"location": "Shanghai"}} ``` if i don't change skip_special_tokens to false, it will get the output like this: ``` {"name": "get_current_weather", "parameters": {"location": "Shanghai"}} ``` so i think the incorrect parameter is cased by the guide decoding logic, done anyone meet the same situation?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ne guided_decode_logits_processor in serving_chat.py to None and skip_special_tokens to false, it will get the correct parameters. ``` {"name": "get_current_weather", "parameters": {"location": "Shanghai"}} ``` if i don...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: guide decoding lead to an incorrect function call arguments bug;stale ### Your current environment ### 🐛 Describe the bug while i test the function call of openai api base on internlm model, i got the incorrect p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;import_error;mismatch;nan_inf env_dependency Your current environment
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;import_error;mismatch;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: culative_decoding cuda;operator;sampling;triton build_error;import_error;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
