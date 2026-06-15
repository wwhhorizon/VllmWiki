# vllm-project/vllm#1368: Make multi replicas to make a balancer.

| 字段 | 值 |
| --- | --- |
| Issue | [#1368](https://github.com/vllm-project/vllm/issues/1368) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Make multi replicas to make a balancer.

### Issue 正文摘录

Hi, I am working on `make multi replicas to make a balancer`. But now I found that some of the globals are setted onece one instance is initiated. I manage to solve by reset thoese varaiables, but now I do not know how to set the device for the new replica to the device id 1 (given that device 0 has been set to the first instance). Also, I tried to use the multi threading which cause `signal error` and `adress error` separately. Here is my implementation: ```python class EngineManager: def __init__(self, engine_args_list): self.engines = [] # CUDA_VISIBLE_DEVICES=3 gpu_id = 0 for args in engine_args_list: import vllm.model_executor.parallel_utils.parallel_state as parallel_state parallel_state._DATA_PARALLEL_GROUP = None parallel_state._TENSOR_MODEL_PARALLEL_GROUP = None parallel_state._PIPELINE_MODEL_PARALLEL_GROUP = None parallel_state._MODEL_PARALLEL_GROUP = None parallel_state._EMBEDDING_GROUP = None parallel_state._POSITION_EMBEDDING_GROUP = None parallel_state._VIRTUAL_PIPELINE_MODEL_PARALLEL_RANK = None parallel_state._VIRTUAL_PIPELINE_MODEL_PARALLEL_WORLD_SIZE = None parallel_state._PIPELINE_MODEL_PARALLEL_SPLIT_RANK = None parallel_state._MPU_TENSOR_MODEL_PARALLEL_WORLD_S...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: =3 gpu_id = 0 for args in engine_args_list: import vllm.model_executor.parallel_utils.parallel_state as parallel_state parallel_state._DATA_PARALLEL_GROUP = None parallel_state._TENSOR_MODEL_PARALLEL_GROUP = None parall...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ef __init__(self, engine_args_list): self.engines = [] # CUDA_VISIBLE_DEVICES=3 gpu_id = 0 for args in engine_args_list: import vllm.model_executor.parallel_utils.parallel_state as parallel_state parallel_state._DATA_PA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: gpu_id = 0 for args in engine_args_list: import vllm.model_executor.parallel_utils.parallel_state as parallel_state parallel_state._DATA_PARALLEL_GROUP = None parallel_state._TENSOR_MODEL_PARALLEL_GROUP = None parallel_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
