# vllm-project/vllm#14607: [Usage]: How to get original total hidden_states

| 字段 | 值 |
| --- | --- |
| Issue | [#14607](https://github.com/vllm-project/vllm/issues/14607) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to get original total hidden_states

### Issue 正文摘录

### Proposal to improve performance I want to get the original total hidden_states like transformers output, here is my transformer example: `from transformers import AutoModel base_model_path = "../Llama-3.2-3B-Instruct" base_model = AutoModel.from_pretrained(base_model_path,torch_dtype=torch.float32) base_model.to("cuda") inputs = tokenizer("what's the weather today",return_tensors="pt") cuda_inputs ={} for key in inputs: cuda_inputs[key] = inputs[key].to(peft_model.device) with torch.no_grad(): outputs = base_model (**cuda_inputs) print(outputs[0])` The output likes blow: `tensor([[[ 0.0127, -0.4116, -0.2221, ..., 0.4073, 0.3212, 0.2383], [-1.7105, -1.9136, 2.1987, ..., -1.1063, -1.1604, 1.9475], [-2.3868, -0.6762, 0.6541, ..., -1.8436, -2.8037, -0.2768], [-1.2720, -1.5623, 1.6725, ..., -0.5808, -2.6175, 1.5599], [-1.3572, -3.6725, 2.8592, ..., -1.5065, -1.3943, 1.0695], [ 0.0378, -1.8762, 3.3803, ..., -2.6625, -0.3675, 3.0536]]], device='cuda:0')` The shape of the output is [1,6,3072]. Because the input seq lenth is 6, and the batch_size is 1. **How can I get this result in vllm?** I have tried the embed and encode method in vllm. But the output shape is [3072]. And is differe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: transformers output, here is my transformer example: `from transformers import AutoModel base_model_path = "../Llama-3.2-3B-Instruct" base_model = AutoModel.from_pretrained(base_model_path,torch_dtype=torch.float32) bas...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: B-Instruct" base_model = AutoModel.from_pretrained(base_model_path,torch_dtype=torch.float32) base_model.to("cuda") inputs = tokenizer("what's the weather today",return_tensors="pt") cuda_inputs ={} for key in inputs: c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rom_pretrained(base_model_path,torch_dtype=torch.float32) base_model.to("cuda") inputs = tokenizer("what's the weather today",return_tensors="pt") cuda_inputs ={} for key in inputs: cuda_inputs[key] = inputs[key].to(pef...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s output, here is my transformer example: `from transformers import AutoModel base_model_path = "../Llama-3.2-3B-Instruct" base_model = AutoModel.from_pretrained(base_model_path,torch_dtype=torch.float32) base_model.to(...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: code(prompts) encode_outputs[0].outputs.data` ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
