# vllm-project/vllm#2948: AWQ Quantization Memory Usage

| 字段 | 值 |
| --- | --- |
| Issue | [#2948](https://github.com/vllm-project/vllm/issues/2948) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AWQ Quantization Memory Usage

### Issue 正文摘录

Hello! First of all, great job with this inference engine! Thanks a lot for your work! Here's my issue: I have run vllm with both a mistral instruct model and it's AWQ quantized version. I've quantized the model myself with AutoAWQ. It seems that both of them use around the same amount of GPU memory, whereas I'd expect the AWQ quantized version to use far less memory. Here is the GPU memory with the mistral model: Here is the GPU memory with the AWQ quantized mistral model: I am mostly using default parameters when running `entrypoints/openai/api_server.py`, except for `--max-model-len 24000` and `--enforce-eager`. Initially I thought that vllm reserves GPU memory up to 90% due to `--gpu-memory-utilization`, but it seems that that is not the case, as the real utilization is not equal between the 2 models and it is also not 90% of the total GPU memory. Could you explain what and why is happening here? Thank you so much!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: have run vllm with both a mistral instruct model and it's AWQ quantized version. I've quantized the model myself with AutoAWQ. It seems that both of them use around the same amount of GPU memory, whereas I'd expect the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: AWQ Quantization Memory Usage stale Hello! First of all, great job with this inference engine! Thanks a lot for your work! Here's my issue: I have run vllm with both a mistral instruct model and it's AWQ quantized versi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: f with AutoAWQ. It seems that both of them use around the same amount of GPU memory, whereas I'd expect the AWQ quantized version to use far less memory. Here is the GPU memory with the mistral model: Here is the GPU me...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: our work! Here's my issue: I have run vllm with both a mistral instruct model and it's AWQ quantized version. I've quantized the model myself with AutoAWQ. It seems that both of them use around the same amount of GPU me...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: AWQ Quantization Memory Usage stale Hello! First of all, great job with this inference engine! Thanks a lot for your work! Here's my issue: I have run vllm with both a mistral instruct model and it's AWQ quantized versi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
