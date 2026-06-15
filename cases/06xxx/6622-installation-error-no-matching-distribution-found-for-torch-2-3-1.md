# vllm-project/vllm#6622: [Installation]: ERROR: No matching distribution found for torch==2.3.1

| 字段 | 值 |
| --- | --- |
| Issue | [#6622](https://github.com/vllm-project/vllm/issues/6622) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: ERROR: No matching distribution found for torch==2.3.1

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... Traceback (most recent call last): File "/Users/asif.ali/Workspace/llama-project/collect_env.py", line 728, in main() File "/Users/asif.ali/Workspace/llama-project/collect_env.py", line 707, in main output = get_pretty_env_info() File "/Users/asif.ali/Workspace/llama-project/collect_env.py", line 702, in get_pretty_env_info return pretty_str(get_env_info()) File "/Users/asif.ali/Workspace/llama-project/collect_env.py", line 534, in get_env_info vllm_version = get_vllm_version() File "/Users/asif.ali/Workspace/llama-project/collect_env.py", line 266, in get_vllm_version return vllm.__version__ AttributeError: module 'vllm' has no attribute '__version__' ``` My conda env looks like: ``` ❯ conda list # packages in environment at /Users/asif.ali/anaconda3/envs/env_vllm: # # Name Version Build Channel bzip2 1.0.8 hfdf4475_7 conda-forge ca-certificates 2024.7.4 h8857fd0_0 conda-forge ccache 4.10.1 hee5fd93_0 conda-forge filelock 3.15.4 pyhd8ed1ab_0 conda-forge fsspec 2024.6.1 pyhff2d567_0 conda-forge gmp 6.3.0 hf036a51_2 conda-forge gmpy2 2.1.5 py310h0310db1_1 conda-forge icu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: ERROR: No matching distribution found for torch==2.3.1 installation;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... Traceback (most
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ```text The output of `python collect_env.py` Collecting environment information... Traceback (most recent call last): File "/Users/asif.ali/Workspace/llama-project/collect_env.py", line 728, in main() File "/Users/asif...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: osted.org/packages/c7/cf/49911ac6220ecf89aa667064c9fff64657107e999c612cf3fa3a3bb7a9dd/vllm-0.5.0.tar.gz (from https://pypi.org/simple/vllm/) (requires-python:>=3.8), version: 0.5.0 Skipping link: none of the wheel's tag...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: y3-none-macosx_10_10_x86_64.macosx_11_0_universal2.macosx_11_0_arm64.whl.metadata Using cached cmake-3.30.0-py3-none-macosx_10_10_x86_64.macosx_11_0_universal2.macosx_11_0_arm64.whl.metadata (6.1 kB) Collecting ninja Ob...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: on]: ERROR: No matching distribution found for torch==2.3.1 installation;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... Traceback (most recent call...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
