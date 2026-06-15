# vllm-project/vllm#28135: [RFC]: Robust End-to-End CI/CD Regression Testing for Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#28135](https://github.com/vllm-project/vllm/issues/28135) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | gemm;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Robust End-to-End CI/CD Regression Testing for Speculative Decoding

### Issue 正文摘录

### Motivation. ## Executive Summary Proposes regression testing for speculative decoding in vLLM, starting with Eagle3 and expanding to all variants. **Objectives:** - Prevent regressions in acceptance rates and speedup - Detect performance degradation in CI - Validate correctness across variants - Manage CI costs **Impact:** - Detect regressions in hours vs. days - Provide performance baselines --- ## Table of Contents 1. [Background and Motivation](#background-and-motivation) 2. [Current State Analysis](#current-state-analysis) 3. [Proposal Overview](#proposal-overview) 4. [Design Details](#design-details) 5. [Phased Implementation](#phased-implementation) 6. [CI Resource Management](#ci-resource-management) 7. [Benchmarking Strategy](#benchmarking-strategy) 8. [Future Expansion](#future-expansion) 9. [Open Questions](#open-questions) 10. [References](#references) 11. [Call to Action](#call-to-action) --- ## Background and Motivation Speculative decoding improves LLM latency 2-3x by using a draft model to predict tokens ahead, verified in parallel. vLLM supports n-gram, EAGLE/Eagle3, Medusa, and MTP variants. **Problem:** Small code changes can break acceptance rates and speedu...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: ivation Speculative decoding improves LLM latency 2-3x by using a draft model to predict tokens ahead, verified in parallel. vLLM supports n-gram, EAGLE/Eagle3, Medusa, and MTP variants. **Problem:** Small code changes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [RFC]: Robust End-to-End CI/CD Regression Testing for Speculative Decoding RFC;stale ### Motivation. ## Executive Summary Proposes regression testing for speculative decoding in vLLM, starting with Eagle3 and expanding...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: [RFC]: Robust End-to-End CI/CD Regression Testing for Speculative Decoding RFC;stale ### Motivation. ## Executive Summary Proposes regression testing for speculative decoding in vLLM, starting with Eagle3 and expanding...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [RFC]: Robust End-to-End CI/CD Regression Testing for Speculative Decoding RFC;stale ### Motivation. ## Executive Summary Proposes regression testing for speculative decoding in vLLM, starting with Eagle3 and expanding...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: M supports n-gram, EAGLE/Eagle3, Medusa, and MTP variants. **Problem:** Small code changes can break acceptance rates and speedup without failing correctness tests. **Current Gaps:** 1. No acceptance rate tracking in `t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
