# vllm-project/vllm#22836: [CI Failure][NIGHTLY FIRE DRILL]: Language Models Test (Pooling)

| 字段 | 值 |
| --- | --- |
| Issue | [#22836](https://github.com/vllm-project/vllm/issues/22836) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][NIGHTLY FIRE DRILL]: Language Models Test (Pooling)

### Issue 正文摘录

### Name of failing test models/language/pooling/test_intfloat.py::test_embed_models_mteb models/language/pooling/test_override_pooler_config.py::test_embed_models_using_normalize[half-intfloat/multilingual-e5-small] models/language/pooling/test_snowflake_arctic_embed.py::test_embed_models_mteb[model_info0] models/language/pooling/test_snowflake_arctic_embed.py::test_embed_models_mteb[model_info5] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```python models/language/pooling/test_intfloat.py::test_embed_models_mteb models/language/pooling/test_override_pooler_config.py::test_embed_models_using_normalize[half-intfloat/multilingual-e5-small] models/language/pooling/test_snowflake_arctic_embed.py::test_embed_models_mteb[model_info0] models/language/pooling/test_snowflake_arctic_embed.py::test_embed_models_mteb[model_info5] ``` ### 📝 History of failing test - https://buildkite.com/vllm/ci/builds/26788#0198a196-b391-41ab-8761-e778aa0a6d0a ### CC List. cc @DarkLight1337

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure][NIGHTLY FIRE DRILL]: Language Models Test (Pooling) ci-failure ### Name of failing test models/language/pooling/test_intfloat.py::test_embed_models_mteb models/language/pooling/test_override_pooler_config.p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][NIGHTLY FIRE DRILL]: Language Models Test (Pooling) ci-failure ### Name of failing test models/language/pooling/test_intfloat.py::test_embed_models_mteb models/language/pooling/test_override_pooler_config.py
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: els_mteb[model_info5] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```python models/language/pooling/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nfig.py::test_embed_models_using_normalize[half-intfloat/multilingual-e5-small] models/language/pooling/test_snowflake_arctic_embed.py::test_embed_models_mteb[model_info0] models/language/pooling/test_snowflake_arctic_e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure][NIGHTLY FIRE DRILL]: Language Models Test (Pooling) ci-failure ### Name of failing test models/language/pooling/test_intfloat.py::test_embed_models_mteb models/language/pooling/test_override_pooler_config.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
