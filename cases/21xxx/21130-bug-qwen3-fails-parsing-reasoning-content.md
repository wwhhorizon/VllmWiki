# vllm-project/vllm#21130: [Bug]: Qwen3 fails parsing reasoning content

| 字段 | 值 |
| --- | --- |
| Issue | [#21130](https://github.com/vllm-project/vllm/issues/21130) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 fails parsing reasoning content

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying Qwen/Qwen3-32B-AWQ with vllm:0.9.1 using --reasoning-parser qwen3 the parser does not distinguish between reasoning_content and content. As result the response has only the content attribute, which contains both the thinking process and the answer. ``` import openai writer_llm = openai.Client( api_key=openai_api_key, base_url=openai_api_base ) system_prompt = ( "You are an assistant that answers user questions in Italian. " "Provide a **short, direct and generic answer**. " "Do NOT explain details. Simply indicate where the information can be found." ) messages = [ {"role": "system", "content": system_prompt}, {"role": "user", "content": "cos'è uno scrum master?"} ] response = writer_llm.chat.completions.create( model=MODEL_NAME, messages=messages, temperature=0.3) print(response) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3 fails parsing reasoning content bug;stale ### Your current environment ### 🐛 Describe the bug When deploying Qwen/Qwen3-32B-AWQ with vllm:0.9.1 using --reasoning-parser qwen3 the parser does not distinguish...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: attribute, which contains both the thinking process and the answer. ``` import openai writer_llm = openai.Client( api_key=openai_api_key, base_url=openai_api_base ) system_prompt = ( "You are an assistant that answers u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen3 fails parsing reasoning content bug;stale ### Your current environment ### 🐛 Describe the bug When deploying Qwen/Qwen3-32B-AWQ with vllm:0.9.1 using --reasoning-parser qwen3 the parser does not distinguish...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
