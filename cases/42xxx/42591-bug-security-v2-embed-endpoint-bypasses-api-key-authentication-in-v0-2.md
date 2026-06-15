# vllm-project/vllm#42591: [Bug]: Security: /v2/embed endpoint bypasses API Key authentication in v0.20.2

| 字段 | 值 |
| --- | --- |
| Issue | [#42591](https://github.com/vllm-project/vllm/issues/42591) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Security: /v2/embed endpoint bypasses API Key authentication in v0.20.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The API key authorization (enabled via --api-key or VLLM_API_KEY) is not correctly enforced on the /v2/embed endpoint, while it works as expected on the /v1/embeddings endpoint. This allows unauthorized access to embedding services. Steps to Reproduce: Start vLLM server with --api-key "your_secret_key". Access /v1/embeddings without a key: Returns 401 Unauthorized (Correct). Access /v2/embed without a key (using application/json header): Returns 200 OK with embeddings (Security Bug). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: dpoint. This allows unauthorized access to embedding services. Steps to Reproduce: Start vLLM server with --api-key "your_secret_key". Access /v1/embeddings without a key: Returns 401 Unauthorized (Correct). Access /v2/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
