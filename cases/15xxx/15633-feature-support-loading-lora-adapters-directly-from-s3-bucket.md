# vllm-project/vllm#15633: [Feature]: Support loading LoRA adapters directly from s3 bucket

| 字段 | 值 |
| --- | --- |
| Issue | [#15633](https://github.com/vllm-project/vllm/issues/15633) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support loading LoRA adapters directly from s3 bucket

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently vLLM supports dynamically loading and unloading LoRA adapters at runtime through dedicated API endpoints. The supported behaviour is described in the documentation: https://docs.vllm.ai/en/stable/features/lora.html#dynamically-serving-lora-adapters. For the base model you can load the weights in safetensors format using the run:ai model streamer: https://docs.vllm.ai/en/v0.7.1/models/extensions/runai_model_streamer.html If you try to load LoRAs (adapter_model.safetensors/adapter_config.json) from s3 you get a validation error shown below: ``` ERROR 03-27 15:27:33 [utils.py:229] Error downloading the HuggingFace model ERROR 03-27 15:27:33 [utils.py:229] Traceback (most recent call last): ERROR 03-27 15:27:33 [utils.py:229] File "/opt/venv/lib/python3.12/site-packages/vllm/lora/utils.py", line 223, in get_adapter_absolute_path ERROR 03-27 15:27:33 [utils.py:229] local_snapshot_path = huggingface_hub.snapshot_download( ERROR 03-27 15:27:33 [utils.py:229] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-27 15:27:33 [utils.py:229] File "/opt/venv/lib/python3.12/site-packages/huggingface_hub/utils/_validators.py", line 106, in _inner_fn ERROR...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: able/features/lora.html#dynamically-serving-lora-adapters. For the base model you can load the weights in safetensors format using the run:ai model streamer: https://docs.vllm.ai/en/v0.7.1/models/extensions/runai_model_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support loading LoRA adapters directly from s3 bucket feature request;stale ### 🚀 The feature, motivation and pitch Currently vLLM supports dynamically loading and unloading LoRA adapters at runtime through d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
