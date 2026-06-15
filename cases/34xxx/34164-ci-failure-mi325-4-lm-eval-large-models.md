# vllm-project/vllm#34164: [CI Failure]:  mi325_4: LM Eval Large Models

| 字段 | 值 |
| --- | --- |
| Issue | [#34164](https://github.com/vllm-project/vllm/issues/34164) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_4: LM Eval Large Models

### Issue 正文摘录

### Name of failing test `pytest -s -v test_lm_eval_correctness.py --config-list-file=configs/models-large.txt --tp-size=4` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in this test group. It might be infra related: `OSError: [Errno 28] No space left on device: '/root/.cache/huggingface/hub/models--Qwen--Qwen2-57B-A14B-Instruct'` (https://buildkite.com/vllm/amd-ci/builds/4400/steps/canvas?sid=019c4133-8c50-451e-acf5-b0776ee0334f&tab=output#019c4192-785e-4a46-b3a3-6ffce390e3ac/L1398) ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/4400/steps/canvas?sid=019c4133-8c50-451e-acf5-b0776ee0334f&tab=output

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [CI Failure]: mi325_4: LM Eval Large Models ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py --config-list-file=configs/models-large.txt --tp-size=4` ### Basic information - [ ] Flaky test -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: mi325_4: LM Eval Large Models ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py --config-list-file=configs/models-large.txt --tp-size=4` ### Basic information - [ ] Flaky test -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_4: LM Eval Large Models ci-failure ### Name of failing test `pytest -s -v test_lm_eval_correctness.py --config-list-file=configs/models-large.txt --tp-size=4` ### Basic information - [ ] Flaky test
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: arge.txt --tp-size=4` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
