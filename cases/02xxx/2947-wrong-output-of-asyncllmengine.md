# vllm-project/vllm#2947: wrong output of AsyncLLMEngine

| 字段 | 值 |
| --- | --- |
| Issue | [#2947](https://github.com/vllm-project/vllm/issues/2947) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> wrong output of AsyncLLMEngine

### Issue 正文摘录

When deploying the Qwen 1.5 model with FastChat and vllm, there is an error in the output of the [AsyncLLMEngine.](https://github.com/lm-sys/FastChat/blob/main/fastchat/serve/vllm_worker.py#L119) One example of `request_output.outputs` from #L128 is `[CompletionOutput(index=0, text='Tom886', token_ids=[24732, 23, 23, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 151645], cumulative_logprob=0.0, logprobs=None, finish_reason=stop)]`. The content of **token_ids** is inconsistent with the **text**, and the token_ids is the correct output. In my test, the text is always 10 tokens shorter than token_ids. package: fastchat==0.2.36, vllm==0.3.1

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: wrong output of AsyncLLMEngine When deploying the Qwen 1.5 model with FastChat and vllm, there is an error in the output of the [AsyncLLMEngine.](https://github.com/lm-sys/FastChat/blob/main/fastchat/serve/vllm_worker.p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: FastChat/blob/main/fastchat/serve/vllm_worker.py#L119) One example of `request_output.outputs` from #L128 is `[CompletionOutput(index=0, text='Tom886', token_ids=[24732, 23, 23, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: stent with the **text**, and the token_ids is the correct output. In my test, the text is always 10 tokens shorter than token_ids. package: fastchat==0.2.36, vllm==0.3.1

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
