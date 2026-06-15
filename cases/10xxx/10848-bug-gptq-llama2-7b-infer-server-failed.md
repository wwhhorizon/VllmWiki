# vllm-project/vllm#10848: [Bug]: GPTQ llama2-7b infer server failed!!!

| 字段 | 值 |
| --- | --- |
| Issue | [#10848](https://github.com/vllm-project/vllm/issues/10848) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPTQ llama2-7b infer server failed!!!

### Issue 正文摘录

### Your current environment I am currently performing gptq quantization on the llama2-7b-hf model. The model can be quantized successfully, but the following problems are encountered during inference: `vllm serve shakechen/Llama-2-7b-hf-W8A8-Dynamic-Per-Token --quantization gptq` ![15559753edb202cb72e64026f1a6d5bd](https://github.com/user-attachments/assets/fc6d3366-4343-491b-9037-ceca8dc38962) The model conversion process is as follows: ```from datasets import load_dataset from llmcompressor.transformers import oneshot from llmcompressor.modifiers.quantization import GPTQModifier from llmcompressor.modifiers.smoothquant import SmoothQuantModifier MODEL_ID = "shakechen/Llama-2-7b-hf" NUM_CALIBRATION_SAMPLES=512 MAX_SEQUENCE_LENGTH=4096 DATASET_NAME = "HuggingFaceH4/ultrachat_200k" QUANT_SCHEME = "W8A8" SAVE_DIR = "shakechen/Llama-2-7b-hf-W8A8-Dynamic-Per-Token" model = AutoModelForCausalLM.from_pretrained( MODEL_ID, device_map="auto", torch_dtype="auto", ) tokenizer = AutoTokenizer.from_pretrained(MODEL_ID) ds = load_dataset(DATASET_NAME, split="train_sft") ds = ds.shuffle(seed=42).select(range(NUM_CALIBRATION_SAMPLES)) def preprocess(example): messages = example["messages"] conv...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: er-attachments/assets/fc6d3366-4343-491b-9037-ceca8dc38962) The model conversion process is as follows: ```from datasets import load_dataset from llmcompressor.transformers import oneshot from llmcompressor.modifiers.qu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: GPTQ llama2-7b infer server failed!!! bug;stale ### Your current environment I am currently performing gptq quantization on the llama2-7b-hf model. The model can be quantized successfully, but the following probl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ! bug;stale ### Your current environment I am currently performing gptq quantization on the llama2-7b-hf model. The model can be quantized successfully, but the following problems are encountered during inference: `vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: .modifiers.quantization import GPTQModifier from llmcompressor.modifiers.smoothquant import SmoothQuantModifier MODEL_ID = "shakechen/Llama-2-7b-hf" NUM_CALIBRATION_SAMPLES=512 MAX_SEQUENCE_LENGTH=4096 DATASET_NAME = "H...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: it). def tokenize(sample): return tokenizer(sample["text"], padding=False, max_length=MAX_SEQUENCE_LENGTH, truncation=True, add_special_tokens=False) ds = ds.map(tokenize, remove_columns=ds.column_names) recipe = [ Smoo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
