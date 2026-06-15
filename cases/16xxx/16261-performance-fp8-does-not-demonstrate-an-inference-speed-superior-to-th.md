# vllm-project/vllm#16261: [Performance]: FP8 does not demonstrate an inference speed superior to that of FP16

| 字段 | 值 |
| --- | --- |
| Issue | [#16261](https://github.com/vllm-project/vllm/issues/16261) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: FP8 does not demonstrate an inference speed superior to that of FP16

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression As the [blog](https://developers.redhat.com/articles/2024/07/15/vllm-brings-fp8-inference-open-source-community) said, FP8 can bring about **3x throughput improvement** compared with FP16. ![Image](https://github.com/user-attachments/assets/bcecca4b-b2b4-49a7-b817-e7377e5ba15c) However, we compared the performance of FP16 and FP8 on vllm 0.8.0, the number of model params is about 80B and the resuts is blow. ![Image](https://github.com/user-attachments/assets/d191f86f-0696-427a-8b4f-340c3d90e301) Reproduce: 1. Quantize FP8 model offline: https://github.com/vllm-project/llm-compressor/tree/main/examples/quantization_w8a8_fp8#2-apply-quantization 2. Deploy FP8 model with TP8 ```python # 1. Quant recipe recipe = QuantizationModifier( targets="Linear", scheme="FP8_DYNAMIC", ignore=["lm_head"]) # 2. Deploy command vllm serve /model/path/to/FP8-Dynamic \ --trust-remote-code --host "0.0.0.0" --port 9101 --tensor-parallel-size 8 ``` ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before subm...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression As the [blog](https://developers.redhat.com/articles/2024/07/15/vllm-brings-fp8-inference-open-source-community) said, FP8 can bring abou...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Performance]: FP8 does not demonstrate an inference speed superior to that of FP16 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression As the [blog](https://develope...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ithub.com/user-attachments/assets/d191f86f-0696-427a-8b4f-340c3d90e301) Reproduce: 1. Quantize FP8 model offline: https://github.com/vllm-project/llm-compressor/tree/main/examples/quantization_w8a8_fp8#2-apply-quantizat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: -apply-quantization 2. Deploy FP8 model with TP8 ```python # 1. Quant recipe recipe = QuantizationModifier( targets="Linear", scheme="FP8_DYNAMIC", ignore=["lm_head"]) # 2. Deploy command vllm serve /model/path/to/FP8-D...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
