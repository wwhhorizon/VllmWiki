# vllm-project/vllm#10849: [Feature]: add DoRA support

| 字段 | 值 |
| --- | --- |
| Issue | [#10849](https://github.com/vllm-project/vllm/issues/10849) |
| 状态 | open |
| 标签 | feature request;keep-open |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: add DoRA support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The recent ICML'24 Oral paper, DoRA, has shown consistent improvement over LoRA on various tasks (LLM, MLLM, etc.) and backbones (LLaMA, LLaVA, etc.) [Code] https://github.com/NVlabs/DoRA DoRA has also been integrated into various open-source library/framework: * Hugging Face: [peft](https://huggingface.co/docs/peft/en/developer_guides/lora), [diffusers](https://github.com/huggingface/diffusers/blob/main/examples/dreambooth/README_sdxl.md) * Apple: [MLX](https://github.com/ml-explore/mlx) * Meta: [torchtune](https://github.com/pytorch/torchtune/releases/tag/v0.3.0) * NVIDIA: [NeMo](https://github.com/NVIDIA/NeMo/pulls?q=dora) * [Unsloth AI](https://unsloth.ai/): [unsloth](https://github.com/unslothai/unsloth) * [Answer.AI](https://www.answer.ai/posts/2024-04-26-fsdp-qdora-llama3.html): [QDoRA + FSDP](https://github.com/AnswerDotAI/fsdp_qlora) * [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) * [LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS) * ..., etc. ![teaser_v2_bg](https://github.com/user-attachments/assets/ea77fdbb-06d8-4ecb-89a2-922335e33362) ### Alternatives _No response_ ### Additional context _No response_ ### Before s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: improvement over LoRA on various tasks (LLM, MLLM, etc.) and backbones (LLaMA, LLaVA, etc.) [Code] https://github.com/NVlabs/DoRA DoRA has also been integrated into various open-source library/framework: * Hugging Face:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .3.0) * NVIDIA: [NeMo](https://github.com/NVIDIA/NeMo/pulls?q=dora) * [Unsloth AI](https://unsloth.ai/): [unsloth](https://github.com/unslothai/unsloth) * [Answer.AI](https://www.answer.ai/posts/2024-04-26-fsdp-qdora-ll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: add DoRA support feature request;keep-open ### 🚀 The feature, motivation and pitch The recent ICML'24 Oral paper, DoRA, has shown consistent improvement over LoRA on various tasks (LLM, MLLM, etc.) and backbo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
