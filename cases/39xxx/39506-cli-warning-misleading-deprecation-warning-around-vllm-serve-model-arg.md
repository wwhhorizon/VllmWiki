# vllm-project/vllm#39506: [CLI / Warning] Misleading deprecation warning around `vllm serve --model ...` arg

| 字段 | 值 |
| --- | --- |
| Issue | [#39506](https://github.com/vllm-project/vllm/issues/39506) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CLI / Warning] Misleading deprecation warning around `vllm serve --model ...` arg

### Issue 正文摘录

### 📚 The doc issue Hey, I've been seeing the following warning for a while `WARNING [argparse_utils.py:191] With vllm serve, you should provide the model as a positional argument or in a config file instead of via the --model option. The --model option will be removed in v0.13.`, and I was wondering when will that be really deprecated (if it will ever be), and if so to update the warning message for the actual version in which it'll be finally deprecated. See https://github.com/vllm-project/vllm/blob/8d0f908b98cd692204753421dd39695f3094c8f0/vllm/utils/argparse_utils.py#L186-L217. Thanks in advance 🤗 P.S. Apologies, but I thought that "documentation" was the best category that fits within this issue as neither of the existing categories matches this issue AFAIK, but apologies if that's the case! ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CLI / Warning] Misleading deprecation warning around `vllm serve --model ...` arg documentation ### 📚 The doc issue Hey, I've been seeing the following warning for a while `WARNING [argparse_utils.py:191] With vllm ser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: it will ever be), and if so to update the warning message for the actual version in which it'll be finally deprecated. See https://github.com/vllm-project/vllm/blob/8d0f908b98cd692204753421dd39695f3094c8f0/vllm/utils/ar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
