# vllm-project/vllm#2980: When using AWQ quantization on the yi-34b-chat model, its performance is lower than the unquantized model under high concurrency.

| 字段 | 值 |
| --- | --- |
| Issue | [#2980](https://github.com/vllm-project/vllm/issues/2980) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When using AWQ quantization on the yi-34b-chat model, its performance is lower than the unquantized model under high concurrency.

### Issue 正文摘录

- A6000 * 4 - max_token = 512 - yi-34b-chat vs yi-34b-chat_awq_int - - `python3 -m vllm.entrypoints.openai.api_server --model /output/yi-34b-chat/ --engine-use-ray --host 0.0.0.0 --port 8080 --worker-use-ray --max-num-seqs 16 --tensor-parallel-size 4 --max-model-len 32768` - - `python3 -m vllm.entrypoints.openai.api_server --model /output/yi_awq_4_dataset_16/ --engine-use-ray --host 0.0.0.0 --port 8080 --worker-use-ray --max-num-seqs 16 --tensor-parallel-size 4 --max-model-len 32768 --quantization awq` ![image](https://github.com/vllm-project/vllm/assets/42427430/4ca94349-3a32-4f14-b68f-e062454e5a71)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: When using AWQ quantization on the yi-34b-chat model, its performance is lower than the unquantized model under high concurrency. - A6000 * 4 - max_token = 512 - yi-34b-chat vs yi-34b-chat_awq_int - - `python3 -m vllm.e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: When using AWQ quantization on the yi-34b-chat model, its performance is lower than the unquantized model under high concurrency. - A6000 * 4 - max_token = 512 - yi-34b-chat vs yi-34b-chat_awq_int - - `python3 -m vllm.e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
