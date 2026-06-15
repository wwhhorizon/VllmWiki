# vllm-project/vllm#9523: [Bug]: Failed to Load  8-bit Quantized Model 

| 字段 | 值 |
| --- | --- |
| Issue | [#9523](https://github.com/vllm-project/vllm/issues/9523) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to Load  8-bit Quantized Model 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The code is ```python from datasets import load_dataset from transformers import AutoTokenizer, AutoModelForCausalLM from llmcompressor.modifiers.quantization import GPTQModifier from llmcompressor.modifiers.smoothquant import SmoothQuantModifier from llmcompressor.transformers import SparseAutoModelForCausalLM, oneshot # Select model and load it. MODEL_ID = "meta-llama/Meta-Llama-3.1-8B-Instruct" model = SparseAutoModelForCausalLM.from_pretrained( MODEL_ID, device_map="cuda:0", torch_dtype="auto", ) tokenizer = AutoTokenizer.from_pretrained(MODEL_ID) # Select calibration dataset. DATASET_ID = "/data2/liziniu/datasets/AIMO/NuminaMath-CoT" DATASET_SPLIT = "train" # Select number of samples. 512 samples is a good place to start. # Increasing the number of samples can improve accuracy. NUM_CALIBRATION_SAMPLES = 1024 MAX_SEQUENCE_LENGTH = 4096 # Load dataset and preprocess. ds = load_dataset(DATASET_ID, split=DATASET_SPLIT) ds = ds.shuffle(seed=42).select(range(NUM_CALIBRATION_SAMPLES)) def preprocess(example): return { "text": tokenizer.apply_chat_template( example["messages"], tokenize=False, ) }...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: esponse_ ### 🐛 Describe the bug The code is ```python from datasets import load_dataset from transformers import AutoTokenizer, AutoModelForCausalLM from llmcompressor.modifiers.quantization import GPTQModifier from llm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Failed to Load 8-bit Quantized Model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The code is ```python from datasets import load_dataset from transformers import Au...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: .modifiers.quantization import GPTQModifier from llmcompressor.modifiers.smoothquant import SmoothQuantModifier from llmcompressor.transformers import SparseAutoModelForCausalLM, oneshot # Select model and load it. MODE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Failed to Load 8-bit Quantized Model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The code is ```python from datasets import load_dataset from transformers import Au...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ) output = model.generate(input_ids, max_new_tokens=100) print(tokenizer.decode(output[0])) print("==========================================\n\n") # Save to disk compressed. SAVE_DIR = MODEL_ID.split("/")[1] + "-W8A8-D...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
