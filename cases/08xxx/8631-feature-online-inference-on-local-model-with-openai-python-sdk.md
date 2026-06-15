# vllm-project/vllm#8631: [Feature]: Online Inference on local model with OpenAI Python SDK

| 字段 | 值 |
| --- | --- |
| Issue | [#8631](https://github.com/vllm-project/vllm/issues/8631) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Online Inference on local model with OpenAI Python SDK

### Issue 正文摘录

### 🚀 The feature, motivation and pitch OpenAI recently provided a new endpoint batch inference (https://platform.openai.com/docs/guides/batch/overview?lang=curl). It would be nice if it works using the batch format from OpenAI but with a local model. I created an usage Issue for that before (https://github.com/vllm-project/vllm/issues/8567) Something like that: ```python from openai import OpenAI client = OpenAI( api_key="EMPTY", base_url="http://localhost:8000/v1", ) batch_input_file = client.files.create( file=open("batchinput.jsonl", "rb"), purpose="batch" ) client.batches.create( input_file_id= batch_input_file.id, endpoint="/v1/chat/completions", completion_window="24h", metadata={ "description": "nightly eval job" } ) ``` At the moment there will be an error: `NotFoundError: Error code: 404 - {'detail': 'Not Found'}` Advantages for the implementation: - vllm can be run as a docker container and function only as endpoint - It is compatible with the OpenAI Python SDK, so easier to use for newbies also the model can be easily switched from the OpenAI server to local models - Consistent workflow, if you use the docker for Chat ### Alternatives Internal Implementation: There was...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: m-project/vllm/issues/8567) Something like that: ```python from openai import OpenAI client = OpenAI( api_key="EMPTY", base_url="http://localhost:8000/v1", ) batch_input_file = client.files.create( file=open("batchinput...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Online Inference on local model with OpenAI Python SDK feature request;stale ### 🚀 The feature, motivation and pitch OpenAI recently provided a new endpoint batch inference (https://platform.openai.com/docs/g...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: Online Inference on local model with OpenAI Python SDK feature request;stale ### 🚀 The feature, motivation and pitch OpenAI recently provided a new endpoint batch inference (https://platform.openai.com/docs/gu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: completion_window="24h", metadata={ "description": "nightly eval job" } ) ``` At the moment there will be an error: `NotFoundError: Error code: 404 - {'detail': 'Not Found'}` Advantages for the implementation: - vllm ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
