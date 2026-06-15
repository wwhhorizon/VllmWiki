# vllm-project/vllm#12258: [Usage]: deepseek v3 can not set tensor_parallel_size=16 and pipeline-parallel-size=2 on L20 #12256 Open

| 字段 | 值 |
| --- | --- |
| Issue | [#12258](https://github.com/vllm-project/vllm/issues/12258) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: deepseek v3 can not set tensor_parallel_size=16 and pipeline-parallel-size=2 on L20 #12256 Open

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` (RayWorkerWrapper pid=5057, ip=10.121.129.5) Cache shape torch.Size([163840, 64]) [repeated 30x across cluster] (RayWorkerWrapper pid=5849, ip=10.121.129.12) INFO 01-21 00:46:19 model_runner.py:1099] Loading model weights took 18.9152 GB [repeated 7x across cluster] (RayWorkerWrapper pid=5148, ip=10.121.129.13) INFO 01-21 00:46:25 model_runner.py:1099] Loading model weights took 21.4118 GB [repeated 8x across cluster] (RayWorkerWrapper pid=5050, ip=10.121.129.5) INFO 01-21 00:47:24 model_runner.py:1099] Loading model weights took 21.4118 GB [repeated 8x across cluster] (RayWorkerWrapper pid=5054, ip=10.121.129.5) WARNING 01-21 00:47:31 fused_moe.py:374] Using default MoE config. Performance might be sub-optimal! Config file not found at /usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/configs/E=256,N=128,device_name=NVIDIA_L20,dtype=fp8_w8a8.json (RayWorkerWrapper pid=5053, ip=10.121.129.5) INFO 01-21 00:47:24 model_runner.py:1099] Loading model weights took 21.4118 GB [repeated 7x across cluster] WARNING 01-21 00:47:34 fused_moe.py:374] Using default MoE config. Performance...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: r] ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: del_executor/layers/fused_moe/configs/E=256,N=128,device_name=NVIDIA_L20,dtype=fp8_w8a8.json (RayWorkerWrapper pid=5053, ip=10.121.129.5) INFO 01-21 00:47:24 model_runner.py:1099] Loading model weights took 21.4118 GB [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uster] (RayWorkerWrapper pid=5849, ip=10.121.129.12) INFO 01-21 00:46:19 model_runner.py:1099] Loading model weights took 18.9152 GB [repeated 7x across cluster] (RayWorkerWrapper pid=5148, ip=10.121.129.13) INFO 01-21...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: er pid=5146, ip=10.121.129.13) INFO 01-21 00:47:39 worker.py:241] Memory profiling takes 14.78 seconds (RayWorkerWrapper pid=5146, ip=10.121.129.13) INFO 01-21 00:47:39 worker.py:241] the current vLLM instance can use t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
