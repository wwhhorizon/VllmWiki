# vllm-project/vllm#6947: [Feature]: Add embeddings api for Llama 

| 字段 | 值 |
| --- | --- |
| Issue | [#6947](https://github.com/vllm-project/vllm/issues/6947) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add embeddings api for Llama 

### Issue 正文摘录

currently I load openai api server using the command python3 -m vllm.entrypoints.openai.api_server --model Llama3-8B-Instruct --dtype auto --host 0.0.0.0 --port 8051 --gpu-memory-utilization 0.8 --enforce-eager I want to try embedding using llama3 but. after loading i can see that embedding API is not loaded ![image](https://github.com/user-attachments/assets/17018d2d-90b4-4b67-bc0d-7d335806d0a2) I couldn't find any parm to enable embeddings. Help me to enable embeddings API

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Add embeddings api for Llama feature request;stale currently I load openai api server using the command python3 -m vllm.entrypoints.openai.api_server --model Llama3-8B-Instruct --dtype auto --host 0.0.0.0 --p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add embeddings api for Llama feature request;stale currently I load openai api server using the command python3 -m vllm.entrypoints.openai.api_server --model Llama3-8B-Instruct --dtype auto --host 0.0.0.0 --p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: thon3 -m vllm.entrypoints.openai.api_server --model Llama3-8B-Instruct --dtype auto --host 0.0.0.0 --port 8051 --gpu-memory-utilization 0.8 --enforce-eager I want to try embedding using llama3 but. after loading i can s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
