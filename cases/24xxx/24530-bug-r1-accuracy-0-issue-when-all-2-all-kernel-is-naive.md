# vllm-project/vllm#24530: [Bug]: R1 accuracy 0 issue when all 2 all kernel is "naive"

| 字段 | 值 |
| --- | --- |
| Issue | [#24530](https://github.com/vllm-project/vllm/issues/24530) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: R1 accuracy 0 issue when all 2 all kernel is "naive"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1" --max-num-seqs 512 --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.9 --port 9256 --disable-log-requests --no-enable-prefix-caching` `lm_eval --model local-completions --model_args "base_url=http://127.0.0.1:9256/v1/completions,model=deepseek-ai/DeepSeek-R1,num_concurrent=256" --tasks gsm8k --limit 100` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ | 0|± | 0| | | |strict-match | 5|exact_match|↑ | 0|± | 0| ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: R1 accuracy 0 issue when all 2 all kernel is "naive" bug ### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1" --max-num-seqs 512 --data-parallel-size 8 --enable-expert...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1/completions,model=deepseek-ai/DeepSeek-R1,num_concurrent=256" --tasks gsm8k --limit 100` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: R1 accuracy 0 issue when all 2 all kernel is "naive" bug ### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1" --max-num-seqs 512 --data-parallel-size 8 --enable-expert...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ek-ai/DeepSeek-R1,num_concurrent=256" --tasks gsm8k --limit 100` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g ### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1" --max-num-seqs 512 --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.9 --port 9256 --disable-l...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
