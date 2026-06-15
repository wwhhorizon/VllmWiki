# vllm-project/vllm#7374: [Bug]: Tensor Parallel > 1 causes desc_act=True GPTQ models to give bad output on ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#7374](https://github.com/vllm-project/vllm/issues/7374) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tensor Parallel > 1 causes desc_act=True GPTQ models to give bad output on ROCm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GPTQ models with `desc_act=True` fail to generate valid text when using `--tensor-parallel-size` above 1 This can be easily tested with two models, [Llama 3.1 8B GPTQ with desc_act=False](https://huggingface.co/ModelCloud/Meta-Llama-3.1-8B-Instruct-gptq-4bit) and [Llama 3.1 GPTQ with desc_act=True](https://huggingface.co/hugging-quants/Meta-Llama-3.1-8B-Instruct-GPTQ-INT4) Both models are ran with the OpenAI endpoint launched with the following command: ``` VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_NCCL_SO_PATH=/opt/rocm/lib/liibrccl.so.1 python -m vllm.entrypoints.openai.api_server --gpu-memory-utilization 0.7 --model --quantization gptq --max-model-len 1024 --dtype half --tensor-parallel-size ``` With TP = 1, both models return perfect output to the prompt `Write a haiku about vLLM` With TP = 2 (or more), the model with `desc_act=True` outputs nonsense This issue explains my [other ticket](https://github.com/vllm-project/vllm/issues/7011), but the [original Command R+ ticket](https://github.com/vllm-project/vllm/issues/3980) uses [an example model that works](https://huggingface.co/TheBloke/goliath-120b-GPTQ) with `desc_act=True`...

## 现有链接修复摘要

#17583 [Bugfix][ROCm] Fix incorrect casting in GPTQ GEMM kernel

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n I was still splitting across 4 cards. Though this was on an older vLLM version (0.4.1) which doesnt support Llama 3.1, so I cant test it. Users on the vLLM Discord tried the `desc_act=True` variant on their NVidia mul...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ) and [Llama 3.1 GPTQ with desc_act=True](https://huggingface.co/hugging-quants/Meta-Llama-3.1-8B-Instruct-GPTQ-INT4) Both models are ran with the OpenAI endpoint launched with the following command: ``` VLLM_WORKER_MUL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Tensor Parallel > 1 causes desc_act=True GPTQ models to give bad output on ROCm bug;rocm;stale ### Your current environment ### 🐛 Describe the bug GPTQ models with `desc_act=True` fail to generate valid text when...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nsor Parallel > 1 causes desc_act=True GPTQ models to give bad output on ROCm bug;rocm;stale ### Your current environment ### 🐛 Describe the bug GPTQ models with `desc_act=True` fail to generate valid text when using `-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: > 1 causes desc_act=True GPTQ models to give bad output on ROCm bug;rocm;stale ### Your current environment ### 🐛 Describe the bug GPTQ models with `desc_act=True` fail to generate valid text when using `--tensor-parall...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17583](https://github.com/vllm-project/vllm/pull/17583) | closes_keyword | 0.95 | [Bugfix][ROCm] Fix incorrect casting in GPTQ GEMM kernel | FIX #7374 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
