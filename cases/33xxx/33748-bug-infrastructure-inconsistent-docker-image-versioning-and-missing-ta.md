# vllm-project/vllm#33748: [Bug][Infrastructure]: Inconsistent Docker Image Versioning and Missing Tags on Docker Hub

| 字段 | 值 |
| --- | --- |
| Issue | [#33748](https://github.com/vllm-project/vllm/issues/33748) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;multimodal_vlm |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Infrastructure]: Inconsistent Docker Image Versioning and Missing Tags on Docker Hub

### Issue 正文摘录

### 🐛 Describe the bug There is NO comprehensive issue tracking all Docker versioning inconsistencies together. The existing issues are fragmented and focus on specific missing versions rather than the systemic problem. The current Docker image release process creates systematic reproducibility barriers that undermine vLLM's adoption in production and research environments. Missing version tags (e.g., v0.6.6.post1), stale latest tags lagging weeks behind releases, and absent CUDA 13+ images force users to spend hours rebuilding locally or accept version mismatches across platforms. This particularly impacts multi-accelerator benchmarking (Intel, NVIDIA, AMD) where version consistency is critical for valid comparisons. We need automated Docker builds for every PyPI release, immediate latest tag updates, and nightly/pre-release channels to restore deployment reliability and enable reproducible research. Without these changes, vLLM's official images are becoming a deployment liability rather than an asset. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](h...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug][Infrastructure]: Inconsistent Docker Image Versioning and Missing Tags on Docker Hub bug ### 🐛 Describe the bug There is NO comprehensive issue tracking all Docker versioning inconsistencies together. The existing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ducibility barriers that undermine vLLM's adoption in production and research environments. Missing version tags (e.g., v0.6.6.post1), stale latest tags lagging weeks behind releases, and absent CUDA 13+ images force us...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: + images force users to spend hours rebuilding locally or accept version mismatches across platforms. This particularly impacts multi-accelerator benchmarking (Intel, NVIDIA, AMD) where version consistency is critical f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: hich can answer lots of frequently asked questions. correctness ci_build;multimodal_vlm cuda mismatch 🐛 Describe the bug
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: esearch environments. Missing version tags (e.g., v0.6.6.post1), stale latest tags lagging weeks behind releases, and absent CUDA 13+ images force users to spend hours rebuilding locally or accept version mismatches acr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
