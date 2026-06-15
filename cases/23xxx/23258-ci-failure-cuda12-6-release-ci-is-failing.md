# vllm-project/vllm#23258: [CI Failure]: CUDA12.6 Release CI is failing

| 字段 | 值 |
| --- | --- |
| Issue | [#23258](https://github.com/vllm-project/vllm/issues/23258) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: CUDA12.6 Release CI is failing

### Issue 正文摘录

### Name of failing test Build wheel - CUDA 12.6 ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test CUDA12.6 release CI is failing the release pipeline, causing the nightly wheel failed to upload. (https://github.com/vllm-project/vllm/pull/23084#issuecomment-3204485734) ### 📝 History of failing test CUDA12.6 release CI started to fail after vllm-flash-attention update: https://buildkite.com/vllm/release/builds/7331/steps/canvas ### CC List. cc @LucasWilkinson

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: CUDA12.6 Release CI is failing stale;ci-failure ### Name of failing test Build wheel - CUDA 12.6 ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g.
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ild wheel - CUDA 12.6 ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test CUDA12.6 release CI is failing the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: CUDA12.6 Release CI is failing stale;ci-failure ### Name of failing test Build wheel - CUDA 12.6 ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: i-failure ### Name of failing test Build wheel - CUDA 12.6 ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI Failure]: CUDA12.6 Release CI is failing stale;ci-failure ### Name of failing test Build wheel - CUDA 12.6 ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [x] Caused by external libraries (e.g....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
