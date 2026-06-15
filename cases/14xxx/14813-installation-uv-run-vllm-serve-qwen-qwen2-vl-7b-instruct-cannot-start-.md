# vllm-project/vllm#14813: [Installation]: uv run vllm serve "Qwen/Qwen2-VL-7B-Instruct" cannot start. uvloop does not support windows

| 字段 | 值 |
| --- | --- |
| Issue | [#14813](https://github.com/vllm-project/vllm/issues/14813) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: uv run vllm serve "Qwen/Qwen2-VL-7B-Instruct" cannot start. uvloop does not support windows

### Issue 正文摘录

### Your current environment D:\AI-Apps\vLLM2>uv run vllm serve "Qwen/Qwen2-VL-7B-Instruct" Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "D:\AI-Apps\vLLM2\.venv\Scripts\vllm.exe\__main__.py", line 4, in File "D:\AI-Apps\vLLM2\.venv\Lib\site-packages\vllm\entrypoints\cli\main.py", line 9, in import vllm.entrypoints.cli.serve File "D:\AI-Apps\vLLM2\.venv\Lib\site-packages\vllm\entrypoints\cli\serve.py", line 6, in import uvloop ModuleNotFoundError: No module named 'uvloop' D:\AI-Apps\vLLM2>uv pip install uvloop Resolved 1 package in 1.49s × Failed to build `uvloop==0.21.0` ├─▶ The build backend returned an error ╰─▶ Call to `setuptools.build_meta.build_wheel` failed (exit code: 1) [stderr] Traceback (most recent call last): File " ", line 14, in File "C:\Users\xiaoh\AppData\Local\uv\cache\builds-v0\.tmpe0SVix\Lib\site-packages\setuptools\build_meta.py", line 334, in get_requires_for_build_wheel return self._get_build_requires(config_settings, requirements=[]) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "C:\Users\xiaoh\AppData\Local\uv\cache\builds-v0\.tmpe0SVix\Lib\site-packages\setuptools\buil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: uv run vllm serve "Qwen/Qwen2-VL-7B-Instruct" cannot start. uvloop does not support windows installation;stale ### Your current environment D:\AI-Apps\vLLM2>uv run vllm serve "Qwen/Qwen2-VL-7B-Instruct" T
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Installation]: uv run vllm serve "Qwen/Qwen2-VL-7B-Instruct" cannot start. uvloop does not support windows installation;stale ### Your current environment D:\AI-Apps\vLLM2>uv run vllm serve "Qwen/Qwen2-VL-7B-Instruct"...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 1 package in 1.49s × Failed to build `uvloop==0.21.0` ├─▶ The build backend returned an error ╰─▶ Call to `setuptools.build_meta.build_wheel` failed (exit code: 1) [stderr] Traceback (most recent call last): File " ", l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -7B-Instruct" cannot start. uvloop does not support windows installation;stale ### Your current environment D:\AI-Apps\vLLM2>uv run vllm serve "Qwen/Qwen2-VL-7B-Instruct" Traceback (most recent call last): File " ", lin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
