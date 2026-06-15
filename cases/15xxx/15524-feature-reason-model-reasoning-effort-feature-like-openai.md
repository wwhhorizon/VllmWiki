# vllm-project/vllm#15524: [Feature]: Reason model reasoning effort feature like OpenAI

| 字段 | 值 |
| --- | --- |
| Issue | [#15524](https://github.com/vllm-project/vllm/issues/15524) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Reason model reasoning effort feature like OpenAI

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, So, I am running Qwen/QwQ-32B-AWQ model and serving using below parameter ``` vllm serve Qwen/QwQ-32B-AWQ \ --port 8000 \ --max-model-len 12000 \ --gpu-memory-utilization 0.7 \ --quantization awq \ --enable-reasoning \ --reasoning-parser deepseek_r1 ``` and for running a simple code below it took 1 mint to process. ``` %%time import os import openai client = openai.OpenAI( base_url="http://localhost:8000/v1/", api_key="dummy" ) chat_completion = client.chat.completions.create( messages = [ { 'role': 'system', 'content': "You are an assistant" }, { 'role': 'user', 'content': "Tell me joke on bear" } ], model= "Qwen/QwQ-32B-AWQ", temperature=0.0, stream=False, ) reasoning_content = chat_completion.choices[0].message.reasoning_content content = chat_completion.choices[0].message.content print("reasoning_content:", reasoning_content) print("content:", content) ``` I know reasoning model will take time to process but can we have a feature where instead of think token as first token we have something direct inference to it and also reasoning too as in someplace I need thinking someplace I don't. Kindly help me if there is another way or can we...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Reason model reasoning effort feature like OpenAI feature request;stale ### 🚀 The feature, motivation and pitch Hi, So, I am running Qwen/QwQ-32B-AWQ model and serving using below parameter ``` vllm serve Qwe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Reason model reasoning effort feature like OpenAI feature request;stale ### 🚀 The feature, motivation and pitch Hi, So, I am running Qwen/QwQ-32B-AWQ model and serving using below parameter ``` vllm serve Qwe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: for running a simple code below it took 1 mint to process. ``` %%time import os import openai client = openai.OpenAI( base_url="http://localhost:8000/v1/", api_key="dummy" ) chat_completion = client.chat.completions.cre...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 0 \ --max-model-len 12000 \ --gpu-memory-utilization 0.7 \ --quantization awq \ --enable-reasoning \ --reasoning-parser deepseek_r1 ``` and for running a simple code below it took 1 mint to process. ``` %%time import os...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
