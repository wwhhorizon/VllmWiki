# vllm-project/vllm#29640: [RFC]: Confusing name in FusedMoE

| 字段 | 值 |
| --- | --- |
| Issue | [#29640](https://github.com/vllm-project/vllm/issues/29640) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Confusing name in FusedMoE

### Issue 正文摘录

### **TL;DR** I'm writting this issue is to discuss a naming issue in FusedMoE, and wonder if it's worth to get changed. @mgoin @ProExpertProg ### Motivation. The current FusedMoE architecture uses confusing naming that suggests quantization is the primary operation, when in fact it's an optional optimization: https://github.com/vllm-project/vllm/blob/18523b87f67b12e9044d690dfe9da7cddc390627/vllm/model_executor/layers/fused_moe/layer.py#L1793-L1815 My stance on this: Misleading name: Even UnquantizedFusedMoEMethod uses a "quant_method" name, despite having no quantization Inverted responsibility: The method name suggests quantization is the main operation, but it actually performs the core MoE computation (expert selection, expert execution, etc.) Poor discoverability: New contributors reading the code would naturally assume quant_method.apply() is about quantization, not the core MoE operations ### Proposed Change. Based on my current understanding. We can just modify the naming of variable member `quant_method` and related functions in `vllm/model_executor/layers/fused_moe/layer.py`. For example, how about changing `_get_quant_method` to `_get_fusedmoe_method`, since `quant_meth...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [RFC]: Confusing name in FusedMoE RFC;stale ### **TL;DR** I'm writting this issue is to discuss a naming issue in FusedMoE, and wonder if it's worth to get changed. @mgoin @ProExpertProg ### Motivation. The current Fuse...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: . The current FusedMoE architecture uses confusing naming that suggests quantization is the primary operation, when in fact it's an optional optimization: https://github.com/vllm-project/vllm/blob/18523b87f67b12e9044d69...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t changed. @mgoin @ProExpertProg ### Motivation. The current FusedMoE architecture uses confusing naming that suggests quantization is the primary operation, when in fact it's an optional optimization: https://github.co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/18523b87f67b12e9044d690dfe9da7cddc390627/vllm/model_executor/layers/fused_moe/layer.py#L1793-L1815 My stance on this: Misleading name: Even UnquantizedFusedMoEMethod uses a "quant_method" name...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Confusing name in FusedMoE RFC;stale ### **TL;DR** I'm writting this issue is to discuss a naming issue in FusedMoE, and wonder if it's worth to get changed. @mgoin @ProExpertProg ### Motivation. The current Fuse...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
