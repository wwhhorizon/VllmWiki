# vllm-project/vllm#18131: [Usage]: how to add --compilation-config to vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#18131](https://github.com/vllm-project/vllm/issues/18131) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to add --compilation-config to vllm serve

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm vllm serve model_path --compilation-config "{'cudagraph_capture_sizes': [1, 2, 4, 8]}" returns error below: usage: vllm serve [model_tag] [options] vllm serve: error: argument --compilation-config/-O: invalid value: "{'cudagraph_capture_sizes': [1, 2, 4, 8]}" @youkaichao ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ould you like to use vllm vllm serve model_path --compilation-config "{'cudagraph_capture_sizes': [1, 2, 4, 8]}" returns error below: usage: vllm serve [model_tag] [options] vllm serve: error: argument --compilation-con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: how to add --compilation-config to vllm serve usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm vllm serve model_path --compilation-config "...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
