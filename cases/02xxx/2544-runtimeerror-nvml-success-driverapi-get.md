# vllm-project/vllm#2544: RuntimeError: NVML_SUCCESS == DriverAPI::get()

| 字段 | 值 |
| --- | --- |
| Issue | [#2544](https://github.com/vllm-project/vllm/issues/2544) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: NVML_SUCCESS == DriverAPI::get()

### Issue 正文摘录

My env: Python 3.10.13 torch 2.1.2 vllm 0.2.7 My cuda version is: ![WechatIMG3](https://github.com/vllm-project/vllm/assets/61838642/477073ce-d733-4097-9d4a-9ca46c004dba) I use llm: llm = LLM(model="../open-source-llms/Llama-2-7b-chat-hf") cause issue: RuntimeError: NVML_SUCCESS == DriverAPI::get()->nvmlDeviceGetHandleByPciBusId_v2_( pci_id, &nvml_device) INTERNAL ASSERT FAILED at "../c10/cuda/CUDACachingAllocator.cpp":1139, please report a bug to PyTorch. Please help me to fix it

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: I::get() My env: Python 3.10.13 torch 2.1.2 vllm 0.2.7 My cuda version is: ![WechatIMG3](https://github.com/vllm-project/vllm/assets/61838642/477073ce-d733-4097-9d4a-9ca46c004dba) I use llm: llm = LLM(model="../open-sou...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ets/61838642/477073ce-d733-4097-9d4a-9ca46c004dba) I use llm: llm = LLM(model="../open-source-llms/Llama-2-7b-chat-hf") cause issue: RuntimeError: NVML_SUCCESS == DriverAPI::get()->nvmlDeviceGetHandleByPciBusId_v2_( pci...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: verAPI::get() My env: Python 3.10.13 torch 2.1.2 vllm 0.2.7 My cuda version is: ![WechatIMG3](https://github.com/vllm-project/vllm/assets/61838642/477073ce-d733-4097-9d4a-9ca46c004dba) I use llm: llm = LLM(model="../ope...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
