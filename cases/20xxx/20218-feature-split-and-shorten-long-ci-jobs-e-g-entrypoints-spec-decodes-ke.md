# vllm-project/vllm#20218: [Feature]:  Split and shorten long CI jobs (e.g. entrypoints, spec decodes, kernels, etc.)

| 字段 | 值 |
| --- | --- |
| Issue | [#20218](https://github.com/vllm-project/vllm/issues/20218) |
| 状态 | closed |
| 标签 | feature request;ci/build;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;kernel;moe;quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]:  Split and shorten long CI jobs (e.g. entrypoints, spec decodes, kernels, etc.)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Related to [issues-16284](https://github.com/vllm-project/vllm/issues/16284) ## Analysis of current CI test process problems The vLLM project currently uses Buildkite as the main CI system, which has the following problems: 1. **Long-running tests**: Some tests run too long, and even 2-hour tests are skipped 2. **Test classification is not detailed enough**: Although there are entry point tests, specification decoding tests, kernel tests and other classifications, there is a lack of effective grouping based on execution time 3. **Insufficient parallelism**: The current CI configuration does not fully utilize the parallel execution capability ## Detailed design plan ### 1. Test layering strategy **First layer: Fast Check** - Based on the existing fast_check tag - Execution time: 60 minutes - Includes: large-scale testing, stress testing, complete performance benchmark testing [6](#0-5) ### 2. Split strategy by functional module **Entry point test module split** - `entrypoints-llm`: LLM interface testing - `entrypoints-openai`: OpenAI API compatibility testing - `entrypoints-offline`: offline mode testing **Spec decoding test module split** -...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: f effective grouping based on execution time 3. **Insufficient parallelism**: The current CI configuration does not fully utilize the parallel execution capability ## Detailed design plan ### 1. Test layering strategy *...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Split and shorten long CI jobs (e.g. entrypoints, spec decodes, kernels, etc.) feature request;ci/build;stale ### 🚀 The feature, motivation and pitch Related to [issues-16284](https://github.com/vllm-project/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ://github.com/vllm-project/vllm/issues/16284) ## Analysis of current CI test process problems The vLLM project currently uses Buildkite as the main CI system, which has the following problems: 1. **Long-running tests**:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Split and shorten long CI jobs (e.g. entrypoints, spec decodes, kernels, etc.) feature request;ci/build;stale ### 🚀 The feature, motivation and pitch Related to [issues-16284](https://github.com/vllm-project/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: existing fast_check tag - Execution time: 60 minutes - Includes: large-scale testing, stress testing, complete performance benchmark testing [6](#0-5) ### 2. Split strategy by functional module **Entry point test module...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
