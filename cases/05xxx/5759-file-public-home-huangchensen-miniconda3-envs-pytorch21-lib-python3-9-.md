# vllm-project/vllm#5759:   File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/executor/ray_gpu_executor.py", line 324, in _run_workers     driver_worker_output = getattr(self.driver_worker,   File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/worker/worker.py", line 100, in init_device     init_distributed_environment(self.parallel_config, self.rank,   File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/worker/worker.py", line 287, in init_distributed_environment     pynccl_utils.init_process_group(   File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/model_executor/parallel_utils/pynccl_utils.py", line 46, in init_process_group     comm = NCCLCommunicator(init_method=init_method,   File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/model_executor/parallel_utils/pynccl.py", line 249, in __init__     assert result == 0 AssertionError

| 字段 | 值 |
| --- | --- |
| Issue | [#5759](https://github.com/vllm-project/vllm/issues/5759) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

>   File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/executor/ray_gpu_executor.py", line 324, in _run_workers     driver_worker_output = getattr(self.driver_worker,   File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/worker/worker.py", line 100, in init_device     init_distributed_environment(self.parallel_config, self.rank,   File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/worker/worker.py", line 287, in init_distributed_environment     pynccl_utils.init_process_group(   File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/model_executor/parallel_utils/pynccl_utils.py", line 46, in init_process_group     comm = NCCLCommunicator(init_method=init_method,   File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/model_executor/parallel_utils/pynccl.py", line 249, in __init__     assert result == 0 AssertionError

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: line 100, in init_device init_distributed_environment(self.parallel_config, self.rank, File "/public/home/huangchensen/miniconda3/envs/pytorch21/lib/python3.9/site-packages/vllm/worker/worker.py", line 287, in init_dist...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
