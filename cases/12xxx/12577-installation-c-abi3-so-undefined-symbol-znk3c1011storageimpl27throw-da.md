# vllm-project/vllm#12577: [Installation]: _C.abi3.so:  undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

| 字段 | 值 |
| --- | --- |
| Issue | [#12577](https://github.com/vllm-project/vllm/issues/12577) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: _C.abi3.so:  undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

### Issue 正文摘录

### Your current environment ```text WARNING 01-30 20:57:18 _custom_ops.py:14] Failed to import from vllm._C with ImportError('/home/orin/tools/anaconda3/envs/sglang/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv') Collecting environment information... Traceback (most recent call last): File "/home/orin/collect_env.py", line 765, in main() File "/home/orin/collect_env.py", line 744, in main output = get_pretty_env_info() File "/home/orin/collect_env.py", line 739, in get_pretty_env_info return pretty_str(get_env_info()) File "/home/orin/collect_env.py", line 568, in get_env_info vllm_version = get_vllm_version() File "/home/orin/collect_env.py", line 273, in get_vllm_version from vllm import __version__, __version_tuple__ ImportError: cannot import name '__version_tuple__' from 'vllm' (/home/orin/tools/anaconda3/envs/sglang/lib/python3.10/site-packages/vllm/__init__.py) ``` ### How you are installing vllm build from source, tag: `0.5.3.post1+cu118` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: _C.abi3.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv installation ### Your current environment ```text WARNING 01-30 20:57:18 _custom_ops.py:14] Failed to import from vllm._
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 18` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 011StorageImpl27throw_data_ptr_access_errorEv') Collecting environment information... Traceback (most recent call last): File "/home/orin/collect_env.py", line 765, in main() File "/home/orin/collect_env.py", line 744,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
