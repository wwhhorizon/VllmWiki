# vllm-project/vllm#6521: [Bug]: vLLM server crashes when `echo=True` and `max_tokens=0`

| 字段 | 值 |
| --- | --- |
| Issue | [#6521](https://github.com/vllm-project/vllm/issues/6521) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM server crashes when `echo=True` and `max_tokens=0`

### Issue 正文摘录

### Your current environment ```text vLLM server latest, as of July 17th 2024: vllm/vllm-openai:latest ``` ### 🐛 Describe the bug I'm trying to get the logprobability of the last token (Yes or No) of the prompt. In my client, I set: - echo to True - logprobs to 1 - max_tokens to 0 ```python import requests generation_args = { "prompt": "Your answer: Yes", "temperature": self.temperature, "top_p": self.top_p if self.do_sample else 1.0, "top_k": self.top_k if self.do_sample else -1, "best_of": self.best_of, "repetition_penalty": self.repetition_penalty if self.do_sample else 1.0, "max_tokens": 0, # no additional tokens to generate (using 1 to not crash vllm server?) "n": 1, "model": self.model_alias, "echo": True, # include prompt in response, must be true for getting prompt logprobs, see https://github.com/vllm-project/vllm/blob/5f0b9933e63839e816b9736a65a3c55005df2cfe/vllm/entrypoints/openai/protocol.py#L634 "logprobs": 1 } url = f"{self.base_url}/v1/completions" r = requests.post(url, json=generation_args ``` However, as soon as i query the vLLM server, it crashes with the following message inthe logs ``` Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-pac...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: mperature": self.temperature, "top_p": self.top_p if self.do_sample else 1.0, "top_k": self.top_k if self.do_sample else -1, "best_of": self.best_of, "repetition_penalty": self.repetition_penalty if self.do_sample else...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tokens to generate (using 1 to not crash vllm server?) "n": 1, "model": self.model_alias, "echo": True, # include prompt in response, must be true for getting prompt logprobs, see https://github.com/vllm-project/vllm/bl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vLLM server crashes when `echo=True` and `max_tokens=0` bug;stale ### Your current environment ```text vLLM server latest, as of July 17th 2024: vllm/vllm-openai:latest ``` ### 🐛 Describe the bug I'm trying to ge...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: _tokens=0` bug;stale ### Your current environment ```text vLLM server latest, as of July 17th 2024: vllm/vllm-openai:latest ``` ### 🐛 Describe the bug I'm trying to get the logprobability of the last token (Yes or No) o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
