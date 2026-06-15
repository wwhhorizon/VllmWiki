# vllm-project/vllm#41324: [CI Failure]:  mi355_2: GPQA Eval (GPT-OSS) (2xB200-2xMI355)

| 字段 | 值 |
| --- | --- |
| Issue | [#41324](https://github.com/vllm-project/vllm/issues/41324) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | fp8;triton |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_2: GPQA Eval (GPT-OSS) (2xB200-2xMI355)

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_2-gpqa-eval-gpt-oss-2xb200-2xmi355 && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && uv pip install --system 'gpt-oss[eval]==0.0.5' && pytest -s -v evals/gpt_oss/test_gpqa_correctness.py --config-list-file=configs/models-gfx950.txt` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-rocm-quark-mxfp4-fp8-triton] ``` ### 📝 History of failing test - Current streak start: 2026-04-27 - First failure in 60d window: 2026-04-21 - Last successful nightly: 2026-04-26 - Break frequency (60d, pass↔fail flips): 4 - Latest nightly date: 2026-04-29 - Latest build(s): [amd-ci #8058](https://buildkite.com/vllm/amd-ci/builds/8058) - Latest hardware status: `mi355_2`=fail ### CC List. _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: s/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-rocm-quark-mxfp4-fp8-triton] ``` ### 📝 History of failing test - Current streak start: 2026-04-27 - First failure in 60d window: 2026-04-21 - Last successful...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [CI Failure]: mi355_2: GPQA Eval (GPT-OSS) (2xB200-2xMI355) rocm;ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_2-gpqa-eval-gpt-oss-2xb200-2xmi355 && export VLLM_ALL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [CI Failure]: mi355_2: GPQA Eval (GPT-OSS) (2xB200-2xMI355) rocm;ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_2-gpqa-eval-gpt-oss-2xb200-2xmi355 && export VLLM_ALL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi355_2: GPQA Eval (GPT-OSS) (2xB200-2xMI355) rocm;ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_2-gpqa-eval-gpt-oss-2xb200-2xmi355 && export VLLM_ALL
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi355_2: GPQA Eval (GPT-OSS) (2xB200-2xMI355) rocm;ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi355_2-gpqa-eval-gpt-oss-2xb200-2xmi355 && export VLLM_ALL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
