# vllm-project/vllm#22403: [Bug]: For GPT OSS 120B: Expected 2 output messages (reasoning and final), but got 7.

| 字段 | 值 |
| --- | --- |
| Issue | [#22403](https://github.com/vllm-project/vllm/issues/22403) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 102; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: For GPT OSS 120B: Expected 2 output messages (reasoning and final), but got 7.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Use the following prompt: ```json { "messages": [ { "role": "system", "content": "You are an autonomous intelligent agent tasked with navigating a web browser to complete specific objectives. You have access to a simplified representation of the webpage and can perform various acti... [TRUNCATED]" }, { "role": "user", "content": "URL: http://metis.lti.cs.cmu.edu:7770/\nTitle: One Stop Market\n\nHTML:\n <a href=\"http://metis.lti.cs.cmu.edu:7... [TRUNCATED]" } ] } ``` Will result in randomly 200, 400 and 500. Sometime it responds normally (it will say it don't know what to do because of the prompt os truncated), sometimes it returns 400 bad request: ```json { "object": "error", "message": "Expected 2 output messages (reasoning and final), but got 7.", "type": "BadRequestError", "param": null, "code": 400 } ``` and sometimes it returns 500 internal server error. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: us intelligent agent tasked with navigating a web browser to complete specific objectives. You have access to a simplified representation of the webpage and can perform various acti... [TRUNCATED]" }, { "role": "user",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: to do because of the prompt os truncated), sometimes it returns 400 bad request: ```json { "object": "error", "message": "Expected 2 output messages (reasoning and final), but got 7.", "type": "BadRequestError", "param"...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
