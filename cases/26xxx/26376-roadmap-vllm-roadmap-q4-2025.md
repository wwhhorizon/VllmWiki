# vllm-project/vllm#26376: [Roadmap] vLLM Roadmap Q4 2025

| 字段 | 值 |
| --- | --- |
| Issue | [#26376](https://github.com/vllm-project/vllm/issues/26376) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;moe |
| 症状 | build_error;nondeterministic |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Roadmap] vLLM Roadmap Q4 2025

### Issue 正文摘录

This page is accessible via [roadmap.vllm.ai](http://roadmap.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel in the [vLLM Slack](https://slack.vllm.ai) --- *In the [Q3 2025](https://github.com/vllm-project/vllm/issues/20336), we fully removed V0 code path and made vLLM excel in large scale serving with mature wide E and prefill disaggregation. In this quarter, our goal is to continue to drive down the CPU overhead, enhance vLLM on frontier clusters, and strengthen our RL integrations.* We list help wanted item as 🙋in areas that the committer group is seeking more dedicated contributions. ### Engine Core * [x] Async Scheduling on by default ([#sig-default-async-sched](https://vllm-dev.slack.com/archives/C09HD0B0H25)) * [x] Optimize Input Preparation (“Persistent Batch V2”) * [ ] Multimodal Processing Simplification ([#sig-multi-modality](https://vllm-dev.slack.com/archives/C07QCGVDNUF)) * [ ] 🙋Speculative Decoding Enhancements (Suffix Decoding, CUDA Graph/torch.compile support) ([#feat-spec-decode](https://vllm-dev.slack.com/archives/C07RFT2UT16)) ### Large Scale Serving * [ ] Elastic Experts ([#feat-elastic-ep]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: D0B0H25)) * [x] Optimize Input Preparation (“Persistent Batch V2”) * [ ] Multimodal Processing Simplification ([#sig-multi-modality](https://vllm-dev.slack.com/archives/C07QCGVDNUF)) * [ ] 🙋Speculative Decoding Enhancem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ing on by default ([#sig-default-async-sched](https://vllm-dev.slack.com/archives/C09HD0B0H25)) * [x] Optimize Input Preparation (“Persistent Batch V2”) * [ ] Multimodal Processing Simplification ([#sig-multi-modality](...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Roadmap] vLLM Roadmap Q4 2025 stale This page is accessible via [roadmap.vllm.ai](http://roadmap.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: p.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel in the [vLLM Slack](https://slack.vllm.ai) --- *In the [Q3 2025](https://github.com/vllm-project/v...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ://vllm-dev.slack.com/archives/C07UUL8E61Z)) * [x] Full determinism and batch invariance * [x] Add more testing cases for popular integrations * [ ] Custom checkpoint loader, custom model format * [x] Simple data parall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
