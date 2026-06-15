# vllm-project/vllm#1398: When I export logits in VLLM during first forward it's more slowly than torch. Does anyone have experience about llama-70B-chat-hf VLLM inference speed with 2 batch size? 

| 字段 | 值 |
| --- | --- |
| Issue | [#1398](https://github.com/vllm-project/vllm/issues/1398) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When I export logits in VLLM during first forward it's more slowly than torch. Does anyone have experience about llama-70B-chat-hf VLLM inference speed with 2 batch size? 

### Issue 正文摘录

For harness test framework. it uses "logits"to calculate the PPL like this: ``` def _model_call( self, inputs: TokenSequence, labels: Optional[TokenSequence] = None ) -> TokenSequence: return self.model(inputs)["logits"] ``` Then, I've added the VLLM implement in the test pipeline with exporting the logits for the first forward. ``` def _model_call( self, inputs: TokenSequence, labels: Optional[TokenSequence] = None ) -> TokenSequence: sampling_params = SamplingParams(max_tokens=self._max_gen_toks, temperature=0.0, top_p=1.0, top_k=-1, logprobs=1, export_logits=True, step_limit=1,) # I added this for only executing one time forward prompt_token_ids_list = [input_token[0].squeeze(0).tolist() for input_token in inputs] outputs = self.llm.generate(prompt_token_ids=prompt_token_ids_list, sampling_params=sampling_params, use_tqdm=False) return outputs ``` I found it's running very slowly, when I tested Llama-70B-chat-hf model. Model: Llama2-chat-70b-hf VLLM baseline commit ID: bc0644574ca12d754a031596bdcfe8e1f0e6ab39 VLLM batch_size = 2 (In other words, len(prompt_token_ids_list) == 2) VLLM TP = 8 Using VLLM inference got test speed 38/38 [03:08 Any: ...... if self.parallel_config.work...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: t forward it's more slowly than torch. Does anyone have experience about llama-70B-chat-hf VLLM inference speed with 2 batch size? For harness test framework. it uses "logits"to calculate the PPL like this: ``` def _mod...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g_params=sampling_params, use_tqdm=False) return outputs ``` I found it's running very slowly, when I tested Llama-70B-chat-hf model. Model: Llama2-chat-70b-hf VLLM baseline commit ID: bc0644574ca12d754a031596bdcfe8e1f0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t llama-70B-chat-hf VLLM inference speed with 2 batch size? For harness test framework. it uses "logits"to calculate the PPL like this: ``` def _model_call( self, inputs: TokenSequence, labels: Optional[TokenSequence] =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
