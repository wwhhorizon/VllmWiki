# vllm-project/vllm#20461: [CI Failure]: Language Models Test (Extended Pooling)

| 字段 | 值 |
| --- | --- |
| Issue | [#20461](https://github.com/vllm-project/vllm/issues/20461) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Language Models Test (Extended Pooling)

### Issue 正文摘录

### Name of failing test See below ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Remaining failures: ``` FAILED models/language/pooling/test_scoring.py::test_cross_encoder_1_to_1[cross-encoder/ms-marco-MiniLM-L-6-v2] - assert 9.265625 == 1.0 ± 1.0e-02 comparison failed Obtained: 9.265625 Expected: 1.0 ± 1.0e-02 FAILED models/language/pooling/test_scoring.py::test_cross_encoder_1_to_N[cross-encoder/ms-marco-MiniLM-L-6-v2] - assert 9.265625 == 1.0 ± 1.0e-02 comparison failed Obtained: 9.265625 Expected: 1.0 ± 1.0e-02 FAILED models/language/pooling/test_scoring.py::test_cross_encoder_N_to_N[cross-encoder/ms-marco-MiniLM-L-6-v2] - assert 9.265625 == 1.0 ± 1.0e-02 comparison failed Obtained: 9.265625 Expected: 1.0 ± 1.0e-02 ``` Fixed by #20168: ``` FAILED models/language/pooling/test_embedding.py::test_models[False-sentence-transformers/all-MiniLM-L12-v2] - pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig Value error, User-specified max_model_len (512) is greater than the derived max_model_len (max_position_embeddings=128 or model_max_leng...

## 现有链接修复摘要

#20168 [Model][3/N] Automatic conversion of CrossEncoding model

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Language Models Test (Extended Pooling) ci-failure ### Name of failing test See below ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tr
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Language Models Test (Extended Pooling) ci-failure ### Name of failing test See below ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `tra...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: iling test See below ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Remaining failures: ``` FAILED mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: one in model's config.json). This may lead to incorrect model outputs or CUDA errors. To allow overriding this maximum, set the env var VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 [type=value_error, input_value=ArgsKwargs((), {'mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: N=1 [type=value_error, input_value=ArgsKwargs((), {'model': ...attention_dtype': None}), input_type=ArgsKwargs] For further information visit https://errors.pydantic.dev/2.11/v/value_error FAILED models/language/pooling...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20168](https://github.com/vllm-project/vllm/pull/20168) | closes_keyword | 0.95 | [Model][3/N] Automatic conversion of CrossEncoding model | FIX (partial) #20461 ## Test Plan pytest tests/models/language/pooling/test_qwen3_reranker.py pytest tests/models/language/pooling/test_mxbai_rerank.py ## Test Result pass ## ( |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
