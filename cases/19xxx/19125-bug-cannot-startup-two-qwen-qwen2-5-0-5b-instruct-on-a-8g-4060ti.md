# vllm-project/vllm#19125: [Bug]: cannot startup two Qwen/Qwen2.5-0.5B-Instruct on a 8G 4060ti

| 字段 | 值 |
| --- | --- |
| Issue | [#19125](https://github.com/vllm-project/vllm/issues/19125) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: cannot startup two Qwen/Qwen2.5-0.5B-Instruct on a 8G 4060ti

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to run two small model on my 8GB GPU. "gpu_memory_utilization" should be help me to allocate memory for those 2 vLLM instance. So I conducted an experiment to verify this function. Steps summary: ```txt Step1, start Qwen/Qwen2.5-0.5B-Instruct with gpu_memory_utilization 0.4. Step2, observe the VRAM usage with nvidia-smi, 3578MiB/8188MiB has already been occupied. Step3, start another vLLM instance with the same arguments, and listening on another port. But got exception: "No available memory for the cache blocks." Step4, increase gpu_memory_utilization to 0.8 and start another vLLM instance with listening on another port. Both of 2 vLLM instances could work. 6768MiB/8188MiB has been occupied by 2 instances. ``` According to the [user manual](https://github.com/vllm-project/vllm/blob/1409ef913446aa282f6426efbb0ed02a59320467/vllm/config.py#L1451C39-L1451C40), and if I understand correctly. The gpu_memory_utilization of 2 vLLMs, 0.4+0.4 should be correct, but the actual situation is 0.4+0.8. I guess that the denominator of gpu_memory_utilization is the available VRAM size, rather than the total VRAM size. I think this is a bu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cache;cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: our current environment ### 🐛 Describe the bug I want to run two small model on my 8GB GPU. "gpu_memory_utilization" should be help me to allocate memory for those 2 vLLM instance. So I conducted an experiment to verify...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: cannot startup two Qwen/Qwen2.5-0.5B-Instruct on a 8G 4060ti bug ### Your current environment ### 🐛 Describe the bug I want to run two small model on my 8GB GPU. "gpu_memory_utilization" should be help me to allo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attention;cache;cuda;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf dtyp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tive_decoding attention;cache;cuda;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
