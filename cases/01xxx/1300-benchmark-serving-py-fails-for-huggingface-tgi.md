# vllm-project/vllm#1300: Benchmark_serving.py fails for HuggingFace TGI

| 字段 | 值 |
| --- | --- |
| Issue | [#1300](https://github.com/vllm-project/vllm/issues/1300) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Benchmark_serving.py fails for HuggingFace TGI

### Issue 正文摘录

I am seeing the below error about max_tokens when I run benchmark_serving.py for HuggingFace TGI. Is there anything else I should be doing? I started the server with: `./launch_tgi_server.sh facebook/opt-125m`. I started the benchmarking script with: `python3 benchmark_serving.py --backend tgi --tokenizer facebook/opt-125m --dataset ShareGPT_V3_unfiltered_cleaned_split.json`. ![MicrosoftTeams-image (1)](https://github.com/vllm-project/vllm/assets/58150256/b4498dca-286e-45fe-906b-b85cd4b20eeb)

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: I started the benchmarking script with: `python3 benchmark_serving.py --backend tgi --tokenizer facebook/opt-125m --dataset ShareGPT_V3_unfiltered_cleaned_split.json`. ![MicrosoftTeams-image (1)](https://github.com/vllm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: when I run benchmark_serving.py for HuggingFace TGI. Is there anything else I should be doing? I started the server with: `./launch_tgi_server.sh facebook/opt-125m`. I started the benchmarking script with: `python3 benc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Benchmark_serving.py fails for HuggingFace TGI I am seeing the below error about max_tokens when I run benchmark_serving.py for HuggingFace TGI. Is there anything else I should be doing? I started the server with: `./la...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Benchmark_serving.py fails for HuggingFace TGI I am seeing the below error about max_tokens when I run benchmark_serving.py for HuggingFace TGI. Is there anything else I should be doing? I started the server with: `./la

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
