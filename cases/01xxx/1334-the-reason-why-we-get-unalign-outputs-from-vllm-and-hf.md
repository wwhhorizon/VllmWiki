# vllm-project/vllm#1334: The reason why we get unalign outputs from vllm and hf?

| 字段 | 值 |
| --- | --- |
| Issue | [#1334](https://github.com/vllm-project/vllm/issues/1334) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> The reason why we get unalign outputs from vllm and hf?

### Issue 正文摘录

Hey guys! Have you ever noticed that the outputs from vllm and hf is unalign even if you use the greedy search strategy? I tried to run the test scripts with pytest in vllm project: [https://github.com/vllm-project/vllm/blob/main/tests/kernels/test_attention.py](url) [https://github.com/vllm-project/vllm/blob/main/tests/kernels/test_layernorm.py](url) yes, they were all passed. then I found the assert expression is like this: `assert torch.allclose(output, ref_output, atol=1e-3, rtol=1e-5)` `assert torch.allclose(out, ref_out, atol=1e-2, rtol=1e-5)` Then I changed the atol to 1e-4 and 1e-3, the tests failed! So I wonder, is it normal to have such a big numerical difference between vllm cuda operators and torch operators? That's why when I used baichuan-13B to run the model test script, it failed and I found that the front part of the two generated sentences are the same but diverged in the middle. I guess it's because the numerical difference will become bigger and bigger with the inference steps? So is there any way to solve this problem?

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: ere all passed. then I found the assert expression is like this: `assert torch.allclose(output, ref_output, atol=1e-3, rtol=1e-5)` `assert torch.allclose(out, ref_out, atol=1e-2, rtol=1e-5)` Then I changed the atol to 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hat the outputs from vllm and hf is unalign even if you use the greedy search strategy? I tried to run the test scripts with pytest in vllm project: [https://github.com/vllm-project/vllm/blob/main/tests/kernels/test_att...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: The reason why we get unalign outputs from vllm and hf? Hey guys! Have you ever noticed that the outputs from vllm and hf is unalign even if you use the greedy search strategy? I tried to run the test scripts with pytes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: o solve this problem? correctness model_support cuda;kernel;operator env_dependency Hey guys! Have you ever noticed that the outputs from vllm and hf is unalign even if you use the greedy search strategy?
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: unalign even if you use the greedy search strategy? I tried to run the test scripts with pytest in vllm project: [https://github.com/vllm-project/vllm/blob/main/tests/kernels/test_attention.py](url) [https://github.com/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
