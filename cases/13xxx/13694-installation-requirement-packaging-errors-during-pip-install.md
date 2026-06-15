# vllm-project/vllm#13694: [Installation]: requirement packaging errors during pip install

| 字段 | 值 |
| --- | --- |
| Issue | [#13694](https://github.com/vllm-project/vllm/issues/13694) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: requirement packaging errors during pip install

### Issue 正文摘录

### Your current environment Got through installation on Linux Mint Cinnamon after installing rust and cargo via linux mint repos But still got this error during the install: ERROR: huggingface-hub 0.29.1 has requirement packaging>=20.9, but you'll have packaging 20.3 which is incompatible. ERROR: transformers 4.46.3 has requirement tokenizers =0.20, but you'll have tokenizers 0.21.0 which is incompatible. ERROR: mistral-common 1.5.3 has requirement pillow>=10.3.0, but you'll have pillow 7.0.0 which is incompatible. ERROR: ray 2.10.0 has requirement protobuf!=3.19.5,>=3.15.3, but you'll have protobuf 3.6.1 which is incompatible. ERROR: datasets 3.1.0 has requirement fsspec[http] =2023.1.0, but you'll have fsspec 2025.2.0 which is incompatible. ERROR: datasets 3.1.0 has requirement tqdm>=4.66.3, but you'll have tqdm 4.66.1 which is incompatible. so when try to serve it vllm serve "microsoft/OmniParser-v2.0" or any other model gives Traceback (most recent call last): File "/home/aaronmint1/.local/bin/vllm", line 5, in from vllm.scripts import main File "/home/aaronmint1/.local/lib/python3.8/site-packages/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: requirement packaging errors during pip install installation;stale ### Your current environment Got through installation on Linux Mint Cinnamon after installing rust and cargo via linux mint repos But st
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: a linux mint repos But still got this error during the install: ERROR: huggingface-hub 0.29.1 has requirement packaging>=20.9, but you'll have packaging 20.3 which is incompatible. ERROR: transformers 4.46.3 has require...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tallation]: requirement packaging errors during pip install installation;stale ### Your current environment Got through installation on Linux Mint Cinnamon after installing rust and cargo via linux mint repos But still...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
