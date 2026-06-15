# vllm-project/vllm#11128: [Bug]: vllm 0.6.4 部署 MiniCPM-V_2_6_awq_int4 报错

| 字段 | 值 |
| --- | --- |
| Issue | [#11128](https://github.com/vllm-project/vllm/issues/11128) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm 0.6.4 部署 MiniCPM-V_2_6_awq_int4 报错

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm 0.6.4 部署 [MiniCPM-V_2_6_awq_int4](https://www.modelscope.cn/models/linglingdan/MiniCPM-V_2_6_awq_int4) 报错。错误信息如上。另外，也尝试用vllm0.6.4 部署 MiniCPM-V_2_6 的 bnb、gptq int4量化版本，均未成功。 但vllm 0.5.4 部署 [MiniCPM-V_2_6_awq_int4](https://www.modelscope.cn/models/linglingdan/MiniCPM-V_2_6_awq_int4) 可以成功。 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: vllm 0.6.4 部署 MiniCPM-V_2_6_awq_int4 报错 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm 0.6.4 部署 [MiniCPM-V_2_6_awq_int4](https://www.modelscope.cn/models/lingling...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 成功。 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .4 部署 MiniCPM-V_2_6_awq_int4 报错 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm 0.6.4 部署 [MiniCPM-V_2_6_awq_int4](https://www.modelscope.cn/models/linglingdan/MiniCPM-V_2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
