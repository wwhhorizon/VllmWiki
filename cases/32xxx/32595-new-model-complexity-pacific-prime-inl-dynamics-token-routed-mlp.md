# vllm-project/vllm#32595: [New Model]: Complexity (Pacific-Prime) - INL Dynamics + Token-Routed MLP

| 字段 | 值 |
| --- | --- |
| Issue | [#32595](https://github.com/vllm-project/vllm/issues/32595) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;gemm_linear;model_support;moe;sampling_logits |
| 子分类 |  |
| Operator 关键词 | activation;attention;cuda;kernel;moe |
| 症状 | nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [New Model]: Complexity (Pacific-Prime) - INL Dynamics + Token-Routed MLP

### Issue 正文摘录

### The model to consider. https://huggingface.co/Pacific-Prime/pacific-prime Implementation ready: https://github.com/Complexity-ML/complexity-vllm ### The closest model vllm already supports. LlamaForCausalLM (vllm/model_executor/models/llama.py) The Complexity model is LLaMA-based with the same core components: - RMSNorm - Grouped Query Attention (GQA) - RoPE positional embeddings - SwiGLU MLP activation Key differences from LLaMA: 1. INLDynamics layer after attention (velocity-tracked equilibrium control) 2. Token-Routed MLP instead of standard MLP (deterministic expert routing) 3. Mu-guided attention projections (mu_to_q, mu_to_k, mu_to_v) ### What's your difficulty of supporting the model you want? ## New Components Required ### 1. INLDynamics (new layer type) PID-like control with velocity tracking for numerical stability: ```python # Learnable parameters self.mu = Parameter(hidden_size) # equilibrium self.mu_proj = Linear(H, H) # contextual adjustment self.controller_in = Linear(2*H, 64) self.controller_out = Linear(64, 3*H) # alpha, beta, gate # Forward error = h - (mu + mu_proj(h)) v_next = alpha * v - beta * error h_next = h + dt * gate * v_next 2. TokenRoutedMLP (new M...

## 现有链接修复摘要

#32803 [Model] Add Pacific-Prime / Complexity model support

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: rium control) 2. Token-Routed MLP instead of standard MLP (deterministic expert routing) 3. Mu-guided attention projections (mu_to_q, mu_to_k, mu_to_v) ### What's your difficulty of supporting the model you want? ## New...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: racked equilibrium control) 2. Token-Routed MLP instead of standard MLP (deterministic expert routing) 3. Mu-guided attention projections (mu_to_q, mu_to_k, mu_to_v) ### What's your difficulty of supporting the model yo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Complexity (Pacific-Prime) - INL Dynamics + Token-Routed MLP ### The model to consider. https://huggingface.co/Pacific-Prime/pacific-prime Implementation ready: https://github.com/Complexity-ML/complexity-v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ntrol) 2. Token-Routed MLP instead of standard MLP (deterministic expert routing) 3. Mu-guided attention projections (mu_to_q, mu_to_k, mu_to_v) ### What's your difficulty of supporting the model you want? ## New Compon...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [New Model]: Complexity (Pacific-Prime) - INL Dynamics + Token-Routed MLP ### The model to consider. https://huggingface.co/Pacific-Prime/pacific-prime Implementation ready: https://github.com/Complexity-ML/complexity-v...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32803](https://github.com/vllm-project/vllm/pull/32803) | closes_keyword | 0.95 | [Model] Add Pacific-Prime / Complexity model support | Closes #32595 **Model**: https://huggingface.co/Pacific-Prime/pacific-prime **Paper**: https://zenodo.org/records/18293026 ### Key Innovations - **INL Dynamics**: PID-like contro |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
