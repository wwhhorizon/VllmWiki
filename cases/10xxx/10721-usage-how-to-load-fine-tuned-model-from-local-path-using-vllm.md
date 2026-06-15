# vllm-project/vllm#10721: [Usage]: How to Load Fine-Tuned Model from Local Path Using vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#10721](https://github.com/vllm-project/vllm/issues/10721) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to Load Fine-Tuned Model from Local Path Using vllm?

### Issue 正文摘录

### Your current environment 1 ### How would you like to use vllm I’ve been able to load a model from a local directory with the following command: ```bash `vllm serve "/home/users/Llama-3.2-1B-Instruct"` ``` This works because I downloaded the model directly from Hugging Face. However, after fine-tuning the model and saving it using: ```python trainer.save_model("/home/users/train/result/11_27/1/checkpoint-7980") ``` I tried to serve the fine-tuned model using the following command: ```bash vllm serve "/home/users/train/result/11_27/1/checkpoint-7980" ``` But this fails with the error message: **huggingface_hub.errors.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/home/users/train/result/11_27/1/checkpoint-7980'** I tried renaming the checkpoint folder to Llama-3.2-1B-Instruct and running: ```bash vllm serve "/home/users/train/result/11_27/1/Llama-3.2-1B-Instruct" ``` But I still get the same error. It seems like the model’s saving format might be causing the issue. Is there something special I need to do when saving a fine-tuned model to load it locally using vllm? Or is the format of the saved model compatible with vllm, or do I need to r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How to Load Fine-Tuned Model from Local Path Using vllm? usage;stale ### Your current environment 1 ### How would you like to use vllm I’ve been able to load a model from a local directory with the following co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: model’s saving format might be causing the issue. Is there something special I need to do when saving a fine-tuned model to load it locally using vllm? Or is the format of the saved model compatible with vllm, or do I n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to Load Fine-Tuned Model from Local Path Using vllm? usage;stale ### Your current environment 1 ### How would you like to use vllm I’ve been able to load a model from a local directory with the following co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
