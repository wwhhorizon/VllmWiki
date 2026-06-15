# vllm-project/vllm#488: AssertionError for WizardCoder-15B-V1.0 Again

| 字段 | 值 |
| --- | --- |
| Issue | [#488](https://github.com/vllm-project/vllm/issues/488) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AssertionError for WizardCoder-15B-V1.0 Again

### Issue 正文摘录

2023.07.18 I pulled the latest code and ran: `pip3 install . -e` `python3 -c "from vllm import LLM;llm = LLM('/root//models/wizardcoder', tensor_parallel_size = 2)"` and I got: `AssertionError: transformer.h.0.attn.c_attn.weight shape mismatch between model and checkpoint: torch.Size([3200, 6144]) != torch.Size([3328, 6144])` It seems that: ``` param.shape[0] = (6144 + 128 * 2) / tp_size = 3200 loaded_weight.shape[0] = 6144 / tp_size + 128 * 2 = 3328 ``` under MQA setting, which causes mismatch. can you reproduce this? (or am I missing something)

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ` and I got: `AssertionError: transformer.h.0.attn.c_attn.weight shape mismatch between model and checkpoint: torch.Size([3200, 6144]) != torch.Size([3328, 6144])` It seems that: ``` param.shape[0] = (6144 + 128 * 2) /...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: r-15B-V1.0 Again bug 2023.07.18 I pulled the latest code and ran: `pip3 install . -e` `python3 -c "from vllm import LLM;llm = LLM('/root//models/wizardcoder', tensor_parallel_size = 2)"` and I got: `AssertionError: tran...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: and I got: `AssertionError: transformer.h.0.attn.c_attn.weight shape mismatch between model and checkpoint: torch.Size([3200, 6144]) != torch.Size([3328, 6144])` It seems that: ``` param.shape[0] = (6144 + 128 * 2) / tp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: `pip3 install . -e` `python3 -c "from vllm import LLM;llm = LLM('/root//models/wizardcoder', tensor_parallel_size = 2)"` and I got: `AssertionError: transformer.h.0.attn.c_attn.weight shape mismatch between model and ch...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ertionError for WizardCoder-15B-V1.0 Again bug 2023.07.18 I pulled the latest code and ran: `pip3 install . -e` `python3 -c "from vllm import LLM;llm = LLM('/root//models/wizardcoder', tensor_parallel_size = 2)"` and I...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
