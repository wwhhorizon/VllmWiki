# vllm-project/vllm#29541: [CI Failure]: mi325_1: Entrypoints Integration Test (API Server 1)

| 字段 | 值 |
| --- | --- |
| Issue | [#29541](https://github.com/vllm-project/vllm/issues/29541) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;multimodal_vlm |
| 子分类 | wrong_output |
| Operator 关键词 | gemm |
| 症状 | build_error;mismatch |
| 根因提示 | shape |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Entrypoints Integration Test (API Server 1)

### Issue 正文摘录

### Name of failing test `pytest -v -s entrypoints/openai/test_collective_rpc.py; pytest -v -s entrypoints/openai --ignore=entrypoints/openai/test_chat_with_tool_reasoning.py --ignore=entrypoints/openai/test_oot_registration.py --ignore=entrypoints/openai/test_tensorizer_entrypoint.py --ignore=entrypoints/openai/correctness/ --ignore=entrypoints/openai/test_collective_rpc.py --ignore=entrypoints/openai/tool_parsers/; pytest -v -s entrypoints/test_chat_utils.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests Summary:** **test_abort_metrics_reset in test_metrics.py** Tests: Metrics reset after request abort with frontend multiprocessing disabled Failure: AssertionError Configuration: --disable-frontend-multiprocessing-text flag Likely cause: Metrics tracking not properly resetting abort counts when frontend multiprocessing is disabled, possible state management issue in metrics collection **test_openapi_stateless[POST /tokenize] in test_openai_schema.py** Tests: OpenAPI schema validation for tokenize endpoint using schemathesis Failure: SUBFAIL during s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: tool_parsers/; pytest -v -s entrypoints/test_chat_utils.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: s/test_chat_utils.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Tests Summary:** **test_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Entrypoints Integration Test (API Server 1) ci-failure ### Name of failing test `pytest -v -s entrypoints/openai/test_collective_rpc.py; pytest -v -s entrypoints/openai --ignore=entrypoints/openai/
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ess endpoint validation with generated test cases Likely cause: Schema mismatch between OpenAPI spec and actual tokenize endpoint behavior, possibly incorrect request/response format or missing field validation **test_m...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: mentation issues with request formatting, response handling, or endpoint routing for score/rerank operations **test_same_response_as_chat_completions in test_serving_tokens.py** Tests: Token serving consistency with cha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
