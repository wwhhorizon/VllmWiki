# vllm-project/vllm#4733: VRAM USAGE WHEN LOADING THE MODEL

| 字段 | 值 |
| --- | --- |
| Issue | [#4733](https://github.com/vllm-project/vllm/issues/4733) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> VRAM USAGE WHEN LOADING THE MODEL

### Issue 正文摘录

### Anything you want to discuss about vllm. Hi guys, I have some question regarding. I have 256 GB VRAM of Tesla V100 32GB. I deploy model from TheBloke/Llama-2-70B-Chat-GPTQ. I set the dtype = float16. And then when i monitor the gpu usage, I can see that each of the layer take around 17GB per layer. My question is, it is supposed that when i load the model, it will take around 40GB total (model size) out of 256GB, but when I load it, the GPU usage is more than that. Why this is happened?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: V100 32GB. I deploy model from TheBloke/Llama-2-70B-Chat-GPTQ. I set the dtype = float16. And then when i monitor the gpu usage, I can see that each of the layer take around 17GB per layer. My question is, it is suppose...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: VRAM USAGE WHEN LOADING THE MODEL ### Anything you want to discuss about vllm. Hi guys, I have some question regarding. I have 256 GB VRAM of Tesla V100 32GB. I deploy model from TheBloke/Llama-2-70B-Chat-GPTQ. I set th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
