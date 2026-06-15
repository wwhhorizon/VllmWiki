# vllm-project/vllm#10300: [Bug]: undefined symbol: __nvJitLinkComplete_12_4, version libnvJitLink.so.12

| 字段 | 值 |
| --- | --- |
| Issue | [#10300](https://github.com/vllm-project/vllm/issues/10300) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: undefined symbol: __nvJitLinkComplete_12_4, version libnvJitLink.so.12

### Issue 正文摘录

### Your current environment i cannot execute collect_env.py because of this error. in my another environment: torch is 2.4.0 and the version of vllm is `0.6.3.post1` which works fine. ### Model Input Dumps _No response_ ### 🐛 Describe the bug following installation guide: https://docs.vllm.ai/en/stable/getting_started/installation.html#install-the-latest-code `vllm version: 0.6.3.post2.dev386+g0b8bb86b` however, it forces the installation of torch to be `2.5.1` which causes the error : > Traceback (most recent call last): > File "/home/ubuntu/vllm/collect_env.py", line 15, in > from vllm.envs import environment_variables > File "/home/ubuntu/vllm/vllm/__init__.py", line 3, in > from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs > File "/home/ubuntu/vllm/vllm/engine/arg_utils.py", line 8, in > import torch > File "/opt/conda/envs/vllmsource/lib/python3.11/site-packages/torch/__init__.py", line 367, in > from torch._C import * # noqa: F403 > ^^^^^^^^^^^^^^^^^^^^^^ > ImportError: /opt/conda/envs/vllmsource/lib/python3.11/site-packages/torch/lib/../../nvidia/cusparse/lib/libcusparse.so.12: undefined symbol: __nvJitLinkComplete_12_4, version libnvJitLink.so.12 ### Before su...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: undefined symbol: __nvJitLinkComplete_12_4, version libnvJitLink.so.12 bug;stale ### Your current environment i cannot execute collect_env.py because of this error. in my another environment: torch is 2.4.0 and t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .12 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is 2.4.0 and the version of vllm is `0.6.3.post1` which works fine. ### Model Input Dumps _No response_ ### 🐛 Describe the bug following installation guide: https://docs.vllm.ai/en/stable/getting_started/installation.ht...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: defined symbol: __nvJitLinkComplete_12_4, version libnvJitLink.so.12 bug;stale ### Your current environment i cannot execute collect_env.py because of this error. in my another environment: torch is 2.4.0 and the versio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: //docs.vllm.ai/en/stable/getting_started/installation.html#install-the-latest-code `vllm version: 0.6.3.post2.dev386+g0b8bb86b` however, it forces the installation of torch to be `2.5.1` which causes the error : > Trace...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
