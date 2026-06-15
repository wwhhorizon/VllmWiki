# vllm-project/vllm#2748: 4 times memory usage comparing to text-generation-webui

| 字段 | 值 |
| --- | --- |
| Issue | [#2748](https://github.com/vllm-project/vllm/issues/2748) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 4 times memory usage comparing to text-generation-webui

### Issue 正文摘录

I am using **TheBloke_deepseek-coder-6.7B-instruct-GPTQ** as our model, which is a GPTQ quantized as the name suggests. When I run it in text-generation-webui the memory usage is around **4894MB** while when I use the following command to run it using VLLM the memory usage is **17164MiB** which is almost 4 times as large. `python -m vllm.entrypoints.openai.api_server --model ../text-generation-webui/models/TheBloke_deepseek-coder-6.7B-instruct-GPTQ --dtype float16 --max-model-len 16000 --gpu-memory-utilization .7 --quantization gpt` Am I missing something here, or there is a memory leaking issue?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Bloke_deepseek-coder-6.7B-instruct-GPTQ** as our model, which is a GPTQ quantized as the name suggests. When I run it in text-generation-webui the memory usage is around **4894MB** while when I use the following command...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -webui I am using **TheBloke_deepseek-coder-6.7B-instruct-GPTQ** as our model, which is a GPTQ quantized as the name suggests. When I run it in text-generation-webui the memory usage is around **4894MB** while when I us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
