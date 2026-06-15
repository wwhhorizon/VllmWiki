# vllm-project/vllm#9319: [Bug]: Installed vllm successfully for AMD MI60 but inference is failing

| 字段 | 值 |
| --- | --- |
| Issue | [#9319](https://github.com/vllm-project/vllm/issues/9319) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Installed vllm successfully for AMD MI60 but inference is failing

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have 2x AMD MI60 and 1x 3060 for video output. I installed all the dependencies for vllm under ROCm successfully. However, when I try to deploy a model, I am facing an error. I ran this command in terminal: `vllm serve /media/saidp/datasets/text_generation/models/unsloth_llama-3-8b-Instruct` It seems like ROCm is missing paged_attention. And yes, I tried a clean install of VLLM again and that did not work as well. Let me know what is missing or how to fix this bug. Thanks! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Installed vllm successfully for AMD MI60 but inference is failing bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have 2x AMD MI60 and 1x 3060 for video output. I inst
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: x 3060 for video output. I installed all the dependencies for vllm under ROCm successfully. However, when I try to deploy a model, I am facing an error. I ran this command in terminal: `vllm serve /media/saidp/datasets/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;cuda;kernel;operator;quantization;sampling;triton build_error;crash;import_error;nan_i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in terminal: `vllm serve /media/saidp/datasets/text_generation/models/unsloth_llama-3-8b-Instruct` It seems like ROCm is missing paged_attention. And yes, I tried a clean install of VLLM again and that did not work as w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: D MI60 but inference is failing bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have 2x AMD MI60 and 1x 3060 for video output. I installed all the dependencies for vllm unde...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
