# vllm-project/vllm#8923: [Bug]: Model multimodal config initialisation unhandled and irrelevant error when no architectures found

| 字段 | 值 |
| --- | --- |
| Issue | [#8923](https://github.com/vllm-project/vllm/issues/8923) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model multimodal config initialisation unhandled and irrelevant error when no architectures found

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When initialising multimodal model config, if no architectures are found, an unhandled error happens and a not helpful error is show. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Model multimodal config initialisation unhandled and irrelevant error when no architectures found bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When initialising multi
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;hardware_porting;model_support;multimodal_vlm cuda build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: multimodal config initialisation unhandled and irrelevant error when no architectures found bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When initialising multimodal model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting;model_support;multimodal_vlm cuda build_error e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
