# vllm-project/vllm#12893: [Installation]: vllm > 0.6 on Apple Device (Mac) 

| 字段 | 值 |
| --- | --- |
| Issue | [#12893](https://github.com/vllm-project/vllm/issues/12893) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: vllm > 0.6 on Apple Device (Mac) 

### Issue 正文摘录

### Your current environment ``` python collect_env.py ``` ```text Traceback (most recent call last): File "/Users/simo/Developer/test-vllm/collect_env.py", line 17, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm ``` --- When I able to install vllm main() File "/Users/simo/Developer/test-vllm/collect_env.py", line 746, in main output = get_pretty_env_info() ^^^^^^^^^^^^^^^^^^^^^ File "/Users/simo/Developer/test-vllm/collect_env.py", line 741, in get_pretty_env_info return pretty_str(get_env_info()) ^^^^^^^^^^^^^^ File "/Users/simo/Developer/test-vllm/collect_env.py", line 539, in get_env_info pip_version, pip_list_output = get_pip_packages(run_lambda) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/simo/Developer/test-vllm/collect_env.py", line 493, in get_pip_packages out = run_with_pip([sys.executable, '-mpip']) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/Users/simo/Developer/test-vllm/collect_env.py", line 489, in run_with_pip return "\n".join(line for line in out.splitlines() ^^^^^^^^^^^^^^ AttributeError: 'NoneType' object has no attribute 'splitlines' ``` ### How you are installing vllm **Platform** - Macbook Pro M1 Max 32GB - Sequoia...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: vllm > 0.6 on Apple Device (Mac) installation ### Your current environment ``` python collect_env.py ``` ```text Traceback (most recent call last): File "/Users/simo/Developer/test-vllm/collect_env.py"
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ```text Traceback (most recent call last): File "/Users/simo/Developer/test-vllm/collect_env.py", line 17, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm ``` --- When I able to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
