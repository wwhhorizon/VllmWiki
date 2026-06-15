# vllm-project/vllm#4979: [Bug]: Unsloth model inference not working well

| 字段 | 值 |
| --- | --- |
| Issue | [#4979](https://github.com/vllm-project/vllm/issues/4979) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unsloth model inference not working well

### Issue 正文摘录

### Your current environment ```text vLLM v0.4.2 (cuda 12.2) ``` ### 🐛 Describe the bug I'm training a Qwen1.5 with unsloth, and it seems that the inference does not work as expected and gives this result, composed only by "!": `['!!!!!!!!!!!!!!!!!!....!!!!!!!!!!!!!!!!!!!!!!!]` Using the same network without vLLM, but with the transformers library, everything seems to work: `AutoModelForCausalLM.from_pretrained(path)` Further details of unsloth's config.json file: ``` { "_name_or_path": "llamafy_models/Qwen1.5-0.5B-llamafy", "architectures": [ "LlamaForCausalLM" ], ... } ``` Are unsloth models supported by vLLM v0.4.2? Thanks

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Unsloth model inference not working well bug;stale ### Your current environment ```text vLLM v0.4.2 (cuda 12.2) ``` ### 🐛 Describe the bug I'm training a Qwen1.5 with unsloth, and it seems that the inference does...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: orking well bug;stale ### Your current environment ```text vLLM v0.4.2 (cuda 12.2) ``` ### 🐛 Describe the bug I'm training a Qwen1.5 with unsloth, and it seems that the inference does not work as expected and gives this...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Unsloth model inference not working well bug;stale ### Your current environment ```text vLLM v0.4.2 (cuda 12.2) ``` ### 🐛 Describe the bug I'm training a Qwen1.5 with unsloth, and it seems that the inference does...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Unsloth model inference not working well bug;stale ### Your current environment ```text vLLM v0.4.2 (cuda 12.2) ``` ### 🐛 Describe the bug I'm training a Qwen1.5 with unsloth, and it seems that the inference does...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
