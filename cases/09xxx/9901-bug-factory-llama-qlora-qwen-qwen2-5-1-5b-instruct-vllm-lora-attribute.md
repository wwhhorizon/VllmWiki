# vllm-project/vllm#9901: [Bug]: 我在使用factory_llama工具以qlora的方式训练Qwen/Qwen2.5-1.5B-Instruct模型，然后以vllm加载lora的方式启动，结果报错：AttributeError: Model Qwen2ForCausalLM does not support BitsAndBytes quantization yet.，有大佬知道是哪儿的问题吗

| 字段 | 值 |
| --- | --- |
| Issue | [#9901](https://github.com/vllm-project/vllm/issues/9901) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 我在使用factory_llama工具以qlora的方式训练Qwen/Qwen2.5-1.5B-Instruct模型，然后以vllm加载lora的方式启动，结果报错：AttributeError: Model Qwen2ForCausalLM does not support BitsAndBytes quantization yet.，有大佬知道是哪儿的问题吗

### Issue 正文摘录

### Your current environment """ This example shows how to use LoRA with different quantization techniques for offline inference. Requires HuggingFace credentials for access. """ import gc from typing import List, Optional, Tuple import torch from huggingface_hub import snapshot_download from vllm import EngineArgs, LLMEngine, RequestOutput, SamplingParams from vllm.lora.request import LoRARequest def create_test_prompts( lora_path: str ) -> List[Tuple[str, SamplingParams, Optional[LoRARequest]]]: return [ # this is an example of using quantization without LoRA ("My name is", SamplingParams(temperature=0.0, logprobs=1, prompt_logprobs=1, max_tokens=128), None), # the next three examples use quantization with LoRA ("my name is", SamplingParams(temperature=0.0, logprobs=1, prompt_logprobs=1, max_tokens=128), LoRARequest("lora-test-1", 1, lora_path)), ("The capital of USA is", SamplingParams(temperature=0.0, logprobs=1, prompt_logprobs=1, max_tokens=128), LoRARequest("lora-test-2", 1, lora_path)), ("The capital of France is", SamplingParams(temperature=0.0, logprobs=1, prompt_logprobs=1, max_tokens=128), LoRARequest("lora-test-3", 1, lora_path)), ] def process_requests(engine: LLMEng...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: 我在使用factory_llama工具以qlora的方式训练Qwen/Qwen2.5-1.5B-Instruct模型，然后以vllm加载lora的方式启动，结果报错：AttributeError: Model Qwen2ForCausalLM does not support BitsAndBytes quantization yet.，有大佬知道是哪儿的问题吗 bug;stale ### Your current en...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: or offline inference. Requires HuggingFace credentials for access. """ import gc from typing import List, Optional, Tuple import torch from huggingface_hub import snapshot_download from vllm import EngineArgs, LLMEngine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: for the next test del engine gc.collect() torch.cuda.empty_cache() if __name__ == '__main__': main() ### Model Input Dumps _No response_ ### 🐛 Describe the bug [Bug]: 我在使用factory_llama工具以qlora的方式训练Qwen/Qwen2.5-1.5B-Inst...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ausalLM does not support BitsAndBytes quantization yet.，有大佬知道是哪儿的问题吗 bug;stale ### Your current environment """ This example shows how to use LoRA with different quantization techniques for offline inference. Requires H...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 果报错：AttributeError: Model Qwen2ForCausalLM does not support BitsAndBytes quantization yet.，有大佬知道是哪儿的问题吗 bug;stale ### Your current environment """ This example shows how to use LoRA with different quantization technique...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
