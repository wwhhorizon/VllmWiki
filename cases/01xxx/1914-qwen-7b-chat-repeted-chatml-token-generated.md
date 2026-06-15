# vllm-project/vllm#1914: qwen-7b-chat  repeted chatml token generated

| 字段 | 值 |
| --- | --- |
| Issue | [#1914](https://github.com/vllm-project/vllm/issues/1914) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> qwen-7b-chat  repeted chatml token generated

### Issue 正文摘录

start service ```bash VLLM_USE_MODELSCOPE =True python -m vllm.entrypoints.openai.api_server \ --model="qwen/Qwen-7B-Chat" --revision="v1.1.8" --trust-remote-code ``` visit service using ```bash curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "qwen/Qwen-7B-Chat", "prompt": "San Francisco is a", "max_tokens": 256, "temperature": 0 }' ``` the output is ```text {"id":"cmpl-19a2305d9b214b90a98e5e99494f4bcc","object":"text_completion","created":13734354,"model":"qwen/Qwen-7B-Chat","choices":[{"index":0,"text":" city in California, United States. It is located on the west coast of the United States and is known for its iconic landmarks such as the Golden Gate Bridge, Alcatraz Island, and Fisherman's Wharf. San Francisco is also known for its diverse culture, with a large LGBTQ+ community and a thriving arts scene. The city is home to many tech companies, including Google, Apple, and Facebook, and is a hub for innovation and entrepreneurship. Despite its reputation as a bustling metropolis, San Francisco also has a laid-back, hippie vibe and is known for its beautiful parks and gardens. Overall, San Francisco is a vibrant and exciting city...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: qwen-7b-chat repeted chatml token generated start service ```bash VLLM_USE_MODELSCOPE =True python -m vllm.entrypoints.openai.api_server \ --model="qwen/Qwen-7B-Chat" --revision="v1.1.8" --trust-remote-code ``` visit se
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: plication/json" \ -d '{ "model": "qwen/Qwen-7B-Chat", "prompt": "San Francisco is a", "max_tokens": 256, "temperature": 0 }' ``` the output is ```text {"id":"cmpl-19a2305d9b214b90a98e5e99494f4bcc","object":"text_complet...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: oogle, Apple, and Facebook, and is a hub for innovation and entrepreneurship. Despite its reputation as a bustling metropolis, San Francisco also has a laid-back, hippie vibe and is known for its beautiful parks and gar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
