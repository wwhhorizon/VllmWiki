# vllm-project/vllm#14538: [Bug]: vLLM-GPU only uses 2 of the 28 CPU cores (alway @ >100%) when TPP=2

| 字段 | 值 |
| --- | --- |
| Issue | [#14538](https://github.com/vllm-project/vllm/issues/14538) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM-GPU only uses 2 of the 28 CPU cores (alway @ >100%) when TPP=2

### Issue 正文摘录

### Your current environment I am using: Nvidia 2*H100 Linux Ubuntu amd64 AMD EPYC 9545 48-Core Processor (vLMM only uses 2 cores) Using latest vLLM container image ### 🐛 Describe the bug I think I tried every parameter/attribute in order to try my vLLM model running on 2 H100 GPU's ("--tensor-parallel-size", "2", with CUDA_VISIBLE_DEVICES=2,3) run on more than 2 of 48 CPU cores I have. The two CPU's are constantly at >100% creating a bottleneck. I tried combinations of some/all below: "--gpu_memory_utilization", "1.00" OMP_NUM_THREADS=12 VLLM_CPU_OMP_THREADS_BIND=12-23 type bfloat 16 Tried loading different models (32B, 70B) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: >100%) when TPP=2 bug ### Your current environment I am using: Nvidia 2*H100 Linux Ubuntu amd64 AMD EPYC 9545 48-Core Processor (vLMM only uses 2 cores) Using latest vLLM container image ### 🐛 Describe the bug I think I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: using: Nvidia 2*H100 Linux Ubuntu amd64 AMD EPYC 9545 48-Core Processor (vLMM only uses 2 cores) Using latest vLLM container image ### 🐛 Describe the bug I think I tried every parameter/attribute in order to try my vLLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: u amd64 AMD EPYC 9545 48-Core Processor (vLMM only uses 2 cores) Using latest vLLM container image ### 🐛 Describe the bug I think I tried every parameter/attribute in order to try my vLLM model running on 2 H100 GPU's (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
