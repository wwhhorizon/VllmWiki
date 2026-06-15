# vllm-project/vllm#25364: [CI]: Tests skipped for V0 deprecation

| 字段 | 值 |
| --- | --- |
| Issue | [#25364](https://github.com/vllm-project/vllm/issues/25364) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Tests skipped for V0 deprecation

### Issue 正文摘录

### Name of failing test Listed below ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Tracking issue for the tests skipped for V0 deprecation. These tests should be re-enabled with proper fixes or removed. - [x] Skipped because it is flaky in CI https://github.com/vllm-project/vllm/blob/6d0b827cbd0510173f6a9e77549d917828e80c76/tests/entrypoints/openai/test_completion_with_prompt_embeds.py#L66 - [x] Skipped because of lack of knowledge on the tests https://github.com/vllm-project/vllm/blob/6d0b827cbd0510173f6a9e77549d917828e80c76/tests/kernels/attention/test_attention_selector.py#L70 - [x] OOT registration failed somehow https://github.com/vllm-project/vllm/blob/6d0b827cbd0510173f6a9e77549d917828e80c76/tests/models/test_oot_registration.py#L45 - [x] Pipeline test failed for some reason https://github.com/vllm-project/vllm/blob/6d0b827cbd0510173f6a9e77549d917828e80c76/tests/distributed/test_pipeline_parallel.py#L385 ### 📝 History of failing test After V0 deprecation ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: precation ci-failure ### Name of failing test Listed below ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ng test Listed below ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Tracking issue for the tests skippe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI]: Tests skipped for V0 deprecation ci-failure ### Name of failing test Listed below ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`)
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Tests skipped for V0 deprecation ci-failure ### Name of failing test Listed below ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`)...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
