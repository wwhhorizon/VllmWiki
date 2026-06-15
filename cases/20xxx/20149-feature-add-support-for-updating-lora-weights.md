# vllm-project/vllm#20149: [Feature]: Add Support for Updating Lora Weights

| 字段 | 值 |
| --- | --- |
| Issue | [#20149](https://github.com/vllm-project/vllm/issues/20149) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Support for Updating Lora Weights

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are using TRL to train an updated version of one of our models which has a modality specific LoRA adapter (i.e., same as granite speech, phi4mm). TRL does have support for integrating into vLLM, but the way it handles adapters doesn't work effectively for this sort of model, because it assumes the lora weights can be merged (e.g., [here](https://github.com/huggingface/trl/blob/79ec242aefedc108de9edbea62be6d95070fde03/trl/trainer/grpo_trainer.py#L924)). As far as I know, the way we would currently 'update' the adapter is to save it out and then reload it, e.g., using the [worker lora manager](https://github.com/vllm-project/vllm/blob/main/vllm/lora/worker_manager.py#L86). It would be nice to have a supported way of updating the LoRA tensors being trained without exporting them though. If this is possible already, that would be great! Otherwise happy to take a pass at contributing it. @jeejeelee @avishaiElmakies ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docum...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: The feature, motivation and pitch We are using TRL to train an updated version of one of our models which has a modality specific LoRA adapter (i.e., same as granite speech, phi4mm). TRL does have support for integratin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on and pitch We are using TRL to train an updated version of one of our models which has a modality specific LoRA adapter (i.e., same as granite speech, phi4mm). TRL does have support for integrating into vLLM, but the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add Support for Updating Lora Weights feature request;stale ### 🚀 The feature, motivation and pitch We are using TRL to train an updated version of one of our models which has a modality specific LoRA adapter...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
