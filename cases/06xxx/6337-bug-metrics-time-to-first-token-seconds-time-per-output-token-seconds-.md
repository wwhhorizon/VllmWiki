# vllm-project/vllm#6337: [Bug]: Metrics time_to_first_token_seconds, time_per_output_token_seconds not working correctly

| 字段 | 值 |
| --- | --- |
| Issue | [#6337](https://github.com/vllm-project/vllm/issues/6337) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Metrics time_to_first_token_seconds, time_per_output_token_seconds not working correctly

### Issue 正文摘录

### Your current environment vllm==0.5.1 ### 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server --model /secondary/thies/Hermes-2-Theta-Llama-3-70B/ --tensor-parallel-size 8 --max-num-batched-tokens 8192 ``` The entries of the histograms - time_to_first_token_seconds - time_per_output_token_seconds are identical for all buckets, so the time values are apparently always 0 seconds. ``` # HELP vllm:time_to_first_token_seconds Histogram of time to first token in seconds. # TYPE vllm:time_to_first_token_seconds histogram vllm:time_to_first_token_seconds_bucket{le="0.001",model_name="/secondary/thies/Hermes-2-Theta-Llama-3-70B/"} 208.0 vllm:time_to_first_token_seconds_bucket{le="0.005",model_name="/secondary/thies/Hermes-2-Theta-Llama-3-70B/"} 208.0 vllm:time_to_first_token_seconds_bucket{le="0.01",model_name="/secondary/thies/Hermes-2-Theta-Llama-3-70B/"} 208.0 vllm:time_to_first_token_seconds_bucket{le="0.02",model_name="/secondary/thies/Hermes-2-Theta-Llama-3-70B/"} 208.0 vllm:time_to_first_token_seconds_bucket{le="0.04",model_name="/secondary/thies/Hermes-2-Theta-Llama-3-70B/"} 208.0 vllm:time_to_first_token_seconds_bucket{le="0.06",model_name="/secondary/thies/Herm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server --model /secondary/thies/Hermes-2-Theta-Llama-3-70B/ --tensor-parallel-size 8 --max-num-batched-tokens 8192 ``` The entries of the histograms - time_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
