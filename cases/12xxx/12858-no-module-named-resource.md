# vllm-project/vllm#12858: No module named 'resource'

| 字段 | 值 |
| --- | --- |
| Issue | [#12858](https://github.com/vllm-project/vllm/issues/12858) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | quantization |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> No module named 'resource'

### Issue 正文摘录

### Your current environment (base) C:\Windows\system32>cd C:\Users\TARGET STORE\Desktop\1\vllm (base) C:\Users\TARGET STORE\Desktop\1\vllm>conda activate myenv2 (myenv2) C:\Users\TARGET STORE\Desktop\1\vllm>python -c "import vllm" Traceback (most recent call last): File " ", line 1, in File "C:\Users\TARGET STORE\Desktop\1\vllm\vllm\__init__.py", line 7, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "C:\Users\TARGET STORE\Desktop\1\vllm\vllm\engine\arg_utils.py", line 13, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "C:\Users\TARGET STORE\Desktop\1\vllm\vllm\config.py", line 24, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, File "C:\Users\TARGET STORE\Desktop\1\vllm\vllm\model_executor\__init__.py", line 3, in from vllm.model_executor.parameter import (BasevLLMParameter, File "C:\Users\TARGET STORE\Desktop\1\vllm\vllm\model_executor\parameter.py", line 9, in from vllm.distributed import get_tensor_model_parallel_rank File "C:\Users\TARGET STORE\Desktop\1\vllm\vllm\distributed\__init__.py", line 3, in from .communication_op import * File "C:\Users\TARGET STORE\Desktop\1\vllm\vllm\distributed\...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: No module named 'resource' installation ### Your current environment (base) C:\Windows\system32>cd C:\Users\TARGET STORE\Desktop\1\vllm (base) C:\Users\TARGET STORE\Desktop\1\vllm>conda activate myenv2 (myenv2) C:\Users...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: RE\Desktop\1\vllm\vllm\engine\arg_utils.py", line 13, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "C:\Users\TARGET STORE\Desktop\1\vllm\vllm\config.py", line 24, in from vllm.model_exe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s 75.8.0 six 1.17.0 smart-open 7.1.0 sniffio 1.3.1 starlette 0.45.3 sympy 1.13.1 tiktoken 0.7.0 tokenizers
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: \vllm\vllm\config.py", line 24, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, File "C:\Users\TARGET STORE\Desktop\1\vllm\vllm\model_executor\__init__.py", line 3, in from vllm.model_execu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.28.1 idna 3.10 importlib_metadata 8.6.1 interegular 0.3.3 Jinja2 3.1.4 jiter 0.8.2 jsonschema 4.23.0 jsonschema-specifications

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
