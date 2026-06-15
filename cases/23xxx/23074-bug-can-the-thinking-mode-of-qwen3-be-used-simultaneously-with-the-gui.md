# vllm-project/vllm#23074: [Bug]:  Can the thinking mode of qwen3 be used simultaneously with the guided_json of vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#23074](https://github.com/vllm-project/vllm/issues/23074) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]:  Can the thinking mode of qwen3 be used simultaneously with the guided_json of vllm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug xinference1.9.0, qwen3-14b deployed on vllm, with thinking mode enabled and guided_json used simultaneously, the output content is always an empty value ChatCompletion(id='chat089f8a26-7be4-11f0-b8f5-3cecefb477d0', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, reasoning_content=' \n{\n\n\n "item_name": "统一阿萨姆（原味奶茶)",\n "item_production_date": null,\n "item_shelf_life": "9月",\n "item_due_time": null\n}'))], created=1755487977, model='qwen3-1.7b', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=45, prompt_tokens=2320, total_tokens=2365, completion_tokens_details=None, prompt_tokens_details=None)) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e)) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Can the thinking mode of qwen3 be used simultaneously with the guided_json of vllm bug;stale ### Your current environment ### 🐛 Describe the bug xinference1.9.0, qwen3-14b deployed on vllm, with thinking mode ena...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ng mode of qwen3 be used simultaneously with the guided_json of vllm bug;stale ### Your current environment ### 🐛 Describe the bug xinference1.9.0, qwen3-14b deployed on vllm, with thinking mode enabled and guided_json...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
