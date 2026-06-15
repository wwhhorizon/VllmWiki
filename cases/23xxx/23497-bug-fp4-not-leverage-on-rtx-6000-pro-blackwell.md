# vllm-project/vllm#23497: [Bug]: FP4 not leverage on RTX 6000 Pro (Blackwell)

| 字段 | 值 |
| --- | --- |
| Issue | [#23497](https://github.com/vllm-project/vllm/issues/23497) |
| 状态 | open |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: FP4 not leverage on RTX 6000 Pro (Blackwell)

### Issue 正文摘录

### Your current environment Run with Docker ```Dockerfile FROM vllm/vllm-openai:v0.10.1 RUN uv pip install --system -U nvidia-nccl-cu12 ``` I build it as vllm-new and then run it as ``` docker run -it --gpus all --entrypoint /bin/bash vllm-new ``` Then wget and run the collect script inside and receive the below output. ### 🐛 Describe the bug When running GPT-Oss 120B I see ``` vllm-1 | (EngineCore_0 pid=270) WARNING 08-24 09:51:03 [marlin_utils_fp4.py:196] Your GPU does not have native support for FP4 computation but FP4 quantization is being used. Weight-only FP4 compression will be used leveraging the Marlin kernel. This may degrade performance for compute-heavy workloads. ``` in the output. It still runs ~100 tokens/s for a single request- but maybe there's performance left on the table. This is possibly related to the merged PR here : #21309 though Maybe the message should be changed to FP4 is not supported by vLLM on your GPU yet? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequentl...

## 现有链接修复摘要

#21309 Support CUTLASS NVFP4 (w4a4) for Blackwell Geforce GPUs (SM120)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e on RTX 6000 Pro (Blackwell) bug ### Your current environment Run with Docker ```Dockerfile FROM vllm/vllm-openai:v0.10.1 RUN uv pip install --system -U nvidia-nccl-cu12 ``` I build it as vllm-new and then run it as ``...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: FP4 not leverage on RTX 6000 Pro (Blackwell) bug ### Your current environment Run with Docker ```Dockerfile FROM vllm/vllm-openai:v0.10.1 RUN uv pip install --system -U nvidia-nccl-cu12 ``` I build it as vllm-new...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP4 not leverage on RTX 6000 Pro (Blackwell) bug ### Your current environment Run with Docker ```Dockerfile FROM vllm/vllm-openai:v0.10.1 RUN uv pip install --system -U nvidia-nccl-cu12 ``` I build it as vllm-new...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: g_logits;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;nan_inf env_dependency #21309 Support CUTLASS NVFP4 (w4a4) for Blackwell Geforce GPUs (SM120) Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e and receive the below output. ### 🐛 Describe the bug When running GPT-Oss 120B I see ``` vllm-1 | (EngineCore_0 pid=270) WARNING 08-24 09:51:03 [marlin_utils_fp4.py:196] Your GPU does not have native support for FP4 c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21309](https://github.com/vllm-project/vllm/pull/21309) | mentioned | 0.45 | Support CUTLASS NVFP4 (w4a4) for Blackwell Geforce GPUs (SM120) | left on the table. this is possibly related to the merged pr here : #21309 though maybe the message should be changed to fp4 is not supported by vllm on your gpu yet? ### before s… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
