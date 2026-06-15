# vllm-project/vllm#9879: [Usage]: Hidden States not working in Speculative Decode

| 字段 | 值 |
| --- | --- |
| Issue | [#9879](https://github.com/vllm-project/vllm/issues/9879) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Hidden States not working in Speculative Decode

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When using speculative decoding, I understand that` KV-cache `or `hidden_states` rollback should accompany the process. I only found one piece of logic implementing this, located in: `/usr/local/lib/python3.10/dist-packages/vllm/spec_decode/spec_decode_worker.py` Here is the relevant code: ``` hidden_states = proposal_scores.hidden_states if hidden_states is not None: # Contract hidden states based on accepted tokens hs_size = hidden_states.shape[-1] accepted_index = accepted_token_ids + 1 # Convert -1 to 0 accepted_index = accepted_index.count_nonzero(dim=1).add_(-1) index = accepted_index[:, None, None].expand(-1, 1, hs_size) second_last_token_hidden_states = hidden_states[:, -2] # b x d hidden_states = hidden_states.gather(1, index).squeeze(1) # b x d # Store hidden states from target model for subsequent decode step self.previous_hidden_states = HiddenStates( hidden_states, seq_group_metadata_list, second_last_token_hidden_states) ``` However, when I print out these `hidden_states`, I see that they are actually `None`. Upon investigation, I found that in the target...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Hidden States not working in Speculative Decode usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When using speculative decoding, I u...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: s_hidden_states = HiddenStates( hidden_states, seq_group_metadata_list, second_last_token_hidden_states) ``` However, when I print out these `hidden_states`, I see that they are actually `None`. Upon investigation, I fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: index).squeeze(1) # b x d # Store hidden states from target model for subsequent decode step self.previous_hidden_states = HiddenStates( hidden_states, seq_group_metadata_list, second_last_token_hidden_states) ``` Howev...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n a long-standing challenge for me. Any assistance would be greatly appreciated! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ing currently supports hidden_states? I am using the Qwen-7B and Qwen-7B-int4 models, and this issue has been a long-standing challenge for me. Any assistance would be greatly appreciated! ### Before submitting a new is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
