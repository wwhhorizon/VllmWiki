# vllm-project/vllm#39576: [Bug]: vLLM inference produces garbled output on long context for SFT'd Qwen3-14B (short context is normal)

| 字段 | 值 |
| --- | --- |
| Issue | [#39576](https://github.com/vllm-project/vllm/issues/39576) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM inference produces garbled output on long context for SFT'd Qwen3-14B (short context is normal)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1. System Info 1.1 training env - llamafactory-cli version 0.9.5.dev0 - transformers Version: 5.2.0 - Python 3.12.12 - torch 2.8.0+cu128 - torchaudio 2.8.0+cu128 - torchdata 0.11.0 - torchvision 0.23.0+cu128 1.2 Inference env - vllm docker：vllm/vllm-openai:v0.18.0 - vllm docker transformers Version: 4.57.6 2、Reproduce step 2.1 After SFT of the Qwen3-14B model, the parameters for merging and exporting are configured as follows: model_name_or_path: ~/work/basemodel/Qwen3-14B adapter_name_or_path: saves/qwen3-14b-g3.0/train template: qwen3 trust_remote_code: true export export_dir: saves/qwen3-14b-g3.0/export export_size: 5 export_device: auto export_legacy_format: false 2.2 The following error occurs when loading the exported model in vLLM for the first time: Upon starting the merged model on vLLM 0.18.0, an error is raised indicating that a specific parameter in tokenizer_config.json is expected to be a dict {}, but a list [] was provided: "extra_special_tokens": [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " ], 2.3 I referenced the original Qwen3-14B tokenizer_config.json and changed extra_special_tokens to add...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vLLM inference produces garbled output on long context for SFT'd Qwen3-14B (short context is normal) bug ### Your current environment ### 🐛 Describe the bug 1. System Info 1.1 training env - llamafactory-cli vers...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: # 🐛 Describe the bug 1. System Info 1.1 training env - llamafactory-cli version 0.9.5.dev0 - transformers Version: 5.2.0 - Python 3.12.12 - torch 2.8.0+cu128 - torchaudio 2.8.0+cu128 - torchdata 0.11.0 - torchvision 0.2...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: r：vllm/vllm-openai:v0.18.0 - vllm docker transformers Version: 4.57.6 2、Reproduce step 2.1 After SFT of the Qwen3-14B model, the parameters for merging and exporting are configured as follows: model_name_or_path: ~/work...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t?" ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: b-g3.0/export export_size: 5 export_device: auto export_legacy_format: false 2.2 The following error occurs when loading the exported model in vLLM for the first time: Upon starting the merged model on vLLM 0.18.0, an e...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
