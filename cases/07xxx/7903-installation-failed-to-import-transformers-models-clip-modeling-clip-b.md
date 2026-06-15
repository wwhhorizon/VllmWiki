# vllm-project/vllm#7903: [Installation]: Failed to import transformers.models.clip.modeling_clip because of the following error (look up to see its traceback): libcudart.so.12: cannot open shared object file: No such file or directory

| 字段 | 值 |
| --- | --- |
| Issue | [#7903](https://github.com/vllm-project/vllm/issues/7903) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Failed to import transformers.models.clip.modeling_clip because of the following error (look up to see its traceback): libcudart.so.12: cannot open shared object file: No such file or directory

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: Failed to import transformers.models.clip.modeling_clip because of the following error (look up to see its traceback): libcudart.so.12: cannot open shared object file: No such file or directory installat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g_clip because of the following error (look up to see its traceback): libcudart.so.12: cannot open shared object file: No such file or directory installation;stale ### Your current environment ```text The output of `pyt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Installation]: Failed to import transformers.models.clip.modeling_clip because of the following error (look up to see its traceback): libcudart.so.12: cannot open shared object file: No such file or directory installat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : cannot open shared object file: No such file or directory installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip install -vvv vllm `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
