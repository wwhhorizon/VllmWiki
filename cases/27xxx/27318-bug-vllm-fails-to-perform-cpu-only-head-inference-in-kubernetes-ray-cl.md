# vllm-project/vllm#27318: [Bug]: vLLM fails to perform CPU-only-head inference in Kubernetes + Ray cluster environment

| 字段 | 值 |
| --- | --- |
| Issue | [#27318](https://github.com/vllm-project/vllm/issues/27318) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;kernel |
| 症状 | crash;import_error |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM fails to perform CPU-only-head inference in Kubernetes + Ray cluster environment

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Additional Information Environment: Kubernetes cluster with Ray orchestration Model: DeepSeek-R1-Distill-Qwen-1.5B Expected: CPU-only inference should work Actual: Device type inference fails completely Impact: Blocks CPU-only inference in containerized environments ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: le ### Your current environment ### 🐛 Describe the bug Additional Information Environment: Kubernetes cluster with Ray orchestration Model: DeepSeek-R1-Distill-Qwen-1.5B Expected: CPU-only inference should work Actual:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nts ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ce distributed_parallel;hardware_porting;model_support cuda;kernel crash;import_error dtype Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: d_parallel;hardware_porting;model_support cuda;kernel crash;import_error dtype Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rence should work Actual: Device type inference fails completely Impact: Blocks CPU-only inference in containerized environments ### Before submitting a new issue... - [x] Make sure you already searched for relevant iss...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
