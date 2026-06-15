# vllm-project/vllm#15805: [Bug]: TypeError: Unknown image model type: qwen2

| 字段 | 值 |
| --- | --- |
| Issue | [#15805](https://github.com/vllm-project/vllm/issues/15805) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: Unknown image model type: qwen2

### Issue 正文摘录

### Your current environment Version： vllm 0.8.1+cu121 transformers 4.48.2 python 3.10.6 System： ubuntu20.04 ### 🐛 Describe the bug 1、Deploy the OpenAI interface using vLLM, with the model being DeepSeek-R1-Distill-Qwen-32B, using the following command: python -m vllm.entrypoints.openai.api_server --model /home/DeepSeek-R1-Distill-Qwen-32B --served-model-name DeepSeekR1-32B --gpu-memory-utilization 0.9 2、Use the Chatbox client for interaction. 3、When uploading an image, the Chatbox client reports the following error API Error: Status Code 400, {"object":"error","message":"Unknown image model type: qwen2","type":"BadRequestError","param":null,"code":400} 4、The backend reports the following error: [serving_chat.py:204] TypeError: Unknown image model type: qwen2 5、I have seen similar issues resolved in previous discussions, but due to differences in vLLM versions, I cannot directly apply those solutions. How can I resolve this issue in vLLM version 0.8.1+cu121 so that the OpenAI interface deployed with vLLM can support local image uploads using the [image] format? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot livi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: TypeError: Unknown image model type: qwen2 bug ### Your current environment Version： vllm 0.8.1+cu121 transformers 4.48.2 python 3.10.6 System： ubuntu20.04 ### 🐛 Describe the bug 1、Deploy the OpenAI interface usi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: del type: qwen2","type":"BadRequestError","param":null,"code":400} 4、The backend reports the following error: [serving_chat.py:204] TypeError: Unknown image model type: qwen2 5、I have seen similar issues resolved in pre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Error: Unknown image model type: qwen2 bug ### Your current environment Version： vllm 0.8.1+cu121 transformers 4.48.2 python 3.10.6 System： ubuntu20.04 ### 🐛 Describe the bug 1、Deploy the OpenAI interface using vLLM, wi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: at? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: {"object":"error","message":"Unknown image model type: qwen2","type":"BadRequestError","param":null,"code":400} 4、The backend reports the following error: [serving_chat.py:204] TypeError: Unknown image model type: qwen2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
