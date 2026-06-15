# vllm-project/vllm#1116: Cannot use LLama-70b with multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#1116](https://github.com/vllm-project/vllm/issues/1116) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Cannot use LLama-70b with multiple GPUs

### Issue 正文摘录

Hi there, I failed to use LLama-70b on an 8-A100 machine. The script I use is `model = LLM(model=script_args.model_name, tensor_parallel_size=2)` The error is ``` 2023-09-20 18:06:25,855 WARNING services.py:1889 -- WARNING: The object store is using /tmp instead of /dev/shm because /dev/shm has only 67108864 bytes available. This will harm performance! You may be able to free up space by deleting files in /dev/shm. If you are inside a Docker container, you can increase /dev/shm size by passing '--shm-size=10.24gb' to 'docker run' (or add it to the run_options list in a Ray cluster config). Make sure to set this to more than 30% of available RAM. 2023-09-20 18:06:26,013 INFO worker.py:1642 -- Started a local Ray instance. Traceback (most recent call last): File "vllm_rank_model_id.py", line 124, in model = LLM(model=script_args.model_name, tensor_parallel_size=1) File "/opt/conda/envs/vllm/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line 66, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/opt/conda/envs/vllm/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 220, in from_engine_args distributed_init_method, placement_group = initiali...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Cannot use LLama-70b with multiple GPUs Hi there, I failed to use LLama-70b on an 8-A100 machine. The script I use is `model = LLM(model=script_args.model_name, tensor_parallel_size=2)` The error is ``` 2023-09-20 18:06...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: able to free up space by deleting files in /dev/shm. If you are inside a Docker container, you can increase /dev/shm size by passing '--shm-size=10.24gb' to 'docker run' (or add it to the run_options list in a Ray clust...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Lama-70b with multiple GPUs Hi there, I failed to use LLama-70b on an 8-A100 machine. The script I use is `model = LLM(model=script_args.model_name, tensor_parallel_size=2)` The error is ``` 2023-09-20 18:06:25,855 WARN...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
