# vllm-project/vllm#8352: [Bug]: Kernel died while waiting for execute reply in Kaggle TPU VM v3-8 (2024-08-22)

| 字段 | 值 |
| --- | --- |
| Issue | [#8352](https://github.com/vllm-project/vllm/issues/8352) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Kernel died while waiting for execute reply in Kaggle TPU VM v3-8 (2024-08-22)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Follow instructions in https://docs.vllm.ai/en/stable/getting_started/tpu-installation.html#build-from-source, but - use `libopenblas-dev` instead of `libopenblas-base` because latter is not available for Debian Bookworm Run `import vllm`, kernel dies after about half a minute: ``` 129.7s | 1009 | /usr/local/lib/python3.10/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html -- | -- | -- 129.7s | 1010 | from .autonotebook import tqdm as notebook_tqdm 129.7s | 1011 | 129.7s | 1012 | /usr/local/lib/python3.10/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html 129.7s | 1013 | from .autonotebook import tqdm as notebook_tqdm 141.7s | 1014 | Kernel died while waiting for execute reply. 141.8s | 1015 | Traceback (most recent call last): 141.8s | 1016 | File " ", line 1, in 141.8s | 1017 | File "/usr/local/lib/python3.10/site-packages/papermill/execute.py", line 116, in execute_notebook 141.8s | 1018 | nb =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ollow instructions in https://docs.vllm.ai/en/stable/getting_started/tpu-installation.html#build-from-source, but - use `libopenblas-dev` instead of `libopenblas-base` because latter is not available for Debian Bookworm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Kernel died while waiting for execute reply in Kaggle TPU VM v3-8 (2024-08-22) bug ### Your current environment ### 🐛 Describe the bug Follow instructions in https://docs.vllm.ai/en/stable/getting_started/tpu-ins...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
