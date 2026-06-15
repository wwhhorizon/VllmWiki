# vllm-project/vllm#14170: [Bug]: If I include the stop parameter, the output of reasoning_content gets truncated, and the output of content will display /think>

| 字段 | 值 |
| --- | --- |
| Issue | [#14170](https://github.com/vllm-project/vllm/issues/14170) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: If I include the stop parameter, the output of reasoning_content gets truncated, and the output of content will display /think>

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I deploy the `deepseek-ai/DeepSeek-R1-Distill-Llama-70B` model using vLLM, if I include the `stop` parameter, the output of `reasoning_content` gets truncated, and the output of `content` will display `/think>`. However, when I remove the `stop` parameter, everything works normally. You can find the whole result from here. [bb.txt](https://github.com/user-attachments/files/19062853/bb.txt) ``` curl --location --request POST 'http://localhost:8000/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data-raw '{ "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B", "messages": [ { "role": "user", "content": "given 3(x+5)=27, output the value of x" } ], "stream": true, "stop": ["✿RESULT✿", "✿RETURN✿"] }' ``` ``` ... data: {"id":"chatcmpl-0a1f3e2aefcb4a768522a97bb690cc40","object":"chat.completion.chunk","created":1741050706,"model":"deepseek-ai/DeepSeek-R1-Distill-Llama-70B","choices":[{"index":0,"delta":{"reasoning_content":" I fi"},"logprobs":null,"finish_reason":null}]} data: {"id":"chatcmpl-0a1f3e2aefcb4a768522a97bb690cc40","object":"chat.completion.chunk","created":1741050706,"model":"deepseek-ai/DeepSeek-R...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ntent gets truncated, and the output of content will display /think> bug;stale ### Your current environment ### 🐛 Describe the bug When I deploy the `deepseek-ai/DeepSeek-R1-Distill-Llama-70B` model using vLLM, if I inc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # 🐛 Describe the bug When I deploy the `deepseek-ai/DeepSeek-R1-Distill-Llama-70B` model using vLLM, if I include the `stop` parameter, the output of `reasoning_content` gets truncated, and the output of `content` will...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
