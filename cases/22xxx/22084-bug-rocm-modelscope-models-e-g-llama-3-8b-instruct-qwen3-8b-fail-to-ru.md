# vllm-project/vllm#22084: [Bug]: ROCm: ModelScope models (e.g., Llama-3-8B-Instruct, Qwen3-8B) fail to run on vllm v0.10.0, but work on v0.8.5.

| 字段 | 值 |
| --- | --- |
| Issue | [#22084](https://github.com/vllm-project/vllm/issues/22084) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ROCm: ModelScope models (e.g., Llama-3-8B-Instruct, Qwen3-8B) fail to run on vllm v0.10.0, but work on v0.8.5.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug """ python >>> from vllm import LLM, SamplingParams INFO 08-01 18:49:14 [__init__.py:235] Automatically detected platform rocm. >>> >>> prompts = [ ... "Hello, my name is", ... "The president of the United States is", ... "The capital of France is", ... "The future of AI is", ... ] >>> sampling_params = SamplingParams(temperature=0.8, top_p=0.95) >>> model_name = "LLM-Research/Meta-Llama-3-8B-Instruct" >>> llm = LLM(model=model_name) Downloading Model from https://www.modelscope.cn to directory: /home/wei/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3-8B-Instruct Downloading Model from https://www.modelscope.cn to directory: /home/wei/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3-8B-Instruct ERROR 08-01 18:49:38 [registry.py:396] Error in inspecting model architecture 'LlamaForCausalLM' ERROR 08-01 18:49:38 [registry.py:396] Traceback (most recent call last): ERROR 08-01 18:49:38 [registry.py:396] File "/home/wei/Desktop/ROCm6.4.1/llm010/vllm/vllm/model_executor/models/registry.py", line 672, in _run_in_subprocess ERROR 08-01 18:49:38 [registry.py:396] returned.check_returncode() ERROR 08-01 18:49:38 [registry.py...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ROCm: ModelScope models (e.g., Llama-3-8B-Instruct, Qwen3-8B) fail to run on vllm v0.10.0, but work on v0.8.5. bug ### Your current environment ### 🐛 Describe the bug """ python >>> from vllm import LLM, Sampling...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment ### 🐛 Describe the bug """ python >>> from vllm import LLM, SamplingParams INFO 08-01 18:49:14 [__init__.py:235] Automatically detected platform rocm. >>> >>> prompts = [ ... "Hello, my name is", ......
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ROR 08-01 18:49:38 [registry.py:396] from vllm.model_executor.layers.quantization.utils.fp8_utils import ( ERROR 08-01 18:49:38 [registry.py:396] File "/home/wei/Desktop/ROCm6.4.1/llm010/vllm/vllm/model_executor/layers/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: ROCm: ModelScope models (e.g., Llama-3-8B-Instruct, Qwen3-8B) fail to run on vllm v0.10.0, but work on v0.8.5. bug ### Your current environment ### 🐛 Describe the bug """ python >>> from vllm import LLM, Sampling...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n;sampling_logits;speculative_decoding cuda;kernel;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
