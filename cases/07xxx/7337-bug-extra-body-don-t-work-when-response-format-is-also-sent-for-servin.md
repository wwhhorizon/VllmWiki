# vllm-project/vllm#7337: [Bug]: Extra body don't work when response_format is also sent for serving.

| 字段 | 值 |
| --- | --- |
| Issue | [#7337](https://github.com/vllm-project/vllm/issues/7337) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Extra body don't work when response_format is also sent for serving.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I start a server for `MiniCPM-V2.5` like this ```shell vllm serve openbmb/MiniCPM-Llama3-V-2_5 --dtype auto --api-key token-abc123 --gpu_memory_utilization 1 --trust-remote-code ``` And then I start a request as follows: ```python from openai import OpenAI openai_api_key = "token-abc123" # your api key set in launch server openai_api_base = "http://localhost:8000/v1" # http id client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) text_prompt = "Please describe this image." image_url = "https://air-example-data-2.s3.us-west-2.amazonaws.com/vllm_opensource_llava/stop_sign.jpg" chat_response = client.chat.completions.create( model="openbmb/MiniCPM-Llama3-V-2_5", messages=[{ "role": "user", "content": [ {"type": "text", "text": text_prompt}, { "type": "image_url", "image_url": { "url": image_url, }, }, ], }], # response_format={'type': 'json_object'}, extra_body={ "stop_token_ids": [128001, 128009] }, ) ``` There're extra `stop_token_ids` required for `MiniCPM-V2.5`. And if I use `response_format`, which is upon `extra_body`, the inference won't stop until to the max number of tokens. Otherwise, it works well. It seems...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: te-code ``` And then I start a request as follows: ```python from openai import OpenAI openai_api_key = "token-abc123" # your api key set in launch server openai_api_base = "http://localhost:8000/v1" # http id client =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Extra body don't work when response_format is also sent for serving. bug;stale ### Your current environment ### 🐛 Describe the bug I start a server for `MiniCPM-V2.5` like this ```shell vllm serve openbmb/MiniCPM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Extra body don't work when response_format is also sent for serving. bug;stale ### Your current environment ### 🐛 Describe the bug I start a server for `MiniCPM-V2.5` like this ```shell vllm serve openbmb/MiniCPM-Llama3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: niCPM-V2.5` like this ```shell vllm serve openbmb/MiniCPM-Llama3-V-2_5 --dtype auto --api-key token-abc123 --gpu_memory_utilization 1 --trust-remote-code ``` And then I start a request as follows: ```python from openai...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
