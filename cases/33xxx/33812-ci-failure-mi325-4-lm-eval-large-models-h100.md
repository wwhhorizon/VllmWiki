# vllm-project/vllm#33812: [CI Failure]:  mi325_4: LM Eval Large Models (H100)

| 字段 | 值 |
| --- | --- |
| Issue | [#33812](https://github.com/vllm-project/vllm/issues/33812) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_4: LM Eval Large Models (H100)

### Issue 正文摘录

### Name of failing test `pytest -s -v test_lm_eval_correctness.py --config-list-file=configs/models-large-hopper.txt --tp-size=4` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in this TG: `FAILED test_lm_eval_correctness.py::test_lm_eval_correctness_param[config_filename1]` Related logs: ```log E pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig E Value error, modelopt quantization is currently not supported in rocm. [type=value_error, input_value=ArgsKwargs((), {'model': ...rocessor_plugin': None}), input_type=ArgsKwargs] E For further information visit https://errors.pydantic.dev/2.12/v/value_error ``` ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/4130/steps/canvas?sid=019c2773-95cc-495c-a583-07776eb32dd1&tab=output

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [CI Failure]: mi325_4: LM Eval Large Models (H100) ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py --config-list-file=configs/models-large-hopper.txt --tp-size=4` ### Basic information - [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi325_4: LM Eval Large Models (H100) ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py --config-list-file=configs/models-large-hopper.txt --tp-size=4` ### Basic information - [...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: mi325_4: LM Eval Large Models (H100) ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py --config-list-file=configs/models-large-hopper.txt --tp-size=4` ### Basic information - [...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_4: LM Eval Large Models (H100) ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py --config-list-file=configs/models-large-hopper.txt --tp-size=4` ### Basic information -
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pper.txt --tp-size=4` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
