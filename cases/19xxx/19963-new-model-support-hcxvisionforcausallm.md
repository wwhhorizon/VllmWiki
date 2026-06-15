# vllm-project/vllm#19963: [New Model]: Support HCXVisionForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#19963](https://github.com/vllm-project/vllm/issues/19963) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support HCXVisionForCausalLM

### Issue 正文摘录

### The model to consider. https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B/discussions/18#682a9cacf85a263216f27b97 > We are currently working on supporting vLLM (including the VLM module), and we expect to have support ready by the end of June. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Support HCXVisionForCausalLM ### The model to consider. https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B ### The closest model vllm already supports. _No response_ ### What's your
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
