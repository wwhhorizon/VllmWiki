# vllm-project/vllm#1400: Using VLLM with a Tesla T4 on SageMaker Studio (ml.g4dn.xlarge instance)

| 字段 | 值 |
| --- | --- |
| Issue | [#1400](https://github.com/vllm-project/vllm/issues/1400) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | quantization;sampling |
| 症状 | oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Using VLLM with a Tesla T4 on SageMaker Studio (ml.g4dn.xlarge instance)

### Issue 正文摘录

Hi everyone. I'm trying to use vLLM using a T4, but I'm facing some problems. I'm trying to run Mistral models using vllm 0.2.1 With the following code, I receive a `ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla T4 GPU has compute capability 7.5.` ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="TheBloke/Mistral-7B-Instruct-v0.1-AWQ", quantization='awq', dtype='bfloat16', gpu_memory_utilization=0.5) ``` If I use another dtype or remove the `quantization` parameter, I get an OOM error.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: dels using vllm 0.2.1 With the following code, I receive a `ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla T4 GPU has compute capability 7.5.` ``` from vllm import LLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: arge instance) Hi everyone. I'm trying to use vLLM using a T4, but I'm facing some problems. I'm trying to run Mistral models using vllm 0.2.1 With the following code, I receive a `ValueError: Bfloat16 is only supported...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: I receive a `ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla T4 GPU has compute capability 7.5.` ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: If I use another dtype or remove the `quantization` parameter, I get an OOM error. performance model_support;quantization;sampling_logits quantization;sampling oom dtype Hi everyone. I'm trying to use vLLM using a T4, b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: LM using a T4, but I'm facing some problems. I'm trying to run Mistral models using vllm 0.2.1 With the following code, I receive a `ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
