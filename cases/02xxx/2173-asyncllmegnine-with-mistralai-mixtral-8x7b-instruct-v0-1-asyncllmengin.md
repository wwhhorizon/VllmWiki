# vllm-project/vllm#2173: AsyncLLMEgnine with mistralai/Mixtral-8x7B-Instruct-v0.1 - AsyncLLMEngine dead and Invalid config blocking attribute value -2147483648

| 字段 | 值 |
| --- | --- |
| Issue | [#2173](https://github.com/vllm-project/vllm/issues/2173) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AsyncLLMEgnine with mistralai/Mixtral-8x7B-Instruct-v0.1 - AsyncLLMEngine dead and Invalid config blocking attribute value -2147483648

### Issue 正文摘录

I am trying to stream the output from Mixtral-8x7B-Instruct-v0.1 using the AsyncLLM engine and running into some problems. My code has been working perfectly for Mistral7B model. The error trace is given below: xception raised in creation task: The actor died because of an error raised in its creation task, ray::_AsyncLLMEngine.__init__() (pid=641091, ip=10.146.0.2, actor_id=12feec12736fa57cc721e47901000000, repr= ) (_AsyncLLMEngine pid=641091) File "/usr/lib/python3.8/concurrent/futures/_base.py", line 444, in result (_AsyncLLMEngine pid=641091) return self.__get_result() (_AsyncLLMEngine pid=641091) File "/usr/lib/python3.8/concurrent/futures/_base.py", line 389, in __get_result (_AsyncLLMEngine pid=641091) raise self._exception (_AsyncLLMEngine pid=641091) File "/home/abhisek.swain/code/derai-continuous-deployment/venv/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 108, in __init__ (_AsyncLLMEngine pid=641091) self._init_workers_ray(placement_group) (_AsyncLLMEngine pid=641091) File "/home/abhisek.swain/code/derai-continuous-deployment/venv/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 191, in _init_workers_ray (_AsyncLLMEngine pid=641091) self._run...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:219, invalid argument, NCCL version 2.14.3 (_AsyncLLMEngine pid=641091) ncclInvalidArgument: Invalid value for an argument. (_AsyncLLMEngine pid=641091) Last error: (_AsyncLL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: h mistralai/Mixtral-8x7B-Instruct-v0.1 - AsyncLLMEngine dead and Invalid config blocking attribute value -2147483648 I am trying to stream the output from Mixtral-8x7B-Instruct-v0.1 using the AsyncLLM engine and running...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ll_outputs) (_AsyncLLMEngine pid=641091) ray.exceptions.RayTaskError(DistBackendError): ray::RayWorkerVllm.execute_method() (pid=641194, ip=10.146.0.2, actor_id=d6d45db57fe6b04b1ec82ae801000000, repr= ) (_AsyncLLMEngine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: yncLLMEngine pid=641091) torch.distributed.all_reduce(torch.zeros(1).cuda()) (_AsyncLLMEngine pid=641091) File "/home/abhisek.swain/code/derai-continuous-deployment/venv/lib/python3.8/site-packages/torch/distributed/c10...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: alai/Mixtral-8x7B-Instruct-v0.1 - AsyncLLMEngine dead and Invalid config blocking attribute value -2147483648 I am trying to stream the output from Mixtral-8x7B-Instruct-v0.1 using the AsyncLLM engine and running into s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
