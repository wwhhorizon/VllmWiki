# vllm-project/vllm#43021: [Feature]: Fuse QK Norm + mRoPE + KV cache write + FP8 quant

| 字段 | 值 |
| --- | --- |
| Issue | [#43021](https://github.com/vllm-project/vllm/issues/43021) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;quantization |
| 子分类 |  |
| Operator 关键词 | activation;cache;cuda;fp8;kernel;operator;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Fuse QK Norm + mRoPE + KV cache write + FP8 quant

### Issue 正文摘录

#### Purpose For the QK-RMSNorm + mRoPE models (such as Qwen3-VL), the operations for Q/K RMSNorm, mRoPE, and the KV cache write with FP8 quantization currently run as separate kernels. This results in intermediate global memory round-trips and multiple kernel launches. This PR introduces a kernel fusion that combines these operations into a single fused CUDA kernel. This new kernel will handle Q/K RMSNorm, mRoPE, KV cache writing, and per-tensor FP8 quantization, all in a single op. As part of https://github.com/vllm-project/vllm/issues/36066 #### Additional context _No response_ #### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#43056 [Perf][Kernel] Fused QK-RMSNorm + mRoPE CUDA kernel for Qwen3-VL

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Fuse QK Norm + mRoPE + KV cache write + FP8 quant feature request #### Purpose For the QK-RMSNorm + mRoPE models (such as Qwen3-VL), the operations for Q/K RMSNorm, mRoPE, and the KV cache write with FP8 quan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: duces a kernel fusion that combines these operations into a single fused CUDA kernel. This new kernel will handle Q/K RMSNorm, mRoPE, KV cache writing, and per-tensor FP8 quantization, all in a single op. As part of htt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ite + FP8 quant feature request #### Purpose For the QK-RMSNorm + mRoPE models (such as Qwen3-VL), the operations for Q/K RMSNorm, mRoPE, and the KV cache write with FP8 quantization currently run as separate kernels. T...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Fuse QK Norm + mRoPE + KV cache write + FP8 quant feature request #### Purpose For the QK-RMSNorm + mRoPE models (such as Qwen3-VL), the operations for Q/K RMSNorm, mRoPE, and the KV cache write with FP8 quan...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Fuse QK Norm + mRoPE + KV cache write + FP8 quant feature request #### Purpose For the QK-RMSNorm + mRoPE models (such as Qwen3-VL), the operations for Q/K RMSNorm, mRoPE, and the KV cache write with FP8 quan...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43056](https://github.com/vllm-project/vllm/pull/43056) | closes_keyword | 0.95 | [Perf][Kernel] Fused QK-RMSNorm + mRoPE CUDA kernel for Qwen3-VL | Fixes / part of #43021. Contributes to the broader fusion work tracker #36066. For Qwen3-VL, the current attention forward pass dispatches three separate CUDA kernel launches: q_n |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
