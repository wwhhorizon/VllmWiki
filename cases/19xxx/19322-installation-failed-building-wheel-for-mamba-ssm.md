# vllm-project/vllm#19322: [Installation]: `Failed building wheel for mamba-ssm`

| 字段 | 值 |
| --- | --- |
| Issue | [#19322](https://github.com/vllm-project/vllm/issues/19322) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: `Failed building wheel for mamba-ssm`

### Issue 正文摘录

### Your current environment I am trying to get started with contributing to the vllm code base. I followed [the developer guide](https://docs.vllm.ai/en/latest/contributing/) to set things up. When running `pip install -r requirements/dev.txt`, I got `Failed building wheel for mamba-ssm` error. Note: I added `--extra-index-url https://download.pytorch.org/whl/cu128` to `requirements/dev.txt`. The `collect_env.py` ran into some error as well ```text pip install vllm --extra-index-url https://download.pytorch.org/whl/cu128 ((venv) ) root@a3a95b0352ca:~/vllm# python collect_env.py /workspace/vllm/vllm/__init__.py:6: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from .version import __version__, __version_tuple__ # isort:skip INFO 06-08 00:01:23 [__init__.py:244] Automatically detected platform cuda. Traceback (most recent call last): File "/workspace/vllm/collect_env.py", line 19, in from vllm.envs import environment_variables File "/workspace/vllm/vllm/__init__.py", line 13, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/workspace/vllm/vllm/engine/arg_utils.py", line 22, in from vllm.config import (BlockSize, CacheConfig, Cache...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: `Failed building wheel for mamba-ssm` installation ### Your current environment I am trying to get started with contributing to the vllm code base. I followed [the developer guide](https://docs.vllm.ai/en
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Installation]: `Failed building wheel for mamba-ssm` installation ### Your current environment I am trying to get started with contributing to the vllm code base. I followed [the developer guide](https://docs.vllm.ai/e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: line 22, in from vllm.config import (BlockSize, CacheConfig, CacheDType, CompilationConfig, File "/workspace/vllm/vllm/config.py", line 37, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, F...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: "/workspace/vllm/vllm/engine/arg_utils.py", line 22, in from vllm.config import (BlockSize, CacheConfig, CacheDType, CompilationConfig, File "/workspace/vllm/vllm/config.py", line 37, in from vllm.model_executor.layers....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lm/vllm/engine/arg_utils.py", line 22, in from vllm.config import (BlockSize, CacheConfig, CacheDType, CompilationConfig, File "/workspace/vllm/vllm/config.py", line 37, in from vllm.model_executor.layers.quantization i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
