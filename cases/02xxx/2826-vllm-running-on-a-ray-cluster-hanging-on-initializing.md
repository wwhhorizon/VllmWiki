# vllm-project/vllm#2826: vLLM running on a Ray Cluster Hanging on Initializing

| 字段 | 值 |
| --- | --- |
| Issue | [#2826](https://github.com/vllm-project/vllm/issues/2826) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vLLM running on a Ray Cluster Hanging on Initializing

### Issue 正文摘录

It isn't clear what is at fault here. Whether it be vLLM or Ray. There is a thread here on the ray forums that outlines the issue, it is 16 days old, there is no reply to it. https://discuss.ray.io/t/running-vllm-script-on-multi-node-cluster/13533 Taking from that thread, but this is identical for me. ``` 2024-01-24 13:57:17,308 INFO worker.py:1540 – Connecting to existing Ray cluster at address: HOST_IP_ADDRESS… 2024-01-24 13:57:17,317 INFO worker.py:1715 – Connected to Ray cluster. View the dashboard at 127.0.0.1:8265 INFO 01-24 13:57:39 llm_engine.py:70] Initializing an LLM engine with config: model=‘mistralai/Mistral-7B-Instruct-v0.2’, tokenizer=‘mistralai/Mistral-7B-Instruct-v0.2’, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, enforce_eager=False, seed=0) But after that it hangs, and eventually quits. ``` I have exactly this same problem. The thread details the other points, that the "ray status" seems to show nodes working and communicating, that it stays like this for an age then eventually crashes with some error m...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, enforce_eager=False, seed...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 65 INFO 01-24 13:57:39 llm_engine.py:70] Initializing an LLM engine with config: model=‘mistralai/Mistral-7B-Instruct-v0.2’, tokenizer=‘mistralai/Mistral-7B-Instruct-v0.2’, tokenizer_mode=auto, revision=None, tokenizer_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, quantization=None, enforce_eager=False,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
