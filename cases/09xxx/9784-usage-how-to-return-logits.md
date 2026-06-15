# vllm-project/vllm#9784: [Usage]: how to return logits

| 字段 | 值 |
| --- | --- |
| Issue | [#9784](https://github.com/vllm-project/vllm/issues/9784) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to return logits

### Issue 正文摘录

### Your current environment ``` Collecting environment information... WARNING 10-29 04:40:34 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of them are installed, `pynvml` will take precedence and cause errors. See https://pypi.org/project/pynvml for more information. Traceback (most recent call last): File "/workspace/collect_env.py", line 743, in main() File "/workspace/collect_env.py", line 722, in main output = get_pretty_env_info() File "/workspace/collect_env.py", line 717, in get_pretty_env_info return pretty_str(get_env_info()) File "/workspace/collect_env.py", line 549, in get_env_info vllm_version = get_vllm_version() File "/workspace/collect_env.py", line 270, in get_vllm_version from vllm import __version__, __version_tuple__ ImportError: cannot import name '__version_tuple__' from 'vllm' (/workspace/code/vllm/vllm/__init__.py) but I am using v0.6.0 vllm ``` ### How would you like to use vllm I tried to return logits part of output and like ``` {"text":["this is new vllm with logits bla bla....."],"logits":[1.0,2.0]} ``` I found each model (e.g.. llama.py) call and return l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 04:40:34 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of them are installed, `pynvml` will take precedence and cause erro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: logits usage ### Your current environment ``` Collecting environment information... WARNING 10-29 04:40:34 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: onment ``` Collecting environment information... WARNING 10-29 04:40:34 cuda.py:22] You are using a deprecated `pynvml` package. Please install `nvidia-ml-py` instead, and make sure to uninstall `pynvml`. When both of t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: _model(...) > 0 in worker_base.py I lost connection to return output to RequestOutput to print like above. I appreciate if anyone can help. thanks ### Before submitting a new issue... - [X] Make sure you already searche...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development model_support;sampling_logits cuda crash;import_error Your current enviro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
