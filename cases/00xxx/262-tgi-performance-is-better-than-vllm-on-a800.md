# vllm-project/vllm#262: TGI performance is better than vllm on A800

| 字段 | 值 |
| --- | --- |
| Issue | [#262](https://github.com/vllm-project/vllm/issues/262) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TGI performance is better than vllm on A800

### Issue 正文摘录

I use benchmark_serving as client, api_server for vllm, text_generation_server for TGI, the client cmd is listed below: " python benchmark_serving.py --backend tgi/vllm --tokenizer /data/llama --dataset /data/ShareGPT_V3_unfiltered_cleaned_split.json --host 10.3.1.2 --port 8108 --num-prompts 1000" Why I get the result that TGI is 2x better than vllm?

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: for TGI, the client cmd is listed below: " python benchmark_serving.py --backend tgi/vllm --tokenizer /data/llama --dataset /data/ShareGPT_V3_unfiltered_cleaned_split.json --host 10.3.1.2 --port 8108 --num-prompts 1000"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: elow: " python benchmark_serving.py --backend tgi/vllm --tokenizer /data/llama --dataset /data/ShareGPT_V3_unfiltered_cleaned_split.json --host 10.3.1.2 --port 8108 --num-prompts 1000" Why I get the result that TGI is 2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: TGI performance is better than vllm on A800 bug I use benchmark_serving as client, api_server for vllm, text_generation_server for TGI, the client cmd is listed below: " python benchmark_serving.py --backend tgi/vllm --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
