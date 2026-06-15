# vllm-project/vllm#20336: [Roadmap] vLLM Roadmap Q3 2025

| 字段 | 值 |
| --- | --- |
| Issue | [#20336](https://github.com/vllm-project/vllm/issues/20336) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;moe |
| 症状 | build_error;nondeterministic;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Roadmap] vLLM Roadmap Q3 2025

### Issue 正文摘录

This page is accessible via [roadmap.vllm.ai](https://roadmap.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel in the [vLLM Slack](https://slack.vllm.ai) --- ## Core Themes *In Q3, we continue to iterate towards vLLM 1.0 by fully removing the V0 code path, optimizing and extending the core scheduler, making sure vLLM can serve the most demanding workloads of the world, and enhancing the out of box usability and performance.* ### V1 Engine * [x] V0 Features Parity and Native Features (\#sig-v1) * [x] Pooling Model (#16188) * [x] Mamba Model (https://github.com/vllm-project/vllm/pull/19327) * [x] Priority Scheduling (https://github.com/vllm-project/vllm/pull/19057) * [x] Custom Logits Processing (#17799) * [x] CPU KV Cache (#19854) * [x] Investigate Encoder-Decoder Support (https://github.com/vllm-project/vllm/pull/21088) * [ ] Performance * [x] Async Scheduling https://github.com/vllm-project/vllm/pull/19970 * [ ] Optimize Input Preparation (Persistent Batch V2) * [ ] Speculative Decoding Enhancements (Suffix Decoding, CUDA Graph/torch.compile support) * [ ] Multimodal Processing * [ ] Simplification * [x] Parall...

## 现有链接修复摘要

#21088 [v1] Add Whisper model support (encoder-decoder) | #21270 Support encoder-only models without KV-Cache

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: Accelerator UX Audit and Document Feature Coverage * [ ] Stability and Testing * [ ] Comprehensive Reproducible Performance Suite * [ ] Enhance and Report Accuracy Suite * [x] Large Scale Deployment Tested in CI * [ ] S...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: p.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel in the [vLLM Slack](https://slack.vllm.ai) --- ## Core Themes *In Q3, we continue to iterate towar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Roadmap] vLLM Roadmap Q3 2025 rocm This page is accessible via [roadmap.vllm.ai](https://roadmap.vllm.ai/) This is a living document! For each item here, we intend to link the RFC as well as discussion Slack channel in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [x] V0 Features Parity and Native Features (\#sig-v1) * [x] Pooling Model (#16188) * [x] Mamba Model (https://github.com/vllm-project/vllm/pull/19327) * [x] Priority Scheduling (https://github.com/vllm-project/vllm/pull...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: t Feature Coverage * [ ] Stability and Testing * [ ] Comprehensive Reproducible Performance Suite * [ ] Enhance and Report Accuracy Suite * [x] Large Scale Deployment Tested in CI * [ ] Stress and Longevity Testing * [...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21088](https://github.com/vllm-project/vllm/pull/21088) | mentioned | 0.6 | [v1] Add Whisper model support (encoder-decoder) | mpatibility. Related to V0 deprecation (#18571) and 2025 Q3 roadmap (#20336). Closes #12761 Signed-off-by: Russell Bryant <rbryant@redhat.com> Co-authored-by: NickLucche <nlucches… |
| [#21270](https://github.com/vllm-project/vllm/pull/21270) | mentioned | 0.6 | Support encoder-only models without KV-Cache | lf-attention Related to: - V0 deprecation: #18571 - 2025 Q3 roadmap: #20336 This PR is co-authored with @russellb. It borrows all of the encoder-only attention code from his PR ht… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
