# vllm-project/vllm#3690: [New Model]: Jamba (MoE Mamba from AI21)

| 字段 | 值 |
| --- | --- |
| Issue | [#3690](https://github.com/vllm-project/vllm/issues/3690) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Jamba (MoE Mamba from AI21)

### Issue 正文摘录

### The model to consider. https://huggingface.co/ai21labs/Jamba-v0.1 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? Jamba is a new model and interesting hybrid architecture MoE Mamba model that look very promising. https://www.ai21.com/blog/announcing-jamba

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Jamba (MoE Mamba from AI21) new-model ### The model to consider. https://huggingface.co/ai21labs/Jamba-v0.1 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Mamba model that look very promising. https://www.ai21.com/blog/announcing-jamba
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: porting the model you want? Jamba is a new model and interesting hybrid architecture MoE Mamba model that look very promising. https://www.ai21.com/blog/announcing-jamba
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [New Model]: Jamba (MoE Mamba from AI21) new-model ### The model to consider. https://huggingface.co/ai21labs/Jamba-v0.1 ### The closest model vllm already supports. _No response_ ### What's your difficulty of supportin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
