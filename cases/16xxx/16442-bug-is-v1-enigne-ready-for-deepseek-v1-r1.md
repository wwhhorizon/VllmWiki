# vllm-project/vllm#16442: [Bug]:  Is V1 Enigne ready for DeepSeek-V1/R1 ?

| 字段 | 值 |
| --- | --- |
| Issue | [#16442](https://github.com/vllm-project/vllm/issues/16442) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Is V1 Enigne ready for DeepSeek-V1/R1 ?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```text I use [ v-0.8.3 ](vllm-openai:v0.8.3) image to serve deepseek r1,but get error ``` ```bash 2025-04-11 09:26:35,124 ERROR worker.py:422 -- Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): [36mray::RayWorkerWrapper.__ray_call__()[39m (pid=251, ip=172.20.146.77, actor_id=3e6c34fbceeee21342996d1901000000, repr= ) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/ray/actor.py", line 1722, in __ray_call__ return fn(self, *args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/ray/experimental/channel/torch_tensor_nccl_channel.py", line 658, in _do_init_communicator ctx.communicators[group_id] = _NcclGroup( ^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/ray/experimental/channel/nccl_group.py", line 103, in __init__ from ray.air._internal import torch_utils File "/usr/local/lib/python3.12/dist-packages/ray/air/__init__.py", line 1, in from ray.air.config import ( File "/usr/local/lib/python3.12/dist-packages/ray/air/config.py", line 17, in import pyarrow.fs ModuleNotFoundError: No module named 'pyarrow' ```...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: channel/nccl_group.py", line 103, in __init__ from ray.air._internal import torch_utils File "/usr/local/lib/python3.12/dist-packages/ray/air/__init__.py", line 1, in from ray.air.config import ( File "/usr/local/lib/py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on3.12/dist-packages/ray/air/__init__.py", line 1, in from ray.air.config import ( File "/usr/local/lib/python3.12/dist-packages/ray/air/config.py", line 17, in import pyarrow.fs ModuleNotFoundError: No module named 'py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Is V1 Enigne ready for DeepSeek-V1/R1 ? bug;stale ### Your current environment ### 🐛 Describe the bug ```text I use [ v-0.8.3 ](vllm-openai:v0.8.3) image to serve deepseek r1,but get error ``` ```bash 2025-04-11...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
