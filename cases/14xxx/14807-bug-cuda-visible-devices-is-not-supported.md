# vllm-project/vllm#14807: [Bug]: CUDA_VISIBLE_DEVICES is not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#14807](https://github.com/vllm-project/vllm/issues/14807) |
| 状态 | closed |
| 标签 | bug;documentation;ray |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CUDA_VISIBLE_DEVICES is not supported

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It seems the executor will always select GPU 0,1,2,3... as the devices of ray workers. And this makes it impossible for user to assgin devices using `export CUDA_VISIBLE_DEVICES=2,3` or `os.environ["CUDA_VISIBLE_DEVICES"] = "2,3"`. The bug could come with the below code: worker_node_and_gpu_ids = [] for worker in [self.driver_dummy_worker] + self.workers: if worker is None: # driver_dummy_worker can be None when using ray spmd worker. continue worker_node_and_gpu_ids.append( ray.get(worker.get_node_and_gpu_ids.remote()) \ ) # type: ignore for i, (node_id, gpu_ids) in enumerate(worker_node_and_gpu_ids): node_workers[node_id].append(i) # `gpu_ids` can be a list of strings or integers. # convert them to integers for consistency. # NOTE: gpu_ids can be larger than 9 (e.g. 16 GPUs), # string sorting is not sufficient. # see https://github.com/vllm-project/vllm/issues/5590 gpu_ids = [int(x) for x in gpu_ids] node_gpus[node_id].extend(gpu_ids) for node_id, gpu_ids in node_gpus.items(): node_gpus[node_id] = sorted(gpu_ids) # Set environment variables for the driver and workers. all_args_to_update_environment_variables = [{ current_platfo...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA_VISIBLE_DEVICES is not supported bug;documentation;ray ### Your current environment ### 🐛 Describe the bug It seems the executor will always select GPU 0,1,2,3... as the devices of ray workers. And this make...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e larger than 9 (e.g. 16 GPUs), # string sorting is not sufficient. # see https://github.com/vllm-project/vllm/issues/5590 gpu_ids = [int(x) for x in gpu_ids] node_gpus[node_id].extend(gpu_ids) for node_id, gpu_ids in n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
