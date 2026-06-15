# vllm-project/vllm#32853: [Usage]: How to run a compressed model in MXFP4A16 format

| 字段 | 值 |
| --- | --- |
| Issue | [#32853](https://github.com/vllm-project/vllm/issues/32853) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to run a compressed model in MXFP4A16 format

### Issue 正文摘录

### Your current environment First, I exported an LLM model in MXFP4A16 format using LLM Compressor. Then, I tried to infer this model based on VLLM, but I found that the inference result was incorrect. ### export MXFP4A16 from transformers import AutoModelForCausalLM, AutoTokenizer from llmcompressor import oneshot from llmcompressor.modifiers.quantization import QuantizationModifier from llmcompressor.utils import dispatch_for_generation MODEL_ID = "/data/public/models/llm/hf/Qwen3-1.7B" # Load model. model = AutoModelForCausalLM.from_pretrained(MODEL_ID, dtype="auto", device_map="auto") tokenizer = AutoTokenizer.from_pretrained(MODEL_ID) # Configure the quantization algorithm and scheme. # In this case, we: # * quantize the weights to fp4 with per group 32 via ptq recipe = QuantizationModifier(targets="Linear", scheme="MXFP4A16", ignore=["lm_head"]) # Apply quantization. qmodel = oneshot(model=model, recipe=recipe) print("\n\n") print("========== SAMPLE GENERATION ==============") dispatch_for_generation(model) input_ids = tokenizer("please tell me 1+1 =?", return_tensors="pt").input_ids.to( model.device ) output = model.generate(input_ids, max_new_tokens=100, top_k=1, top_p=0....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How to run a compressed model in MXFP4A16 format usage ### Your current environment First, I exported an LLM model in MXFP4A16 format using LLM Compressor. Then, I tried to infer this model based on VLLM, but I...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: How to run a compressed model in MXFP4A16 format usage ### Your current environment First, I exported an LLM model in MXFP4A16 format using LLM Compressor. Then, I tried to infer this model based on VLLM, but I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e inference result was incorrect. ### export MXFP4A16 from transformers import AutoModelForCausalLM, AutoTokenizer from llmcompressor import oneshot from llmcompressor.modifiers.quantization import QuantizationModifier...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: quantization import QuantizationModifier from llmcompressor.utils import dispatch_for_generation MODEL_ID = "/data/public/models/llm/hf/Qwen3-1.7B" # Load model. model = AutoModelForCausalLM.from_pretrained(MODEL_ID, dt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
