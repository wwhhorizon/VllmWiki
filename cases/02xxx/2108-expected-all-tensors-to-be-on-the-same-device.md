# vllm-project/vllm#2108: Expected all tensors to be on the same device

| 字段 | 值 |
| --- | --- |
| Issue | [#2108](https://github.com/vllm-project/vllm/issues/2108) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Expected all tensors to be on the same device

### Issue 正文摘录

Hello, I was trying to load two different models in two different GPUs. One is a model loaded with vllm on the first GPU, the other is without vllm on the second GPU (a model loaded with load_in_4bits). In inference, I get this error: `Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cuda:1! (when checking argument for argument index in method wrapper_CUDA__index_select)` If instead I just load the model with vllm, I don't have this problem and it works. That's the code how I load the models: ``` first_model = LLM( model=model_name_or_path, tensor_parallel_size=1, gpu_memory_utilization=0.9 ) second_model = AutoModelForCausalLM.from_pretrained(model2_name_or_path, load_in_4bit=True, device_map = "cuda:1") ``` How could I solve it? Thanks

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed all tensors to be on the same device, but found at least two devices, cuda:0 and cuda:1! (when checking argument for argument index in method wrapper_CUDA__index_select)` If instead I just load the model with vllm, I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nsors to be on the same device Hello, I was trying to load two different models in two different GPUs. One is a model loaded with vllm on the first GPU, the other is without vllm on the second GPU (a model loaded with l...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
