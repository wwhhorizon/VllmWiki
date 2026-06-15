# vllm-project/vllm#22837: [CI Failure][NIGHTLY FIRE DRILL]: Multi-Modal Models Test (Extended 1)

| 字段 | 值 |
| --- | --- |
| Issue | [#22837](https://github.com/vllm-project/vllm/issues/22837) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][NIGHTLY FIRE DRILL]: Multi-Modal Models Test (Extended 1)

### Issue 正文摘录

### Name of failing test models/multimodal/pooling/test_dse_qwen2_vl.py::test_models_text[bfloat16-MrLight/dse-qwen2-2b-mrl-v1] models/multimodal/generation/test_ultravox.py::test_online_serving[server0] models/multimodal/generation/test_ultravox.py::test_online_serving[server1] models/multimodal/generation/test_voxtral.py::test_online_serving ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash models/multimodal/pooling/test_dse_qwen2_vl.py::test_models_text[bfloat16-MrLight/dse-qwen2-2b-mrl-v1] models/multimodal/generation/test_ultravox.py::test_online_serving[server0] models/multimodal/generation/test_ultravox.py::test_online_serving[server1] models/multimodal/generation/test_voxtral.py::test_online_serving ``` ### 📝 History of failing test - https://buildkite.com/vllm/ci/builds/26788#0198a196-b391-41ab-8761-e778aa0a6d0a ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure][NIGHTLY FIRE DRILL]: Multi-Modal Models Test (Extended 1) ci-failure ### Name of failing test models/multimodal/pooling/test_dse_qwen2_vl.py::test_models_text[bfloat16-MrLight/dse-qwen2-2b-mrl-v1] models/mu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][NIGHTLY FIRE DRILL]: Multi-Modal Models Test (Extended 1) ci-failure ### Name of failing test models/multimodal/pooling/test_dse_qwen2_vl.py::test_models_text[bfloat16-MrLight/dse-qwen2-2b-mrl-v1] models/mul
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: g test models/multimodal/pooling/test_dse_qwen2_vl.py::test_models_text[bfloat16-MrLight/dse-qwen2-2b-mrl-v1] models/multimodal/generation/test_ultravox.py::test_online_serving[server0] models/multimodal/generation/test...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ::test_online_serving ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash models/multimodal/pooling/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure][NIGHTLY FIRE DRILL]: Multi-Modal Models Test (Extended 1) ci-failure ### Name of failing test models/multimodal/pooling/test_dse_qwen2_vl.py::test_models_text[bfloat16-MrLight/dse-qwen2-2b-mrl-v1] models/mu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
