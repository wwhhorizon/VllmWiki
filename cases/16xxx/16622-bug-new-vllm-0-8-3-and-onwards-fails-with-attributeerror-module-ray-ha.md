# vllm-project/vllm#16622: [Bug]: new vllm 0.8.3 and onwards fails with AttributeError: module 'ray' has no attribute 'is_initialized'

| 字段 | 值 |
| --- | --- |
| Issue | [#16622](https://github.com/vllm-project/vllm/issues/16622) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: new vllm 0.8.3 and onwards fails with AttributeError: module 'ray' has no attribute 'is_initialized'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Bringing up the server does not work. It always fails with ``` File "/home/{user_name}/miniconda3/envs/vllm084/lib/python3.12/site-packages/vllm/utils.py", line 2279, in is_in_ray_actor return (ray.is_initialized() ^^^^^^^^^^^^^^^^^^ AttributeError: module 'ray' has no attribute 'is_initialized' ``` It was fine on vllm 0.7.2, and only thing I have installed with conda env is vllm via pip. (edit : tested on vllm 0.8.1, and it works find too. But problem seems to starts from version 0.8.3) I do not think its a gpu problem because its only using 2x Ada-a6000 via `CUDA_VISIBLE_DEVICES` ``` VLLM_WORKER_MULTIPROC_METHOD=spawn \ python -m vllm.entrypoints.openai.api_server \ --port 14220 \ --model Valdemardi/DeepSeek-R1-Distill-Llama-70B-AWQ \ --quantization awq \ --dtype float16 \ --tensor-parallel-size 2 ``` ``` python -m vllm.entrypoints.openai.api_server \ --host 192.168.0.43 \ --port 14220 \ --dtype auto \ --model google/gemma-3-27b-it \ --tensor-parallel-size 2 ``` Using single GPU also did not solved the problem. also, on the sidenote, when was `--enforce-eager` keyword got deprecated? python -m vllm.entrypoints.openai.api_server...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e 'is_initialized' ``` It was fine on vllm 0.7.2, and only thing I have installed with conda env is vllm via pip. (edit : tested on vllm 0.8.1, and it works find too. But problem seems to starts from version 0.8.3) I do...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -port 14220 \ --model Valdemardi/DeepSeek-R1-Distill-Llama-70B-AWQ \ --quantization awq \ --dtype float16 \ --tensor-parallel-size 2 ``` ``` python -m vllm.entrypoints.openai.api_server \ --host 192.168.0.43 \ --port 14...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: awn \ python -m vllm.entrypoints.openai.api_server \ --port 14220 \ --model Valdemardi/DeepSeek-R1-Distill-Llama-70B-AWQ \ --quantization awq \ --dtype float16 \ --tensor-parallel-size 2 ``` ``` python -m vllm.entrypoin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: do not think its a gpu problem because its only using 2x Ada-a6000 via `CUDA_VISIBLE_DEVICES` ``` VLLM_WORKER_MULTIPROC_METHOD=spawn \ python -m vllm.entrypoints.openai.api_server \ --port 14220 \ --model Valdemardi/Dee...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
