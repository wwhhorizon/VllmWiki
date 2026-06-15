# vllm-project/vllm#17006: [Performance]: Distributed Inference w/ & w/o RDMA over Infiniband (tp=8, pp=2)

| 字段 | 值 |
| --- | --- |
| Issue | [#17006](https://github.com/vllm-project/vllm/issues/17006) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Distributed Inference w/ & w/o RDMA over Infiniband (tp=8, pp=2)

### Issue 正文摘录

### Description During distributed inference I didn't see a lot of performance improvement when using Infiniband vs. not using Infiniband. I have followed the recommendations by the project here on doing [distributed inference](https://docs.vllm.ai/en/latest/serving/distributed_serving.html). And when doing inference with IB enabled you can see vLLM logs like these ([source](https://github.com/surajssd/llm-k8s/blob/8a7fbb969b1edaa8ab40ee9c35dc3bba62c1a6d6/deepseek-v2.5/02_tp8_pp2_ib/lws.sh#L291-L294)): ```bash deepseek-v2-5-0:5969:5969 [0] NCCL INFO Channel 00/0 : 1[0] -> 0[0] [receive] via NET/IB/0/GDRDMA deepseek-v2-5-0:5969:5969 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [receive] via NET/IB/0/GDRDMA deepseek-v2-5-0:5969:5969 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[0] [send] via NET/IB/0/GDRDMA deepseek-v2-5-0:5969:5969 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [send] via NET/IB/0/GDRDMA ``` This blog on the vLLM website also has some benchmarks and it also does not show any significant improvements of using IB or not using IB: https://blog.vllm.ai/2024/07/23/llama31.html ### Report of performance regression Here are the performance results | Test name | GPU | # of req. | Tput (r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ly detected platform cuda. Collecting environment information... PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: rn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndasra100v4-series?tabs=sizebasic). These machines have 8 A100 GPUs each and are connected via Infiniband. I have deployed the GPU operator and network...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: mprovements of using IB or not using IB: https://blog.vllm.ai/2024/07/23/llama31.html ### Report of performance regression Here are the performance results | Test name | GPU | # of req. | Tput (req/s) | Output Tput (tok...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: project here on doing [distributed inference](https://docs.vllm.ai/en/latest/serving/distributed_serving.html). And when doing inference with IB enabled you can see vLLM logs like these ([source](https://github.com/sura...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ributed Inference w/ & w/o RDMA over Infiniband (tp=8, pp=2) performance;stale ### Description During distributed inference I didn't see a lot of performance improvement when using Infiniband vs. not using Infiniband. I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
