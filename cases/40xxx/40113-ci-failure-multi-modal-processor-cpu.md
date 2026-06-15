# vllm-project/vllm#40113: [CI Failure]: Multi-Modal Processor (CPU)

| 字段 | 值 |
| --- | --- |
| Issue | [#40113](https://github.com/vllm-project/vllm/issues/40113) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Multi-Modal Processor (CPU)

### Issue 正文摘录

### Name of failing test `models/multimodal/processing/test_audioflamingo3.py::test_audio_feature_pipeline_matches_hf_small_config` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [Multi-Modal Processor (CPU)](https://buildkite.com/vllm/ci/builds/61575/steps/canvas?sid=019d94e1-7b94-4fc1-bed1-a2ba667385c2) test fails with `AssertionError: Current vLLM config is not set.` on ``` [2026-04-17T05:53:23Z] /opt/venv/lib/python3.12/site-packages/vllm/utils/collection_utils.py:36: in __getitem__ [2026-04-17T05:53:23Z] self._dict[key] = self._factory[key]() [2026-04-17T05:53:23Z] ^^^^^^^^^^^^^^^^^^^^ [2026-04-17T05:53:23Z] /opt/venv/lib/python3.12/site-packages/vllm/model_executor/layers/activation.py:666: in [2026-04-17T05:53:23Z] "gelu": lambda: GELU(), [2026-04-17T05:53:23Z] ^^^^^^ [2026-04-17T05:53:23Z] /opt/venv/lib/python3.12/site-packages/vllm/model_executor/layers/activation.py:256: in __init__ [2026-04-17T05:53:23Z] super().__init__() [2026-04-17T05:53:23Z] /opt/venv/lib/python3.12/site-packages/vllm/model_executor/custom_op.py:133: in __init__ [2026-04-17T05:53:23Z]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: lure]: Multi-Modal Processor (CPU) ci-failure ### Name of failing test `models/multimodal/processing/test_audioflamingo3.py::test_audio_feature_pipeline_matches_hf_small_config` ### Basic information - [ ] Flaky test -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Multi-Modal Processor (CPU) ci-failure ### Name of failing test `models/multimodal/processing/test_audioflamingo3.py::test_audio_feature_pipeline_matches_hf_small_config` ### Basic information - [ ] Flaky
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: :133: in __init__ [2026-04-17T05:53:23Z] self._forward_method = self.dispatch_forward(compile_native=compile_native) [2026-04-17T05:53:23Z] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2026-04-17T05:53:23Z] /op...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ches_hf_small_config` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [Multi-Modal Processor (CPU)](http...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rocessing/test_audioflamingo3.py::test_audio_feature_pipeline_matches_hf_small_config` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
