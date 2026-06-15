# vllm-project/vllm#21097: [Bug]: w8a8 quantization not supporting sm120

| 字段 | 值 |
| --- | --- |
| Issue | [#21097](https://github.com/vllm-project/vllm/issues/21097) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: w8a8 quantization not supporting sm120

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug According to #17280 and https://docs.vllm.ai/en/stable/features/quantization/int8.html#3-applying-quantization we should be able to use w8a8 fp8 with sm120 Used official docker image via ```docker pull vllm/vllm-openai:v0.9.2``` Started docker container via ```docker run -e HF_TOKEN --gpus all --rm -it --entrypoint bash -v ./models:/models -v ./scripts:/scripts vllm/vllm-openai:v0.9.2``` once inside I followed https://docs.vllm.ai/en/stable/features/quantization/int8.html#3-applying-quantization to quantize the example model and got ```CUDA error: no kernel image is available for execution on the device``` Wasn't #17280 supposed to fix this? ``` ((venv) ) root@f8f14b925638:/scripts# python3 quantize.rb INFO 07-17 00:03:09 [__init__.py:244] Automatically detected platform cuda. /scripts/venv/lib/python3.12/site-packages/torch/cuda/__init__.py:287: UserWarning: NVIDIA RTX PRO 6000 Blackwell Workstation Edition with CUDA capability sm_120 is not compatible with the current PyTorch installation. The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90. If you want to use the NVIDIA RTX PRO 6000...

## 现有链接修复摘要

#17280 [NVIDIA] Support Cutlass w8a8 FP8 for Blackwell Geforce GPUs (sm120)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ying-quantization we should be able to use w8a8 fp8 with sm120 Used official docker image via ```docker pull vllm/vllm-openai:v0.9.2``` Started docker container via ```docker run -e HF_TOKEN --gpus all --rm -it --entryp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: w8a8 quantization not supporting sm120 bug;stale ### Your current environment ### 🐛 Describe the bug According to #17280 and https://docs.vllm.ai/en/stable/features/quantization/int8.html#3-applying-quantization...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: w8a8 quantization not supporting sm120 bug;stale ### Your current environment ### 🐛 Describe the bug According to #17280 and https://docs.vllm.ai/en/stable/features/quantization/int8.html#3-applying-quantization...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: llm/vllm-openai:v0.9.2``` Started docker container via ```docker run -e HF_TOKEN --gpus all --rm -it --entrypoint bash -v ./models:/models -v ./scripts:/scripts vllm/vllm-openai:v0.9.2``` once inside I followed https://...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: gits;speculative_decoding cuda;fp8;kernel;operator;quantization;sampling;triton build_error;crash;mismatch;nan_inf dtype;env_dependency #17280 [NVIDIA] Support Cutlass w8a8 FP8 for Blackwell Geforce GPUs (sm120) Your cu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17280](https://github.com/vllm-project/vllm/pull/17280) | mentioned | 0.45 | [NVIDIA] Support Cutlass w8a8 FP8 for Blackwell Geforce GPUs (sm120) | : no kernel image is available for execution on the device``` wasn't #17280 supposed to fix this? ``` ((venv) ) root@f8f14b925638:/scripts# python3 quantize.rb info 07-17 00:03:09… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
