# vllm-project/vllm#13036: [Bug]: Incorrect Device Handling in DeviceMemoryProfiler Causes Zero Memory Usage Log

| 字段 | 值 |
| --- | --- |
| Issue | [#13036](https://github.com/vllm-project/vllm/issues/13036) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect Device Handling in DeviceMemoryProfiler Causes Zero Memory Usage Log

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description When I was using the LLM and specified device="cuda:1", the log from DeviceMemoryProfiler showed that my GPU memory usage was 0. I thought the model had failed to load, but in fact, the model was loaded correctly. The issue was that when DeviceMemoryProfiler calculated the memory usage, it incorrectly set the device to cuda:0, which is why the output was 0. ![Image](https://github.com/user-attachments/assets/0872df7c-3c4b-49ef-bf00-2b4cce9507c0) My Code: ```python from peft import get_peft_model, LoraConfig from transformers import AutoModelForCausalLM from vllm import LLM model = AutoModelForCausalLM.from_pretrained("/l2/zhangzhe/WSDM_Cup/model/LLM-Research/Llama-3___2-1B-Instruct") peft_config = LoraConfig( r=16, lora_alpha=64, lora_dropout=0.05, target_modules=[ "gate_proj", "up_proj", "down_proj" ] ) model = get_peft_model(model, peft_config) llm = LLM( model.name_or_path, device="cuda:1", # the only difference gpu_memory_utilization=0.5, dtype="auto", enable_prefix_caching=True, max_model_len=256, enable_lora=True, max_lora_rank=16 ) print(llm.generate("Hello, my name is", max_length=100)) print("haha") ``` ##...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### 🐛 Describe the bug ## Description When I was using the LLM and specified device="cuda:1", the log from DeviceMemoryProfiler showed that my GPU memory usage was 0. I thought the model had failed to load, but in fact,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e the bug ## Description When I was using the LLM and specified device="cuda:1", the log from DeviceMemoryProfiler showed that my GPU memory usage was 0. I thought the model had failed to load, but in fact, the model wa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eviceMemoryProfiler showed that my GPU memory usage was 0. I thought the model had failed to load, but in fact, the model was loaded correctly. The issue was that when DeviceMemoryProfiler calculated the memory usage, i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Incorrect Device Handling in DeviceMemoryProfiler Causes Zero Memory Usage Log bug ### Your current environment ### 🐛 Describe the bug ## Description When I was using the LLM and specified device="cuda:1", the lo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;mismatch;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
