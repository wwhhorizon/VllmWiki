# vllm-project/vllm#23282: [Bug]: Accuracy issue for R1 DP8 on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#23282](https://github.com/vllm-project/vllm/issues/23282) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support;moe |
| 子分类 | race_cond |
| Operator 关键词 | cuda;moe |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Accuracy issue for R1 DP8 on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1-0528" --max-num-seqs 512 --trust-remote-code --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.75 --port 9256 --disable-log-requests --no-enable-prefix-caching -O '{"full_cuda_graph": true}' --cuda-graph-sizes 16 32 48 64 96 128 160 192 256 512` Something crashed on main now `lm_eval --model local-completions --model_args "base_url=http://127.0.0.1:9256/v1/completions,model=deepseek-ai/DeepSeek-R1-0528,num_concurrent=256" --tasks gsm8k --limit 200` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.005|± | 0.005| | | |strict-match | 5|exact_match|↑ |0.000|± | 0.000| ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Accuracy issue for R1 DP8 on B200 bug ### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1-0528" --max-num-seqs 512 --trust-remote-code --data-parallel-size 8 --enable-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Accuracy issue for R1 DP8 on B200 bug ### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1-0528" --max-num-seqs 512 --trust-remote-code --data-parallel-size 8 --enable-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: i/DeepSeek-R1-0528,num_concurrent=256" --tasks gsm8k --limit 200` |Tasks|Version| Filter |n-shot| Metric | |Value| |Stderr| |-----|------:|----------------|-----:|-----------|---|----:|---|-----:| |gsm8k| 3|flexible-ext...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: " --max-num-seqs 512 --trust-remote-code --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.75 --port 9256 --disable-log-requests --no-enable-prefix-caching -O '{"full_cuda_graph": true}' --cuda-...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Accuracy issue for R1 DP8 on B200 bug ### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1-0528" --max-num-seqs 512 --trust-remote-code --data-parallel-size 8 --enable-...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
