# vllm-project/vllm#35857: [Bug]: NameError: 'IntermediateTensors' is not defined in GPT-OSS model during Pipeline Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#35857](https://github.com/vllm-project/vllm/issues/35857) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NameError: 'IntermediateTensors' is not defined in GPT-OSS model during Pipeline Parallelism

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug A `NameError` occurs when running the `openai/gpt-oss-20b` model with Pipeline Parallelism (PP) enabled in a multi-node Ray cluster. The error indicates that `IntermediateTensors` is not defined in `vllm/model_executor/models/gpt_oss.py`. The model works perfectly with Tensor Parallelism (`tensor_parallel_size: 2`), but fails immediately during the engine initialization phase when using Pipeline Parallelism (`pipeline_parallel_size: 2`). ### Minimal Reproduction I am using the official NVIDIA vLLM image `nvcr.io/nvidia/vllm:25.12.post1-py3`. **Command to reproduce:** ```bash vllm serve openai/gpt-oss-20b \ --pipeline-parallel-size 2 \ --tensor-parallel-size 1 \ --distributed-executor-backend ray \ --max-model-len 8192 (EngineCore_DP0 pid=13858) File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/gpt_oss.py", line 723, in forward (EngineCore_DP0 pid=13858) return self.model(input_ids, positions, intermediate_tensors, inputs_embeds) (EngineCore_DP0 pid=13858) File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/gpt_oss.py", line 277, in forward (EngineCore_DP0 pid=13858) NameError: name 'Int...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ipeline_parallel_size: 2`). ### Minimal Reproduction I am using the official NVIDIA vLLM image `nvcr.io/nvidia/vllm:25.12.post1-py3`. **Command to reproduce:** ```bash vllm serve openai/gpt-oss-20b \ --pipeline-parallel...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -parallel-size 2 \ --tensor-parallel-size 1 \ --distributed-executor-backend ray \ --max-model-len 8192 (EngineCore_DP0 pid=13858) File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/gpt_oss.py", li...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mediateTensors' is not defined in GPT-OSS model during Pipeline Parallelism bug ### Your current environment ### 🐛 Describe the bug A `NameError` occurs when running the `openai/gpt-oss-20b` model with Pipeline Parallel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: NameError: 'IntermediateTensors' is not defined in GPT-OSS model during Pipeline Parallelism bug ### Your current environment ### 🐛 Describe the bug A `NameError` occurs when running the `openai/gpt-oss-20b` mode...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: l NVIDIA vLLM image `nvcr.io/nvidia/vllm:25.12.post1-py3`. **Command to reproduce:** ```bash vllm serve openai/gpt-oss-20b \ --pipeline-parallel-size 2 \ --tensor-parallel-size 1 \ --distributed-executor-backend ray \ -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
