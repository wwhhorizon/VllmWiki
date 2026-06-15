# vllm-project/vllm#6207: c4ai-command-r-plus on 16GPUs 

| 字段 | 值 |
| --- | --- |
| Issue | [#6207](https://github.com/vllm-project/vllm/issues/6207) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> c4ai-command-r-plus on 16GPUs 

### Issue 正文摘录

### Your current environment vllm==0.4.3 numpy==1.26.4 nvidia-nccl-cu12==2.20.5 torch==2.3.0 transformers==4.41.2 triton==2.3.0 ### 🐛 Describe the bug I don't know if this is a bug or if the model just doesn't support this setup. I'm trying to run two machines with 16 L4 GPUs in total and I get this error: ``` [rank0]: ray.exceptions.RayTaskError(RuntimeError): ray::RayWorkerWrapper.execute_method() (pid=10005, ip=10.10.10.171, actor_id=92f69d368cc5f16efeca171f01000000, repr= ) [rank0]: File "/secondary/thies/.virtualenvs/vllm/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 149, in execute_method [rank0]: raise e [rank0]: File "/secondary/thies/.virtualenvs/vllm/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 140, in execute_method [rank0]: return executor(*args, **kwargs) [rank0]: File "/secondary/thies/.virtualenvs/vllm/lib/python3.10/site-packages/vllm/worker/worker.py", line 121, in load_model [rank0]: self.model_runner.load_model() [rank0]: File "/secondary/thies/.virtualenvs/vllm/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 134, in load_model [rank0]: self.model = get_model( [rank0]: File "/secondary/thies/.virtualenvs/vllm/li...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ==2.3.0 ### 🐛 Describe the bug I don't know if this is a bug or if the model just doesn't support this setup. I'm trying to run two machines with 16 L4 GPUs in total and I get this error: ``` [rank0]: ray.exceptions.Ray...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: numpy==1.26.4 nvidia-nccl-cu12==2.20.5 torch==2.3.0 transformers==4.41.2 triton==2.3.0 ### 🐛 Describe the bug I don't know if this is a bug or if the model just doesn't support this setup. I'm trying to run two machines...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: size (8). ``` development distributed_parallel;model_support triton env_dependency;shape Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: c4ai-command-r-plus on 16GPUs bug;stale ### Your current environment vllm==0.4.3 numpy==1.26.4 nvidia-nccl-cu12==2.20.5 torch==2.3.0 transformers==4.41.2 triton==2.3.0 ### 🐛 Describe the bug I don't know if this is a bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
