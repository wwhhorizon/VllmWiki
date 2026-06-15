# vllm-project/vllm#13610: [Performance]:  TTFT Spikes When QPS Increases During DeepSeek-R1 Testing with TP8 and PP2

| 字段 | 值 |
| --- | --- |
| Issue | [#13610](https://github.com/vllm-project/vllm/issues/13610) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]:  TTFT Spikes When QPS Increases During DeepSeek-R1 Testing with TP8 and PP2

### Issue 正文摘录

### Proposal to improve performance When testing the DeepSeek-R1 model with a configuration of **2 nodes (each with 8 H20 GPUs)** using **TP8 and PP2**, I observed that the **Time To First Token (TTFT) suddenly increased** as the Queries Per Second (QPS) grew. This behavior is unexpected and impacts the performance of the system. The TTFT should remain stable or increase gradually as QPS increases, without sudden spikes. Environment: - Hardware: 2 nodes, each with 8 NVIDIA H20 GPUs. - Model: DeepSeek-R1. - Configuration: TP8 (Tensor Parallelism) and PP2 (Pipeline Parallelism). - docker: docker.io/vllm/vllm-openai:v0.7.2 ### Report of performance regression The following is the result of my test. QPS | TTFT-mean (ms) | -- | -- | 8 | 504.33 | 16 | 5668.94 | 32 | 10628.59 | ### Misc discussion on performance The following is the script I used for testing and launching ``` python3 benchmark_serving.py \ --model /root/.cache/huggingface/models/DeepSeek-R1 \ --dataset-name random \ --random-input-len 1000 \ --random-output-len 1000 \ --num-prompts 256 \ --request-rate ``` ``` vllm serve /root/.cache/huggingface/models/DeepSeek-R1 --tensor-parallel-size 8 --pipeline-parallel-size 2 --tru...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: onfiguration: TP8 (Tensor Parallelism) and PP2 (Pipeline Parallelism). - docker: docker.io/vllm/vllm-openai:v0.7.2 ### Report of performance regression The following is the result of my test. QPS | TTFT-mean (ms) | -- |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: IA H20 GPUs. - Model: DeepSeek-R1. - Configuration: TP8 (Tensor Parallelism) and PP2 (Pipeline Parallelism). - docker: docker.io/vllm/vllm-openai:v0.7.2 ### Report of performance regression The following is the result o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ;stale ### Proposal to improve performance When testing the DeepSeek-R1 model with a configuration of **2 nodes (each with 8 H20 GPUs)** using **TP8 and PP2**, I observed that the **Time To First Token (TTFT) suddenly i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: en QPS Increases During DeepSeek-R1 Testing with TP8 and PP2 performance;stale ### Proposal to improve performance When testing the DeepSeek-R1 model with a configuration of **2 nodes (each with 8 H20 GPUs)** using **TP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: TTFT Spikes When QPS Increases During DeepSeek-R1 Testing with TP8 and PP2 performance;stale ### Proposal to improve performance When testing the DeepSeek-R1 model with a configuration of **2 nodes (each...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
