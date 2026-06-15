# vllm-project/vllm#783: torch.cuda.OutOfMemoryError: CUDA out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#783](https://github.com/vllm-project/vllm/issues/783) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;sampling |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> torch.cuda.OutOfMemoryError: CUDA out of memory

### Issue 正文摘录

I have GPU device 1, and there are other processes taking up about 15G of Memory-Usage, but there is 30G of Memory-Usage left, so why does it go OOM when I run a small model? Here is my code： ``` from vllm import LLM import torch import os os.environ["CUDA_VISIBLE_DEVICES"] = "1" from vllm import LLM, SamplingParams if __name__ == '__main__': device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu") prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m",tensor_parallel_size=1) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Exception： torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.63 GiB (GPU 0; 44.56 GiB total capacity; 27.91 GiB already allocated; 565.31 MiB free; 27.93 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation. See d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: oes it go OOM when I run a small model? Here is my code： ``` from vllm import LLM import torch import os os.environ["CUDA_VISIBLE_DEVICES"] = "1" from vllm import LLM, SamplingParams if __name__ == '__main__': device =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: torch.cuda.OutOfMemoryError: CUDA out of memory I have GPU device 1, and there are other processes taking up about 15G of Memory-Usage, but there is 30G of Memory-Usage left, so why does it go OOM when I run a small mod...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: f Memory-Usage, but there is 30G of Memory-Usage left, so why does it go OOM when I run a small model? Here is my code： ``` from vllm import LLM import torch import os os.environ["CUDA_VISIBLE_DEVICES"] = "1" from vllm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in__': device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu") prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_para...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: re is 30G of Memory-Usage left, so why does it go OOM when I run a small model? Here is my code： ``` from vllm import LLM import torch import os os.environ["CUDA_VISIBLE_DEVICES"] = "1" from vllm import LLM, SamplingPar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
