# vllm-project/vllm#4554: [Usage]: Experiencing weird import bugs and errors after installing with pip install -e .

| 字段 | 值 |
| --- | --- |
| Issue | [#4554](https://github.com/vllm-project/vllm/issues/4554) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Experiencing weird import bugs and errors after installing with pip install -e .

### Issue 正文摘录

### Your current environment ```Collecting environment information... Traceback (most recent call last): File "/home/yangzhiyu/workspace/open-long-agent/collect_env.py", line 721, in main() File "/home/yangzhiyu/workspace/open-long-agent/collect_env.py", line 700, in main output = get_pretty_env_info() File "/home/yangzhiyu/workspace/open-long-agent/collect_env.py", line 695, in get_pretty_env_info return pretty_str(get_env_info()) File "/home/yangzhiyu/workspace/open-long-agent/collect_env.py", line 532, in get_env_info vllm_version = get_vllm_version() File "/home/yangzhiyu/workspace/open-long-agent/collect_env.py", line 264, in get_vllm_version return vllm.__version__ AttributeError: module 'vllm' has no attribute '__version__' ``` ### How would you like to use vllm #594 Like in the previous issue, I tried to install from the repo using pip install -e . and had trouble importing LLM. ```from vllm import LLM Traceback (most recent call last): File "", line 1, in ImportError: cannot import name 'LLM' from 'vllm' (unknown location) ``` I got around this issue by using: > 尝试一下使用 from vllm.entrypoints.llm import LLM from vllm.sampling_params import SamplingParams However, I ran into...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: Experiencing weird import bugs and errors after installing with pip install -e . usage;stale ### Your current environment ```Collecting environment information... Traceback (most recent call last): File "/home/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: . usage;stale ### Your current environment ```Collecting environment information... Traceback (most recent call last): File "/home/yangzhiyu/workspace/open-long-agent/collect_env.py", line 721, in main() File "/home/yan...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eird import bugs and errors after installing with pip install -e . usage;stale ### Your current environment ```Collecting environment information... Traceback (most recent call last): File "/home/yangzhiyu/workspace/ope...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
