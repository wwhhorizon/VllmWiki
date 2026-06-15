# vllm-project/vllm#6017: [New Model]: facebook/seamless-m4t-v2-large

| 字段 | 值 |
| --- | --- |
| Issue | [#6017](https://github.com/vllm-project/vllm/issues/6017) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: facebook/seamless-m4t-v2-large

### Issue 正文摘录

### The model to consider. https://huggingface.co/facebook/seamless-m4t-v2-large ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? The yet unsupported architecture `SeamlessM4Tv2Model`. * Their own inference code: https://github.com/facebookresearch/seamless_communication * HF code: https://github.com/facebookresearch/seamless_communication/tree/main/docs/m4t But the SeamlessM4Tv2Model does require encoders (https://github.com/huggingface/transformers/blob/e65502951593a76844e872fee9c56b805598538a/src/transformers/models/seamless_m4t_v2/modeling_seamless_m4t_v2.py#L4319) - Likely this is tackled with https://github.com/vllm-project/vllm/issues/187 ?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: facebook/seamless-m4t-v2-large new-model;stale ### The model to consider. https://huggingface.co/facebook/seamless-m4t-v2-large ### The closest model vllm already supports. _No response_ ### What's your dif...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 's your difficulty of supporting the model you want? The yet unsupported architecture `SeamlessM4Tv2Model`. * Their own inference code: https://github.com/facebookresearch/seamless_communication * HF code: https://githu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: facebook/seamless-m4t-v2-large new-model;stale ### The model to consider. https://huggingface.co/facebook/seamless-m4t-v2-large ### The closest model vllm already supports. _No response_ ### What's your dif...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
