# vllm-project/vllm#15286: [Installation]: installation succeeded but No module named 'vllm._C'

| 字段 | 值 |
| --- | --- |
| Issue | [#15286](https://github.com/vllm-project/vllm/issues/15286) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: installation succeeded but No module named 'vllm._C'

### Issue 正文摘录

### Your current environment My operation system is Windows, and i use anaconda3 to manage my virtual environment and site-packages. I create a new virtual environment with python 3.10. I ran the command ```pip install vllm``` to install vllm in my system The installation process is smooth, and it seems that i successfully installed vllm. However, when i tried to run ```vllm serve "Qwen/Qwen2.5-VL-7B-Instruct"```, it occured such bug: ``` INFO 03-21 17:22:05 [__init__.py:256] Automatically detected platform cuda. Traceback (most recent call last): File "C:\Users\Admin\anaconda3\envs\vllm\lib\runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "C:\Users\Admin\anaconda3\envs\vllm\lib\runpy.py", line 86, in _run_code exec(code, run_globals) File "C:\Users\Admin\anaconda3\envs\vllm\Scripts\vllm.exe\__main__.py", line 4, in File "C:\Users\Admin\anaconda3\envs\vllm\lib\site-packages\vllm\__init__.py", line 11, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "C:\Users\Admin\anaconda3\envs\vllm\lib\site-packages\vllm\engine\arg_utils.py", line 22, in from vllm.executor.executor_base import ExecutorBase File "C:\Users\Admin\anac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: installation succeeded but No module named 'vllm._C' installation ### Your current environment My operation system is Windows, and i use anaconda3 to manage my virtual environment and site-packages. I cre
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: install vllm``` to install vllm in my system The installation process is smooth, and it seems that i successfully installed vllm. However, when i tried to run ```vllm serve "Qwen/Qwen2.5-VL-7B-Instruct"```, it occured s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: successfully installed vllm. However, when i tried to run ```vllm serve "Qwen/Qwen2.5-VL-7B-Instruct"```, it occured such bug: ``` INFO 03-21 17:22:05 [__init__.py:256] Automatically detected platform cuda. Traceback (m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vllm\model_executor\layers\sampler.py", line 23, in from vllm.spec_decode.metrics import SpecDecodeWorkerMetrics File "C:\Users\Admin\anaconda3\envs\vllm\lib\site-packages\vllm\spec_decode\metrics.py", line 9, in from v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda crash;import_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
