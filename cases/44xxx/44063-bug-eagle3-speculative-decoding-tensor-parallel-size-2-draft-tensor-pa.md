# vllm-project/vllm#44063: [Bug]: Eagle3  Speculative Decoding + tensor_parallel_size=2 + draft_tensor_parallel_size=2 causes NCCL timeout / collective deadlock

| 字段 | 值 |
| --- | --- |
| Issue | [#44063](https://github.com/vllm-project/vllm/issues/44063) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Eagle3  Speculative Decoding + tensor_parallel_size=2 + draft_tensor_parallel_size=2 causes NCCL timeout / collective deadlock

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the **official EAGLE3 example** from the vLLM docs with 2-GPU tensor parallelism, the engine immediately hits NCCL collective operation timeouts and deadlocks. ### 🔴 Reproduction code (official example) ```python from vllm import LLM, SamplingParams prompts = ["The future of AI is"] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM( model="/home/liuzhu/tank/在读/liuzhu/Qwen3-8B", tensor_parallel_size=2, speculative_config={ "model": "/home/liuzhu/tank/在读/liuzhu/qwen3_8b_eagle3", "draft_tensor_parallel_size": 2, "num_speculative_tokens": 2, "method": "eagle3", }, ) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Bug info: (EngineCore pid=729594) INFO 05-30 18:09:16 [shm_broadcast.py:698] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). (EngineCore pid=729594) INFO 05-30 18:10:16 [shm_broadcast....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r current environment ### 🐛 Describe the bug When running the **official EAGLE3 example** from the vLLM docs with 2-GPU tensor parallelism, the engine immediately hits NCCL collective operation timeouts and deadlocks. #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: *official EAGLE3 example** from the vLLM docs with 2-GPU tensor parallelism, the engine immediately hits NCCL collective operation timeouts and deadlocks. ### 🔴 Reproduction code (official example) ```python from vllm i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ing_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM( model="/home/liuzhu/tank/在读/liuzhu/Qwen3-8B", tensor_parallel_size=2, speculative_config={ "model": "/home/liuzhu/tank/在读/liuzhu/qwen3_8b_eagle3", "dra...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Eagle3 Speculative Decoding + tensor_parallel_size=2 + draft_tensor_parallel_size=2 causes NCCL timeout / collective deadlock bug ### Your current environment ### 🐛 Describe the bug When running the **official EA...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -30 18:09:16 [shm_broadcast.py:698] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv c...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
