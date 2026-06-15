# vllm-project/vllm#9382: [New Model]: Support Zyphra/Zamba2-7B

| 字段 | 值 |
| --- | --- |
| Issue | [#9382](https://github.com/vllm-project/vllm/issues/9382) |
| 状态 | closed |
| 标签 | new-model;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support Zyphra/Zamba2-7B

### Issue 正文摘录

### The model to consider. Announcement blog: https://www.zyphra.com/post/zamba2-7b Base model: https://huggingface.co/Zyphra/Zamba2-7B Instruct tuned: https://huggingface.co/Zyphra/Zamba2-7B-Instruct ![image](https://github.com/user-attachments/assets/bba7f100-f7cf-4284-b8b0-90ed99d9a522) ### The closest model vllm already supports. Jamba, as it is a mixture of state-space and transformers blocks > Zamba2-7B-Instruct is a hybrid model composed of state-space ([Mamba2](https://github.com/state-spaces/mamba)) and transformer blocks. ### What's your difficulty of supporting the model you want? Should be easy once Mamba2 support lands in https://github.com/vllm-project/vllm/pull/9292, however this `use_shared_attention_lora` case seems possibly complex All of the HF-compatible modeling code can be found here: https://github.com/Zyphra/transformers_zamba2/tree/main/src/transformers/models/zamba2 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Support Zyphra/Zamba2-7B new-model;unstale ### The model to consider. Announcement blog: https://www.zyphra.com/post/zamba2-7b Base model: https://huggingface.co/Zyphra/Zamba2-7B Instruct tuned: https://hug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ba2 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ady supports. Jamba, as it is a mixture of state-space and transformers blocks > Zamba2-7B-Instruct is a hybrid model composed of state-space ([Mamba2](https://github.com/state-spaces/mamba)) and transformer blocks. ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Support Zyphra/Zamba2-7B new-model;unstale ### The model to consider. Announcement blog: https://www.zyphra.com/post/zamba2-7b Base model: https://huggingface.co/Zyphra/Zamba2-7B Instruct tuned: https://hug...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
