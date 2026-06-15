# vllm-project/vllm#6123: [Feature]: multi-lora support older nvidia gpus.

| 字段 | 值 |
| --- | --- |
| Issue | [#6123](https://github.com/vllm-project/vllm/issues/6123) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: multi-lora support older nvidia gpus.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently vLLM only supports LoRA adapters on nvidia gpus with compute capability >= 8.0. This request is to support >= 7.5. The limitation here is that vLLM relies on https://github.com/punica-ai/punica for efficient LoRA and the upstream doesn't support older gpus. Personally I've mainly run into this problem on Kaggle which requires you to run on T4s or older. Others seem to have run into this problem in other environments. Collab: https://github.com/vllm-project/vllm/issues/5199, other V100s https://github.com/vllm-project/vllm/issues/3826 ### Alternatives In some but not all cases this can be mitigated by using a newer gpu or applying the lora to the base model and model swapping. ### Additional context I'm willing to contribute this. I've prototyped this and verified that it's possible to do this efficiently by changing the step of vllm's wheel build which builds the vendored punica kernel.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: here is that vLLM relies on https://github.com/punica-ai/punica for efficient LoRA and the upstream doesn't support older gpus. Personally I've mainly run into this problem on Kaggle which requires you to run on T4s or...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: multi-lora support older nvidia gpus. feature request;unstale ### 🚀 The feature, motivation and pitch Currently vLLM only supports LoRA adapters on nvidia gpus with compute capability >= 8.0. This request is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Currently vLLM only supports LoRA adapters on nvidia gpus with compute capability >= 8.0. This request is to support >= 7.5. The limitation here is that vLLM relies on https://github.com/punica-ai/punica for efficient L...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s can be mitigated by using a newer gpu or applying the lora to the base model and model swapping. ### Additional context I'm willing to contribute this. I've prototyped this and verified that it's possible to do this e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
