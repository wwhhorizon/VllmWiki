# vllm-project/vllm#1614: RuntimeError: CUDA error: out of memory with llama-2-13b-chat-hf model on A100 with vllm 0.2.1.post1 version

| 字段 | 值 |
| --- | --- |
| Issue | [#1614](https://github.com/vllm-project/vllm/issues/1614) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError: CUDA error: out of memory with llama-2-13b-chat-hf model on A100 with vllm 0.2.1.post1 version

### Issue 正文摘录

Hi team, I tried below code on vm with A100 which fastchat and DeepSpeed can both server the same model ``` from vllm import LLM, SamplingParams import os os.environ['CUDA_LAUNCH_BLOCKING'] = "1" prompts = [ "What's the advantage of DeepSpeed", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="llama-2-13b-chat-hf") outputs = llm.generate(prompts, sampling_params) ``` I met the error below, ``` Traceback (most recent call last): File "/home/yalqin/deepspeed_mii/test-vllm.py", line 11, in llm = LLM(model="llama-2-13b-chat-hf") ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/anaconda3/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 93, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/anaconda3/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 231, in from_engine_args engine = cls(*engine_configs, ^^^^^^^^^^^^^^^^^^^^ File "/root/anaconda3/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 110, in __init__ self._init_workers(distributed_init_method) File "/root/anaconda3/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 142, in _init_worke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t of memory with llama-2-13b-chat-hf model on A100 with vllm 0.2.1.post1 version Hi team, I tried below code on vm with A100 which fastchat and DeepSpeed can both server the same model ``` from vllm import LLM, Sampling...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: RuntimeError: CUDA error: out of memory with llama-2-13b-chat-hf model on A100 with vllm 0.2.1.post1 version Hi team, I tried below code on vm with A100 which fastchat and DeepSpeed can both server the same model ``` fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: RuntimeError: CUDA error: out of memory with llama-2-13b-chat-hf model on A100 with vllm 0.2.1.post1 version Hi team, I tried below code on vm with A100 which fastchat and DeepSpeed can both server the same model ``` fr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: api;model_support;sampling_logits cuda;kernel;sampling build_error;crash;mismatch;oom env_dependency Hi team, I tried below code on vm with A100 which fastchat and DeepSpeed can both server the same model
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: _support;sampling_logits cuda;kernel;sampling build_error;crash;mismatch;oom env_dependency Hi team, I tried below code on vm with A100 which fastchat and DeepSpeed can both server the same model

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
