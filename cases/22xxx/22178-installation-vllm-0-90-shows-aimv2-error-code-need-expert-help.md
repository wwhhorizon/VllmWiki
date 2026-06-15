# vllm-project/vllm#22178: [Installation]: vllm 0.90 shows aimv2 error code need expert help

| 字段 | 值 |
| --- | --- |
| Issue | [#22178](https://github.com/vllm-project/vllm/issues/22178) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;moe |
| 子分类 | install |
| Operator 关键词 | cuda;moe |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vllm 0.90 shows aimv2 error code need expert help

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ``` (vast) root@salab-hpedl380g11-03:/mnt/nvme0n1/wayne/vast/VUA# python collect_env.py INFO 08-04 06:54:33 [__init__.py:243] Automatically detected platform cuda. Traceback (most recent call last): File "/mnt/nvme0n1/wayne/vast/VUA/collect_env.py", line 19, in from vllm.envs import environment_variables File "/mnt/nvme0n1/wayne/vast/lib/python3.12/site-packages/vllm/__init__.py", line 12, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/mnt/nvme0n1/wayne/vast/lib/python3.12/site-packages/vllm/engine/arg_utils.py", line 20, in from vllm.config import (BlockSize, CacheConfig, CacheDType, CompilationConfig, File "/mnt/nvme0n1/wayne/vast/lib/python3.12/site-packages/vllm/config.py", line 38, in from vllm.transformers_utils.config import ( File "/mnt/nvme0n1/wayne/vast/lib/python3.12/site-packages/vllm/transformers_utils/config.py", line 31, in from vllm.transformers_utils.configs import (ChatGLMConfig, Cohere2Config, File "/mnt/nvme0n1/wayne/vast/lib/python3.12/site-packages/vllm/transformers_utils/configs/__init__.py", line 26, in from vllm.transformers_utils.configs.ovis import Ovi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: vllm 0.90 shows aimv2 error code need expert help installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ``` (vast) root@salab-hpedl380g11-03:/mnt/nvme0n1/wayne/
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: py INFO 08-04 06:54:33 [__init__.py:243] Automatically detected platform cuda. Traceback (most recent call last): File "/mnt/nvme0n1/wayne/vast/VUA/collect_env.py", line 19, in from vllm.envs import environment_variable...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: es/vllm/engine/arg_utils.py", line 20, in from vllm.config import (BlockSize, CacheConfig, CacheDType, CompilationConfig, File "/mnt/nvme0n1/wayne/vast/lib/python3.12/site-packages/vllm/config.py", line 38, in from vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .12/site-packages/vllm/engine/arg_utils.py", line 20, in from vllm.config import (BlockSize, CacheConfig, CacheDType, CompilationConfig, File "/mnt/nvme0n1/wayne/vast/lib/python3.12/site-packages/vllm/config.py", line 3...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Installation]: vllm 0.90 shows aimv2 error code need expert help installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ``` (vast) root@salab-hpedl380g11-03:/mnt/nvme0n1/wayne...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
