# vllm-project/vllm#41583: [CI Failure]:  mi355_2: LM Eval Small Models (2xB200-2xMI355)

| 字段 | 值 |
| --- | --- |
| Issue | [#41583](https://github.com/vllm-project/vllm/issues/41583) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | fp8 |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_2: LM Eval Small Models (2xB200-2xMI355)

### Issue 正文摘录

### Name of failing test `pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-mi3xx-fp8-and-mixed.txt` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8] ``` ### 📝 History of failing test - Current streak start: 2026-05-02 - First failure in 60d window: 2026-04-21 - Last successful nightly: 2026-05-01 - Break frequency (60d, pass↔fail flips): 2 - Latest nightly date: 2026-05-03 - Latest build(s): [amd-ci #8177](https://buildkite.com/vllm/amd-ci/builds/8177) - Latest hardware status: `mi355_2`=fail

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-mi3xx-fp8-and-mixed.txt` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformer...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi355_2: LM Eval Small Models (2xB200-2xMI355) ci-failure ### Name of failing test `pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-mi3xx-fp8-and-mixed.txt` ### Basic i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_2: LM Eval Small Models (2xB200-2xMI355) ci-failure ### Name of failing test `pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-mi3xx-fp8-and-mixed.txt` ### Basic
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: mi355_2: LM Eval Small Models (2xB200-2xMI355) ci-failure ### Name of failing test `pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-mi3xx-fp8-and-mixed.txt` ### Basic i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi355_2: LM Eval Small Models (2xB200-2xMI355) ci-failure ### Name of failing test `pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-mi3xx-fp8-and-mixed.txt` ### Basic i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
