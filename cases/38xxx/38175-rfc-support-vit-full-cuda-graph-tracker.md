# vllm-project/vllm#38175: [RFC]: Support ViT Full CUDA Graph (Tracker)

| 字段 | 值 |
| --- | --- |
| Issue | [#38175](https://github.com/vllm-project/vllm/issues/38175) |
| 状态 | open |
| 标签 | help wanted;RFC;multi-modality |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;model_support;multimodal_vlm |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;kernel |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Support ViT Full CUDA Graph (Tracker)

### Issue 正文摘录

### Motivation. Multimodal large language models (e.g., Qwen3-VL, Qwen3.5, GLM-V, Kimi K2.5) rely on a Vision Transformer (ViT) encoder to process visual inputs before feeding them into the language model backbone. In production serving scenarios, the ViT forward pass involves launching a large number of small CUDA kernels — including patch embedding, layer normalization, multi-head self-attention, and MLP projections — each of which incurs non-trivial kernel launch overhead on the host side. Currently, vLLM supports CUDA graph capture for the decoder (LLM) portion of the model, which has proven effective at reducing kernel launch costs and improving throughput. However, the ViT encoder is still executed eagerly, meaning every forward pass re-launches all kernels from scratch. Extending full CUDA graph support to the ViT encoder would allow the entire encoder forward pass to be captured and replayed as a single graph, eliminating per-kernel launch overhead and enabling more consistent, low-latency inference for multimodal models. ### Proposed Change. **Model Integration:** - [x] https://github.com/vllm-project/vllm/pull/35963 @b-mu - [x] https://github.com/vllm-project/vllm/pull/3...

## 现有链接修复摘要

#41714 [MM][CG] Profile encoder CUDA graph pool memory | #41759 [MM][Perf][CG] Support ViT full CUDA graph for InternVL | #41908 [MM][CG] Enable encoder cuda graph for Step3VL | #41992 [MM][Perf][CG] Support ViT full CUDA graph for Kimi-VL | #41996 [MM][Perf][CG] Enable encoder CUDA Graph for MiniCPM-V | #42218 [MM][CU] Encoder CudaGraph for Step3VL | #42288 Adjust design around encoder_cudagraph_forward | #42785 [MM][CG] Enable encoder CUDA Graph for MiniCPM-V | #43591 [MM][CG] Gemma3 Encoder CUDA Graph | #44394 [MM][Perf] Add PaddleOCR-VL encoder CUDA graph support

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ull CUDA Graph (Tracker) help wanted;RFC;multi-modality ### Motivation. Multimodal large language models (e.g., Qwen3-VL, Qwen3.5, GLM-V, Kimi K2.5) rely on a Vision Transformer (ViT) encoder to process visual inputs be...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: which has proven effective at reducing kernel launch costs and improving throughput. However, the ViT encoder is still executed eagerly, meaning every forward pass re-launches all kernels from scratch. Extending full CU...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Support ViT Full CUDA Graph (Tracker) help wanted;RFC;multi-modality ### Motivation. Multimodal large language models (e.g., Qwen3-VL, Qwen3.5, GLM-V, Kimi K2.5) rely on a Vision Transformer (ViT) encoder to proc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: he decoder (LLM) portion of the model, which has proven effective at reducing kernel launch costs and improving throughput. However, the ViT encoder is still executed eagerly, meaning every forward pass re-launches all...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 42785 [MM][CG] Enable encoder CUDA Graph for MiniCPM-V | #43591 [MM][CG] Gemma3 Encoder CUDA Graph | #44394 [MM][Perf] Add PaddleOCR-VL encoder CUDA graph support Motivation.

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41714](https://github.com/vllm-project/vllm/pull/41714) | mentioned | 0.6 | [MM][CG] Profile encoder CUDA graph pool memory | ep3-VL / StepVL in this PR. ## Duplicate / Overlap Check - Checked `#38175`. Step3-VL is not covered by an open or merged CUDA Graph PR. - Searched open PRs for Step3-VL / Step3 /… |
| [#41759](https://github.com/vllm-project/vllm/pull/41759) | mentioned | 0.6 | [MM][Perf][CG] Support ViT full CUDA graph for InternVL | ernVL3, InternVL2.5, InternVL2), following #38061 (Qwen3-VL). Part of #38175. InternVL's `InternVisionModel` uses standard ViT attention with no rotary embeddings or variable-leng… |
| [#41908](https://github.com/vllm-project/vllm/pull/41908) | mentioned | 0.6 | [MM][CG] Enable encoder cuda graph for Step3VL | [CG] Enable encoder cuda graph for Step3VL ## Purpose Sub issue from #38175 ## Todo List - [x] cuda graph implementation - [x] docs ## Test Plan Engin serve command ``` vll |
| [#41992](https://github.com/vllm-project/vllm/pull/41992) | mentioned | 0.6 | [MM][Perf][CG] Support ViT full CUDA graph for Kimi-VL | e pattern established in #38061 (Qwen3-VL). Part of the tracker issue #38175.</p> <p>Kimi-VL's <code>MoonVitPretrainedModel</code> contains <code>.tolist()</code> calls in its for… |
| [#41996](https://github.com/vllm-project/vllm/pull/41996) | mentioned | 0.6 | [MM][Perf][CG] Enable encoder CUDA Graph for MiniCPM-V | er CUDA Graph support for MiniCPM-V 2.5, 2.6, 4.0 as part of tracker #38175. This implementation follows the existing workflow introduced in #38061. The captured graph covers both… |
| [#42218](https://github.com/vllm-project/vllm/pull/42218) | mentioned | 0.6 | [MM][CU] Encoder CudaGraph for Step3VL | [MM][CU] Encoder CudaGraph for Step3VL ## Purpose Sub issue from #38175 ## Todo List - [x] cuda graph implementation - [x] docs ## Test Plan Engin serve command ``` vll |
| [#42288](https://github.com/vllm-project/vllm/pull/42288) | mentioned | 0.6 | Adjust design around encoder_cudagraph_forward | re-inputs structure at the same time. This PR is highly related to #38175. It try to simplify the design of `encoder_cudagraph_forward` so the it's more understandable and maintai… |
| [#42785](https://github.com/vllm-project/vllm/pull/42785) | mentioned | 0.6 | [MM][CG] Enable encoder CUDA Graph for MiniCPM-V | er CUDA Graph support for MiniCPM-V 2.5, 2.6, 4.0 as part of tracker #38175. This implementation follows the existing workflow introduced in #38061. The captured graph covers both… |
| [#43591](https://github.com/vllm-project/vllm/pull/43591) | mentioned | 0.6 | [MM][CG] Gemma3 Encoder CUDA Graph | [MM][CG] Gemma3 Encoder CUDA Graph Partial impl of #38175 ## Progress - [x] CUDA graph implementation - [x] docs ## Test Plan Engine serve command: ``` v |
| [#44394](https://github.com/vllm-project/vllm/pull/44394) | closes_keyword | 0.95 | [MM][Perf] Add PaddleOCR-VL encoder CUDA graph support | Closes / contributes to #38175 (umbrella: encoder CUDA graph support for VLMs). **Duplicate-work check** (per AGENTS.md — no open PR found): ```bash gh pr list --repo vllm-pro |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
