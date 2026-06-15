# vllm-project/vllm#6829: llama 3 8b model with A10 GPU, OOM with VLLM, but holds good on HF transformer pipline

| 字段 | 值 |
| --- | --- |
| Issue | [#6829](https://github.com/vllm-project/vllm/issues/6829) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> llama 3 8b model with A10 GPU, OOM with VLLM, but holds good on HF transformer pipline

### Issue 正文摘录

Hi, GPU : A10 24 GB Model size with safe tensors : 26 GB all together With HF pipeline, it was possible to load llama3 8b and then convert it too fp16 and run inference but with VLLM, when I try to load the model itself, it goes OOM, can this be understood that vllm requires a more memory at loading pace and not possible to handle this, only after applying optimizations w.r.t model weights (quantization) will I be able to infer llama 3 8b? blogs like this are kind of misleading with it https://neuralmagic.com/blog/deploy-llama-3-8b-with-vllm/ With int4 quantized models you can use parameter `--gpu-memory-utilization` that take up less GPU memory, for Llama3-8B, this parameter can be set to a minimum of 0.6(~12GB) with 4-bit quantization, but not with the original fp16 model(~19GB)! _Originally posted by @yangxianpku in https://github.com/vllm-project/vllm/issues/2948#issuecomment-2122090059_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: llama 3 8b model with A10 GPU, OOM with VLLM, but holds good on HF transformer pipline stale Hi, GPU : A10 24 GB Model size with safe tensors : 26 GB all together With HF pipeline, it was possible to load llama3 8b and
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e to handle this, only after applying optimizations w.r.t model weights (quantization) will I be able to infer llama 3 8b? blogs like this are kind of misleading with it https://neuralmagic.com/blog/deploy-llama-3-8b-wi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: llama 3 8b model with A10 GPU, OOM with VLLM, but holds good on HF transformer pipline stale Hi, GPU : A10 24 GB Model size with safe tensors : 26 GB all together With HF pipeline, it was possible to load llama3 8b and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: el with A10 GPU, OOM with VLLM, but holds good on HF transformer pipline stale Hi, GPU : A10 24 GB Model size with safe tensors : 26 GB all together With HF pipeline, it was possible to load llama3 8b and then convert i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
