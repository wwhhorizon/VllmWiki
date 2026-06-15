# vllm-project/vllm#24170: [Bug]: Intermittent "Unknown recipient: None" when calling gpt-oss-20b with Responses

| 字段 | 值 |
| --- | --- |
| Issue | [#24170](https://github.com/vllm-project/vllm/issues/24170) |
| 状态 | closed |
| 标签 | bug;gpt-oss |
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

> [Bug]: Intermittent "Unknown recipient: None" when calling gpt-oss-20b with Responses

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On vllm main (commit 56d04089ef508003c684c90429046d90f2117547) I am trying to use the Responses API for gpt-oss-20b. I am seeing occasional errors when the model tries to call a tool; the response JSON from vLLM is: ```json {"error":{"message":"Unknown recipient: None","type":"BadRequestError","param":null,"code":400}} ``` The only place this string occurs in the code is in [harmony_utils.py](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/harmony_utils.py#L248). You can reproduce it (flaky, but happens a lot of the time) with the following script: [inspect-fixed-01-400-request.json](https://github.com/user-attachments/files/22115746/inspect-fixed-01-400-request.json) [inspect-fixed-01-400-request.txt](https://github.com/user-attachments/files/22115752/inspect-fixed-01-400-request.txt) ```bash curl -H @inspect-fixed-01-400-request.txt --data @inspect-fixed-01-400-request.json -X POST http://localhost:8000/v1/responses --verbose ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Intermittent "Unknown recipient: None" when calling gpt-oss-20b with Responses bug;gpt-oss ### Your current environment ### 🐛 Describe the bug On vllm main (commit 56d04089ef508003c684c90429046d90f2117547) I am t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Intermittent "Unknown recipient: None" when calling gpt-oss-20b with Responses bug;gpt-oss ### Your current environment ### 🐛 Describe the bug On vllm main (commit 56d04089ef508003c684c90429046d90f2117547) I am t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: LM is: ```json {"error":{"message":"Unknown recipient: None","type":"BadRequestError","param":null,"code":400}} ``` The only place this string occurs in the code is in [harmony_utils.py](https://github.com/vllm-project/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
