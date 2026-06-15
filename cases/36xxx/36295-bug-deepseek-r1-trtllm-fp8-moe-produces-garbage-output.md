# vllm-project/vllm#36295: [Bug]: Deepseek R1 TRTLLM FP8 MoE produces garbage output

| 字段 | 值 |
| --- | --- |
| Issue | [#36295](https://github.com/vllm-project/vllm/issues/36295) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deepseek R1 TRTLLM FP8 MoE produces garbage output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve deepseek-ai/DeepSeek-R1 -tp 8 ``` ``` lm_eval --model local-completions --model_args "base_url=http://0.0.0.0:8000/v1/completions,max_length=8192,tokenized_requests=False,tokenizer_backend=None,num_concurrent=32" --tasks gsm8k --num_fewshot 5 ``` ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.0114|± |0.0029| | | |strict-match | 5|exact_match|↑ |0.0000|± |0.0000| ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: enized_requests=False,tokenizer_backend=None,num_concurrent=32" --tasks gsm8k --num_fewshot 5 ``` ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|---...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: scribe the bug ``` vllm serve deepseek-ai/DeepSeek-R1 -tp 8 ``` ``` lm_eval --model local-completions --model_args "base_url=http://0.0.0.0:8000/v1/completions,max_length=8192,tokenized_requests=False,tokenizer_backend=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0:8000/v1/completions,max_length=8192,tokenized_requests=False,tokenizer_backend=None,num_concurrent=32" --tasks gsm8k --num_fewshot 5 ``` ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|--...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nd=None,num_concurrent=32" --tasks gsm8k --num_fewshot 5 ``` ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-ex...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Deepseek R1 TRTLLM FP8 MoE produces garbage output bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve deepseek-ai/DeepSeek-R1 -tp 8 ``` ``` lm_eval --model local-completions --model_args "base...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
