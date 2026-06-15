# vllm-project/vllm#5477: [Usage]: OpenRLHF: How can I create a second NCCL Group in a vLLM v0.4.3+ Ray worker?

| 字段 | 值 |
| --- | --- |
| Issue | [#5477](https://github.com/vllm-project/vllm/issues/5477) |
| 状态 | closed |
| 标签 | usage;ray |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | race_cond |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: OpenRLHF: How can I create a second NCCL Group in a vLLM v0.4.3+ Ray worker?

### Issue 正文摘录

### Your current environment We are working on accelerating RLHF algorithms and need to broadcast the weights of the DeepSpeed engine to the vLLM Ray worker. In v0.4.2, we were able to create an additional NCCL group to achieve this. However, after updating to v0.4.3 and incorporating the changes from [this MR](https://github.com/vllm-project/vllm/pull/4894), we found that doing so causes NCCL errors during broadcast. Our weight synchronization code is located at: https://github.com/OpenLLMAI/OpenRLHF/blob/main/openrlhf/trainer/ray/vllm_engine.py. and https://github.com/OpenLLMAI/OpenRLHF/blob/main/openrlhf/trainer/ray/vllm_worker_wrap.py see `init_process_group` (build NCCL group between vLLM and DeepSpeed named `self._model_update_group`) and `update_weight` (Broadcast weights from DeepSpeed to vLLM, `torch.distributed.broadcast(weight, 0, group=self._model_update_group)`) We temporarily replaced the NCCL backend with GLOO to make it work, but the performance was poor。 The error message is: ``` �[36m(RayWorkerWrapper pid=4183, ip=10.3.32.122)�[0m ERROR 06-03 23:13:39 worker_base.py:148] Error executing method start_worker_execution_loop. This might cause deadlock in distributed...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: main/openrlhf/trainer/ray/vllm_worker_wrap.py see `init_process_group` (build NCCL group between vLLM and DeepSpeed named `self._model_update_group`) and `update_weight` (Broadcast weights from DeepSpeed to vLLM, `torch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: OpenRLHF: How can I create a second NCCL Group in a vLLM v0.4.3+ Ray worker? usage;ray ### Your current environment We are working on accelerating RLHF algorithms and need to broadcast the weights of the DeepSp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 48] Error executing method start_worker_execution_loop. This might cause deadlock in distributed execution. �[36m(RayWorkerWrapper pid=4183, ip=10.3.32.122)�[0m ERROR 06-03 23:13:39 worker_base.py:148] Traceback (most r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: , 0, group=self._model_update_group)`) We temporarily replaced the NCCL backend with GLOO to make it work, but the performance was poor。 The error message is: ``` �[36m(RayWorkerWrapper pid=4183, ip=10.3.32.122)�[0m ERR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Actor pid=116812) a5fa65866c9c:116812:120170 [0] proxy.cc:1336 NCCL WARN Cuda failure 1 'invalid argument' (LLMRayActor pid=116812) a5fa65866c9c:116812:120158 [0] transport/p2p.cc:272 NCCL WARN Cuda failure 'invalid arg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
