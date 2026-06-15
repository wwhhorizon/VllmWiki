# vllm-project/vllm#42335: [CI Failure]: e2e scheduling (1 GPU)

| 字段 | 值 |
| --- | --- |
| Issue | [#42335](https://github.com/vllm-project/vllm/issues/42335) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: e2e scheduling (1 GPU)

### Issue 正文摘录

### Name of failing test `v1/e2e/general/test_async_scheduling.py::test_without_spec_decoding` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) Could not reproduce on 1 x B200. Do not have Hopper on hand atm. ### 🧪 Describe the failing test `assert _all_logprobs_match(base_logprobs, test_logprobs)` fails ### 📝 History of failing test Flaky started between commit `2ceea429` and `8b9ea2f8` (dated ~ May 5) ### CC List. _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ernal libraries (e.g. bug in `transformers`) Could not reproduce on 1 x B200. Do not have Hopper on hand atm. ### 🧪 Describe the failing test `assert _all_logprobs_match(base_logprobs, test_logprobs)` fails ### 📝 Histor...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ithout_spec_decoding` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) Could not reproduce on 1 x B200. Do not have Hopper on hand atm. #...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: e2e scheduling (1 GPU) ci-failure ### Name of failing test `v1/e2e/general/test_async_scheduling.py::test_without_spec_decoding` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Ca
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: neral/test_async_scheduling.py::test_without_spec_decoding` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) Could not reproduce on 1 x B...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: e2e scheduling (1 GPU) ci-failure ### Name of failing test `v1/e2e/general/test_async_scheduling.py::test_without_spec_decoding` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Cau...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
