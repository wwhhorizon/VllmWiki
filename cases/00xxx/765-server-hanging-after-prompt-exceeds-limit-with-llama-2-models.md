# vllm-project/vllm#765: Server hanging after prompt exceeds limit with LLaMA 2 models

| 字段 | 值 |
| --- | --- |
| Issue | [#765](https://github.com/vllm-project/vllm/issues/765) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Server hanging after prompt exceeds limit with LLaMA 2 models

### Issue 正文摘录

Hello, I have been trying vllm 0.1.3 with LLaMA 2 model, ``` python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-70b-chat-hf --port 6011 --tensor-parallel-size 8 --tokenizer hf-internal-testing/llama-tokenizer ``` I noticed the server will hang and stop processing further requests after a prompt being too long. The last output is: ``` WARNING 08-15 11:44:47 scheduler.py:130] Input prompt (2715 tokens) is too long and exceeds limit of 2560 ``` I see there is a related fix: #273 but not sure why this still happens. Is there a way to change this behavior and just discard this request instead? Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Server hanging after prompt exceeds limit with LLaMA 2 models Hello, I have been trying vllm 0.1.3 with LLaMA 2 model, ``` python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-70b-chat-hf --port 6011...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tokenizer ``` I noticed the server will hang and stop processing further requests after a prompt being too long. The last output is: ``` WARNING 08-15 11:44:47 scheduler.py:130] Input prompt (2715 tokens) is too long an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 70b-chat-hf --port 6011 --tensor-parallel-size 8 --tokenizer hf-internal-testing/llama-tokenizer ``` I noticed the server will hang and stop processing further requests after a prompt being too long. The last output is:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
