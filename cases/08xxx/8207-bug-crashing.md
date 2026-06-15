# vllm-project/vllm#8207: [Bug]: Crashing

| 字段 | 值 |
| --- | --- |
| Issue | [#8207](https://github.com/vllm-project/vllm/issues/8207) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crashing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `INFO 09-05 18:51:25 importing.py:10] Triton not installed; certain GPU-related functions will not be available. WARNING 09-05 18:51:25 _core_ext.py:180] Failed to import from vllm._core_C with ImportError('/opt/conda/lib/python3.10/site-packages/vllm/_core_C.abi3.so: undefined symbol: _ZN5torch6detail10class_baseC2ERKSsS3_SsRKSt9type_infoS6_') Traceback (most recent call last): File "/opt/conda/bin/vllm", line 5, in from vllm.scripts import main File "/opt/conda/lib/python3.10/site-packages/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/opt/conda/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 11, in from vllm.config import (CacheConfig, DecodingConfig, DeviceConfig, File "/opt/conda/lib/python3.10/site-packages/vllm/config.py", line 12, in from vllm.model_executor.layers.quantization import QUANTIZATION_METHODS File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/quantization/__init__.py", line 3, in from vllm.model_executor.layers.quantization.aqlm import AQLMConfig File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/quant...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: our current environment ### 🐛 Describe the bug `INFO 09-05 18:51:25 importing.py:10] Triton not installed; certain GPU-related functions will not be available. WARNING 09-05 18:51:25 _core_ext.py:180] Failed to import f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s_` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .10/site-packages/vllm/engine/arg_utils.py", line 11, in from vllm.config import (CacheConfig, DecodingConfig, DeviceConfig, File "/opt/conda/lib/python3.10/site-packages/vllm/config.py", line 12, in from vllm.model_exe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: onment ### 🐛 Describe the bug `INFO 09-05 18:51:25 importing.py:10] Triton not installed; certain GPU-related functions will not be available. WARNING 09-05 18:51:25 _core_ext.py:180] Failed to import from vllm._core_C...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: kages/vllm/config.py", line 12, in from vllm.model_executor.layers.quantization import QUANTIZATION_METHODS File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/quantization/__init__.py", line 3, in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
