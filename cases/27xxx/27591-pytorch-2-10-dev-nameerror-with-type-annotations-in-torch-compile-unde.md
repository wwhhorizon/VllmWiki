# vllm-project/vllm#27591: PyTorch 2.10.dev: NameError with type annotations in torch.compile under Pipeline Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#27591](https://github.com/vllm-project/vllm/issues/27591) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> PyTorch 2.10.dev: NameError with type annotations in torch.compile under Pipeline Parallelism

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug error log: https://paste.ubuntu.com/p/9CpFqxhChB/ NameError: name 'IntermediateTensors' is not defined. Did you mean: 'intermediate_tensors'? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: PyTorch 2.10.dev: NameError with type annotations in torch.compile under Pipeline Parallelism bug;torch.compile ### Your current environment ### 🐛 Describe the bug error log: https://paste.ubuntu.com/p/9CpFqxhChB/ NameE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: NameError with type annotations in torch.compile under Pipeline Parallelism bug;torch.compile ### Your current environment ### 🐛 Describe the bug error log: https://paste.ubuntu.com/p/9CpFqxhChB/ NameError: name 'Interm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
