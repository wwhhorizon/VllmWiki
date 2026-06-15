# vllm-project/vllm#32219: [RFC]: Add Helion integration in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#32219](https://github.com/vllm-project/vllm/issues/32219) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;fp8;kernel;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Add Helion integration in vLLM

### Issue 正文摘录

### Motivation. (with significant inputs from @zou3519, @ProExpertProg, @mgoin, @xiaohongchen1991) Helion is PyTorch's latest innovation in authoring custom kernels, featuring simple and familiar syntax, good developer experience, and superior performance. This RFC proposes a developer-friendly framework for integrating Helion kernels into vLLM, making custom ops in vLLM more efficient, enjoyable to write, and performant in production. The proposed integration is [prototyped here](https://github.com/vllm-project/vllm/pull/29051). It is still being actively developed for path finding, so there might be missing features, bugs, lint errors or even minor discrepancies between prototype implementation and what is described in this RFC. ## What is Helion? Helion is a Python-first GPU kernel compiler that makes high-performance CUDA kernel development as simple as writing PyTorch code. **If you know PyTorch, you already know most of Helion.** ### Key Advantages **Familiar Syntax**: Helion uses PyTorch-like syntax with automatic memory management: ```python # Pure Helion kernel - looks like PyTorch! def silu_mul_fp8(input: torch.Tensor, scale: torch.Tensor) -> torch.Tensor: d = input.shap...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: ement: ```python # Pure Helion kernel - looks like PyTorch! def silu_mul_fp8(input: torch.Tensor, scale: torch.Tensor) -> torch.Tensor: d = input.shape[-1] // 2 out = torch.empty(input.shape[:-1] + (d,), device=input.de...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: integrating Helion kernels into vLLM, making custom ops in vLLM more efficient, enjoyable to write, and performant in production. The proposed integration is [prototyped here](https://github.com/vllm-project/vllm/pull/2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Helion is a Python-first GPU kernel compiler that makes high-performance CUDA kernel development as simple as writing PyTorch code. **If you know PyTorch, you already know most of Helion.** ### Key Advantages **Familiar...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: u3519, @ProExpertProg, @mgoin, @xiaohongchen1991) Helion is PyTorch's latest innovation in authoring custom kernels, featuring simple and familiar syntax, good developer experience, and superior performance. This RFC pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: -tuned CUDA kernels - **Flexible deployment**: Easy to configure/compile/dispatch for different input shapes and platforms, to reach optimal performance in real-world deployment. **Developer Productivity**: - **Rapid de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
