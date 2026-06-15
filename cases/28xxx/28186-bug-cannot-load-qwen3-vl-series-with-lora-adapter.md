# vllm-project/vllm#28186: [Bug] Cannot load qwen3-vl series with lora adapter

| 字段 | 值 |
| --- | --- |
| Issue | [#28186](https://github.com/vllm-project/vllm/issues/28186) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Cannot load qwen3-vl series with lora adapter

### Issue 正文摘录

I fine-tuned the `Qwen3-VL-8B-Instruct` model using Unsloth. I moved the saved QLoRA adapter and the `Qwen3-VL-2B-Instruct` model to my vLLM server. Then I ran a command to start model serving with vLLM as shown below. (For reference, the vLLM server has no issues—it was already serving official Qwen3-VL models.) ``` command = [ sys.executable, "-m", "vllm.entrypoints.openai.api_server", "--model", "./Qwen3-VL-2B-Instruct", "--max_model_len", "3500", "--gpu_memory_utilization", "0.85", "--trust-remote-code", "--host", "0.0.0.0", "--port", "8888", # for lora adapter "--enable-lora", "--max-lora-rank", "16", # LoRA rank "--max-loras", "1", "--max-cpu-loras", "1", "--lora-modules", "adapter0=./my_lora_adapter" ] ``` I waited for vLLM to properly load the QLoRA adapter, but the following problem occurred : https://github.com/vllm-project/vllm/issues/26991 When I was feeling hopeless, I tried merging the model instead of saving the LoRA adapter separately by using the `save_pretrained_merged()` function as shown below, and then vLLM was able to load and perform inference normally: ``` save_pretrained_merged( f"my_16bit_model", tokenizer, save_method="merged_16bit") ``` However, I don't...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug] Cannot load qwen3-vl series with lora adapter bug;stale I fine-tuned the `Qwen3-VL-8B-Instruct` model using Unsloth. I moved the saved QLoRA adapter and the `Qwen3-VL-2B-Instruct` model to my vLLM server. Then I r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: (For reference, the vLLM server has no issues—it was already serving official Qwen3-VL models.) ``` command = [ sys.executable, "-m", "vllm.entrypoints.openai.api_server", "--model", "./Qwen3-VL-2B-Instruct", "--max_mod...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: adapter bug;stale I fine-tuned the `Qwen3-VL-8B-Instruct` model using Unsloth. I moved the saved QLoRA adapter and the `Qwen3-VL-2B-Instruct` model to my vLLM server. Then I ran a command to start model serving with vLL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug] Cannot load qwen3-vl series with lora adapter bug;stale I fine-tuned the `Qwen3-VL-8B-Instruct` model using Unsloth. I moved the saved QLoRA adapter and the `Qwen3-VL-2B-Instruct` model to my vLLM server. Then I r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
