# vllm-project/vllm#11153: [Usage]: Support for Specifying ```extra_body``` Parameters in vLLM Terminal Commands for structuring the JSON output 

| 字段 | 值 |
| --- | --- |
| Issue | [#11153](https://github.com/vllm-project/vllm/issues/11153) |
| 状态 | closed |
| 标签 | structured-output;usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Support for Specifying ```extra_body``` Parameters in vLLM Terminal Commands for structuring the JSON output 

### Issue 正文摘录

Hi there, I understand that vLLM currently supports [outlines-dev/outlines](https://github.com/outlines-dev/outlines), [mlc-ai/xgrammar](https://github.com/mlc-ai/xgrammar), and [noamgat/lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) for guided decoding. I would like to directly configure guided decoding via the terminal using the following command: `vllm serve meta-llama/Llama-3.1-8B-Instruct --device neuron --tensor-parallel-size 2 --block-size 8 --max-model-len 4096 --max-num-seqs 32 --guided-decoding-backend lm-format-enforcer ` The challenge I’m facing is how to specify ```extra_body``` parameters such as: `extra_body={"guided_regex": "\w+@\w+\.com\n", "stop": ["\n"]} ` directly from the terminal, so I don’t need to modify any other code. Is there a way to pass these parameters via the CLI, or do I need to rely exclusively on the Python API for such configurations? Any advice or pointers on this would be greatly appreciated! ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https:/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: , [mlc-ai/xgrammar](https://github.com/mlc-ai/xgrammar), and [noamgat/lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) for guided decoding. I would like to directly configure guided decoding via the te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: --block-size 8 --max-model-len 4096 --max-num-seqs 32 --guided-decoding-backend lm-format-enforcer ` The challenge I’m facing is how to specify ```extra_body``` parameters such as: `extra_body={"guided_regex": "\w+@\w+\...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: Support for Specifying ```extra_body``` Parameters in vLLM Terminal Commands for structuring the JSON output structured-output;usage;stale Hi there, I understand that vLLM currently supports [outlines-dev/outli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: a-llama/Llama-3.1-8B-Instruct --device neuron --tensor-parallel-size 2 --block-size 8 --max-model-len 4096 --max-num-seqs 32 --guided-decoding-backend lm-format-enforcer ` The challenge I’m facing is how to specify ```e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
