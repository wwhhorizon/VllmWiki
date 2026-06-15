# vllm-project/vllm#15752: [Bug]: Gemma-3-12B-it model getting stuck in repetitive output loops

| 字段 | 值 |
| --- | --- |
| Issue | [#15752](https://github.com/vllm-project/vllm/issues/15752) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma-3-12B-it model getting stuck in repetitive output loops

### Issue 正文摘录

## Gemma-3-12B-it model getting stuck in repetitive output loops ### 🐛 Describe the bug Description When running Gemma 3 12B-it through vLLM, the model occasionally gets stuck in infinite repetitive loops during text generation. Example prompt that failed: I need help writing a description on a change control ticket. the title is "upgrade the teleport server" and have put "We need to upgrade the teleport server to meet security standards" in the description but need to be at least 3 lines Example output pattern: … * What level of detail is required? * Teleport your organization * Teleport version of your team' your Teleport installation setup with details regarding your configuration, for assistance on more to address the response a I can' description for request, please of assistance with that and description of service. description, can to to the change request information on assistance with information request, and description of to and get-request to to. -description of service andgetrequest andis_description of. request of a todescription andrequest. request. description of torequest, of description, andrequest. I information ofis-request description, andrequest. of informati...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: l of detail is required? * Teleport your organization * Teleport version of your team' your Teleport installation setup with details regarding your configuration, for assistance on more to address the response a I can'...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ,installation,installation ofthat, request Environment - vLLM version: rocm/vllm-dev:nightly_main_20250326 (tried multiple builds) - Model: "google/gemma-3-12b-it GPU: mi250 / rocm + mi300s UI: Open Webui + custom made...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma-3-12B-it model getting stuck in repetitive output loops bug;stale ## Gemma-3-12B-it model getting stuck in repetitive output loops ### 🐛 Describe the bug Description When running Gemma 3 12B-it through vLLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Gemma-3-12B-it model getting stuck in repetitive output loops bug;stale ## Gemma-3-12B-it model getting stuck in repetitive output loops ### 🐛 Describe the bug Description When running Gemma 3 12B-it through vLLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tokens or manual interruption Additional Notes - The issue seems more prevalent with longer conversations or complex queries - The model seems unable to break out of these loops once they start and might continue repeat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
