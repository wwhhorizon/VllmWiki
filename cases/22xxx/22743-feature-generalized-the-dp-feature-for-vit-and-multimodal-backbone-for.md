# vllm-project/vllm#22743: [Feature]: Generalized the DP feature for ViT and multimodal backbone for the benefit of all models

| 字段 | 值 |
| --- | --- |
| Issue | [#22743](https://github.com/vllm-project/vllm/issues/22743) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;multimodal_vlm |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Generalized the DP feature for ViT and multimodal backbone for the benefit of all models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The existing PRs - https://github.com/vllm-project/vllm/pull/18368 - https://github.com/vllm-project/vllm/pull/22697 - https://github.com/vllm-project/vllm/pull/22742 Has clearly shown that hybrid inferencing: (ViT is DP, and LLM is in TP), has greatly reduce the TTFT and improve the overall throughput significantly. There are multiple reasons that we should have ViT implemented as a DP: 1. The ViT are small models, the TP all reduce incurred a larger overhead than the gain from accelerating through TP. 2. ViT are not captured in cuda graphs or torch compile graph, thus the kernel overhead and all reduce overhead will be higher. Extending the support to more models: - #23168 - #23327 - #23876 - #23878 - #23948 - #24955 - #25445 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#23168 [Model] Support dp on ViT on GLM-4.5V | #23948 [Model] Enable encoder DP for MiniCPM-V | #24955 [MM Encoder] Apply DP ViT for Qwen3-VL model series | #25445 [Model] Enable DP for ViT in Qwen2-VL

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: b.com/vllm-project/vllm/pull/22742 Has clearly shown that hybrid inferencing: (ViT is DP, and LLM is in TP), has greatly reduce the TTFT and improve the overall throughput significantly. There are multiple reasons that...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Generalized the DP feature for ViT and multimodal backbone for the benefit of all models feature request ### 🚀 The feature, motivation and pitch The existing PRs - https://github.com/vllm-project/vllm/pull/18...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: iple reasons that we should have ViT implemented as a DP: 1. The ViT are small models, the TP all reduce incurred a larger overhead than the gain from accelerating through TP. 2. ViT are not captured in cuda graphs or t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: , and LLM is in TP), has greatly reduce the TTFT and improve the overall throughput significantly. There are multiple reasons that we should have ViT implemented as a DP: 1. The ViT are small models, the TP all reduce i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: re for ViT and multimodal backbone for the benefit of all models feature request ### 🚀 The feature, motivation and pitch The existing PRs - https://github.com/vllm-project/vllm/pull/18368 - https://github.com/vllm-proje...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23168](https://github.com/vllm-project/vllm/pull/23168) | mentioned | 0.45 | [Model] Support dp on ViT on GLM-4.5V | ce overhead will be higher. extending the support to more models: - #23168 - #23327 - #23876 - #23878 - #23948 - #24955 - #25445 ### alternatives _no response_ ### additional cont… |
| [#23948](https://github.com/vllm-project/vllm/pull/23948) | mentioned | 0.45 | [Model] Enable encoder DP for MiniCPM-V | ng the support to more models: - #23168 - #23327 - #23876 - #23878 - #23948 - #24955 - #25445 ### alternatives _no response_ ### additional context _no response_ ### before submitt |
| [#24955](https://github.com/vllm-project/vllm/pull/24955) | mentioned | 0.6 | [MM Encoder] Apply DP ViT for Qwen3-VL model series | dels - this PR should be merged only after #24727 is merged. Part of #22743 ## Test Plan Running on `Qwen3-VL-30B-A3B-Instruct` with 4xL40s (PCI-E) with the following changes to t… |
| [#25445](https://github.com/vllm-project/vllm/pull/25445) | mentioned | 0.45 | [Model] Enable DP for ViT in Qwen2-VL | more models: - #23168 - #23327 - #23876 - #23878 - #23948 - #24955 - #25445 ### alternatives _no response_ ### additional context _no response_ ### before submitting a new issue... |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
