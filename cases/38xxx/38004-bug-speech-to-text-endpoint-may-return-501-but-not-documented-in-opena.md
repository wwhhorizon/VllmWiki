# vllm-project/vllm#38004: [Bug]: Speech-to-Text endpoint may return 501 but not documented in OpenAPI

| 字段 | 值 |
| --- | --- |
| Issue | [#38004](https://github.com/vllm-project/vllm/issues/38004) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Speech-to-Text endpoint may return 501 but not documented in OpenAPI

### Issue 正文摘录

### Your current environment The output of python collect_env.py ```text (Not strictly required for this issue since it is a code-level/API contract issue rather than runtime-specific behavior. Can provide if needed.) ### 🐛 Describe the bug ## Description The Speech-to-Text (STT) endpoint may return a `501 Not Implemented` response when certain handlers are not available. However, this response code does not appear to be documented in the OpenAPI specification. ## Location vllm/entrypoints/openai/speech_to_text/api_router.py ## Problem - The route may raise `NotImplementedError` when a feature or backend is not implemented. - This results in an HTTP 501 response. - The OpenAPI schema does not document this possible response. ## Expected Behavior One of the following: 1. Document the 501 response in the OpenAPI schema 2. Or convert it into a standardized error response (e.g., 400/404/500) ## Actual Behavior - 501 response may be returned implicitly - Not visible in API documentation ## Minimal Reproduction (Conceptual) This issue can occur when invoking the STT endpoint with a configuration where the handler is not implemented. In such cases, the router raises `NotImplementedError`...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: # Problem - The route may raise `NotImplementedError` when a feature or backend is not implemented. - This results in an HTTP 501 response. - The OpenAPI schema does not document this possible response. ## Expected Beha...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: issue since it is a code-level/API contract issue rather than runtime-specific behavior. Can provide if needed.) ### 🐛 Describe the bug ## Description The Speech-to-Text (STT) endpoint may return a `501 Not Implemented`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: (Conceptual) This issue can occur when invoking the STT endpoint with a configuration where the handler is not implemented. In such cases, the router raises `NotImplementedError`, leading to an HTTP 501 response. (Provi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: specification. ## Location vllm/entrypoints/openai/speech_to_text/api_router.py ## Problem - The route may raise `NotImplementedError` when a feature or backend is not implemented. - This results in an HTTP 501 response...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
