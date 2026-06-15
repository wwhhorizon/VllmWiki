# vllm-project/vllm#41017: [CI Failure]:  Llama-4-Scout-FP8 tp2 fusion_e2e OOM on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#41017](https://github.com/vllm-project/vllm/issues/41017) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;quantization |
| 子分类 | memory |
| Operator 关键词 | fp8 |
| 症状 | oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  Llama-4-Scout-FP8 tp2 fusion_e2e OOM on H100

### Issue 正文摘录

### Name of failing test Fusion E2E TP2 Quick (H100) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Failed CIs - https://buildkite.com/vllm/ci/builds/63098/canvas?jid=019dcf20-46e0-4c44-9581-0b8f21c5d0fe&tab=output ## Error Message ### 📝 History of failing test - https://buildkite.com/vllm/ci/builds/63098/canvas?jid=019dcf20-46e0-4c44-9581-0b8f21c5d0fe - https://buildkite.com/vllm/ci/builds/63091/canvas?jid=019dcf05-0202-4802-b6a9-58c021ec2b32 - https://buildkite.com/vllm/ci/builds/63071#019dcde0-a049-4196-8870-f7c11f35fa2c - https://buildkite.com/vllm/ci/builds/63070/canvas?jid=019dcdd6-c3ed-42d9-b9c6-9fef9ecce17e - https://buildkite.com/vllm/ci/builds/63059/canvas?jid=019dcd7c-b66e-4082-bfd6-c9273276e521 ... ### CC List. _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [CI Failure]: Llama-4-Scout-FP8 tp2 fusion_e2e OOM on H100 ci-failure ### Name of failing test Fusion E2E TP2 Quick (H100) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Llama-4-Scout-FP8 tp2 fusion_e2e OOM on H100 ci-failure ### Name of failing test Fusion E2E TP2 Quick (H100) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external li
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: Llama-4-Scout-FP8 tp2 fusion_e2e OOM on H100 ci-failure ### Name of failing test Fusion E2E TP2 Quick (H100) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: E2E TP2 Quick (H100) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ## Failed CIs - https://buildkite.c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: Llama-4-Scout-FP8 tp2 fusion_e2e OOM on H100 ci-failure ### Name of failing test Fusion E2E TP2 Quick (H100) ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
