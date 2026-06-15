# vllm-project/vllm#7873: [Bug]: run failed on 8*H20

| 字段 | 值 |
| --- | --- |
| Issue | [#7873](https://github.com/vllm-project/vllm/issues/7873) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: run failed on 8*H20

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug llm = LLM(model=model_path, trust_remote_code=True, gpu_memory_utilization=0.9, tensor_parallel_size=args.tp, max_model_len=args.max_model_len, enforce_eager=True, disable_custom_all_reduce=True ) Detail: Traceback (most recent call last): File "/checkpoint/binary/train_package/infer.py", line 127, in llm = LLM(model=model_path, File "/root/.local/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 158, in __init__ self.llm_engine = LLMEngine.from_engine_args( File "/root/.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 445, in from_engine_args engine = cls( File "/root/.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 249, in __init__ self.model_executor = executor_class( File "/root/.local/lib/python3.10/site-packages/vllm/executor/distributed_gpu_executor.py", line 25, in __init__ super().__init__(*args, **kwargs) File "/root/.local/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 47, in __init__ self._init_executor() File "/root/.local/lib/python3.10/site-packages/vllm/executor/multiproc_gpu_executor.py", line 137, in _init_executor self._run_workers("init_devic...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: stale ### Your current environment ### 🐛 Describe the bug llm = LLM(model=model_path, trust_remote_code=True, gpu_memory_utilization=0.9, tensor_parallel_size=args.tp, max_model_len=args.max_model_len, enforce_eager=Tr
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nit_distributed_environment _WORLD = init_world_group(ranks, local_rank, backend) File "/root/.local/lib/python3.10/site-packages/vllm/distributed/parallel_state.py", line 754, in init_world_group return GroupCoordinato...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: th0 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: run failed on 8*H20 bug;stale ### Your current environment ### 🐛 Describe the bug llm = LLM(model=model_path, trust_remote_code=True, gpu_memory_utilization=0.9, tensor_parallel_size=args.tp,
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
