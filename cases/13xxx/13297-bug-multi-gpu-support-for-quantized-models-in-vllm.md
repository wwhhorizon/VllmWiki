# vllm-project/vllm#13297: [Bug]: Multi-GPU Support for Quantized Models in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#13297](https://github.com/vllm-project/vllm/issues/13297) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Multi-GPU Support for Quantized Models in vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I successfully loaded the quantized model (in4) using a single GPU with the following command: ''' CUDA_VISIBLE_DEVICES=0 vllm serve unsloth/Llama-3.3-70B-Instruct-bnb-4bit \ --max-model-len=8192 \ --max-num-batched-token=8192 \ --gpu-memory-utilization=0.99 \ --enforce-eager \ --disable-log-requests \ --max-num-seqs=16 \ --quantization=bitsandbytes \ --load-format=bitsandbytes ''' But when attempting to use multiple GPUs, the following command fails: ''' CUDA_VISIBLE_DEVICES=0,1 vllm serve unsloth/Llama-3.3-70B-Instruct-bnb-4bit \ --max-model-len=8192 \ --max-num-batched-token=8192 \ --gpu-memory-utilization=0.99 \ --enforce-eager \ --disable-log-requests \ --max-num-seqs=16 \ --quantization=bitsandbytes \ --load-format=bitsandbytes \ --tensor-parallel-size 2 ''' For reference, I have successfully used multiple GPUs with a non-quantized model using the following command: ''' CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen/Qwen2.5-1.5B-Instruct --tensor-parallel-size 2 ''' Is there a proper way to load a quantized model across multiple GPUs in vLLM? If so, what configurations are required? Any guidance would be greatly appreciated. ###...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Multi-GPU Support for Quantized Models in vLLM bug ### Your current environment ### 🐛 Describe the bug I successfully loaded the quantized model (in4) using a single GPU with the following command: ''' CUDA_VISIB...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: uantized model (in4) using a single GPU with the following command: ''' CUDA_VISIBLE_DEVICES=0 vllm serve unsloth/Llama-3.3-70B-Instruct-bnb-4bit \ --max-model-len=8192 \ --max-num-batched-token=8192 \ --gpu-memory-util...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: so, what configurations are required? Any guidance would be greatly appreciated. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Multi-GPU Support for Quantized Models in vLLM bug ### Your current environment ### 🐛 Describe the bug I successfully loaded the quantized model (in4) using a single GPU with the following command: ''' CUDA_VISIB...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: GPU with the following command: ''' CUDA_VISIBLE_DEVICES=0 vllm serve unsloth/Llama-3.3-70B-Instruct-bnb-4bit \ --max-model-len=8192 \ --max-num-batched-token=8192 \ --gpu-memory-utilization=0.99 \ --enforce-eager \ --d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
