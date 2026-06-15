# vllm-project/vllm#10828: [Bug]: The following error occurred when I ran the qwen2.5-7b-fp8-dynamic model with vllm0.6.4.post1 on a single card 4090

| 字段 | 值 |
| --- | --- |
| Issue | [#10828](https://github.com/vllm-project/vllm/issues/10828) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | gemm_linear;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The following error occurred when I ran the qwen2.5-7b-fp8-dynamic model with vllm0.6.4.post1 on a single card 4090

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug import torch torch.cuda.empty_cache() from vllm import LLM model = LLM(quant_model_path, gpu_memory_utilization=0.9) result = model.generate("Hello, my name is") print(result[0]) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nt ### Model Input Dumps _No response_ ### 🐛 Describe the bug import torch torch.cuda.empty_cache() from vllm import LLM model = LLM(quant_model_path, gpu_memory_utilization=0.9) result = model.generate("Hello, my name...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: The following error occurred when I ran the qwen2.5-7b-fp8-dynamic model with vllm0.6.4.post1 on a single card 4090 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Dumps _No response_ ### 🐛 Describe the bug import torch torch.cuda.empty_cache() from vllm import LLM model = LLM(quant_model_path, gpu_memory_utilization=0.9) result = model.generate("Hello, my name is") print(result[0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The following error occurred when I ran the qwen2.5-7b-fp8-dynamic model with vllm0.6.4.post1 on a single card 4090 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n2.5-7b-fp8-dynamic model with vllm0.6.4.post1 on a single card 4090 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug import torch torch.cuda.empty_cache() from vllm impo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
