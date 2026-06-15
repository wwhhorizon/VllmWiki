# vllm-project/vllm#25621: [Feature]: Enable torch.compile custom pass by default

| 字段 | 值 |
| --- | --- |
| Issue | [#25621](https://github.com/vllm-project/vllm/issues/25621) |
| 状态 | closed |
| 标签 | feature request;torch.compile |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable torch.compile custom pass by default

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now we set all configs in PassConfig to False by default. According to Luka, this is a relic of the V1 upgrade, and the plan is to enable them by default for the 0.12.0/torch 2.9 release. This issue is created to track the progress of resolving this. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Enable torch.compile custom pass by default feature request;torch.compile ### 🚀 The feature, motivation and pitch Now we set all configs in PassConfig to False by default. According to Luka, this is a relic o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: feature, motivation and pitch Now we set all configs in PassConfig to False by default. According to Luka, this is a relic of the V1 upgrade, and the plan is to enable them by default for the 0.12.0/torch 2.9 release. T...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: st;torch.compile ### 🚀 The feature, motivation and pitch Now we set all configs in PassConfig to False by default. According to Luka, this is a relic of the V1 upgrade, and the plan is to enable them by default for the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Enable torch.compile custom pass by default feature request;torch.compile ### 🚀 The feature, motivation and pitch Now we set all configs in PassConfig to False by default. According to Luka, this is a relic o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
