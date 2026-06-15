# vllm-project/vllm#42684: [Bug]: native Triton top-k/top-p kernel assumes contiguous logits

| 字段 | 值 |
| --- | --- |
| Issue | [#42684](https://github.com/vllm-project/vllm/issues/42684) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: native Triton top-k/top-p kernel assumes contiguous logits

### Issue 正文摘录

### Your current environment vLLM Version: 0.20.1 PyTorch: 2.11.0+cu130 Triton: 3.6.0 CUDA available: True GPU: NVIDIA GH200 120GB Driver: 565.57.01 OS: SUSE Linux Enterprise Server 15 SP6 (aarch64) ### 🐛 Describe the bug `vllm/v1/sample/ops/topk_topp_triton.py::_topk_topp_kernel` computes row pointers as `LOGITS + row_id * VOCAB_SIZE`. That is correct only for contiguous logits. The wrapper `apply_top_k_top_p_triton` checks rank and dtype but **does not check contiguity**, so when the wrapper is handed a logits tensor with `stride(0) != vocab_size` (e.g. a sliced padded-vocab view), the kernel reads the wrong physical row. This is observable end-to-end via `processed_logprobs`: the kernel can mask a logical row to all `-inf`, `logits.log_softmax(dim=-1, dtype=torch.float32)` then emits NaN, and JSON serialization fails with: ``` ValueError: Out of range float values are not JSON compliant: nan ``` The FlashInfer path already defends against this. `vllm/v1/sample/ops/topk_topp_sampler.py::forward_cuda` calls `flashinfer_sample(logits.contiguous(), ...)`, with an inline comment noting fp32 inference + logits-processor slicing can produce non-contiguous logits. `forward_native` does...

## 现有链接修复摘要

#42739 [Bugfix] Fix native Triton top-k/top-p kernel assumes contiguous logi…

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: kernel assumes contiguous logits bug ### Your current environment vLLM Version: 0.20.1 PyTorch: 2.11.0+cu130 Triton: 3.6.0 CUDA available: True GPU: NVIDIA GH200 120GB Driver: 565.57.01 OS: SUSE Linux Enterprise Server...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug]: native Triton top-k/top-p kernel assumes contiguous logits bug ### Your current environment vLLM Version: 0.20.1 PyTorch: 2.11.0+cu130 Triton: 3.6.0 CUDA available: True GPU: NVIDIA GH200 120GB Driver: 565.57.01...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: native Triton top-k/top-p kernel assumes contiguous logits bug ### Your current environment vLLM Version: 0.20.1 PyTorch: 2.11.0+cu130 Triton: 3.6.0 CUDA available: True GPU: NVIDIA GH200 120GB Driver: 565.57.01...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: hat guard, and `processed_logprobs` forces the native path. ### Minimal reproducer ```python import torch from vllm.v1.sample.ops.topk_topp_triton import apply_top_k_top_p_triton assert torch.cuda.is_available() device...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ontiguous logits. The wrapper `apply_top_k_top_p_triton` checks rank and dtype but **does not check contiguity**, so when the wrapper is handed a logits tensor with `stride(0) != vocab_size` (e.g. a sliced padded-vocab...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42739](https://github.com/vllm-project/vllm/pull/42739) | closes_keyword | 0.95 | [Bugfix] Fix native Triton top-k/top-p kernel assumes contiguous logi… | Fixes [#42684](https://github.com/vllm-project/vllm/issues/42684). This PR fixes a correctness bug in the native Triton top-k/top-p path when `logits` is a non-contiguous `[bat |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
