# vllm-project/vllm#9024: [Bug]: When I use cpu VLLM, it show [IndexError: list index out of range]

| 字段 | 值 |
| --- | --- |
| Issue | [#9024](https://github.com/vllm-project/vllm/issues/9024) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When I use cpu VLLM, it show [IndexError: list index out of range]

### Issue 正文摘录

### Your current environment ```python /root/miniconda3/lib/python3.10/site-packages/vllm-0.6.3.dev65+g7f60520d.cpu-py3.10-linux-x86_64.egg/vllm/model_executor/model_loader/weight_utils.py:424: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature. state = torch.load(bin_file, map_location="cpu") Loading pt checkpoint shards: 100% Completed | 1/1 [00:00 [rank0]: outputs = llm.gene...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytor...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: s.py:424: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will ex...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ite-packages/vllm-0.6.3.dev65+g7f60520d.cpu-py3.10-linux-x86_64.egg/vllm/model_executor/model_loader/weight_utils.py:424: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value),...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
