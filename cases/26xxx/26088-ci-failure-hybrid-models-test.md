# vllm-project/vllm#26088: [CI Failure]: Hybrid models test

| 字段 | 值 |
| --- | --- |
| Issue | [#26088](https://github.com/vllm-project/vllm/issues/26088) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Hybrid models test

### Issue 正文摘录

### Name of failing test tests/models/language/generation/test_hybrid.py::test_models[5-64-state-spaces/mamba-130m-hf] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The hybrid models tests are failing on main since https://github.com/vllm-project/vllm/pull/25951 was merged. The reason is that we set max-num-seqs=4 in the hybrid model tests. Since this is less than the now-default setting of cudagraph_capture_sizes=[8] there are no CUDA graphs captured at all for decode batches. This creates some edge case in the mamba1 attention builder. I started changing the code to fix it but then questioned if this is something we really want to allow. Woudl it not be better to raise if the user tries to capture decode only CUDA graphs that are strictly greater than the max-num-seqs? ### 📝 History of failing test Broken since since https://github.com/vllm-project/vllm/pull/25951 was merged. ### CC List. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Hybrid models test ci-failure ### Name of failing test tests/models/language/generation/test_hybrid.py::test_models[5-64-state-spaces/mamba-130m-hf] ### Basic information - [ ] Flaky test - [x] Can reprodu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Hybrid models test ci-failure ### Name of failing test tests/models/language/generation/test_hybrid.py::test_models[5-64-state-spaces/mamba-130m-hf] ### Basic information - [ ] Flaky test - [x] Can reprod
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: spaces/mamba-130m-hf] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The hybrid models tests are failin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e hybrid model tests. Since this is less than the now-default setting of cudagraph_capture_sizes=[8] there are no CUDA graphs captured at all for decode batches. This creates some edge case in the mamba1 attention build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: cudagraph_capture_sizes=[8] there are no CUDA graphs captured at all for decode batches. This creates some edge case in the mamba1 attention builder. I started changing the code to fix it but then questioned if this is...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
