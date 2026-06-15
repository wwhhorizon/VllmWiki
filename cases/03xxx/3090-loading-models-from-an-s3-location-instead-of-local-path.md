# vllm-project/vllm#3090: Loading models from an S3 location instead of local path

| 字段 | 值 |
| --- | --- |
| Issue | [#3090](https://github.com/vllm-project/vllm/issues/3090) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Loading models from an S3 location instead of local path

### Issue 正文摘录

### Discussed in https://github.com/vllm-project/vllm/discussions/3072 Originally posted by **petrosbaltzis** February 28, 2024 Hello, The VLLM library gives the ability to load the model and the tokenizer either from a local folder or directly from HuggingFace. ``` ["python", "-m", "vllm.entrypoints.openai.api_server", \ "--host=0.0.0.0", \ "--port=8080", \ "--model= ", \ "--tokenizer= ", ] ``` I wonder if this functionality can be extended to support s3 locations so that when we initialize the API server, we pass the proper S3 location. ``` ["python", "-m", "vllm.entrypoints.openai.api_server", \ "--host=0.0.0.0", \ "--port=8080", \ "--model= ", \ "--tokenizer= ", ] ``` Petros

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Loading models from an S3 location instead of local path stale ### Discussed in https://github.com/vllm-project/vllm/discussions/3072 Originally posted by **petrosbaltzis** February 28, 2024 Hello, The VLLM library gives
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Loading models from an S3 location instead of local path stale ### Discussed in https://github.com/vllm-project/vllm/discussions/3072 Originally posted by **petrosbaltzis** February 28, 2024 Hello, The VLLM library give...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
