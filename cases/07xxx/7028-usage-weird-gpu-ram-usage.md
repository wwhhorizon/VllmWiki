# vllm-project/vllm#7028: [Usage]: weird GPU RAM usage

| 字段 | 值 |
| --- | --- |
| Issue | [#7028](https://github.com/vllm-project/vllm/issues/7028) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: weird GPU RAM usage

### Issue 正文摘录

### Your current environment ```text Google Colab with T4 GPU ``` ### How would you like to use vllm I want to run inference of a fine-tune awq quantized version of Mistral called Vistral (https://huggingface.co/hiuman/Vistral-7B-Chat-quantize. When I load model with default gpu_memory_utilization (which is 0.9), it loads ok. But when I try to reduce the value of gpu_memory_utilization to 0.1, it gets the error : 'No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine.' I thought when I lower the value of gpu_memory_utilization, the less gpu memory will be use. Can anyone explain for me this issue ? Thank you. Here is the code I am running : from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.1, top_p=0.95, max_tokens = 128) llm = LLM(model="hiuman/Vistral-7B-Chat-quantize", quantization="AWQ",enforce_eager=True, gpu_memory_utilization=0.1)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: u like to use vllm I want to run inference of a fine-tune awq quantized version of Mistral called Vistral (https://huggingface.co/hiuman/Vistral-7B-Chat-quantize. When I load model with default gpu_memory_utilization (w...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ory_utilization to 0.1, it gets the error : 'No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine.' I thought when I lower the value of gpu_memory_utilization, t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: of a fine-tune awq quantized version of Mistral called Vistral (https://huggingface.co/hiuman/Vistral-7B-Chat-quantize. When I load model with default gpu_memory_utilization (which is 0.9), it loads ok. But when I try t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: w would you like to use vllm I want to run inference of a fine-tune awq quantized version of Mistral called Vistral (https://huggingface.co/hiuman/Vistral-7B-Chat-quantize. When I load model with default gpu_memory_util...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ilization to 0.1, it gets the error : 'No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine.' I thought when I lower the value of gpu_memory_utilization, the les...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
