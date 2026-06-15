# vllm-project/vllm#804: 4 GPUs cluster (g5.12xlarge) is doing batch processing faster than 8 GPUs cluster (g5.48xlarge)

| 字段 | 值 |
| --- | --- |
| Issue | [#804](https://github.com/vllm-project/vllm/issues/804) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 4 GPUs cluster (g5.12xlarge) is doing batch processing faster than 8 GPUs cluster (g5.48xlarge)

### Issue 正文摘录

Hey, I am using vllm==0.1.3 with ray >= 2.5.1 on aws sagemaker, with cuda 11.8 and llama2-13b-chat-hf. When I am using the batch processing function (model.generate , with 3/6/15/30/45/60/105/120 texts as python list, all texts are the same one, only different number of them), the 4 gpus cluster (4 x a10g, ml.g5.12xlarge) is faster in all cases against the 8 gpus cluster (8 x a10g, ml.g5.48xlarge). I wonder maybe the tensor parallel is not working well with more than 4 gpus, or the cuda drivers not utilising them as it should be. The temp params I am using are: "temperature": 0.1, "top_p": 0.75, "top_k": 40, "max_tokens": 256, "frequency_penalty": 1.07, "use_beam_search": False, "stop": [" ",'[INST]', ' '] for example, for 105 texts, the 4gpus cluster doing it in 47secs, and the the 8gpus cluster doing it in 59.2 secs. Also, for 60 texts the 4gpus cluster doing it in 27secs, and the the 8gpus cluster doing it in 37.3 secs. I can provide another examples if needed. Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: using vllm==0.1.3 with ray >= 2.5.1 on aws sagemaker, with cuda 11.8 and llama2-13b-chat-hf. When I am using the batch processing function (model.generate , with 3/6/15/30/45/60/105/120 texts as python list, all texts a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ge) Hey, I am using vllm==0.1.3 with ray >= 2.5.1 on aws sagemaker, with cuda 11.8 and llama2-13b-chat-hf. When I am using the batch processing function (model.generate , with 3/6/15/30/45/60/105/120 texts as python lis...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ax_tokens": 256, "frequency_penalty": 1.07, "use_beam_search": False, "stop": [" ",'[INST]', ' '] for example, for 105 texts, the 4gpus cluster doing it in 47secs, and the the 8gpus cluster doing it in 59.2 secs. Also,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
