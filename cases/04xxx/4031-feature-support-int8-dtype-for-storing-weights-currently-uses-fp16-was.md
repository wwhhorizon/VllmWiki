# vllm-project/vllm#4031: [Feature]: Support Int8 dtype for storing weights - currently uses FP16 wasting 50% of VRAM

| 字段 | 值 |
| --- | --- |
| Issue | [#4031](https://github.com/vllm-project/vllm/issues/4031) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Int8 dtype for storing weights - currently uses FP16 wasting 50% of VRAM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Could you please add Int8 as a supported dtype? Currently when using Int8 models such as https://huggingface.co/Qwen/Qwen1.5-7B-Chat-GPTQ-Int8 with xformers instead of FlashAttention, the weights are stored as FP16 taking double the VRAM. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ould you please add Int8 as a supported dtype? Currently when using Int8 models such as https://huggingface.co/Qwen/Qwen1.5-7B-Chat-GPTQ-Int8 with xformers instead of FlashAttention, the weights are stored as FP16 takin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: //huggingface.co/Qwen/Qwen1.5-7B-Chat-GPTQ-Int8 with xformers instead of FlashAttention, the weights are stored as FP16 taking double the VRAM. ### Alternatives _No response_ ### Additional context _No response_
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Support Int8 dtype for storing weights - currently uses FP16 wasting 50% of VRAM feature request ### 🚀 The feature, motivation and pitch Could you please add Int8 as a supported dtype? Currently when using In...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pe for storing weights - currently uses FP16 wasting 50% of VRAM feature request ### 🚀 The feature, motivation and pitch Could you please add Int8 as a supported dtype? Currently when using Int8 models such as https://h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
