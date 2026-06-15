# vllm-project/vllm#19133: [Usage]: Why is the CPU usage fully utilized but the graphics card power is always low when I use vllm to deploy the model in a multi-card environment?

| 字段 | 值 |
| --- | --- |
| Issue | [#19133](https://github.com/vllm-project/vllm/issues/19133) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Why is the CPU usage fully utilized but the graphics card power is always low when I use vllm to deploy the model in a multi-card environment?

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/d81f1446-21ca-4009-be82-f8c25e02d8c2) As shown in the picture, I used two 4090 GPUs to build a Qwen2.5-VL-7B multimodal large model in the vllm framework, but I found that the CPU usage can reach 100% when in use, but the graphics card power is always very low. At present, I find that the image analysis speed is very slow. In this case, I consider whether there is room for optimization? For example, if the graphics card power can also run slowly, can the image analysis speed be made faster? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 4009-be82-f8c25e02d8c2) As shown in the picture, I used two 4090 GPUs to build a Qwen2.5-VL-7B multimodal large model in the vllm framework, but I found that the CPU usage can reach 100% when in use, but the graphics ca...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: but the graphics card power is always low when I use vllm to deploy the model in a multi-card environment? usage;stale ### Your current environment ![Image](https://github.com/user-attachments/assets/d81f1446-21ca-4009-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: analysis speed is very slow. In this case, I consider whether there is room for optimization? For example, if the graphics card power can also run slowly, can the image analysis speed be made faster? ### How would you l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: w when I use vllm to deploy the model in a multi-card environment? usage;stale ### Your current environment ![Image](https://github.com/user-attachments/assets/d81f1446-21ca-4009-be82-f8c25e02d8c2) As shown in the pictu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
