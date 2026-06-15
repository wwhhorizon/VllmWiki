# vllm-project/vllm#42239: [Bug]: Gemma4 MoE routing closure captures `per_expert_scale` Parameter, breaking `torch.func.functional_call` substitution

| 字段 | 值 |
| --- | --- |
| Issue | [#42239](https://github.com/vllm-project/vllm/issues/42239) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;moe;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4 MoE routing closure captures `per_expert_scale` Parameter, breaking `torch.func.functional_call` substitution

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Gemma4 MoE captures the registered `per_expert_scale` parameter in a Python closure in `vllm/model_executor/models/gemma4.py`. This prevents `torch.func.functional_call`-style parameter substitution from reaching the routing function, because the closure keeps the original `Parameter` object even when the module attribute is substituted. This is not specific to TorchAX or TPU execution. TorchAX is one downstream consumer that hits the issue, but the underlying behavior can be demonstrated with plain PyTorch `torch.func.functional_call`: module attribute lookup sees the substituted parameter, while a closure-captured reference keeps pointing at the original `Parameter`. The relevant code is in `Gemma4MoE.__init__`, around: https://github.com/vllm-project/vllm/blob/215e2f7990d9bb8788555a49036002e69ce14eaa/vllm/model_executor/models/gemma4.py#L323-L341 Current pattern: ```python self.per_expert_scale = nn.Parameter(torch.ones(config.num_experts)) per_expert_scale = self.per_expert_scale def routing_function(...): return gemma4_routing_function_torch( gating_output, topk, per_expert_scale ) ``` `per_expert_scale` is registered on the...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [Bug]: Gemma4 MoE routing closure captures `per_expert_scale` Parameter, breaking `torch.func.functional_call` substitution bug ### Your current environment ### 🐛 Describe the bug Gemma4 MoE captures the registered `per...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r` object even when the module attribute is substituted. This is not specific to TorchAX or TPU execution. TorchAX is one downstream consumer that hits the issue, but the underlying behavior can be demonstrated with pla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: l time: ```python def routing_function(...): if current_platform.is_cuda_alike() or current_platform.is_xpu(): return gemma4_fused_routing_kernel_triton( gating_output, topk, self.per_expert_scale ) return gemma4_routin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma4 MoE routing closure captures `per_expert_scale` Parameter, breaking `torch.func.functional_call` substitution bug ### Your current environment ### 🐛 Describe the bug Gemma4 MoE captures the registered `per...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Gemma4 MoE routing closure captures `per_expert_scale` Parameter, breaking `torch.func.functional_call` substitution bug ### Your current environment ### 🐛 Describe the bug Gemma4 MoE captures the registered `per...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
