# vllm-project/vllm#738: does cpu memory have to be greater than model size when using distributed inference?

| 字段 | 值 |
| --- | --- |
| Issue | [#738](https://github.com/vllm-project/vllm/issues/738) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> does cpu memory have to be greater than model size when using distributed inference?

### Issue 正文摘录

I have 2 hosts each has cpu memory 16G and gpu memory 24G, when I tried to load vicuna-13b, it get OOM, here's the error message: ``` (raylet, ip=10.0.6.140) [2023-08-11 10:13:54,613 E 30 30] (raylet) node_manager.cc:3084: 1 Workers (tasks / actors) killed due to memory pressure (OOM), 0 Workers crashed due to other reasons at node (ID: 73fcbc20ed501941efd210b9f60a78dbec0cf0f75fec41d65f19b505, IP: 10.0.6.140) over the last time period. To see more information about the Workers killed on this node, use `ray logs raylet.out -ip 10.0.6.140` (raylet, ip=10.0.6.140) (raylet, ip=10.0.6.140) Refer to the documentation on how to address the out of memory issue: https://docs.ray.io/en/latest/ray-core/scheduling/ray-oom-prevention.html. Consider provisioning more memory on this node or reducing task parallelism by requesting more CPUs per task. To adjust the kill threshold, set the environment variable `RAY_memory_usage_threshold` when starting Ray. To disable worker killing, set the environment variable `RAY_memory_monitor_refresh_ms` to zero. Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, F...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: does cpu memory have to be greater than model size when using distributed inference? I have 2 hosts each has cpu memory 16G and gpu memory 24G, when I tried to load vicuna-13b, it get OOM, here's the error message: ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: er='lmsys/vicuna-13b-v1.3', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=2, seed=0) ``` does each host's cpu me...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: using distributed inference? I have 2 hosts each has cpu memory 16G and gpu memory 24G, when I tried to load vicuna-13b, it get OOM, here's the error message: ``` (raylet, ip=10.0.6.140) [2023-08-11 10:13:54,613 E 30 30...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: m-prevention.html. Consider provisioning more memory on this node or reducing task parallelism by requesting more CPUs per task. To adjust the kill threshold, set the environment variable `RAY_memory_usage_threshold` wh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Consider provisioning more memory on this node or reducing task parallelism by requesting more CPUs per task. To adjust the kill threshold, set the environment variable `RAY_memory_usage_threshold` when starting Ray. To...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
