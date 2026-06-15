# vllm-project/vllm#14714: [Bug]: ModuleNotFoundError: No module named 'vllm._C' at first start

| 字段 | 值 |
| --- | --- |
| Issue | [#14714](https://github.com/vllm-project/vllm/issues/14714) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ModuleNotFoundError: No module named 'vllm._C' at first start

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python sampling_params = SamplingParams(max_tokens=8192, temperature=0.0) llm = LLM(model=model_name, tokenizer_mode="mistral", config_format="mistral", load_format="mistral") ``` ```errINFO 03-13 09:15:09 __init__.py:207] Automatically detected platform cuda. Traceback (most recent call last): File "C:\Projects\PythonProjects\vllm\pyScript.py", line 62, in llm = LLM(model=model_name, File "C:\Projects\PythonProjects\vllm\.venv\lib\site-packages\vllm\utils.py", line 1022, in inner return fn(*args, **kwargs) File "C:\Projects\PythonProjects\vllm\.venv\lib\site-packages\vllm\entrypoints\llm.py", line 212, in __init__ engine_args = EngineArgs( File " ", line 107, in __init__ File "C:\Projects\PythonProjects\vllm\.venv\lib\site-packages\vllm\engine\arg_utils.py", line 235, in __post_init__ load_general_plugins() File "C:\Projects\PythonProjects\vllm\.venv\lib\site-packages\vllm\plugins\__init__.py", line 61, in load_general_plugins from vllm.platforms import current_platform File "C:\Projects\PythonProjects\vllm\.venv\lib\site-packages\vllm\platforms\__init__.py", line 239, in __getattr__ _current_platform = resolve_obj_by_qualnam...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ling_params = SamplingParams(max_tokens=8192, temperature=0.0) llm = LLM(model=model_name, tokenizer_mode="mistral", config_format="mistral", load_format="mistral") ``` ```errINFO 03-13 09:15:09 __init__.py:207] Automat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s\__init__.py", line 61, in load_general_plugins from vllm.platforms import current_platform File "C:\Projects\PythonProjects\vllm\.venv\lib\site-packages\vllm\platforms\__init__.py", line 239, in __getattr__ _current_p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `errINFO 03-13 09:15:09 __init__.py:207] Automatically detected platform cuda. Traceback (most recent call last): File "C:\Projects\PythonProjects\vllm\pyScript.py", line 62, in llm = LLM(model=model_name, File "C:\Proj...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development model_support;sampling_logits cuda crash;import_error env_dependency Your...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
