# vllm-project/vllm#10062: [Performance]: Throughput and Latency degradation with a  single LoRA adapter on A100 40 GB

| 字段 | 值 |
| --- | --- |
| Issue | [#10062](https://github.com/vllm-project/vllm/issues/10062) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Throughput and Latency degradation with a  single LoRA adapter on A100 40 GB

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance --- **Setup Summary for vLLM Benchmarking with Llama-2 Model:** - **Hardware**: A100 40 GB (a2-highgpu-2g) on Google Kubernetes Engine (GKE) - **Model**: `meta-llama/Llama-2-7b-hf` - **GPU Count**: 1 - **Experiments**: - **Experiment 1**: Requests using the base model `meta-llama/Llama-2-7b-hf`. - **Experiment 2**: vLLM deployed with LoRA adapter `vineetsharma/qlora-adapter-Llama-2-7b-hf-TweetSumm` (size 160 MB). - **Experiment 3**: vLLM deployed with LoRA adapter `xtuner/Llama-2-7b-qlora-moss-003-sft` (size 640 MB). For all three experiments, we used the same input prompt (ShareGPT) and observed a similar output length. **Settings**: - **Eager Mode**: Not enabled. - **Max GPU Utilization**: Default at 90%. **Benchmark Metrics**: We measured: - **Latency per output token** - **Throughput** (output tokens per second) You can view detailed results in the benchmark document: [Benchmark 1 server - Sheet7.pdf](https://github.com/user-attachments/files/17640153/Benchmark.1.server.-.Sheet7.pdf). --- **Observations and Questions**: - Using LoRA adapters l...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Performance]: Throughput and Latency degradation with a single LoRA adapter on A100 40 GB performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: scussion on performance --- **Setup Summary for vLLM Benchmarking with Llama-2 Model:** - **Hardware**: A100 40 GB (a2-highgpu-2g) on Google Kubernetes Engine (GKE) - **Model**: `meta-llama/Llama-2-7b-hf` - **GPU Count*...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: atency degradation with a single LoRA adapter on A100 40 GB performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance --- *...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ble degradation in throughput and latency compared to the base model. Specifically, we observed up to a 50% drop in maximum throughput with LoRA compared to the base model. - **Is this performance degradation expected w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ance]: Throughput and Latency degradation with a single LoRA adapter on A100 40 GB performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
