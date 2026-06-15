# vllm-project/vllm#11399: [RFC]: Flexible Weight Sync for vLLM Workers

| 字段 | 值 |
| --- | --- |
| Issue | [#11399](https://github.com/vllm-project/vllm/issues/11399) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Flexible Weight Sync for vLLM Workers

### Issue 正文摘录

### Motivation. **TL;DR:** This RFC proposes optimizing weight synchronization between training processes and vLLM workers for efficient RLHF implementation. We are pleased to see vLLM collaborating with the reinforcement learning (RL) community and working on introducing useful APIs such as `update_weight` as proposed in [#5723](https://github.com/vllm-project/vllm/issues/5723). Following that, a seemingly good practice would be the implementation of OpenRLHF, which can use nccl (previously gloo) as the backend to collect weights for vLLM workers to update. Below is a simple implementation derived from the ongoing discussion in [this comment](https://github.com/vllm-project/vllm/issues/5723#issuecomment-2554389656): ``` # In main training process (rank 0) # Broadcast the parameters on rank 0 to other ranks torch.distributed.broadcast(param.data, 0, group=model_update_group) # In vLLM Engine driver process # Trigger the vLLM workers to update_weight self.llm.llm_engine.model_executor._run_workers("update_weight", name, dtype, shape, empty_cache) # In vLLM SPMD workers # Create an empty tensor and then receive the param.data from rank 0 weight = torch.empty(shape, dtype=dtype, devi...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: am.data from rank 0 weight = torch.empty(shape, dtype=dtype, device="cuda") torch.distributed.broadcast(weight, 0, group=self._model_update_group) self.model_runner.model.load_weights(weights=[(name, weight)]) ``` Using...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ight synchronization between training processes and vLLM workers for efficient RLHF implementation. We are pleased to see vLLM collaborating with the reinforcement learning (RL) community and working on introducing usef...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: chronization between training processes and vLLM workers for efficient RLHF implementation. We are pleased to see vLLM collaborating with the reinforcement learning (RL) community and working on introducing useful APIs...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: implementation of OpenRLHF, which can use nccl (previously gloo) as the backend to collect weights for vLLM workers to update. Below is a simple implementation derived from the ongoing discussion in [this comment](https...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: self.llm.llm_engine.model_executor._run_workers("update_weight", name, dtype, shape, empty_cache) # In vLLM SPMD workers # Create an empty tensor and then receive the param.data from rank 0 weight = torch.empty(shape, d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
