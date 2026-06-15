# vllm-project/vllm#19204: [Bug]: VLLM keeps hanging and failing to initialize engine

| 字段 | 值 |
| --- | --- |
| Issue | [#19204](https://github.com/vllm-project/vllm/issues/19204) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | activation;attention;cache;cuda;kernel;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM keeps hanging and failing to initialize engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to use vLLM (v.0.9.0.1) for generating structured output. With one GPU it works perfectly fine but when i use 2 GPUs with `tensors_parallel_size=2` vLLM hangs. I am using single computation node with two GPUs. At first vLLM did not load the model, which could be solved by adding `NNCL_P2P_DISABLE=1` (https://github.com/vllm-project/vllm/issues/14025). Now the model loads but the program hangs now after `(VllmWorker rank=0 pid=2528103) INFO 06-05 10:48:09 [gpu_model_runner.py:1933] Graph capturing finished in 30 secs, took 2.65 GiB`. In the logs one can see that i never reached the final initialization of the engine. No error is thrown. The script just hangs there for hours. See Slurm log. I am starting my script after loading the following environment variables: ``` export NCCL_DEBUG=INFO export TRANSFORMERS_VERBOSITY=debug export NCCL_P2P_DISABLE=1 export OMP_NUM_THREADS=12 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. performance activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits activation;attention;cache;cuda;kernel;qu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ng single computation node with two GPUs. At first vLLM did not load the model, which could be solved by adding `NNCL_P2P_DISABLE=1` (https://github.com/vllm-project/vllm/issues/14025). Now the model loads but the progr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits activation;attention;cache;cuda;kernel;quantization;sampling;triton build_error dtype;env_dependency;shape Your curre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits activation;attention;cache;cuda;kernel;quantization;sampling;triton build_error dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
