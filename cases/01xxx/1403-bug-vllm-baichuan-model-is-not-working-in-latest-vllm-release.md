# vllm-project/vllm#1403: [BUG] vLLM Baichuan model is not working in latest vLLM release

| 字段 | 值 |
| --- | --- |
| Issue | [#1403](https://github.com/vllm-project/vllm/issues/1403) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG] vLLM Baichuan model is not working in latest vLLM release

### Issue 正文摘录

A simple test from official script ```bash python benchmarks/benchmark_latency.py --trust-remote-code \ --model baichuan-inc/Baichuan-13B-Base \ --input-len 256 --output-len 256 \ --batch-size 32 \ --tensor-parallel 2 ``` Shows error info: ```AttributeError: 'BaichuanTokenizer' object has no attribute 'sp_model'``` This is due to the newest transformers==4.34.0 is not compatiable with currrent vllm Baichuan model. Yet this version required for Mistral model, hence introduces a breaking change in vLLM. @WoosukKwon @zhuohan123

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [BUG] vLLM Baichuan model is not working in latest vLLM release bug A simple test from official script ```bash python benchmarks/benchmark_latency.py --trust-remote-code \ --model baichuan-inc/Baichuan-13B-Base \ --inpu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n model is not working in latest vLLM release bug A simple test from official script ```bash python benchmarks/benchmark_latency.py --trust-remote-code \ --model baichuan-inc/Baichuan-13B-Base \ --input-len 256 --output...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [BUG] vLLM Baichuan model is not working in latest vLLM release bug A simple test from official script ```bash python benchmarks/benchmark_latency.py --trust-remote-code \ --model baichuan-inc/Baichuan-13B-Base \ --inpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
