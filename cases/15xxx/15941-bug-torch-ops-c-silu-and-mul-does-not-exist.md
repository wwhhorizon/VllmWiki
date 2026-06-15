# vllm-project/vllm#15941: [Bug]: torch.ops._C.silu_and_mul  does not exist

| 字段 | 值 |
| --- | --- |
| Issue | [#15941](https://github.com/vllm-project/vllm/issues/15941) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.ops._C.silu_and_mul  does not exist

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/b40e4e5e-dbed-4973-a29d-3cc4f4c78f17) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n answer lots of frequently asked questions. development activation_norm;ci_build;hardware_porting;model_support cuda;operator build_error;crash env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 17) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: y asked questions. development activation_norm;ci_build;hardware_porting;model_support cuda;operator build_error;crash env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development activation_norm;ci_build;hardware_porting;model_support cuda;operator bui...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
