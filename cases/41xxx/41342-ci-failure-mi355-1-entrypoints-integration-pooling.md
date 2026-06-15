# vllm-project/vllm#41342: [CI Failure]:  mi355_1: Entrypoints Integration (Pooling)

| 字段 | 值 |
| --- | --- |
| Issue | [#41342](https://github.com/vllm-project/vllm/issues/41342) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_1: Entrypoints Integration (Pooling)

### Issue 正文摘录

### Name of failing test `pytest -s -v entrypoints/pooling/scoring/test_cross_encoder_online_vision.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED entrypoints/pooling/scoring/test_cross_encoder_online_vision.py::test_score_api_queries_str_documents_str[ROCM_AITER_FA] FAILED entrypoints/pooling/scoring/test_cross_encoder_online_vision.py::test_score_api_queries_str_documents_text_content[ROCM_AITER_FA] FAILED entrypoints/pooling/scoring/test_cross_encoder_online_vision.py::test_score_api_queries_str_documents_list[ROCM_AITER_FA] FAILED entrypoints/pooling/scoring/test_cross_encoder_online_vision.py::test_rerank_api_queries_str_documents_list[ROCM_AITER_FA] FAILED entrypoints/pooling/scoring/test_cross_encoder_online_vision.py::test_score_api_queries_list_documents_list[ROCM_AITER_FA] FAILED entrypoints/pooling/scoring/test_cross_encoder_online_vision.py::test_score_api_queries_str_documents_str[FLEX_ATTENTION] FAILED entrypoints/pooling/scoring/test_cross_encoder_online_vision.py::test_score_api_queries_str_documents_text_content[FLEX_ATTENTION] FAILED...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_1: Entrypoints Integration (Pooling) ci-failure ### Name of failing test `pytest -s -v entrypoints/pooling/scoring/test_cross_encoder_online_vision.py` ### Basic information - [ ] Flaky test - [x]
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _encoder_online_vision.py::test_score_api_queries_str_documents_str[ROCM_AITER_FA] FAILED entrypoints/pooling/scoring/test_cross_encoder_online_vision.py::test_score_api_queries_str_documents_text_content[ROCM_AITER_FA]...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: der_online_vision.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED entrypoints/pooling/sco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cross_encoder_online_vision.py::test_score_api_queries_str_documents_str[ROCM_AITER_FA] FAILED entrypoints/pooling/scoring/test_cross_encoder_online_vision.py::test_score_api_queries_str_documents_text_content[ROCM_AITE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: points/pooling/scoring/test_cross_encoder_online_vision.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
