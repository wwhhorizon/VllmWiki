# vllm-project/vllm#5594: [bug]vllm deployement is failing on nvidia because of numpy2.0 upgrade

| 字段 | 值 |
| --- | --- |
| Issue | [#5594](https://github.com/vllm-project/vllm/issues/5594) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [bug]vllm deployement is failing on nvidia because of numpy2.0 upgrade

### Issue 正文摘录

### Your current environment # python3.9 -c "import vllm; print(vllm.__version__)" A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.0 as it may crash. To support both 1.x and 2.x versions of NumPy, modules must be compiled with NumPy 2.0. Some module may need to rebuild instead e.g. with 'pybind11>=2.12'. If you are a user of the module, the easiest solution will be to downgrade to 'numpy ", line 1, in File "/usr/local/lib64/python3.9/site-packages/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/usr/local/lib64/python3.9/site-packages/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, DeviceConfig, LoRAConfig, ModelConfig, File "/usr/local/lib64/python3.9/site-packages/vllm/config.py", line 7, in import torch File "/usr/local/lib64/python3.9/site-packages/torch/__init__.py", line 1382, in from .functional import * # noqa: F403 File "/usr/local/lib64/python3.9/site-packages/torch/functional.py", line 7, in import torch.nn.functional as F File "/usr/local/lib64/python3.9/site-packages/torch/nn/__init__.py", line 1, in from .modules import * # noqa: F403 File "/usr/local/lib64/python3.9/s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [bug]vllm deployement is failing on nvidia because of numpy2.0 upgrade installation ### Your current environment # python3.9 -c "import vllm; print(vllm.__version__)" A module that was compiled using NumPy 1.x cannot be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n3.9/site-packages/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, DeviceConfig, LoRAConfig, ModelConfig, File "/usr/local/lib64/python3.9/site-packages/vllm/config.py", line 7, in import tor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ine 35, in from .transformer import TransformerEncoder, TransformerDecoder, \ File "/usr/local/lib64/python3.9/site-packages/torch/nn/modules/transformer.py", line 20, in device: torch.device = torch.device(torch._C._ge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
