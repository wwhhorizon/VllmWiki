# vllm-project/vllm#28314: [AMD][CI Failure]: Tracking failure for AMD CI Dependencies & Environments

| 字段 | 值 |
| --- | --- |
| Issue | [#28314](https://github.com/vllm-project/vllm/issues/28314) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [AMD][CI Failure]: Tracking failure for AMD CI Dependencies & Environments

### Issue 正文摘录

Issue to track all AMD CI failures related dependencies & environments: - [x] (@Alexei-V-Ivanov-AMD) Multi-GPU testing: HW issue is fixed, K8S is killing job randomly([context](https://vllm-dev.slack.com/archives/C07QCS7CVEK/p1761091107999459)) - [x] UV is not enabled in AMD docker ([failure](https://buildkite.com/vllm/ci/builds/37953#019a5cb0-954e-49a5-9392-5c2c1ec56bed)) - [ ] torchaudio is not enabled in AMD docker ([failure](https://buildkite.com/vllm/amd-ci/builds/1020#019a5bf9-ad43-4f7c-a17a-cda1ac4d79c9)) (Note) - [ ] terratorch is not enabled in AMD docker (Note: conflict with blinker version installed in original docker) - [ ] pqdm, num2words is not enabled in AMD docker - [ ] ....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [AMD][CI Failure]: Tracking failure for AMD CI Dependencies & Environments rocm;ci-failure Issue to track all AMD CI failures related dependencies & environments: - [x] (@Alexei-V-Ivanov-AMD) Multi-GPU testing: HW issue...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: MD][CI Failure]: Tracking failure for AMD CI Dependencies & Environments rocm;ci-failure Issue to track all AMD CI failures related dependencies & environments: - [x] (@Alexei-V-Ivanov-AMD) Multi-GPU testing: HW issue i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ted dependencies & environments: - [x] (@Alexei-V-Ivanov-AMD) Multi-GPU testing: HW issue is fixed, K8S is killing job randomly([context](https://vllm-dev.slack.com/archives/C07QCS7CVEK/p1761091107999459)) - [x] UV is n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
