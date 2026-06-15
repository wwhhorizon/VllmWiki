# vllm-project/vllm#31202: [Bug]: Mixtral Fp8 Accuracy is Degraded

| 字段 | 值 |
| --- | --- |
| Issue | [#31202](https://github.com/vllm-project/vllm/issues/31202) |
| 状态 | closed |
| 标签 | bug;help wanted |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mixtral Fp8 Accuracy is Degraded

### Issue 正文摘录

### Your current environment H200 ### 🐛 Describe the bug - launch ```bash vllm serve amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV --enforce-eager -tp 2 ``` - eval ```bash lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model=amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV,base_url=http://localhost:8000/v1/completions,num_concurrent=1000,tokenized_requests=False" ``` - on main: ```bash local-completions (model=amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV,base_url=http://localhost:8000/v1/completions,num_concurrent=1000,tokenized_requests=False), gen_kwargs: (None), limit: None, num_fewshot: None, batch_size: 1 |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.2843|± |0.0124| | | |strict-match | 5|exact_match|↑ |0.2108|± |0.0112| ``` - on 0.12.0: ```bash local-completions (model=amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV,base_url=http://localhost:8000/v1/completions,num_concurrent=1000,tokenized_requests=False), gen_kwargs: (None), limit: None, num_fewshot: None, batch_size: 1 |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|--------------...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Mixtral Fp8 Accuracy is Degraded bug;help wanted ### Your current environment H200 ### 🐛 Describe the bug - launch ```bash vllm serve amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV --enforce-eager -tp 2 ``` - eval ```bash...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Mixtral Fp8 Accuracy is Degraded bug;help wanted ### Your current environment H200 ### 🐛 Describe the bug - launch ```bash vllm serve amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV --enforce-eager -tp 2 ``` - eval ```bash...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2 ``` - eval ```bash lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model=amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV,base_url=http://localhost:8000/v1/completions,num_concurrent=1000,tokenized_requests=F...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Mixtral Fp8 Accuracy is Degraded bug;help wanted ### Your current environment H200 ### 🐛 Describe the bug - launch ```bash vllm serve amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV --enforce-eager -tp 2 ``` - eval ```bash...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: gen_kwargs: (None), limit: None, num_fewshot: None, batch_size: 1 |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
