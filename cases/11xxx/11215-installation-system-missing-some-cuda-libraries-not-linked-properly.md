# vllm-project/vllm#11215: [Installation]: System missing some CUDA libraries/not linked properly?

| 字段 | 值 |
| --- | --- |
| Issue | [#11215](https://github.com/vllm-project/vllm/issues/11215) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: System missing some CUDA libraries/not linked properly?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Traceback (most recent call last): File "/home/shxjames/llm-eval/collect_env.py", line 15, in from vllm.envs import environment_variables File "/home/shxjames/.conda/envs/inference/lib/python3.10/site-packages/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/home/shxjames/.conda/envs/inference/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 8, in import torch File "/home/shxjames/.conda/envs/inference/lib/python3.10/site-packages/torch/__init__.py", line 367, in from torch._C import * # noqa: F403 ImportError: /home/shxjames/.conda/envs/inference/lib/python3.10/site-packages/torch/lib/../../nvidia/cusparse/lib/libcusparse.so.12: undefined symbol: __nvJitLinkComplete_12_4, version libnvJitLink.so.12 ``` ### How you are installing vllm ```sh conda create -n inference python=3.10 -y conda activate inference pip install vllm ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: System missing some CUDA libraries/not linked properly? installation;stale ### Your current environment ```text The output of `python collect_env.py` Traceback (most recent call last): File "/home/shxj
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: System missing some CUDA libraries/not linked properly? installation;stale ### Your current environment ```text The output of `python collect_env.py` Traceback (most recent call last): File "/home/shxjam...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t_env.py` Traceback (most recent call last): File "/home/shxjames/llm-eval/collect_env.py", line 15, in from vllm.envs import environment_variables File "/home/shxjames/.conda/envs/inference/lib/python3.10/site-packages...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n]: System missing some CUDA libraries/not linked properly? installation;stale ### Your current environment ```text The output of `python collect_env.py` Traceback (most recent call last): File "/home/shxjames/llm-eval/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
