# vllm-project/vllm#3404: Unable to load LoRA fine-tuned LLM from HF (AssertionError)

| 字段 | 值 |
| --- | --- |
| Issue | [#3404](https://github.com/vllm-project/vllm/issues/3404) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Unable to load LoRA fine-tuned LLM from HF (AssertionError)

### Issue 正文摘录

Following the docs about [Using LoRA Adapters](https://docs.vllm.ai/en/latest/models/lora.html), I am finding an assert problem. My code: ```python from huggingface_hub import snapshot_download from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest lora_path = snapshot_download(repo_id=" ") llm = LLM( model="mistralai/Mistral-7B-v0.1", tokenizer=" ", enable_lora=True) sampling_params = SamplingParams( temperature=0, max_tokens=256, stop=[" "] ) prompts = [ " I'm hungry. Find places to eat please. Sure thing. Which city would you like to eat in? Let's go with Foster City please. Sure. What kind of food are you hungry for? Spicy Indian sound really good. One moment. I found a great restaurant called Pastries N Chaat in Foster City. Give me other suggestions as well How about, Tabla Indian Restaurant in Foster City? Can you find out if they are average priced? sure. The price range would be inexpensive. Perfect. That works Should I reserve for you? Yes, go ahead and do that. " ] outputs = llm.generate( prompts, sampling_params, lora_request=LoRARequest("lora_adapter", 1, lora_path) ) print(outputs) ``` The error: ``` ... INFO 03-14 11:33:38 model_runner.py:756...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Unable to load LoRA fine-tuned LLM from HF (AssertionError) stale Following the docs about [Using LoRA Adapters](https://docs.vllm.ai/en/latest/models/lora.html), I am finding an assert problem. My code: ```python from...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: I am finding an assert problem. My code: ```python from huggingface_hub import snapshot_download from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest lora_path = snapshot_download(repo_id=" ")...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/home/ubuntu/vllm/.venv/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Unable to load LoRA fine-tuned LLM from HF (AssertionError) stale Following the docs about [Using LoRA Adapters](https://docs.vllm.ai/en/latest/models/lora.html), I am finding an assert problem. My code: ```python from...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Following the docs about [Using LoRA Adapters](https://docs.vllm.ai/en/latest/models/lora.html), I am finding an assert problem. My code: ```python from huggingface_hub import snapshot_download from vllm import LLM, Sam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
