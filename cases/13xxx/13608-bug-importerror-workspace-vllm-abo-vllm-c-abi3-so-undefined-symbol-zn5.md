# vllm-project/vllm#13608: [Bug]: ImportError: /workspace/vllm-abo/vllm/_C.abi3.so: undefined symbol: _ZN5torch3jit17parseSchemaOrNameERKSsb

| 字段 | 值 |
| --- | --- |
| Issue | [#13608](https://github.com/vllm-project/vllm/issues/13608) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 48; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ImportError: /workspace/vllm-abo/vllm/_C.abi3.so: undefined symbol: _ZN5torch3jit17parseSchemaOrNameERKSsb

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In my environment, there are some third-party packages that require compiling PyTorch from source, and during the compilation of PyTorch, the compilation option _GLIBCXX_USE_CXX11_ABI=1 is used. Correspondingly, I also need to compile the matching version of torchvision from source. When compiling PyTorch and torchvision, I switched the branches to 2.5.1 and 0.20.1 respectively to meet the version requirements specified in requirements-cuda.txt of vllm. However, after compiling vllm and attempting to import it, I encountered the following error. Could you please help me understand the reason for this issue? ```python import vllm ``` ``` Traceback (most recent call last): File " ", line 1, in File "/workspace/vllm/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/workspace/vllm/vllm/engine/arg_utils.py", line 11, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "/workspace/vllm/vllm/config.py", line 21, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, File "/workspace/vllm/vllm/model_executor/__init__.py", line 1, in from vl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: ImportError: /workspace/vllm-abo/vllm/_C.abi3.so: undefined symbol: _ZN5torch3jit17parseSchemaOrNameERKSsb bug ### Your current environment ### 🐛 Describe the bug In my environment, there are some third-party pac...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: "/workspace/vllm/vllm/engine/arg_utils.py", line 11, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "/workspace/vllm/vllm/config.py", line 21, in from vllm.model_executor.layers.quantizat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: respectively to meet the version requirements specified in requirements-cuda.txt of vllm. However, after compiling vllm and attempting to import it, I encountered the following error. Could you please help me understand...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: /vllm/vllm/config.py", line 21, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, File "/workspace/vllm/vllm/model_executor/__init__.py", line 1, in from vllm.model_executor.parameter import...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;frontend_api;quantizatio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
