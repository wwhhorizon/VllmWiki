# vllm-project/vllm#13745: [Installation]: unkown error while installing for docker

| 字段 | 值 |
| --- | --- |
| Issue | [#13745](https://github.com/vllm-project/vllm/issues/13745) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: unkown error while installing for docker

### Issue 正文摘录

### Your current environment ``` $ wget https://raw.githubusercontent.com/vllm-project/vllm/main/collect_env.py bash: wget: command not found ``` ``` P:\soft\programming\vllm\vllm\__init__.py:5: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from .version import __version__, __version_tuple__ # isort:skip Traceback (most recent call last): File "P:\soft\programming\vllm\collect_env.py", line 17, in from vllm.envs import environment_variables File "P:\soft\programming\vllm\vllm\__init__.py", line 9, in import torch ModuleNotFoundError: No module named 'torch' ``` I know it is not much informative, but have no idea about further actions related you question. ### How you are installing vllm ```sh docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: unkown error while installing for docker installation ### Your current environment ``` $ wget https://raw.githubusercontent.com/vllm-project/vllm/main/collect_env.py bash: wget: command not found ``` ```
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ModuleNotFoundError: No module named 'torch' ``` I know it is not much informative, but have no idea about further actions related you question. ### How you are installing vllm ```sh docker build -f Dockerfile.cpu -t vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
