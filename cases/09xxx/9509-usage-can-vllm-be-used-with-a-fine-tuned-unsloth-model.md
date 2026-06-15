# vllm-project/vllm#9509: [Usage]: Can VLLM be used with a fine-tuned unsloth model

| 字段 | 值 |
| --- | --- |
| Issue | [#9509](https://github.com/vllm-project/vllm/issues/9509) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can VLLM be used with a fine-tuned unsloth model

### Issue 正文摘录

### Your current environment ```text from vllm import LLM from unsloth import FastLanguageModel llm, tokenizer = FastLanguageModel.from_pretrained( model_name=model_path, max_seq_length=2048, dtype=torch.float16, load_in_4bit=True, device_map=device ) FastLanguageModel.for_inference(llm) llm = LLM(model=llm) ``` ### How would you like to use vllm I want to run inference on a finetuned unsloth model ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: from_pretrained( model_name=model_path, max_seq_length=2048, dtype=torch.float16, load_in_4bit=True, device_map=device ) FastLanguageModel.for_inference(llm) llm = LLM(model=llm) ``` ### How would you like to use vllm I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uned unsloth model usage ### Your current environment ```text from vllm import LLM from unsloth import FastLanguageModel llm, tokenizer = FastLanguageModel.from_pretrained( model_name=model_path, max_seq_length=2048, dt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: del ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Usage]: Can VLLM be used with a fine-tuned unsloth model usage ### Your current environment ```text from vllm import LLM from unsloth import FastLanguageModel llm, tokenizer = FastLanguageModel.from_pretrained( model_n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Can VLLM be used with a fine-tuned unsloth model usage ### Your current environment ```text from vllm import LLM from unsloth import FastLanguageModel llm, tokenizer = FastLanguageModel.from_pretrained( model_n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
