# vllm-project/vllm#2132: Unable to run ehartford/dolphin-2.5-mixtral-8x7b

| 字段 | 值 |
| --- | --- |
| Issue | [#2132](https://github.com/vllm-project/vllm/issues/2132) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Unable to run ehartford/dolphin-2.5-mixtral-8x7b

### Issue 正文摘录

Model: https://huggingface.co/ehartford/dolphin-2.5-mixtral-8x7b VLLM version: 0.2.5 Run method: API server endpoint inside a custom docker container (RHEL) Hardware: 4x A100 40GB Cuda version: 12.0 When I try to run it, it states it cannot find any weights. ``` RuntimeError: Cannot find any model weights with `/home/ndurkee/dolphin-2.5-mixtral-8x7b` (RayWorkerVllm pid=2530) /usr/local/lib/python3.8/dist-packages/torch/nn/init.py:412: UserWarning: Initializing zero-element tensors is a no-op [repeated 3x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/ray-logging.html#log-deduplication for more options.) (RayWorkerVllm pid=2530) warnings.warn("Initializing zero-element tensors is a no-op") [repeated 3x across cluster] ``` **What I've tested** I did test mistralai/Mixtral-8x7B-Instruct-v0.1 and that does work on my system. It seems to have something to do with the model. Note that I did still get a warning "_Initializing zero-element tensors is a no-op_" but the model still seems to work fine. Other people have stated that this model works with their setups which indicates t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 7b Model: https://huggingface.co/ehartford/dolphin-2.5-mixtral-8x7b VLLM version: 0.2.5 Run method: API server endpoint inside a custom docker container (RHEL) Hardware: 4x A100 40GB Cuda version: 12.0 When I try to run...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: API server endpoint inside a custom docker container (RHEL) Hardware: 4x A100 40GB Cuda version: 12.0 When I try to run it, it states it cannot find any weights. ``` RuntimeError: Cannot find any model weights with `/ho...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Unable to run ehartford/dolphin-2.5-mixtral-8x7b Model: https://huggingface.co/ehartford/dolphin-2.5-mixtral-8x7b VLLM version: 0.2.5 Run method: API server endpoint inside a custom docker container (RHEL) Hardware: 4x...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ement tensors is a no-op") [repeated 3x across cluster] ``` **What I've tested** I did test mistralai/Mixtral-8x7B-Instruct-v0.1 and that does work on my system. It seems to have something to do with the model. Note tha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
