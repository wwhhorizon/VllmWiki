# vllm-project/vllm#12930: [Feature]: preallocate vram adjust

| 字段 | 值 |
| --- | --- |
| Issue | [#12930](https://github.com/vllm-project/vllm/issues/12930) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: preallocate vram adjust

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I've encountered the following situation. I have two 48GB graphics cards and a 32B model. When using the parameter "--quantization fp8", the VRAM occupancy can be less than 40GB (with "--tensor - parallel 2 --gpu-memory-utilization 0.4 ", the total VRAM is pre - allocated 63GB first and then drops back to about 40GB after loading). Calculating in this way, the model could fit on a single graphics card. However, vLLM pre - allocates at least 63GB of VRAM right from the start (the size of the 32B model in BF16 posiblly), so a single card won't be sufficient and a VRAM shortage error will occur. If the pre - allocation of VRAM can be adjusted, it would enable better utilization of VRAM parameters. For example, when using FP8 quantization, a single graphics card would be enough to run the model. The vLLM Docker image is v0.7.1. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ave two 48GB graphics cards and a 32B model. When using the parameter "--quantization fp8", the VRAM occupancy can be less than 40GB (with "--tensor - parallel 2 --gpu-memory-utilization 0.4 ", the total VRAM is pre - a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: size of the 32B model in BF16 posiblly), so a single card won't be sufficient and a VRAM shortage error will occur. If the pre - allocation of VRAM can be adjusted, it would enable better utilization of VRAM parameters....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: preallocate vram adjust feature request;stale ### 🚀 The feature, motivation and pitch I've encountered the following situation. I have two 48GB graphics cards and a 32B model. When using the parameter "--quan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ntered the following situation. I have two 48GB graphics cards and a 32B model. When using the parameter "--quantization fp8", the VRAM occupancy can be less than 40GB (with "--tensor - parallel 2 --gpu-memory-utilizati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
