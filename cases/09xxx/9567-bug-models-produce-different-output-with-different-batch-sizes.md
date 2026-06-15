# vllm-project/vllm#9567: [Bug]: Models produce different output with different batch sizes

| 字段 | 值 |
| --- | --- |
| Issue | [#9567](https://github.com/vllm-project/vllm/issues/9567) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Models produce different output with different batch sizes

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When the `nm-testing/Meta-Llama-3-8B-Instruct-W8-Channel-A8-Dynamic-Per-Token-Test` model runs requests with temperature=0, the output changes depending on how the scheduler batches the requests. This seems to be the reason the lm-eval tests get different scores as the size of the KV cache is changed. Slack thread for more context: https://vllm-dev.slack.com/archives/C07R5PAL2L9/p1729409919734939 Here's a small repro script that uses `--max-num-seqs` to force different batch sizes: And the input data for that: [request_data_small.json](https://github.com/user-attachments/files/17468017/request_data_small.json) On my A100 machine this produces a diff like so: ``` Diff in output 1: --- +++ @@ -1,6 +1,6 @@ - There are 240 - 80 = >160 Chinese people. -There are 60 boys on the Chinese team, so there are 160 - 60 = >100 girls on the Chinese team. + There are 240 - 80 = >160 Chinese. +There are 60 boys, so there are 160 - 60 = >100 girls. #### 100 -Question: A bakery sells 250 loaves of bread per day. They sell 1/5 of their loaves to a local restaurant. How many loaves of bread does the bakery sell to...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: e is changed. Slack thread for more context: https://vllm-dev.slack.com/archives/C07R5PAL2L9/p1729409919734939 Here's a small repro script that uses `--max-num-seqs` to force different batch sizes: And the input data fo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: eta-Llama-3-8B-Instruct-W8-Channel-A8-Dynamic-Per-Token-Test` model runs requests with temperature=0, the output changes depending on how the scheduler batches the requests. This seems to be the reason the lm-eval tests...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cache...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Models produce different output with different batch sizes bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When the `nm-testing/Meta-Llama-3-8B-Instruct-W8-Channel-A8-Dy
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: # Model Input Dumps _No response_ ### 🐛 Describe the bug When the `nm-testing/Meta-Llama-3-8B-Instruct-W8-Channel-A8-Dynamic-Per-Token-Test` model runs requests with temperature=0, the output changes depending on how th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
