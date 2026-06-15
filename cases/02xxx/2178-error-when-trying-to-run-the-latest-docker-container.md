# vllm-project/vllm#2178: Error when trying to run the latest docker container

| 字段 | 值 |
| --- | --- |
| Issue | [#2178](https://github.com/vllm-project/vllm/issues/2178) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error when trying to run the latest docker container

### Issue 正文摘录

Hey guys -- im currently trying to run the latest vllm docker image on Runpod but I'm getting this 2023-12-15T21:26:55.044618408Z File "/workspace/vllm/init.py", line 3, in 2023-12-15T21:26:55.044620468Z from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs 2023-12-15T21:26:55.044622158Z File "/workspace/vllm/engine/arg_utils.py", line 6, in 2023-12-15T21:26:55.044623408Z from vllm.config import (CacheConfig, ModelConfig, ParallelConfig, 2023-12-15T21:26:55.044624738Z File "/workspace/vllm/config.py", line 8, in 2023-12-15T21:26:55.044626048Z from vllm.utils import get_cpu_memory 2023-12-15T21:26:55.044627258Z File "/workspace/vllm/utils.py", line 8, in 2023-12-15T21:26:55.044628488Z from vllm import cuda_utils 2023-12-15T21:26:55.044630368Z ImportError: libcudart.so.11.0: cannot open shared object file: No such file or directory And so I actually didn't have any issues until recently when I tried updating vllm and i'm guessing it had something to do with a mismatched cuda version or something. But shouldn't using the nvidia/cuda:12.1.0-devel-ubuntu22.04 base cause it to not have any issues? or am I just confused? If this is the case, what would be the best way to edit the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Error when trying to run the latest docker container stale Hey guys -- im currently trying to run the latest vllm docker image on Runpod but I'm getting this 2023-12-15T21:26:55.044618408Z File "/workspace/vllm/init.py"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ls.py", line 8, in 2023-12-15T21:26:55.044628488Z from vllm import cuda_utils 2023-12-15T21:26:55.044630368Z ImportError: libcudart.so.11.0: cannot open shared object file: No such file or directory And so I actually di...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: arg_utils.py", line 6, in 2023-12-15T21:26:55.044623408Z from vllm.config import (CacheConfig, ModelConfig, ParallelConfig, 2023-12-15T21:26:55.044624738Z File "/workspace/vllm/config.py", line 8, in 2023-12-15T21:26:55...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: hen I tried updating vllm and i'm guessing it had something to do with a mismatched cuda version or something. But shouldn't using the nvidia/cuda:12.1.0-devel-ubuntu22.04 base cause it to not have any issues? or am I j...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Error when trying to run the latest docker container stale Hey guys -- im currently trying to run the latest vllm docker image on Runpod but I'm getting this 2023-12-15T21:26:55.044618408Z File "/workspace/vllm/init.py"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
