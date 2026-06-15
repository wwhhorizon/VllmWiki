# vllm-project/vllm#4033: [Feature]: bitsandbytes support

| 字段 | 值 |
| --- | --- |
| Issue | [#4033](https://github.com/vllm-project/vllm/issues/4033) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: bitsandbytes support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Bitsandbytes 4bit quantization support. I know many want that, and also it is discuused before and marked as unplaned, but after I looked how TGI implemented that https://github.com/huggingface/text-generation-inference/blob/main/server/text_generation_server/utils/layers.py#L285 And TGI is based on VLLM ofc. ### Alternatives I know that GPTQ is better quan. compared to b&b 4b, but B&B is great for QLORA merged peft models, while it is almost impossible to gptq/awq quan. a b&b 4bit model (and I am not even talking about nf4 vs fp4 perpelxity case) as they are not offically supporting that (even though others sometimes successfully quantize from merged b&b qlora model to gptq or awq, but I don't for example) ### Additional context As I mentioned above, https://github.com/huggingface/text-generation-inference/blob/main/server/text_generation_server/utils/layers.py#L285 It looks very simple implementation of the Linear4bit class for b&b, I could add a pr myself to vllm, I just wondered why it is not added, maybe something I miss?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ature request ### 🚀 The feature, motivation and pitch Bitsandbytes 4bit quantization support. I know many want that, and also it is discuused before and marked as unplaned, but after I looked how TGI implemented that ht...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: unplaned, but after I looked how TGI implemented that https://github.com/huggingface/text-generation-inference/blob/main/server/text_generation_server/utils/layers.py#L285 And TGI is based on VLLM ofc. ### Alternatives...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: bitsandbytes support feature request ### 🚀 The feature, motivation and pitch Bitsandbytes 4bit quantization support. I know many want that, and also it is discuused before and marked as unplaned, but after I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
