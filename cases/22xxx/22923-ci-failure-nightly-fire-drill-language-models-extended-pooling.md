# vllm-project/vllm#22923: [CI Failure][NIGHTLY FIRE DRILL]: Language Models (Extended Pooling)

| 字段 | 值 |
| --- | --- |
| Issue | [#22923](https://github.com/vllm-project/vllm/issues/22923) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][NIGHTLY FIRE DRILL]: Language Models (Extended Pooling)

### Issue 正文摘录

### Name of failing test `models/language/pooling/test_gte.py::test_embed_models_mteb[model_info7]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash [2025-08-14T17:09:36Z] =================================== FAILURES =================================== -- | [2025-08-14T17:09:36Z] _____________________ test_embed_models_mteb[model_info7] ______________________ | [2025-08-14T17:09:36Z] | [2025-08-14T17:09:36Z] hf_runner = | [2025-08-14T17:09:36Z] vllm_runner = | [2025-08-14T17:09:36Z] model_info = CLSPoolingEmbedModelInfo(name='Alibaba-NLP/gte-base-en-v1.5', is_matryoshka=False, matryoshka_dimensions=None, architecture='GteNewModel', dtype='auto', default_pooling_type='', enable_test=True) | [2025-08-14T17:09:36Z] | [2025-08-14T17:09:36Z] @pytest.mark.parametrize("model_info", MODELS) | [2025-08-14T17:09:36Z] def test_embed_models_mteb(hf_runner, vllm_runner, | [2025-08-14T17:09:36Z] model_info: EmbedModelInfo) -> None: | [2025-08-14T17:09:36Z] if model_info.name == "Alibaba-NLP/gte-Qwen2-1.5B-instruct": | [2025-08-14T17:09:36Z] check_transformers_version(model_i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [CI Failure][NIGHTLY FIRE DRILL]: Language Models (Extended Pooling) ci-failure ### Name of failing test `models/language/pooling/test_gte.py::test_embed_models_mteb[model_info7]` ### Basic information - [ ] Flaky test...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure][NIGHTLY FIRE DRILL]: Language Models (Extended Pooling) ci-failure ### Name of failing test `models/language/pooling/test_gte.py::test_embed_models_mteb[model_info7]` ### Basic information - [ ] Flaky test
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: atryoshka=False, matryoshka_dimensions=None, architecture='GteNewModel', dtype='auto', default_pooling_type='', enable_test=True) | [2025-08-14T17:09:36Z] | [2025-08-14T17:09:36Z] @pytest.mark.parametrize("model_info",...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ls_mteb[model_info7]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash [2025-08-14T17:09:36Z] ===...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: -NLP/gte-base-en-v1.5', is_matryoshka=False, matryoshka_dimensions=None, architecture='GteNewModel', dtype='auto', default_pooling_type='', enable_test=True) | [2025-08-14T17:09:36Z] | [2025-08-14T17:09:36Z] @pytest.mar...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
