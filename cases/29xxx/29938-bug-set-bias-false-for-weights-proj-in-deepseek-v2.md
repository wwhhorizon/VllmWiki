# vllm-project/vllm#29938: [Bug]: set bias=False for weights_proj in deepseek_v2

| 字段 | 值 |
| --- | --- |
| Issue | [#29938](https://github.com/vllm-project/vllm/issues/29938) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: set bias=False for weights_proj in deepseek_v2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In the DeepSeekV2 [implementation](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/deepseek_v2.py#L841), the bias parameter of "weights_proj" lacks explicit initialization to False. This omission creates hardware-dependent behavior: while CUDA's cudaMalloc typically returns zero-initialized memory, other device backends may leave allocated memory uninitialized, potentially introducing calculation inconsistencies when the model executes on non-CUDA platforms. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ls/deepseek_v2.py#L841), the bias parameter of "weights_proj" lacks explicit initialization to False. This omission creates hardware-dependent behavior: while CUDA's cudaMalloc typically returns zero-initialized memory,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ation to False. This omission creates hardware-dependent behavior: while CUDA's cudaMalloc typically returns zero-initialized memory, other device backends may leave allocated memory uninitialized, potentially introduci...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: UDA's cudaMalloc typically returns zero-initialized memory, other device backends may leave allocated memory uninitialized, potentially introducing calculation inconsistencies when the model executes on non-CUDA platfor...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: set bias=False for weights_proj in deepseek_v2 bug;stale ### Your current environment ### 🐛 Describe the bug In the DeepSeekV2 [implementation](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: kV2 [implementation](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/deepseek_v2.py#L841), the bias parameter of "weights_proj" lacks explicit initialization to False. This omission creates har...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
