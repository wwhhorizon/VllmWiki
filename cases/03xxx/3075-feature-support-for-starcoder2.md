# vllm-project/vllm#3075: Feature support for Starcoder2

| 字段 | 值 |
| --- | --- |
| Issue | [#3075](https://github.com/vllm-project/vllm/issues/3075) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feature support for Starcoder2

### Issue 正文摘录

Could any expert support a new architecture (starcoder2)? Might someone already do this work for vLLM.. isn't it? If not, I will try to do it for myself. https://huggingface.co/docs/transformers/main/en/model_doc/starcoder2

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Feature support for Starcoder2 new-model Could any expert support a new architecture (starcoder2)? Might someone already do this work for vLLM.. isn't it? If not, I will try to do it for myself. https://huggingface.co/d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Feature support for Starcoder2 new-model Could any expert support a new architecture (starcoder2)? Might someone already do this work for vLLM.. isn't it? If not, I will try to do it for myself. https://huggingface.co/d...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Feature support for Starcoder2 new-model Could any expert support a new architecture (starcoder2)? Might someone already do this work for vLLM.. isn't it? If not, I will try to do it for myself. https://huggingface.co/d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
