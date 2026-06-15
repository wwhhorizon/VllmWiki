# vllm-project/vllm#34090: what am I doing wrong ? libmpi_cxx.so.40: cannot open shared object file: No such file or directory

| 字段 | 值 |
| --- | --- |
| Issue | [#34090](https://github.com/vllm-project/vllm/issues/34090) |
| 状态 | open |
| 标签 | usage |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> what am I doing wrong ? libmpi_cxx.so.40: cannot open shared object file: No such file or directory

### Issue 正文摘录

### Your current environment installed uv , because I normally use pip and pipx . uv init vllm cd vllm uv venv --python 3.12 --seed ( Using CPython 3.12.12 Creating virtual environment with seed packages at: .venv ) source .venv/bin/activate (vllm) root@ave:~/vllm# uv pip install vllm --extra-index-url https://wheels.vllm.ai/rocm/ ( Resolved 182 packages in 5.71s Installed 182 packages in 125ms ) vllm) root@ave:~/vllm# vllm Traceback (most recent call last): File "/root/vllm/.venv/bin/vllm", line 4, in from vllm.entrypoints.cli.main import main File "/root/vllm/.venv/lib/python3.12/site-packages/vllm/__init__.py", line 14, in import vllm.env_override # noqa: F401 ^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/vllm/.venv/lib/python3.12/site-packages/vllm/env_override.py", line 5, in import torch File "/root/vllm/.venv/lib/python3.12/site-packages/torch/__init__.py", line 426, in _load_global_deps() File "/root/vllm/.venv/lib/python3.12/site-packages/torch/__init__.py", line 379, in _load_global_deps raise err File "/root/vllm/.venv/lib/python3.12/site-packages/torch/__init__.py", line 334, in _load_global_deps ctypes.CDLL(global_deps_lib_path, mode=ctypes.RTLD_GLOBAL) File "/root/.local/shar...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ject file: No such file or directory usage ### Your current environment installed uv , because I normally use pip and pipx . uv init vllm cd vllm uv venv --python 3.12 --seed ( Using CPython 3.12.12 Creating virtual env...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ave:~/vllm# uv pip install vllm --extra-index-url https://wheels.vllm.ai/rocm/ ( Resolved 182 packages in 5.71s Installed 182 packages in 125ms ) vllm) root@ave:~/vllm# vllm Traceback (most recent call last): File "/roo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
