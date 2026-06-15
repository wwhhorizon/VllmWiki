# vllm-project/vllm#15896: [Feature]: Enable CUDA Graph without turn on torch.compile / Inductor for V1

| 字段 | 值 |
| --- | --- |
| Issue | [#15896](https://github.com/vllm-project/vllm/issues/15896) |
| 状态 | closed |
| 标签 | feature request;torch.compile |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Enable CUDA Graph without turn on torch.compile / Inductor for V1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch For simple models, we may not need fusion from torch.compile. And piecewise approach may be slow. So we would like to enable this feature. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#17345 Add ability to use CUDAGraphs with use_inductor=False

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature]: Enable CUDA Graph without turn on torch.compile / Inductor for V1 feature request;torch.compile ### 🚀 The feature, motivation and pitch For simple models, we may not need fusion from torch.compile. And piecew...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Enable CUDA Graph without turn on torch.compile / Inductor for V1 feature request;torch.compile ### 🚀 The feature, motivation and pitch For simple models, we may not need fusion from torch.compile. And piecew...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: env_dependency #17345 Add ability to use CUDAGraphs with use_inductor=False 🚀 The feature, motivation and pitch
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: equest;torch.compile ### 🚀 The feature, motivation and pitch For simple models, we may not need fusion from torch.compile. And piecewise approach may be slow. So we would like to enable this feature. ### Alternatives _N...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nable CUDA Graph without turn on torch.compile / Inductor for V1 feature request;torch.compile ### 🚀 The feature, motivation and pitch For simple models, we may not need fusion from torch.compile. And piecewise approach...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17345](https://github.com/vllm-project/vllm/pull/17345) | closes_keyword | 0.95 | Add ability to use CUDAGraphs with use_inductor=False | fix #15896, unless users actually want to turn off TorchDynamo too (keep reading for context) This PR adds the ability to specify `use_inductor=False` in a CompilationConfig. The |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
