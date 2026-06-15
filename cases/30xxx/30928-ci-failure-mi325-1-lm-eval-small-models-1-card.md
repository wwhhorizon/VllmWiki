# vllm-project/vllm#30928: [CI Failure]:  mi325_1: LM Eval Small Models (1 Card)

| 字段 | 值 |
| --- | --- |
| Issue | [#30928](https://github.com/vllm-project/vllm/issues/30928) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: LM Eval Small Models (1 Card)

### Issue 正文摘录

### Name of failing test `pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-small.txt --tp-size=1` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test is evaluating small language models using lm-eval tool. This is a newly added test. ### 📝 History of failing test Test started failing on 17th of Dec 2025 ### CC List. This is

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi325_1: LM Eval Small Models (1 Card) ci-failure ### Name of failing test `pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-small.txt --tp-size=1` ### Basic information...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_1: LM Eval Small Models (1 Card) ci-failure ### Name of failing test `pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-small.txt --tp-size=1` ### Basic information...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: mall.txt --tp-size=1` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Test is evaluating small language...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: mi325_1: LM Eval Small Models (1 Card) ci-failure ### Name of failing test `pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-small.txt --tp-size=1` ### Basic informatio
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: mi325_1: LM Eval Small Models (1 Card) ci-failure ### Name of failing test `pytest -s -v evals/gsm8k/test_gsm8k_correctness.py --config-list-file=configs/models-small.txt --tp-size=1` ### Basic information...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
