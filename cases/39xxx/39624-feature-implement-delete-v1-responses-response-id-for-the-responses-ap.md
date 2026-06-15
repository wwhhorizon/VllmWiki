# vllm-project/vllm#39624: [Feature]: Implement DELETE /v1/responses/{response_id} for the Responses API

| 字段 | 值 |
| --- | --- |
| Issue | [#39624](https://github.com/vllm-project/vllm/issues/39624) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Implement DELETE /v1/responses/{response_id} for the Responses API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The Responses API currently retains per-response state in memory when `VLLM_ENABLE_RESPONSES_API_STORE=1`. However, there is no API to explicitly delete stored responses once they are no longer needed. The OpenAI-compatible Responses API defines a deletion endpoint: DELETE /v1/responses/{response_id} vLLM currently implements: - POST /v1/responses - GET /v1/responses/{response_id} - POST /v1/responses/{response_id}/cancel but is missing the DELETE endpoint. This proposal adds support for `DELETE /v1/responses/{response_id}` to: - Provide an explicit deletion path for stored responses - Remove associated in-memory state (`response_store`, `msg_store`, `event_store`) - Align vLLM with the OpenAI-compatible Responses API Note: this proposal does not attempt to address the broader storage backend design (e.g. pluggable backends or eviction strategies). It only adds the missing API surface and ensures the current implementation can clean up stored response state. I am happy to submit a PR implementing this. --- ### Alternatives Currently, users can: 1. Disable the store entirely (not enabling `VLLM_ENABLE_RESPONSES_API_STORE`) 2. Restart the serv...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ulated state However, neither provides a fine-grained or runtime mechanism to manage stored responses. An explicit DELETE endpoint allows users to control the lifecycle of stored responses directly, regardless of the un...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: API Note: this proposal does not attempt to address the broader storage backend design (e.g. pluggable backends or eviction strategies). It only adds the missing API surface and ensures the current implementation can cl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n `VLLM_ENABLE_RESPONSES_API_STORE=1`. However, there is no API to explicitly delete stored responses once they are no longer needed. The OpenAI-compatible Responses API defines a deletion endpoint: DELETE /v1/responses...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: plement DELETE /v1/responses/{response_id} for the Responses API feature request ### 🚀 The feature, motivation and pitch The Responses API currently retains per-response state in memory when `VLLM_ENABLE_RESPONSES_API_S...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
