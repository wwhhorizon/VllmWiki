# vllm-project/vllm#10708: [Misc]: nsys profile can not show CUDA HW on all devices

| 字段 | 值 |
| --- | --- |
| Issue | [#10708](https://github.com/vllm-project/vllm/issues/10708) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 |  |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: nsys profile can not show CUDA HW on all devices

### Issue 正文摘录

### Anything you want to discuss about vllm. I want to use nsys profile to check the performance of vllm. I test vllm with an llama2-7B model using tp4 on four Nvidia A10 gpus, and here is my test script which does not use cuda_graph ```python import torch import time import vllm from vllm import LLM, SamplingParams print(vllm.__file__) def generate_fixed_shape_requests(tokenizer_or_model_path, batch_size: int = 1, input_len: int = 2048, output_len: int = 2048): if isinstance(tokenizer_or_model_path, str): from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretrained(tokenizer_or_model_path, trust_remote_code=True) else: tokenizer = tokenizer_or_model_path prompt = None vocab_size = tokenizer.vocab_size token_id = int(vocab_size / 5) pass_num = 5 while True: start_len = input_len - pass_num if (input_len - pass_num) > 0 else 0 end_len = input_len + pass_num for i in range(start_len, end_len): prompt_token = [token_id] * i prompt = tokenizer.decode(prompt_token, skip_special_tokens=True) if len(tokenizer.encode(prompt)) == input_len: break if len(tokenizer.encode(prompt)) == input_len: break token_id += 1 request: List[Tuple[str, int, int]] = [] for i in (range(b...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: o use nsys profile to check the performance of vllm. I test vllm with an llama2-7B model using tp4 on four Nvidia A10 gpus, and here is my test script which does not use cuda_graph ```python import torch import time imp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: pus, and here is my test script which does not use cuda_graph ```python import torch import time import vllm from vllm import LLM, SamplingParams print(vllm.__file__) def generate_fixed_shape_requests(tokenizer_or_model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Misc]: nsys profile can not show CUDA HW on all devices ### Anything you want to discuss about vllm. I want to use nsys profile to check the performance of vllm. I test vllm with an llama2-7B model using tp4 on four Nv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: port LLM, SamplingParams print(vllm.__file__) def generate_fixed_shape_requests(tokenizer_or_model_path, batch_size: int = 1, input_len: int = 2048, output_len: int = 2048): if isinsta
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Misc]: nsys profile can not show CUDA HW on all devices ### Anything you want to discuss about vllm. I want to use nsys profile to check the performance of vllm. I test vllm with an llama2-7B model using tp4 on four Nv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
