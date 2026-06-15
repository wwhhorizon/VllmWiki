# vllm-project/vllm#24777: [Bug] / [Feature]: Determinism in E2E Spec Decode Test

| 字段 | 值 |
| --- | --- |
| Issue | [#24777](https://github.com/vllm-project/vllm/issues/24777) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] / [Feature]: Determinism in E2E Spec Decode Test

### Issue 正文摘录

### Your current environment Latest main as of 010acc6e1ea1d59ef530459e1078e8fde80f2082 ### 🐛 Describe the bug The n-gram speculative decoding test in `tests/v1/e2e/test_spec_decode.py` is **flaky** - the match rate between reference and speculative outputs varies randomly between test runs, even with deterministic settings (`temperature=0`). This causes intermittent CI failures and reduces test reliability. This kind of issue may also exist in other spec decode method. See comments: https://github.com/vllm-project/vllm/pull/24771#pullrequestreview-3218208030 Related issue: https://github.com/vllm-project/vllm/issues/24314 Related PRs: https://github.com/vllm-project/vllm/pull/24528, https://github.com/vllm-project/vllm/pull/24771 Investigation steps: 1. N-gram spec decode: this should be relatively easy-to-inspect. 2. Other eagle-/model-based spec decode: Could we achieve some degree of determinism if we set `temperature=0`? This would be helpful to set a strict but fine-if-correct threshold to our test and make us easier to reproduce problems. Target: Investigate the deterministic part and assert it strictly in the tests. (The tests would should have the exact behavior as what w...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug] / [Feature]: Determinism in E2E Spec Decode Test bug;stale ### Your current environment Latest main as of 010acc6e1ea1d59ef530459e1078e8fde80f2082 ### 🐛 Describe the bug The n-gram speculative decoding test in `te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: nce and speculative outputs varies randomly between test runs, even with deterministic settings (`temperature=0`). This causes intermittent CI failures and reduces test reliability. This kind of issue may also exist in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug] / [Feature]: Determinism in E2E Spec Decode Test bug;stale ### Your current environment Latest main as of 010acc6e1ea1d59ef530459e1078e8fde80f2082 ### 🐛 Describe the bug The n-gram speculative decoding test in `te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug] / [Feature]: Determinism in E2E Spec Decode Test bug;stale ### Your current environment Latest main as of 010acc6e1ea1d59ef530459e1078e8fde80f2082 ### 🐛 Describe the bug The n-gram speculative decoding test in `te...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: with deterministic settings (`temperature=0`). This causes intermittent CI failures and reduces test reliability. This kind of issue may also exist in other spec decode method. See comments: https://github.com/vllm-proj...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
