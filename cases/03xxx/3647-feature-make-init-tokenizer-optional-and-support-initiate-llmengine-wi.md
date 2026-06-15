# vllm-project/vllm#3647: [Feature]: make _init_tokenizer optional and support initiate LLMEngine without tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#3647](https://github.com/vllm-project/vllm/issues/3647) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: make _init_tokenizer optional and support initiate LLMEngine without tokenizer

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the `generate` method supports inference based on `prompt_token_ids`: ``` def generate( self, prompts: Optional[Union[str, List[str]]] = None, sampling_params: Optional[SamplingParams] = None, prompt_token_ids: Optional[List[List[int]]] = None, use_tqdm: bool = True, lora_request: Optional[LoRARequest] = None, ) -> List[RequestOutput]: ``` that means tokenizer is optional to the LLM engine. However, to initiate an LLM engine, it always calls [`_init_tokenizer` ](https://github.com/vllm-project/vllm/blob/main/vllm/engine/llm_engine.py#L167), which effectively makes tokenizer required. The LLM engine cannot be initialized without a valid tokenizer argument. In our application, we would love to use LLM's powerful engine for inference, but want to keep tokenizer as a separate service. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: enizer optional and support initiate LLMEngine without tokenizer feature request ### 🚀 The feature, motivation and pitch Currently the `generate` method supports inference based on `prompt_token_ids`: ``` def generate(...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
