# vllm-project/vllm#2735: ERROR: Could not build wheels for vllm, which is required to install pyproject.toml-based projects

| 字段 | 值 |
| --- | --- |
| Issue | [#2735](https://github.com/vllm-project/vllm/issues/2735) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ERROR: Could not build wheels for vllm, which is required to install pyproject.toml-based projects

### Issue 正文摘录

(vllm) PS C:\Users\hub1\gen-ai-training-abshek\gen-ai-training\vllm-main> pip install -e . Looking in indexes: http://art.nwie.net/artifactory/api/pypi/pypi/simple Obtaining file:///C:/Users/hub1/gen-ai-training-abshek/gen-ai-training/vllm-main Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... done Preparing editable metadata (pyproject.toml) ... done Collecting ninja (from vllm==0.3.0) Using cached http://art.nwie.net/artifactory/api/pypi/pypi/packages/packages/b6/2f/a3bc50fa63fc4fe9348e15b53dc8c87febfd4e0c660fcf250c4b19a3aa3b/ninja-1.11.1.1-py2.py3-none-win_amd64.whl (312 kB) Requirement already satisfied: psutil in c:\users\hub1\gen-ai-training-abshek\gen-ai-training\vllm\lib\site-packages (from vllm==0.3.0) (5.9.8) Collecting ray>=2.9 (from vllm==0.3.0) Using cached http://art.nwie.net/artifactory/api/pypi/pypi/packages/packages/a2/77/2cd1967982ef518065f181f5273e2bdf84cdcda586941b307c7f17aaad16/ray-2.9.1-cp311-cp311-win_amd64.whl (25.6 MB) Collecting sentencepiece (from vllm==0.3.0) Using cached http://art.nwie.net/artifactory/api/pypi/pypi/packages/packages/cc/07/d6951e3b4079df819d76353...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ERROR: Could not build wheels for vllm, which is required to install pyproject.toml-based projects stale (vllm) PS C:\Users\hub1\gen-ai-training-abshek\gen-ai-training\vllm-main> pip install -e . Looking in indexes: htt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ges (from ray>=2.9->vllm==0.3.0) (2.28.1) Requirement already satisfied: huggingface-hub =0.19.3 in c:\users\hub1\gen-ai-training-abshek\gen-ai-training\vllm\lib\site-packages (from transformers>=4.37.0->vllm==0.3.0) (0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: device(torch._C._get_default_device()), # torch.device('cpu'), No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1' running editable_wheel creating C:\Users\hub1\AppData\L...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: g/vllm-main Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... done Preparing editable metadata (pyproject.toml) ... done Collect...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: setuptools handles editable installations, please submit a reproducible example (see https://stackoverflow.com/help/minimal-reproducible-example) to: https://github.com/pypa/setuptools/issues See https://setuptools.pypa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
