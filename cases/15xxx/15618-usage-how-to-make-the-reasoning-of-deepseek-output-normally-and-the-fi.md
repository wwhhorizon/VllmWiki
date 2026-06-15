# vllm-project/vllm#15618: [Usage]: How to make the Reasoning of deepseek output normally and the final content structured output

| 字段 | 值 |
| --- | --- |
| Issue | [#15618](https://github.com/vllm-project/vllm/issues/15618) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to make the Reasoning of deepseek output normally and the final content structured output

### Issue 正文摘录

### Your current environment ```text I use Docker to run vllm version 0.8.2. ``` ### How would you like to use vllm Is there a way to make the reasoning output by deepseek normal, and ultimately output as structured content? The code I tried is as follows: ``` import httpx from openai import OpenAI from pydantic import BaseModel client = OpenAI( base_url="xxx", api_key="xxx", http_client=httpx.Client(verify=False), timeout=500 ) completion = client.chat.completions.create( model="xxxLLM", messages=[ {"role": "user", "content": "Classify this sentiment: vLLM is wonderful!"} ], extra_body={"guided_choice": ["positive", "negative"]}, ) if __name__ == '__main__': print("reasoning_content: ", completion.choices[0].message.reasoning_content) print("content: ", completion.choices[0].message.content) ``` the output is: ``` reasoning_content: positive content: None ``` After that, I removed --enable-reasoning and --reasoning-parser deepseek_r1 from the command execution. the out put is: ``` positive reasoning_content: None content: positive ``` Is there a way to ensure that the reasoning_content is normally output when deekseek structures the final conclusion? like ``` reasoning_content: F...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tructured output usage;stale ### Your current environment ```text I use Docker to run vllm version 0.8.2. ``` ### How would you like to use vllm Is there a way to make the reasoning output by deepseek normal, and ultima...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: base_url="xxx", api_key="xxx", http_client=httpx.Client(verify=False), timeout=500 ) completion = client.chat.completions.create( model="xxxLLM", messages=[ {"role": "user", "content": "Classify this sentiment: vLLM is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ws: ``` import httpx from openai import OpenAI from pydantic import BaseModel client = OpenAI( base_url="xxx", api_key="xxx", http_client=httpx.Client(verify=False), timeout=500 ) completion = client.chat.completions.cr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: f deepseek output normally and the final content structured output usage;stale ### Your current environment ```text I use Docker to run vllm version 0.8.2. ``` ### How would you like to use vllm Is there a way to make t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
