# vllm-project/vllm#18263: Performance Regression with p2p Mode

| 字段 | 值 |
| --- | --- |
| Issue | [#18263](https://github.com/vllm-project/vllm/issues/18263) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Performance Regression with p2p Mode

### Issue 正文摘录

### Your current environment I have 8 * 7900xtx cards in my environment. I want to see the performance improvements from P2P mode in vllm. Before I run the vllm tests, I test the RCCL add reduce performance between the enable p2p mode and disable p2p mode by using ``` export NCCL_P2P_DISABLE=0 and export NCCL_P2P_DISABLE=1```. Here is the data ![Image](https://github.com/user-attachments/assets/6c851ff4-14fe-40fe-996b-efea185c913e) and ![Image](https://github.com/user-attachments/assets/a8911d8f-27c2-47ba-a028-7cc78f714923) We can see the significant performance improvements from the p2p mode like the table. But why there is no performance improvements from VLLM? Here is the command line I used: ``` NCCL_P2P_DISABLE=0 \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ VLLM_MLA_DISABLE=1 \ vllm serve /app/model \ --block-size 16 \ --dtype bfloat16 \ --enable-chunked-prefill \ --gpu-memory-utilization 1 \ --max-model-len 4096 \ --tensor-parallel-size 8 \ --trust-remote-code \ --use-v2-block-manager \ --disable-log-requests \ --disable-log-stats \ --max-num-seqs 384 \ --max-num-batched-tokens 8192 \ --enable-prefix-caching Client command: NCCL_P2P_DISABLE=0 \ python vllm/benchmarks/benchmark_ser...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: A_DISABLE=1 \ vllm serve /app/model \ --block-size 16 \ --dtype bfloat16 \ --enable-chunked-prefill \ --gpu-memory-utilization 1 \ --max-model-len 4096 \ --tensor-parallel-size 8 \ --trust-remote-code \ --use-v2-block-m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Performance Regression with p2p Mode usage;stale ### Your current environment I have 8 * 7900xtx cards in my environment. I want to see the performance improvements from P2P mode in vllm. Before I run the vllm tests, I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Performance Regression with p2p Mode usage;stale ### Your current environment I have 8 * 7900xtx cards in my environment. I want to see the performance improvements from P2P mode in vllm. Before I run the vllm tests, I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: NCCL_P2P_DISABLE=0 \ python vllm/benchmarks/benchmark_serving.py \ --backend vllm \ --dataset-name sharegpt \ --dataset-path /app/ShareGPT_V3_unfiltered_cleaned_split.json \ --model /app/model \ --num-prompts 1000 \ --r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
