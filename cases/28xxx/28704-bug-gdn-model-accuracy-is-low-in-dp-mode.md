# vllm-project/vllm#28704: [Bug]: GDN model accuracy is low in DP mode

| 字段 | 值 |
| --- | --- |
| Issue | [#28704](https://github.com/vllm-project/vllm/issues/28704) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GDN model accuracy is low in DP mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve moonshotai/Kimi-Linear-48B-A3B-Instruct -tp 4 -dp 2 --trust-remote-code lm_eval --model local-completions --tasks gsm8k --model_args model=moonshotai/Kimi-Linear-48B-A3B-Instruct,base_url=http://0.0.0.0:8000/v1/completions,max_retries=3,tokenized_requests=False,timeout=1200,max_gen_toks=2048,max_length=8192 --batch_size 2048 --trust_remote_code ``` Note: qwen3-next has same issue. `--compilation_config.cudagraph_mode=FULL_AND_PIECEWISE` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.7301|± |0.0122| | | |strict-match | 5|exact_match|↑ |0.6914|± |0.0127| `PIECEWISE` or `NONE` or `--enforce-eager` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.8886|± |0.0087| | | |strict-match | 5|exact_match|↑ |0.8726|± |0.0092| ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right co...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: p 4 -dp 2 --trust-remote-code lm_eval --model local-completions --tasks gsm8k --model_args model=moonshotai/Kimi-Linear-48B-A3B-Instruct,base_url=http://0.0.0.0:8000/v1/completions,max_retries=3,tokenized_requests=False...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GDN model accuracy is low in DP mode bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve moonshotai/Kimi-Linear-48B-A3B-Instruct -tp 4 -dp 2 --trust-remote-code lm_eval --model local-comp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: GDN model accuracy is low in DP mode bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve moonshotai/Kimi-Linear-48B-A3B-Instruct -tp 4 -dp 2 --trust-remote-code lm_eval --model local-comp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: GDN model accuracy is low in DP mode bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve moonshotai/Kimi-Linear-48B-A3B-Instruct -tp 4 -dp 2 --trust-remote-code lm_eval --model local-comp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: GDN model accuracy is low in DP mode bug;stale ### Your current environment ### 🐛 Describe the bug ``` vllm serve moonshotai/Kimi-Linear-48B-A3B-Instruct -tp 4 -dp 2 --trust-remote-code lm_eval --model local-comp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
