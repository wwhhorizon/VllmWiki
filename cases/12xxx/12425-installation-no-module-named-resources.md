# vllm-project/vllm#12425: [Installation]: no module named "resources"

| 字段 | 值 |
| --- | --- |
| Issue | [#12425](https://github.com/vllm-project/vllm/issues/12425) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: no module named "resources"

### Issue 正文摘录

### Your current environment ```text vllm serve "bytedance-research/UI-TARS-7B-DPO" Traceback (most recent call last): File "C:\Users\yepyy\anaconda3\envs\vllm\lib\runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "C:\Users\yepyy\anaconda3\envs\vllm\lib\runpy.py", line 86, in _run_code exec(code, run_globals) File "C:\Users\yepyy\anaconda3\envs\vllm\Scripts\vllm.exe\__main__.py", line 4, in File "C:\Users\yepyy\anaconda3\envs\vllm\lib\site-packages\vllm\__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "C:\Users\yepyy\anaconda3\envs\vllm\lib\site-packages\vllm\engine\arg_utils.py", line 11, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "C:\Users\yepyy\anaconda3\envs\vllm\lib\site-packages\vllm\config.py", line 22, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, File "C:\Users\yepyy\anaconda3\envs\vllm\lib\site-packages\vllm\model_executor\__init__.py", line 1, in from vllm.model_executor.parameter import (BasevLLMParameter, File "C:\Users\yepyy\anaconda3\envs\vllm\lib\site-packages\vllm\model_executor\parameter.py", line 7, in from vllm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lib\site-packages\vllm\engine\arg_utils.py", line 11, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "C:\Users\yepyy\anaconda3\envs\vllm\lib\site-packages\vllm\config.py", line 22, in fro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: no module named "resources" installation ### Your current environment ```text vllm serve "bytedance-research/UI-TARS-7B-DPO" Traceback (most recent call last): File "C:\Users\yepyy\anaconda3\envs\vllm\l
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: kages\vllm\config.py", line 22, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, File "C:\Users\yepyy\anaconda3\envs\vllm\lib\site-packages\vllm\model_executor\__init__.py", line 1, in from...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: allation ### Your current environment ```text vllm serve "bytedance-research/UI-TARS-7B-DPO" Traceback (most recent call last): File "C:\Users\yepyy\anaconda3\envs\vllm\lib\runpy.py", line 196, in _run_module_as_main re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
