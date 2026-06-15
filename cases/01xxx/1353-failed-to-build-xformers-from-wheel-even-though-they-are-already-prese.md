# vllm-project/vllm#1353: Failed to build xformers from wheel even though they are already present

| 字段 | 值 |
| --- | --- |
| Issue | [#1353](https://github.com/vllm-project/vllm/issues/1353) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Failed to build xformers from wheel even though they are already present

### Issue 正文摘录

I tried to install vllm in a fresh Conda environment today. It depends on xformers, but fails to build them: ``` File "C:\Users\tomas\miniconda3\envs\llm_server\Lib\site-packages\setuptools\_distutils\util.py", line 139, in convert_path raise ValueError("path '%s' cannot be absolute" % pathname) ValueError: path '/__w/xformers/xformers/third_party/flash-attention/csrc/flash_attn/flash_api.cpp' cannot be absolute [end of output] note: This error originates from a subprocess, and is likely not a problem with pip. ERROR: Failed building wheel for xformers Running setup.py clean for xformers Failed to build xformers ERROR: Could not build wheels for xformers, which is required to install pyproject.toml-based projects ``` Indeed, latest xformers release fails to work on Windows. So I tried to install minimum supported version xformers 0.0.22 via pip and it succedded: ``` filelock 3.9.0 fsspec 2023.4.0 Jinja2 3.1.2 MarkupSafe 2.1.2 mpmath 1.3.0 mypy-extensions 1.0.0 networkx 3.0 numpy 1.26.0 pip 23.2.1 pyre-extensions 0.0.29 setuptools 68.0.0 sympy 1.12 torch 2.0.1 typing_extensions 4.4.0 typing-inspect 0.9.0 wheel 0.41.2 xformers 0.0.22 ``` However, vllm installer seems to ignore it an...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Failed to build xformers from wheel even though they are already present I tried to install vllm in a fresh Conda environment today. It depends on xformers, but fails to build them: ``` File "C:\Users\tomas\miniconda3\e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tire installation process. More details: https://github.com/facebookresearch/xformers/issues/886#issuecomment-1762922926
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: which is required to install pyproject.toml-based projects ``` Indeed, latest xformers release fails to work on Windows. So I tried to install minimum supported version xformers 0.0.22 via pip and it succedded: ``` file...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
