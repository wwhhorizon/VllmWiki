# vllm-project/vllm#38660: [Bug]: CUDA assert in triton attention for MolmoWeb models (Molmo2 architecture with different max_position_embeddings)

| 字段 | 值 |
| --- | --- |
| Issue | [#38660](https://github.com/vllm-project/vllm/issues/38660) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA assert in triton attention for MolmoWeb models (Molmo2 architecture with different max_position_embeddings)

### Issue 正文摘录

### Your current environment - vLLM version: 0.18.1 (Docker `vllm/vllm-openai:latest`) - GPU: NVIDIA RTX 5090 (24GB) - CUDA: 13.2 - PyTorch: 2.7 ### Model `allenai/MolmoWeb-8B` and `allenai/MolmoWeb-4B` — both use `Molmo2ForConditionalGeneration` architecture (`model_type: "molmo2"`), identical to `allenai/Molmo2-8B`. ### Bug description MolmoWeb models crash with a CUDA device-side assert in the triton attention kernel during inference. `allenai/Molmo2-8B` works fine with the same code. The crash occurs in `triton_attn.py` at `mm_prefix_range_tensor` property, specifically at: ```python torch.tensor(r, dtype=torch.int32, device=device).view(-1, 2) ``` This is in the multimodal bidirectional attention path (`is_mm_prefix_lm = True`), which is enabled for all `model_type: "molmo2"` models. ### Root cause analysis The **only config difference** between `allenai/MolmoWeb-8B` and `allenai/Molmo2-8B` is: - `max_position_embeddings`: **10240** (MolmoWeb) vs **36864** (Molmo2) Everything else — architecture, text config dimensions, vision config, processor code — is identical (`diff` of `processing_molmo2.py` shows zero functional differences). The lower `max_position_embeddings` likely...

## 现有链接修复摘要

#42161 Fix Molmo2 image token metadata | #42162 Fix Molmo2 image token metadata | #42163 Document MolmoWeb hf_overrides

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: different max_position_embeddings) ### Your current environment - vLLM version: 0.18.1 (Docker `vllm/vllm-openai:latest`) - GPU: NVIDIA RTX 5090 (24GB) - CUDA: 13.2 - PyTorch: 2.7 ### Model `allenai/MolmoWeb-8B` and `al...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: CUDA assert in triton attention for MolmoWeb models (Molmo2 architecture with different max_position_embeddings) ### Your current environment - vLLM version: 0.18.1 (Docker `vllm/vllm-openai:latest`) - GPU: NVIDI...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA assert in triton attention for MolmoWeb models (Molmo2 architecture with different max_position_embeddings) ### Your current environment - vLLM version: 0.18.1 (Docker `vllm/vllm-openai:latest`) - GPU: NVIDI...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ion_embeddings`: **10240** (MolmoWeb) vs **36864** (Molmo2) Everything else — architecture, text config dimensions, vision config, processor code — is identical (`diff` of `processing_molmo2.py` shows zero functional di...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: CUDA assert in triton attention for MolmoWeb models (Molmo2 architecture with different max_position_embeddings) ### Your current environment - vLLM version: 0.18.1 (Docker `vllm/vllm-openai:latest`) - GPU: NVIDI...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42161](https://github.com/vllm-project/vllm/pull/42161) | closes_keyword | 0.95 | Fix Molmo2 image token metadata | Fixes #38660. |
| [#42162](https://github.com/vllm-project/vllm/pull/42162) | closes_keyword | 0.95 | Fix Molmo2 image token metadata | Fixes #38660. |
| [#42163](https://github.com/vllm-project/vllm/pull/42163) | mentioned | 0.6 | Document MolmoWeb hf_overrides | idation evidence before marking this PR ready for review. Related to #38660 and stacked on #42162. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
