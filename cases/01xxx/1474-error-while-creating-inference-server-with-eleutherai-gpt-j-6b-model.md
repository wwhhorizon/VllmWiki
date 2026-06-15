# vllm-project/vllm#1474: Error while creating inference server with EleutherAI/gpt-j-6b model.

| 字段 | 值 |
| --- | --- |
| Issue | [#1474](https://github.com/vllm-project/vllm/issues/1474) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error while creating inference server with EleutherAI/gpt-j-6b model.

### Issue 正文摘录

I am trying to run GPTj-6b on an instance with 8 L4 GPU getting the below error. Using version 0.2. but tried with latest as well. python -m vllm.entrypoints.api_server --model EleutherAI/gpt-j-6b --tensor-parallel-size 8 --dtype float16 --host 0.0.0.0 --port 8000 --gpu-memory-utilization 0.95 File "/opt/conda/envs/myenv/lib/python3.8/site-packages/ray/_private/auto_init_hook.py", line 24, in auto_init_wrapper return fn(args, **kwargs) File "/opt/conda/envs/myenv/lib/python3.8/site-packages/ray/_private/client_mode_hook.py", line 103, in wrapper return func(args, kwargs) File "/opt/conda/envs/myenv/lib/python3.8/site-packages/ray/_private/worker.py", line 2547, in get raise value.as_instanceof_cause() ray.exceptions.RayTaskError(AssertionError): ray::RayWorker.execute_method() (pid=17501, ip=10.138.15.207, actor_id=6393f8b00b5b463275043b0b01000000, repr= ) File "/opt/conda/envs/myenv/lib/python3.8/site-packages/vllm/engine/ray_utils.py", line 32, in execute_method return executor(*args, kwargs) File "/opt/conda/envs/myenv/lib/python3.8/site-packages/vllm/worker/worker.py", line 68, in init_model self.model = get_model(self.model_config) File "/opt/conda/envs/myenv/lib/python3.8/si...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_server --model EleutherAI/gpt-j-6b --tensor-parallel-size 8 --dtype float16 --host 0.0.0.0 --port 8000 --gpu-memory-utilization 0.95 File "/opt/conda/envs/myenv/lib/python3.8/site-packages/ray/_private/auto_init_hook....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Error while creating inference server with EleutherAI/gpt-j-6b model. I am trying to run GPTj-6b on an instance with 8 L4 GPU getting the below error. Using version 0.2. but tried with latest as well. python -m vllm.ent...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: run GPTj-6b on an instance with 8 L4 GPU getting the below error. Using version 0.2. but tried with latest as well. python -m vllm.entrypoints.api_server --model EleutherAI/gpt-j-6b --tensor-parallel-size 8 --dtype floa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: th 8 L4 GPU getting the below error. Using version 0.2. but tried with latest as well. python -m vllm.entrypoints.api_server --model EleutherAI/gpt-j-6b --tensor-parallel-size 8 --dtype float16 --host 0.0.0.0 --port 800...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
