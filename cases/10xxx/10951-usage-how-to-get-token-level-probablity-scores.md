# vllm-project/vllm#10951: [Usage]: How to get token level probablity scores

| 字段 | 值 |
| --- | --- |
| Issue | [#10951](https://github.com/vllm-project/vllm/issues/10951) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to get token level probablity scores

### Issue 正文摘录

### Your current environment How to get token level probablity scores through vllm llm_engine Below is the code snippet, through which I could get the scores using huggingface library. ``` outputs = model.generate( **inputs, max_new_tokens=1, temperature=0.01, top_k=50, pad_token_id=2, num_return_sequences=1, return_dict_in_generate=True, use_cache=True, output_scores=True) transition_scores = model.compute_transition_scores( outputs.sequences, outputs.scores, normalize_logits=True ) decoded_tokens, probability_scores,tok_id=[],[],[] input_length = 1 if model.config.is_encoder_decoder else inputs.input_ids.shape[1] generated_tokens = outputs.sequences[:, input_length:] for tok, score in zip(generated_tokens[0], transition_scores[0]): decoded_tokens.append(tokenizer.decode(tok, skip_special_tokens=True)) probability_scores.append(np.exp(score.numpy())) tok_id.append(tok) print(f"| {tok:5d} | {tokenizer.decode(tok, skip_special_tokens=True):8s} | {score.numpy():.18f} | {np.exp(score.numpy()):.2%}") ``` I couldn't get the same results using vllm logprobs=1. ``` vllm_sampling_params = SamplingParams(temperature=0.7, max_tokens=1, top_k=5, top_p=0.1, logprobs=1) outputs = llm.generate(...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ne Below is the code snippet, through which I could get the scores using huggingface library. ``` outputs = model.generate( **inputs, max_new_tokens=1, temperature=0.01, top_k=50, pad_token_id=2, num_return_sequences=1,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tion_scores[0]): decoded_tokens.append(tokenizer.decode(tok, skip_special_tokens=True)) probability_scores.append(np.exp(score.numpy())) tok_id.append(tok) print(f"| {tok:5d} | {tokenizer.decode(tok, skip_special_tokens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to get token level probablity scores usage;stale ### Your current environment How to get token level probablity scores through vllm llm_engine Below is the code snippet, through which I could get the scores...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: es,tok_id=[],[],[] input_length = 1 if model.config.is_encoder_decoder else inputs.input_ids.shape[1] generated_tokens = outputs.sequences[:, input_length:] for tok, score in zip(generated_tokens[0], transition_scores[0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
