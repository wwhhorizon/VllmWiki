# vllm-project/vllm#22454: [Bug]: Low time to first token of prefill and decode instances but high TTFT with 1p1d

| 字段 | 值 |
| --- | --- |
| Issue | [#22454](https://github.com/vllm-project/vllm/issues/22454) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Low time to first token of prefill and decode instances but high TTFT with 1p1d

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am testing the performance of 1p1d PD disaggregation for the `DeepSeek-R1-Distill-Qwen-7B` model using `NIXLConnector`. In a scenario with isl=5000, osl=2000, and qps=1.5, I observed unusually long TTFT. To identify which instance reached the bottleneck, I intended to monitor the metrics. However, both the prefill and decode instances showed very short time to first token values. Below are the specific metrics: Prefill instance metrics: ``` ... vllm:time_to_first_token_seconds_count{engine="0",model_name="/home/hadoop-dpsr/dolphinfs_hdd_hadoop-dpsr/dongyanchu/data/huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"} 501.0 vllm:time_to_first_token_seconds_sum{engine="0",model_name="/home/hadoop-dpsr/dolphinfs_hdd_hadoop-dpsr/dongyanchu/data/huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"} 245.34050130844116 ... vllm:request_queue_time_seconds_count{engine="0",model_name="/home/hadoop-dpsr/dolphinfs_hdd_hadoop-dpsr/dongyanchu/data/huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"} 501.0 vllm:request_queue_time_seconds_sum{engine="0",model_name="/home/hadoop-dpsr/dolphinfs_hdd_hadoop-dpsr/dongyanchu/data/huggingf...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: g the performance of 1p1d PD disaggregation for the `DeepSeek-R1-Distill-Qwen-7B` model using `NIXLConnector`. In a scenario with isl=5000, osl=2000, and qps=1.5, I observed unusually long TTFT. To identify which instan...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Low time to first token of prefill and decode instances but high TTFT with 1p1d bug;stale ### Your current environment ### 🐛 Describe the bug I am testing the performance of 1p1d PD disaggregation for the `DeepSe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: _TP_SIZE=${DECODER_TP_SIZE:-1} # Find the git repository root directory SMI_BIN=$(which nvidia-smi || which rocm-smi) # Trap the SIGINT signal (triggered by Ctrl+C) trap 'kill $(jobs -pr)' SIGINT SIGTERM EXIT # Waits fo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: instances showed very short time to first token values. Below are the specific metrics: Prefill instance metrics: ``` ... vllm:time_to_first_token_seconds_count{engine="0",model_name="/home/hadoop-dpsr/dolphinfs_hdd_had...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: bug;stale ### Your current environment ### 🐛 Describe the bug I am testing the performance of 1p1d PD disaggregation for the `DeepSeek-R1-Distill-Qwen-7B` model using `NIXLConnector`. In a scenario with isl=5000, osl=20...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
