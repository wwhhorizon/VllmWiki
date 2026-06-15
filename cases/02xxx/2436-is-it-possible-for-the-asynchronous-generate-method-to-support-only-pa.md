# vllm-project/vllm#2436: Is it possible for the asynchronous generate method to support only passing the prompt_token_ids parameter without requiring the prompt parameter? This would be advantageous for customizing the input of tokens.

| 字段 | 值 |
| --- | --- |
| Issue | [#2436](https://github.com/vllm-project/vllm/issues/2436) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Is it possible for the asynchronous generate method to support only passing the prompt_token_ids parameter without requiring the prompt parameter? This would be advantageous for customizing the input of tokens.

### Issue 正文摘录

Is it possible for the asynchronous generate method to support only passing the prompt_token_ids parameter without requiring the prompt parameter? This would be advantageous for customizing the input of tokens. We have observed that using the tokenizer.encode method directly to generate tokens can lead to certain issues. Customizing the input by passing prompt_token_ids can resolve these problems. https://github.com/vllm-project/vllm/blob/35c4bc20d9d454f58506b561b6770d3ae4752bf9/vllm/engine/async_llm_engine.py#L408C10-L408C10 ``` async def generate( self, prompt: Optional[str], sampling_params: SamplingParams, request_id: str, prompt_token_ids: Optional[List[int]] = None ) -> AsyncI ```terator[RequestOutput]:

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: : str, prompt_token_ids: Optional[List[int]] = None ) -> AsyncI ```terator[RequestOutput]:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: prompt: Optional[str], sampling_params: SamplingParams, request_id: str, prompt_token_ids: Optional[List[int]] = None ) -> AsyncI ```terator[RequestOutput]:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
