# vllm-project/vllm#2406: Multi-node serving with vLLM - Problems with Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#2406](https://github.com/vllm-project/vllm/issues/2406) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Multi-node serving with vLLM - Problems with Ray

### Issue 正文摘录

I am trying to run a distributed (multi-node) inference server with vLLM using ray, but I keep getting the following ValueError: `Ray does not allocate any GPUs on the driver node. Consider adjusting the Ray placement group or running the driver on a GPU node.` I'm not sure how exactly to resolve this. I suspect the issue is with this script https://github.com/vllm-project/vllm/blob/main/vllm/engine/ray_utils.py, especially when a `ray_address` is passed. Is there a specific ray_address arg that gets passed during the ray.init() stage? More specifically, it seems like this error is raised because of the `driver_dummy_worker` in line 182 of https://github.com/vllm-project/vllm/blob/main/vllm/engine/llm_engine.py. I'm confused what's going on with this piece of code ``` def _init_workers_ray(self, placement_group: "PlacementGroup", **ray_remote_kwargs): if self.parallel_config.tensor_parallel_size == 1: num_gpus = self.cache_config.gpu_memory_utilization else: num_gpus = 1 self.driver_dummy_worker: RayWorkerVllm = None self.workers: List[RayWorkerVllm] = [] driver_ip = get_ip() for bundle_id, bundle in enumerate(placement_group.bundle_specs): if not bundle.get("GPU", 0): continue sc...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: **ray_remote_kwargs): if self.parallel_config.tensor_parallel_size == 1: num_gpus = self.cache_config.gpu_memory_utilization else: num_gpus = 1 self.driver_dummy_worker: RayWorkerVllm = None self.workers: List[
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s://github.com/vllm-project/vllm/blob/main/vllm/engine/ray_utils.py, especially when a `ray_address` is passed. Is there a specific ray_address arg that gets passed during the ray.init() stage? More specifically, it see...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: num_gpus = self.cache_config.gpu_memory_utilization else: num_gpus = 1 self.driver_dummy_worker: RayWorkerVllm = None self.workers: List[RayWorkerVllm] = [] driver_ip = get_ip() for bundle_id, bundle in enumerate(placem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
