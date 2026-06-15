# vllm-project/vllm#27602: [Bug]: quantized medgemma-27b-text-it producing garbage outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#27602](https://github.com/vllm-project/vllm/issues/27602) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: quantized medgemma-27b-text-it producing garbage outputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running a bits and bytes quantized version of medgemma from huggingface with the latest version of vllm (0.11.0). The llm initially starts to answer the prompt correctly but after a few lines it starts to generate nonsensical or repeating outputs including special characters. I tried downgrading to vllm 0.9.2 with transformers version 4.53.3 after reviewing other issues but these produced complete nonsensical outputs, and do not support structured outputs. I observed this behavior using both structured and unstructured outputs for different prompts and output lengths. ```python model = "unsloth/medgemma-27b-text-it-unsloth-bnb-4bit" sample_prompt = ("Describe the different types of lung nodules and how their follow up recommendations differ based on established guidelines (LRADS and Fleischner Society).") sampling_params = SamplingParams(temperature=0.1, max_tokens=2048, repetition_penalty=1.9) llm = LLM(model=model, dtype=torch.bfloat16, quantization="bitsandbytes") outputs = llm.generate(prompts=sample_prompt, sampling_params=sampling_params) ``` Example output: ### Before submitting a new issue... - [x] Make sure you alre...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: quantized medgemma-27b-text-it producing garbage outputs bug;stale ### Your current environment ### 🐛 Describe the bug I am running a bits and bytes quantized version of medgemma from huggingface with the latest...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: quantized medgemma-27b-text-it producing garbage outputs bug;stale ### Your current environment ### 🐛 Describe the bug I am running a bits and bytes quantized version of medgemma from huggingface with the latest...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: quantized medgemma-27b-text-it producing garbage outputs bug;stale ### Your current environment ### 🐛 Describe the bug I am running a bits and bytes quantized version of medgemma from huggingface with the latest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: outputs for different prompts and output lengths. ```python model = "unsloth/medgemma-27b-text-it-unsloth-bnb-4bit" sample_prompt = ("Describe the different types of lung nodules and how their follow up recommendations...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
