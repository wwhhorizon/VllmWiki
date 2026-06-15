# vllm-project/vllm#37471: [Bug]: Accuracy issue running Model Runner V2 with Qwen3.5

| 字段 | 值 |
| --- | --- |
| Issue | [#37471](https://github.com/vllm-project/vllm/issues/37471) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Accuracy issue running Model Runner V2 with Qwen3.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `export MODEL="Qwen/Qwen3.5-35B-A3B-FP8"` `vllm serve "$MODEL" --tensor-parallel-size 2 --data-parallel-size 2 --enable-expert-parallel --port 9256` `lm_eval --model local-completions --model_args "base_url=http://127.0.0.1:9256/v1/completions,model=$MODEL,num_concurrent=1024" --tasks gsm8k` ```bash # export VLLM_USE_V2_MODEL_RUNNER=0 |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.7824|± |0.0114| | | |strict-match | 5|exact_match|↑ |0.7635|± |0.0117| # export VLLM_USE_V2_MODEL_RUNNER=1 |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.1425|± |0.0096| | | |strict-match | 5|exact_match|↑ |0.1334|± |0.0094| ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Accuracy issue running Model Runner V2 with Qwen3.5 bug ### Your current environment ### 🐛 Describe the bug `export MODEL="Qwen/Qwen3.5-35B-A3B-FP8"` `vllm serve "$MODEL" --tensor-parallel-size 2 --data-parallel
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 127.0.0.1:9256/v1/completions,model=$MODEL,num_concurrent=1024" --tasks gsm8k` ```bash # export VLLM_USE_V2_MODEL_RUNNER=0 |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Accuracy issue running Model Runner V2 with Qwen3.5 bug ### Your current environment ### 🐛 Describe the bug `export MODEL="Qwen/Qwen3.5-35B-A3B-FP8"` `vllm serve "$MODEL" --tensor-parallel-size 2 --data-parallel-...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Accuracy issue running Model Runner V2 with Qwen3.5 bug ### Your current environment ### 🐛 Describe the bug `export MODEL="Qwen/Qwen3.5-35B-A3B-FP8"` `vllm serve "$MODEL" --tensor-parallel-size 2 --data-parallel
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 1024" --tasks gsm8k` ```bash # export VLLM_USE_V2_MODEL_RUNNER=0 |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
