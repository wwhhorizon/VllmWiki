# vllm-project/vllm#8747: [Bug]: OLMoE produces incorrect output with TP>1

| 字段 | 值 |
| --- | --- |
| Issue | [#8747](https://github.com/vllm-project/vllm/issues/8747) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OLMoE produces incorrect output with TP>1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We can perform evaluations for GSM8k with lm-eval to see the issue. Please use `pip install lm-eval==0.4.3` TP=1 ``` VLLM_WORKER_MULTIPROC_METHOD=spawn lm_eval --model vllm --model_args pretrained=allenai/OLMoE-1B-7B-0924-Instruct,tensor_parallel_size=1 --tasks gsm8k --num_fewshot 5 --batch_size auto vllm (pretrained=allenai/OLMoE-1B-7B-0924-Instruct,tensor_parallel_size=1), gen_kwargs: (None), limit: None, num_fewshot: 5, batch_size: auto |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.3457|± |0.0131| | | |strict-match | 5|exact_match|↑ |0.3313|± |0.0130| ``` TP=2 ``` VLLM_WORKER_MULTIPROC_METHOD=spawn lm_eval --model vllm --model_args pretrained=allenai/OLMoE-1B-7B-0924-Instruct,tensor_parallel_size=2 --tasks gsm8k --num_fewshot 5 --batch_size auto vllm (pretrained=allenai/OLMoE-1B-7B-0924-Instruct,tensor_parallel_size=2), gen_kwargs: (None), limit: None, num_fewshot: 5, batch_size: auto |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|--...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Model Input Dumps _No response_ ### 🐛 Describe the bug We can perform evaluations for GSM8k with lm-eval to see the issue. Please use `pip install lm-eval==0.4.3` TP=1 ``` VLLM_WORKER_MULTIPROC_METHOD=spawn lm_eval --mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: orm evaluations for GSM8k with lm-eval to see the issue. Please use `pip install lm-eval==0.4.3` TP=1 ``` VLLM_WORKER_MULTIPROC_METHOD=spawn lm_eval --model vllm --model_args pretrained=allenai/OLMoE-1B-7B-0924-Instruct...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _No response_ ### 🐛 Describe the bug We can perform evaluations for GSM8k with lm-eval to see the issue. Please use `pip install lm-eval==0.4.3` TP=1 ``` VLLM_WORKER_MULTIPROC_METHOD=spawn lm_eval --model vllm --model_a...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: xact_match|↑ |0.0091|± |0.0026| ``` You can see that the strict-match accuracy goes from 33.13% to 0.91%, so it is clear the outputs are degraded very much. ### Before submitting a new issue... - [X] Make sure you alrea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ncorrect output with TP>1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We can perform evaluations for GSM8k with lm-eval to see the issue. Please use `pip install lm-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
