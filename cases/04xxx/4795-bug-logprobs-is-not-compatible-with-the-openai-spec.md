# vllm-project/vllm#4795: [Bug]: `logprobs` is not compatible with the OpenAI spec

| 字段 | 值 |
| --- | --- |
| Issue | [#4795](https://github.com/vllm-project/vllm/issues/4795) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `logprobs` is not compatible with the OpenAI spec

### Issue 正文摘录

### Your current environment I'm using Runpod Serverless vLLM (https://github.com/runpod-workers/worker-vllm) so I can't run this command. However, I confirmed that the issue is in the codebase in `main`: https://github.com/vllm-project/vllm/blob/0fca3cdcf265cd375bca684d951702b6b7adf65a/vllm/entrypoints/openai/protocol.py ### 🐛 Describe the bug The behavior of `logprobs=True` does not match OpenAI's. I identified two issues: **(1) vLLM throws an error when `logprobs=True` and `top_logprobs` is missing.** OpenAI works fine: ```py completion = openai_client.chat.completions.create( model="gpt-4-turbo-preview", messages=[ {"role": "user", "content": "Hi!"} ], logprobs=True, ) ``` ``` ChatCompletion(id='chatcmpl-9OY4XFK8suJ7ed0yw5vglbTsOZUt1', choices=[Choice(finish_reason='stop', index=0, logprobs=ChoiceLogprobs(content=[ChatCompletionTokenLogprob(token='Hello', bytes=[72, 101, 108, 108, 111], logprob=-0.0008963357, top_logprobs=[]), ChatCompletionTokenLogprob(token='!', bytes=[33], logprob=-9.729906e-06, top_logprobs=[]), ChatCompletionTokenLogprob(token=' How', bytes=[32, 72, 111, 119], logprob=-1.4140442e-05, top_logprobs=[]), ChatCompletionTokenLogprob(token=' can', bytes=[32, 99...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: works fine: ```py completion = openai_client.chat.completions.create( model="gpt-4-turbo-preview", messages=[ {"role": "user", "content": "Hi!"} ], logprobs=True, ) ``` ``` ChatCompletion(id='chatcmpl-9OY4XFK8suJ7ed0yw5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ssage='Top logprobs must be set when logprobs is.', param=None, type='BadRequestError') ``` via https://github.com/vllm-project/vllm/blob/0fca3cdcf265cd375bca684d951702b6b7adf65a/vllm/entrypoints/openai/protocol.py#L162...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
