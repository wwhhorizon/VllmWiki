# vllm-project/vllm#2459: Potential speedup for Mixtral to avoid forward pass of MOE layer if expert is not selected

| 字段 | 值 |
| --- | --- |
| Issue | [#2459](https://github.com/vllm-project/vllm/issues/2459) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;moe;scheduler_memory |
| 子分类 | shape_align |
| Operator 关键词 | cuda;gemm;kernel;moe |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Potential speedup for Mixtral to avoid forward pass of MOE layer if expert is not selected

### Issue 正文摘录

In Mixtral, we are doing the following in MixtralMoE layer ``` for expert_idx in self.expert_indicies: expert_layer = self.experts[expert_idx] expert_mask = (selected_experts == expert_idx) expert_weights = (routing_weights * expert_mask).sum(dim=-1, keepdim=True) current_hidden_states = expert_layer(hidden_states).mul_( expert_weights) if final_hidden_states is None: final_hidden_states = current_hidden_states else: final_hidden_states.add_(current_hidden_states) ``` There might be some inefficiencies here because, even if the expert on a rank is not selected, it still undergoes a forward pass on hidden_states (though the output will be multiplied by 0 - expert_weights since the expert is not selected). Considering a 10% selection rate of an expert, it means 90% of expert_weights are 0 for that expert. It might be wise to use sparse dense matmul. In the most extreme case where the expert is not selected by all the tokens in an inference batch, we should simply bypass the expert and return a zero tensor of shape [batch * seq_len, hidden_dim]. I was trying to achieve that with: ``` if expert_weights.any(): current_hidden_states = expert_layer(hidden_states).mul_( expert_weights) ``...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: he following in MixtralMoE layer ``` for expert_idx in self.expert_indicies: expert_layer = self.experts[expert_idx] expert_mask = (selected_experts == expert_idx) expert_weights = (routing_weights * expert_mask).sum(di...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: Potential speedup for Mixtral to avoid forward pass of MOE layer if expert is not selected In Mixtral, we are doing the following in MixtralMoE layer ``` for expert_idx in self.expert_indicies: expert_layer = self.exper...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: py", line 88, in forward if torch.any(expert_weights): RuntimeError: CUDA error: operation not permitted when stream is capturing CUDA kernel errors might be asynchronously reported at some other API call, so the stackt...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: final_hidden_states = current_hidden_states else: final_hidden_states.add_(current_hidden_states) ``` There might be some inefficiencies here because, even if the expert on a rank is not selected, it still undergoes a f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rt_mask = (selected_experts == expert_idx) expert_weights = (routing_weights * expert_mask).sum(dim=-1, keepdim=True) current_hidden_states = expert_layer(hidden_states).mul_( expert_weig

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
