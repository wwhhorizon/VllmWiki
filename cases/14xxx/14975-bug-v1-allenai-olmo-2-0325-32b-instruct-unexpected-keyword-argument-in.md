# vllm-project/vllm#14975: [Bug][V1]: allenai/OLMo-2-0325-32B-Instruct - unexpected keyword argument 'inputs_embeds'

| 字段 | 值 |
| --- | --- |
| Issue | [#14975](https://github.com/vllm-project/vllm/issues/14975) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][V1]: allenai/OLMo-2-0325-32B-Instruct - unexpected keyword argument 'inputs_embeds'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am hitting the following ``` ERROR 03-17 17:56:39 [core.py:340] TypeError: Olmo2ForCausalLM.forward() got an unexpected keyword argument 'inputs_embeds' ``` When running `vllm serve allenai/OLMo-2-0325-32B-Instruct --tensor-parallel-size 2` in V1. V0 is fine: ``` ERROR 03-17 17:56:39 [core.py:340] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-17 17:56:39 [core.py:340] File "/home/tms/vllm/vllm/v1/engine/core.py", line 332, in run_engine_core ERROR 03-17 17:56:39 [core.py:340] engine_core = EngineCoreProc(*args, **kwargs) ERROR 03-17 17:56:39 [core.py:340] File "/home/tms/vllm/vllm/v1/engine/core.py", line 287, in __init__ ERROR 03-17 17:56:39 [core.py:340] super().__init__(vllm_config, executor_class, log_stats) ERROR 03-17 17:56:39 [core.py:340] File "/home/tms/vllm/vllm/v1/engine/core.py", line 62, in __init__ ERROR 03-17 17:56:39 [core.py:340] num_gpu_blocks, num_cpu_blocks = self._initialize_kv_caches( ERROR 03-17 17:56:39 [core.py:340] File "/home/tms/vllm/vllm/v1/engine/core.py", line 121, in _initialize_kv_caches ERROR 03-17 17:56:39 [core.py:340] available_gpu_memory = self.model_executor.dete...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: in __init__ ERROR 03-17 17:56:39 [core.py:340] super().__init__(vllm_config, executor_class, log_stats) ERROR 03-17 17:56:39 [core.py:340] File "/home/tms/vllm/vllm/v1/engine/core.py", line 62, in __init__ ERROR 03-17 1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency Your current...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
