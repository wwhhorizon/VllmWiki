# vllm-project/vllm#11208: [Bug]: extremely slow launching time possibly due to calling ray.init() again after it has already been called when launching vllm through ray cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#11208](https://github.com/vllm-project/vllm/issues/11208) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;mismatch;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: extremely slow launching time possibly due to calling ray.init() again after it has already been called when launching vllm through ray cluster

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug it takes 5 mins just to launch vllm when launching through ray. inspecting the log, it seems to call ray.init again when my code has already call it. Why is this the case? why is it taking so long? if i am launching it wrongly, can you kindly suggest how i can resolve this? code to reproduce: ``` import ray from ray.util.placement_group import placement_group from datetime import timedelta from typing import Any, Optional, Union import ray import torch import torch.distributed from ray.util.placement_group import placement_group from ray.util.scheduling_strategies import PlacementGroupSchedulingStrategy from torch.distributed.distributed_c10d import ( Backend, PrefixStore, Store, _new_process_group_helper, _world, default_pg_timeout, rendezvous, ) from vllm.worker.worker import Worker import time # Copy from pytorch to allow creating multiple main groups. # https://github.com/pytorch/pytorch/blob/main/torch/distributed/distributed_c10d.py def init_process_group( backend: Union[str, Backend] = None, init_method: Optional[str] = None, timeout: Optional[timedelta] = None, world_size: int = -1, ran...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: ng vllm through ray cluster bug;ray ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug it takes 5 mins just to launch vllm when launching through ray. inspecting the log, it seems to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: can you kindly suggest how i can resolve this? code to reproduce: ``` import ray from ray.util.placement_group import placement_group from datetime import timedelta from typing import Any, Optional, Union import ray imp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: LM engine (v0.6.4.post1) with config: model='Qwen/Qwen2-VL-7B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2-VL-7B-Instruct', skip_tokenizer_init =False, tokenizer_mode=auto, revision=None, override_neuron_co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: , group_name={group_name}", ) def update_weight(self, name, dtype, shape, empty_cache=False): """Broadcast weight to all vllm workers from source rank 0 (actor model)""" # print(f"update_weight: {name}, dtype: {dtype},...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: pSchedulingStrategy from torch.distributed.distributed_c10d import ( Backend, PrefixStore, Store, _new_process_group_helper, _world, default_pg_timeout, rendezvous, ) from vllm.worker.worker import Worker import time #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
