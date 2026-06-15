# vllm-project/vllm#28807: [Bug]: doesn't work with cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#28807](https://github.com/vllm-project/vllm/issues/28807) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: doesn't work with cpu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I simply want to run vllm on cpu to test some things, but it doesn't work, even when ran from docker. I am using this guide: https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html#build-image-from-source, but it cannot be used for several reasons listed below: 1. `docker run --rm --security-opt seccomp=unconfined --cap-add SYS_NICE --shm-size=4g -p 8000:8000 -e VLLM_CPU_KVCACHE_SPACE=4g -e VLLM_CPU_OMP_THREADS_BIND=4 vllm-cpu-env --model=meta-llama/Llama-3.2-1B-Instruct --dtype=bfloat16` doesn't work, because model has to be passed as a positional arg. 2. `docker run --rm --security-opt seccomp=unconfined --cap-add SYS_NICE --shm-size=4g -p 8000:8000 -e VLLM_CPU_KVCACHE_SPACE=4g -e VLLM_CPU_OMP_THREADS_BIND=4 vllm-cpu-env meta-llama/Llama-3.2-1B-Instruct --dtype=bfloat16` doesn't work, because one needs to provide some creds, but there is no such step in the docs 3. `docker run --rm --security-opt seccomp=unconfined --cap-add SYS_NICE --shm-size=4g -p 8000:8000 -e VLLM_CPU_KVCACHE_SPACE=4g -e VLLM_CPU_OMP_THREADS_BIND=4 vllm-cpu-env Qwen/Qwen2.5-1.5B-Instruct --dtype=bfloat16` - I use Qwen, because it is mentioned i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: vllm on cpu to test some things, but it doesn't work, even when ran from docker. I am using this guide: https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html#build-image-from-source, but it cannot be used...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: P_THREADS_BIND=4 vllm-cpu-env --model=meta-llama/Llama-3.2-1B-Instruct --dtype=bfloat16` doesn't work, because model has to be passed as a positional arg. 2. `docker run --rm --security-opt seccomp=unconfined --cap-add...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: VLLM_CPU_KVCACHE_SPACE=4g -e VLLM_CPU_OMP_THREADS_BIND=4 vllm-cpu-env --model=meta-llama/Llama-3.2-1B-Instruct --dtype=bfloat16` doesn't work, because model has to be passed as a positional arg. 2. `docker run --rm --se...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ineCore_DP0 pid=76) sampled_ids.shape[0] if sampled_ids is not None else 0 (EngineCore_DP0 pid=76) ^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=76) AttributeError: 'list' object has no attribute 'shape' ``` Full detailed log i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
