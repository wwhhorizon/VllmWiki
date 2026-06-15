# vllm-project/vllm#25144: [RFC]: vLLM’s Path to Sustainable CI/CD

| 字段 | 值 |
| --- | --- |
| Issue | [#25144](https://github.com/vllm-project/vllm/issues/25144) |
| 状态 | closed |
| 标签 | RFC;ci/build;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;multimodal_vlm;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | attention;kernel |
| 症状 | build_error |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: vLLM’s Path to Sustainable CI/CD

### Issue 正文摘录

### Motivation. CI is the foundation for helping every contributor to develop on top of vLLM and gatekeep quality and performance for each release. vLLM’s CI has been in a very worrisome state: The CI/CD system is plagued by slowness, frequent failures, and an inability to reliably detect correctness and performance regressions in critical models. This has led developers to first suspect CI flakiness rather than code issues when tests fail. While efforts like https://github.com/vllm-project/vllm/issues/22992 are underway to refactor gold tests, deprecate V0, improve V1 test coverage, and address timeouts, flaky tests, and hardware resource acquisition, we also need to consider fundamental structural and process changes. These changes are crucial to prevent CI from reverting to a detrimental state and turn CI/CD into shared responsibilities of all contributors. ### Proposed Change. ## Principles 1. Trunk should be green >95% time. 2. Flaky tests are worse than no tests. 3. Reduce humans in the loop. 4. Optimize for effective test<>fix loop. 5. Test what is modified. ## Success Criteria Measured in buildkite CI: - Reliability > 90% - Speed - Format | - Unit tests - Component integra...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: using recommended recipes (including multimodal models) - on Hx00 and GB200 **P1:** - numerical stability - on A100, Mi300x, TPU, etc. - all serving paradigms (disagg, multi-node EP, w/ native tool call) - dependency ve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: y to reliably detect correctness and performance regressions in critical models. This has led developers to first suspect CI flakiness rather than code issues when tests fail. While efforts like https://github.com/vllm-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ailures, and an inability to reliably detect correctness and performance regressions in critical models. This has led developers to first suspect CI flakiness rather than code issues when tests fail. While efforts like...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [RFC]: vLLM’s Path to Sustainable CI/CD RFC;ci/build;stale ### Motivation. CI is the foundation for helping every contributor to develop on top of vLLM and gatekeep quality and performance for each release. vLLM’s CI ha...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: cipes (including multimodal models) - on Hx00 and GB200 **P1:** - numerical stability - on A100, Mi300x, TPU, etc. - all serving paradigms (disagg, multi-node EP, w/ native tool call) - dependency version compatibility...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
