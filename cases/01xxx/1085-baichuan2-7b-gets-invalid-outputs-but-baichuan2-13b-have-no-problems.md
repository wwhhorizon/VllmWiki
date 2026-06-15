# vllm-project/vllm#1085: Baichuan2-7B gets invalid outputs but Baichuan2-13B have no problems

| 字段 | 值 |
| --- | --- |
| Issue | [#1085](https://github.com/vllm-project/vllm/issues/1085) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Baichuan2-7B gets invalid outputs but Baichuan2-13B have no problems

### Issue 正文摘录

Change https://github.com/vllm-project/vllm/blob/171db473496d204d0507af9745b78447a65667bf/examples/offline_inference_baichuan.py to Baichuan2-7B get invalid outputs ``` INFO 09-18 15:31:19 llm_engine.py:72] Initializing an LLM engine with config: model='baichuan-inc/Baichuan2-7B-Chat', tokenizer='baichuan-inc/Baichuan2-7B-Chat', tokenizer_mode=slow, trust_remote_code=True, dtype=torch.bfloat16, download_dir=None, load_format=auto, tensor_parallel_size=1, seed=0) WARNING 09-18 15:31:19 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. INFO 09-18 15:31:30 llm_engine.py:199] # GPU blocks: 7095, # CPU blocks: 512 Processed prompts: 100%|██████████| 4/4 [00:58 How are you? "], sampling_params=sampling_params) for output in outputs: print(output.outputs[0].text) # output # As a language model language model language analysis "," "The text file script sequence ' ac script script script engine engine engine engine ``` `model.generate` in `huggingface` can generate normal output ``` I'm fine, thank you! How about yourself? ``` Baichuan2-13B-Chat does not have the same issue.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `` INFO 09-18 15:31:19 llm_engine.py:72] Initializing an LLM engine with config: model='baichuan-inc/Baichuan2-7B-Chat', tokenizer='baichuan-inc/Baichuan2-7B-Chat', tokenizer_mode=slow, trust_remote_code=True, dtype=tor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: uan-inc/Baichuan2-7B-Chat', tokenizer_mode=slow, trust_remote_code=True, dtype=torch.bfloat16, download_dir=None, load_format=auto, tensor_parallel_size=1, seed=0) WARNING 09-18 15:31:19 tokenizer.py:64] Using a slow to...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g a fast tokenizer instead. INFO 09-18 15:31:30 llm_engine.py:199] # GPU blocks: 7095, # CPU blocks: 512 Processed prompts: 100%|██████████| 4/4 [00:58 How are you? "], sampling_params=sampling_params) for output in out...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
