# vllm-project/vllm#27945: [Bug][CI Failure]: Triton Attention not respects bad words filter on AMD

| 字段 | 值 |
| --- | --- |
| Issue | [#27945](https://github.com/vllm-project/vllm/issues/27945) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;sampling_logits |
| 子分类 |  |
| Operator 关键词 | attention;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][CI Failure]: Triton Attention not respects bad words filter on AMD

### Issue 正文摘录

### Name of failing test tests/v1/sample/test_sampling_params_e2e.py::test_bad_words ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `tests/v1/sample/test_sampling_params_e2e.py::test_bad_words` is consistently failing on AMD CI: ``` params = SamplingParams(temperature=0, bad_words=[bad_words_1, bad_words_2]) output = llm.generate(PROMPT, params) new_text = output[0].outputs[0].text assert bad_words_1 not in new_text > assert bad_words_2 not in new_text E AssertionError: assert 'presencelambdaimes' not in ' ancكroph\\...celambdaimes' E E 'presencelambdaimes' is contained here: E ancكroph\istoire gek reasons video clés interactive dello must COM presencelambdaimes E ? ++++++++++++++++++ tests/v1/sample/test_sampling_params_e2e.py:131: AssertionError ``` However, when using a different attention backed(eg. AITER FA with `VLLM_ROCM_USE_AITER=1`), tests can pass with a reasonable result. ### 📝 History of failing test Locally reproducible. ### CC List. @Alexei-V-Ivanov-AMD @HAIAI

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug][CI Failure]: Triton Attention not respects bad words filter on AMD rocm;ci-failure ### Name of failing test tests/v1/sample/test_sampling_params_e2e.py::test_bad_words ### Basic information - [ ] Flaky test - [x]...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: 2e.py::test_bad_words ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test `tests/v1/sample/test_sampling_par...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug][CI Failure]: Triton Attention not respects bad words filter on AMD rocm;ci-failure ### Name of failing test tests/v1/sample/test_sampling_params_e2e.py::test_bad_words ### Basic information - [ ] Flaky test - [x]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug][CI Failure]: Triton Attention not respects bad words filter on AMD rocm;ci-failure ### Name of failing test tests/v1/sample/test_sampling_params_e2e.py::test_bad_words ### Basic information - [ ] Flaky test - [x]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tests/v1/sample/test_sampling_params_e2e.py::test_bad_words ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
