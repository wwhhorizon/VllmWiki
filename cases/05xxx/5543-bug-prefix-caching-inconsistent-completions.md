# vllm-project/vllm#5543: [Bug]: prefix-caching: inconsistent completions

| 字段 | 值 |
| --- | --- |
| Issue | [#5543](https://github.com/vllm-project/vllm/issues/5543) |
| 状态 | open |
| 标签 | bug;keep-open |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: prefix-caching: inconsistent completions

### Issue 正文摘录

### Your current environment ```text vLLM version 0.5.0.post1 ``` ### 🐛 Describe the bug Hi, Seems that there is a dirty cache issue with `--enable-prefix-caching`. We noticed it as we saw internal eval scores significantly degrade when running with `--enable-prefix-caching` and here I'll show how to reproduce it with a short snippet. Running 2 vLLM servers with: without prefix caching: ```bash python -m vllm.entrypoints.openai.api_server --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 --port 8001 ``` and another with prefix caching: ```bash python -m vllm.entrypoints.openai.api_server --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 --port 8002 --enable-prefix-caching ``` Then running this snippet: ```python import string import random import openai vllms = { "no-prefix-caching": "http://localhost:8001/v1", "with-prefix-caching": "http://localhost:8002/v1", } random.seed(0) prompts = [] for i in range(16): prompts.append(''.join(random.choices(string.ascii_lowercase + string.digits, k=512))) runs = [] for run in range(2): print(f"\n🏃 run #{run+1}") completions = {k: [] for k in vllms.keys()} runs.append(completions) for name, endpoint in vllms.items(): print(f"vLLM {name=}, {endpoint=}") cl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ent completions bug;keep-open ### Your current environment ```text vLLM version 0.5.0.post1 ``` ### 🐛 Describe the bug Hi, Seems that there is a dirty cache issue with `--enable-prefix-caching`. We noticed it as we saw...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t prefix caching: ```bash python -m vllm.entrypoints.openai.api_server --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 --port 8001 ``` and another with prefix caching: ```bash python -m vllm.entrypoints.openai.api_server --m...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: de when running with `--enable-prefix-caching` and here I'll show how to reproduce it with a short snippet. Running 2 vLLM servers with: without prefix caching: ```bash python -m vllm.entrypoints.openai.api_server --mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: issue with `--enable-prefix-caching`. We noticed it as we saw internal eval scores significantly degrade when running with `--enable-prefix-caching` and here I'll show how to reproduce it with a short snippet. Running 2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
