# vllm-project/vllm#20765: [New Model]: Add support for Jina Embeddings V4 with multimodal pooling

| 字段 | 值 |
| --- | --- |
| Issue | [#20765](https://github.com/vllm-project/vllm/issues/20765) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Add support for Jina Embeddings V4 with multimodal pooling

### Issue 正文摘录

### The model to consider. https://huggingface.co/jinaai/jina-embeddings-v4-vllm-retrieval - 3.75B parameters, based on Qwen2.5-VL - Multimodal embeddings with custom vision token pooling - CC-BY-NC-4.0 license ### The closest model vllm already supports. `qwen2_vl.py` - Same base architecture but different purpose (embeddings vs generation) ### What's your difficulty of supporting the model you want? ### Core Challenge: Dynamic Token-Type-Aware Pooling ```python # Required logic VISION_START_TOKEN_ID = 151652 VISION_END_TOKEN_ID = 151653 if has_vision_tokens: # Extract ONLY vision tokens pooled = hidden_states[vision_start:vision_end].mean() else: # Use all tokens for text pooled = hidden_states.mean() pooled = F.normalize(pooled, dim=-1) ``` ### Current Limitation - vLLM Pooler only supports fixed strategies (LAST, ALL, MEAN) - No model-specific pooling handlers - Token IDs not accessible in pooling layer ### Proposed Solution Phase 1: Minimal conditional logic in Pooler Phase 2: Extensible pooling registry system

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Add support for Jina Embeddings V4 with multimodal pooling ### The model to consider. https://huggingface.co/jinaai/jina-embeddings-v4-vllm-retrieval - 3.75B parameters, based on Qwen2.5-VL - Multimodal emb
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Pooler only supports fixed strategies (LAST, ALL, MEAN) - No model-specific pooling handlers - Token IDs not accessible in pooling layer ### Proposed Solution Phase 1: Minimal conditional logic in Pooler Phase 2: Extens...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ## The closest model vllm already supports. `qwen2_vl.py` - Same base architecture but different purpose (embeddings vs generation) ### What's your difficulty of supporting the model you want? ### Core Challenge: Dynami...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: n tokens pooled = hidden_states[vision_start:vision_end].mean() else: # Use all tokens for text pooled = hidden_states.mean() pooled = F.normalize(pooled, dim=-1) ``` ### Current Limitation - vLLM Pooler only supports f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: to consider. https://huggingface.co/jinaai/jina-embeddings-v4-vllm-retrieval - 3.75B parameters, based on Qwen2.5-VL - Multimodal embeddings with custom vision token pooling - CC-BY-NC-4.0 license ### The closest model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
