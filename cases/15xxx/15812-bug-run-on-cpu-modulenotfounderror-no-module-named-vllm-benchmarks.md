# vllm-project/vllm#15812: [Bug]: run on cpu:  ModuleNotFoundError: No module named 'vllm.benchmarks'

| 字段 | 值 |
| --- | --- |
| Issue | [#15812](https://github.com/vllm-project/vllm/issues/15812) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: run on cpu:  ModuleNotFoundError: No module named 'vllm.benchmarks'

### Issue 正文摘录

### Your current environment enviroment install follow: [official guide ](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html#) run： `vllm serve facebook/opt-125m` error info： > INFO 03-31 18:44:44 [__init__.py:239] Automatically detected platform cpu. Traceback (most recent call last): File "/opt/conda/envs/vllm/bin/vllm", line 33, in sys.exit(load_entry_point('vllm==0.8.3.dev136+geffc5d24.cpu', 'console_scripts', 'vllm')()) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/envs/vllm/bin/vllm", line 25, in importlib_load_entry_point return next(matches).load() ^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/envs/vllm/lib/python3.12/importlib/metadata/__init__.py", line 205, in load module = import_module(match.group('module')) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/envs/vllm/lib/python3.12/importlib/__init__.py", line 90, in import_module return _bootstrap._gcd_import(name[level:], package, level) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File " ", line 1387, in _gcd_import File " ", line 1360, in _find_and_load File " ", line 1331, in _find_and_load_unlocked File " ", line 935, in _load_unlocked File...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ule named 'vllm.benchmarks' bug ### Your current environment enviroment install follow: [official guide ](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html#) run： `vllm serve facebook/opt-125m` error...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: run on cpu: ModuleNotFoundError: No module named 'vllm.benchmarks' bug ### Your current environment enviroment install follow: [official guide ](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.htm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ks' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ^^^^^^^^^^^^^^^^^^ File "/opt/conda/envs/vllm/lib/python3.12/importlib/metadata/__init__.py", line 205, in load module = import_module(match.group('module')) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/envs/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
