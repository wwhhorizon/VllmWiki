# vllm-project/vllm#18906: [Bug]: vllm0.9.0 cannot load eagle30-llama3.3-70b-inst model

| 字段 | 值 |
| --- | --- |
| Issue | [#18906](https://github.com/vllm-project/vllm/issues/18906) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm0.9.0 cannot load eagle30-llama3.3-70b-inst model

### Issue 正文摘录

### Your current environment vllm-0.9.0+cu126 torch-2.7.0+cu126 cuda 12.6 ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: del bug ### Your current environment vllm-0.9.0+cu126 torch-2.7.0+cu126 cuda 12.6 ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatb...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm0.9.0 cannot load eagle30-llama3.3-70b-inst model bug ### Your current environment vllm-0.9.0+cu126 torch-2.7.0+cu126 cuda 12.6 ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tly asked questions. correctness model_support;speculative_decoding cuda mismatch dtype;env_dependency;shape Your current environment
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . correctness model_support;speculative_decoding cuda mismatch dtype;env_dependency;shape Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: questions. correctness model_support;speculative_decoding cuda mismatch dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
