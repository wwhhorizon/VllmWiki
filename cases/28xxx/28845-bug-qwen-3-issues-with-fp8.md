# vllm-project/vllm#28845: [Bug]: Qwen 3 issues with FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#28845](https://github.com/vllm-project/vllm/issues/28845) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen 3 issues with FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If I run the current vLLM main with the Qwen-3 model using FP8 quantization, the inference breaks and it starts producing gibberish, whereas it works reasonably well on the latest release 0.11. ``` from vllm import LLM from vllm import SamplingParams qwen_32b = LLM( model = "Qwen/Qwen3-8B-FP8", # same happens with 32B-FP8 as well. # device = "cuda", max_model_len = 4096, # gpu_memory_utilization = 0.6, ) text = "What is the sqrt of 101?" sampling_params = SamplingParams( max_tokens = 1024, temperature = 0.7, top_p = 0.9, ) out = qwen_32b.generate(text, sampling_params) ``` Note that the same happens with/without chat template. Qwen3-8B-FP8 Output on main: ``` ' Rachel 哉vasiveuessuessuess0uessivedfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -3 model using FP8 quantization, the inference breaks and it starts producing gibberish, whereas it works reasonably well on the latest release 0.11. ``` from vllm import LLM from vllm import SamplingParams qwen_32b = L...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen 3 issues with FP8 bug ### Your current environment ### 🐛 Describe the bug If I run the current vLLM main with the Qwen-3 model using FP8 quantization, the inference breaks and it starts producing gibberish,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Qwen/Qwen3-8B-FP8", # same happens with 32B-FP8 as well. # device = "cuda", max_model_len = 4096, # gpu_memory_utilization = 0.6, ) text = "What is the sqrt of 101?" sampling_params = SamplingParams( max_tokens = 1024,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen 3 issues with FP8 bug ### Your current environment ### 🐛 Describe the bug If I run the current vLLM main with the Qwen-3 model using FP8 quantization, the inference breaks and it starts producing gibberish,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;fp8;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
