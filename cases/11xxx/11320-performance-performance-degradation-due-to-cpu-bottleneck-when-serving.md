# vllm-project/vllm#11320: [Performance]: Performance degradation due to CPU bottleneck when serving embedding models to GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#11320](https://github.com/vllm-project/vllm/issues/11320) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Performance degradation due to CPU bottleneck when serving embedding models to GPUs

### Issue 正文摘录

### Proposal to improve performance When you serve your Embedding model to the GPU and load it up, you hit a throughput bottleneck due to CPU bottlenecks. Here are the arguments we set up to serve the model. ``` - --model - /data/models/bge-m3-embed-beta1 - --load-format - "auto" - --dtype - "float16" - --max-num-batched-tokens - "131072" - --tokenizer-pool-size - "4" ``` We increased the number of users by 1 every 10 seconds, with each user sending a request to /v1/embeddings once every 0.5 seconds. (Number of prompt tokens: 3K) In our tests, the throughput increased up to 12TPS, and then did not increase after that. It is not clear what the cause is, but the CPU utilization of the python process reaches 100% when the bottleneck is reached. ![image](https://github.com/user-attachments/assets/83497680-7148-46b5-9ec3-027b1c57b639) ``` top - 21:52:19 up 23 days, 20:08, 0 users, load average: 2.05, 2.53, 2.57 Tasks: 5 total, 3 running, 2 sleeping, 0 stopped, 0 zombie %Cpu(s): 1.6 us, 0.2 sy, 0.0 ni, 98.2 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st MiB Mem : 2063755.+total, 1418614.+free, 59389.1 used, 585751.8 buff/cache MiB Swap: 0.0 total, 0.0 free, 0.0 used. 1987294.+avail Mem PID USER PR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: it is necessary) ```text Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e]: Performance degradation due to CPU bottleneck when serving embedding models to GPUs performance;stale ### Proposal to improve performance When you serve your Embedding model to the GPU and load it up, you hit a thro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: When you serve your Embedding model to the GPU and load it up, you hit a throughput bottleneck due to CPU bottlenecks. Here are the arguments we set up to serve the model. ``` - --model - /data/models/bge-m3-embed-beta1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: models/bge-m3-embed-beta1 - --load-format - "auto" - --dtype - "float16" - --max-num-batched-tokens - "131072" - --tokenizer-pool-size - "4" ``` We increased the number of users by 1 every 10 seconds, with each user sen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
