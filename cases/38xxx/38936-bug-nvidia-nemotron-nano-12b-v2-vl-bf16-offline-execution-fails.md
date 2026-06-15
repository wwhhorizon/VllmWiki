# vllm-project/vllm#38936: [Bug]: NVIDIA-Nemotron-Nano-12B-v2-VL-BF16 offline execution fails

| 字段 | 值 |
| --- | --- |
| Issue | [#38936](https://github.com/vllm-project/vllm/issues/38936) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVIDIA-Nemotron-Nano-12B-v2-VL-BF16 offline execution fails

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have a new conda environment ``` conda create -n vllm-env python=3.12 pip install uv uv pip install vllm --torch-backend=cu128 ``` I am trying to use the following model `Nemotron-Nano-12B-v2-VL` to work. ``` from vllm import LLM, SamplingParams model_path = "nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16" llm = LLM( model=model_path, trust_remote_code=True, max_model_len=131072 ) ``` This fails with ``` --------------------------------------------------------------------------- AttributeError Traceback (most recent call last) File [~/miniconda3/envs/vllm-env-1/lib/python3.10/site-packages/vllm/multimodal/processing/context.py:269](http://localhost:8888/lab/tree/1_projects/2_public_safety_engine/miniconda3/envs/vllm-env-1/lib/python3.10/site-packages/vllm/multimodal/processing/context.py#line=268), in InputProcessingContext.call_hf_processor(self, hf_processor, data, kwargs, num_tries, max_tries) 268 try: --> 269 output = hf_processor(**data, **allowed_kwargs) 270 except Exception as exc: 271 # See https://github.com/huggingface/tokenizers/issues/537 File [~/miniconda3/envs/vllm-env-1/lib/python3.10/site-packages/vllm/transformers_...

## 现有链接修复摘要

#39561 [Bugfix]Fix issue #38936 NVIDIA-Nemotron-Nano-12B-v2-VL-BF16 offline execution

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ave a new conda environment ``` conda create -n vllm-env python=3.12 pip install uv uv pip install vllm --torch-backend=cu128 ``` I am trying to use the following model `Nemotron-Nano-12B-v2-VL` to work. ``` from vllm i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: install vllm --torch-backend=cu128 ``` I am trying to use the following model `Nemotron-Nano-12B-v2-VL` to work. ``` from vllm import LLM, SamplingParams model_path = "nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16" llm = L...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: reate -n vllm-env python=3.12 pip install uv uv pip install vllm --torch-backend=cu128 ``` I am trying to use the following model `Nemotron-Nano-12B-v2-VL` to work. ``` from vllm import LLM, SamplingParams model_path =...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: NVIDIA-Nemotron-Nano-12B-v2-VL-BF16 offline execution fails bug ### Your current environment ### 🐛 Describe the bug I have a new conda environment ``` conda create -n vllm-env python=3.12 pip install uv uv pip in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39561](https://github.com/vllm-project/vllm/pull/39561) | closes_keyword | 0.95 | [Bugfix]Fix issue #38936 NVIDIA-Nemotron-Nano-12B-v2-VL-BF16 offline execution | Fix issue #38936: NanoNemotronVLProcessor is a custom processor implementation that does not inherit from Huggingface's ProcessorMixin., it lacks standard properties like image_pr |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
