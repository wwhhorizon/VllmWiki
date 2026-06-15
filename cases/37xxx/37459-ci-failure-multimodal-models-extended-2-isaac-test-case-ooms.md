# vllm-project/vllm#37459: [CI Failure]: MultiModal Models Extended 2 - isaac test case OOMs

| 字段 | 值 |
| --- | --- |
| Issue | [#37459](https://github.com/vllm-project/vllm/issues/37459) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: MultiModal Models Extended 2 - isaac test case OOMs

### Issue 正文摘录

### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models[isaac-test_case35] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The OOMs started recently with nightly run triggered Tuesday 2AM EST (March 17th) - https://buildkite.com/vllm/ci/builds/56555#019cfa63-99c7-4529-b370-c2b45ea05393 Curiously, it showed up when other tests in the batch started failing. maybe flaky. ### 📝 History of failing test The OOMs started recently with nightly run triggered Tuesday 2AM (March 17th) - https://buildkite.com/vllm/ci/builds/56555#019cfa63-99c7-4529-b370-c2b45ea05393 ### CC List. cc @AkshatSh @ywang96 @oscardev256

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: MultiModal Models Extended 2 - isaac test case OOMs ci-failure ### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models[isaac-test_case35] ### Basic information - [ ]...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: MultiModal Models Extended 2 - isaac test case OOMs ci-failure ### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models[isaac-test_case35] ### Basic information - [
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s[isaac-test_case35] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The OOMs started recently with nigh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: The OOMs started recently with nightly run triggered Tuesday 2AM EST (March 17th) - https://buildkite.com/vllm/ci/builds/56555#019cfa63-99c7-4529-b370-c2b45ea05393 Curiously, it showed up when other tests in the batch s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [CI Failure]: MultiModal Models Extended 2 - isaac test case OOMs ci-failure ### Name of failing test models/multimodal/generation/test_common.py::test_single_image_models[isaac-test_case35] ### Basic information - [ ]...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
