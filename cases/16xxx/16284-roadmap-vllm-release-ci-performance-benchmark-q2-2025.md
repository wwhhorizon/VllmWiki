# vllm-project/vllm#16284: [Roadmap] vLLM Release/CI/Performance Benchmark Q2 2025

| 字段 | 值 |
| --- | --- |
| Issue | [#16284](https://github.com/vllm-project/vllm/issues/16284) |
| 状态 | open |
| 标签 | keep-open |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;slowdown |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Roadmap] vLLM Release/CI/Performance Benchmark Q2 2025

### Issue 正文摘录

This is a living document! If you're interested in contributing to any item, please join `#sig-ci` channel in [vLLM Slack](https://slack.vllm.ai)! If any of the items you wanted is not on the roadmap, your suggestion and contribution is strongly welcomed! Please feel free to comment in this thread, open feature request, or create an RFC. --- #### Release *In this quarter, we want to support & publish built-in artifacts for various platforms & hardwares on a more regular basis* ✅ Finished 🛣️ In roadmap | | Per Commit wheel | Nightly wheel | Versioned wheel | Per commit image | Nightly image | Versioned image | | -------------- | ---------------- | ------------- | --------------- | ---------------- | ------------- | --------------- | | CUDA (Default) | ✅ | 🛣️ | ✅ | ✅ | 🛣️ | ✅ | | CUDA 11.8 | ✅ | | ✅ | | 🛣️ | 🛣️ | | CUDA 12.1 | ✅ | | ✅ | | 🛣️ | 🛣️ | | aarch (GH200) | 🛣️ | 🛣️ | 🛣️ | | 🛣️ | 🛣️ | | ROCm | | 🛣️ | 🛣️ | | 🛣️ | 🛣️ | | TPU | | 🛣️ | 🛣️ | | 🛣️ | 🛣️ | | Neuron | | 🛣️ | 🛣️ | | 🛣️ | 🛣️ | | CPU | | 🛣️ | 🛣️ | | 🛣️ | 🛣️ | | HPU | | | | | | 🛣️ | | XPU | | | | | | 🛣️ | | IBM Power | |🛣️ | | | 🛣️ | | | IBM Z (s390x) | | | | | 🛣️ | | #### CI *Our CI has been growing and that comes with...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: --------------- | ---------------- | ------------- | --------------- | | CUDA (Default) | ✅ | 🛣️ | ✅ | ✅ | 🛣️ | ✅ | | CUDA 11.8 | ✅ | | ✅ | | 🛣️
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ernels, etc.) - [ ] Optimize image build time - [ ] Reduce number of models used in unit tests - [ ] Implement better conditional testing strategy - [ ] Stability - [ ] #16353 - [ ] Add long-running stress tests for rel...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Roadmap] vLLM Release/CI/Performance Benchmark Q2 2025 keep-open This is a living document! If you're interested in contributing to any item, please join `#sig-ci` channel in [vLLM Slack](https://slack.vllm.ai)! If any...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Roadmap] vLLM Release/CI/Performance Benchmark Q2 2025 keep-open This is a living document! If you're interested in contributing to any item, please join `#sig-ci` channel in [vLLM Slack](https://slack.vllm.ai)! If any...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: rpose of benchmark into two: - Developer facing: performance regression, accuracy, stress test, release gating performance tests. - User facing: versioned benchmarks on a variety of workloads with reproducible commands....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
