# vllm-project/vllm#11064: [Bug]: When I use llmcompressor to quantify the llama3 70b model to int8-a8w8,it shows ValueError: Failed to invert hessian due to numerical instability.

| 字段 | 值 |
| --- | --- |
| Issue | [#11064](https://github.com/vllm-project/vllm/issues/11064) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When I use llmcompressor to quantify the llama3 70b model to int8-a8w8,it shows ValueError: Failed to invert hessian due to numerical instability.

### Issue 正文摘录

### Your current environment When I use llmcompressor to quantify the llama3 70b model to int8-a8w8,it shows ValueError: Failed to invert hessian due to numerical instability. Consider increasing GPTQModifier.dampening_frac, increasing the number of calibration samples, or shuffling the calibration dataset,so how can i do? H20/llama3.1 70B export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 step1: pip install llmcompressor==0.3.0 from llmcompressor.transformers import SparseAutoModelForCausalLM from transformers import AutoTokenizer MODEL_ID = "/llama3_1_70B" model = SparseAutoModelForCausalLM.from_pretrained( MODEL_ID, device_map="auto", torch_dtype="auto", ) tokenizer = AutoTokenizer.from_pretrained(MODEL_ID) step2 : from datasets import load_dataset NUM_CALIBRATION_SAMPLES = 512 MAX_SEQUENCE_LENGTH = 2048 # Load and preprocess the dataset ds = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft") ds = ds.shuffle(seed=42).select(range(NUM_CALIBRATION_SAMPLES)) def preprocess(example): return {"text": tokenizer.apply_chat_template(example["messages"], tokenize=False)} ds = ds.map(preprocess) def tokenize(sample): return tokenizer(sample["text"], padding=False, max_length=MAX_SE...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: When I use llmcompressor to quantify the llama3 70b model to int8-a8w8,it shows ValueError: Failed to invert hessian due to numerical instability. bug;stale ### Your current environment When I use llmcompressor t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 20/llama3.1 70B export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 step1: pip install llmcompressor==0.3.0 from llmcompressor.transformers import SparseAutoModelForCausalLM from transformers import AutoTokenizer MODEL_ID = "/l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: fling the calibration dataset,so how can i do? H20/llama3.1 70B export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 step1: pip install llmcompressor==0.3.0 from llmcompressor.transformers import SparseAutoModelForCausalLM from...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: model to int8-a8w8,it shows ValueError: Failed to invert hessian due to numerical instability. bug;stale ### Your current environment When I use llmcompressor to quantify the llama3 70b model to int8-a8w8,it shows Value...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: When I use llmcompressor to quantify the llama3 70b model to int8-a8w8,it shows ValueError: Failed to invert hessian due to numerical instability. bug;stale ### Your current environment When I use llmcompressor t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
