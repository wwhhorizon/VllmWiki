# vllm-project/vllm#31883: [Feature]: draft model about spec decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#31883](https://github.com/vllm-project/vllm/issues/31883) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: draft model about spec decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch now i can't use draft model, following is my vllm code: vllm serve /Qwen/Qwen3-4B \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --host 0.0.0.0 \ --port 8199 \ --speculative_config '{"model": "/Qwen/Qwen3-0___6B", "num_speculative_tokens": 5}' the result is : (APIServer pid=135812) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=135812) File "/root/anaconda3/envs/vllm_env/lib/python3.11/site-packages/pydantic/_internal/_dataclasses.py", line 121, in __init__ (APIServer pid=135812) s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s) (APIServer pid=135812) File "/root/anaconda3/envs/vllm_env/lib/python3.11/site-packages/vllm/config/speculative.py", line 380, in __post_init__ (APIServer pid=135812) raise NotImplementedError( (APIServer pid=135812) NotImplementedError: Speculative decoding with draft model is not supported yet. Please consider using other speculative decoding methods such as ngram, medusa, eagle, or mtp. my vllm version is 0.13.0, gpu is NVIDIA GeForce RTX 4070, system is wsl2-ubuntu20.04 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new i...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: draft model about spec decoding feature request;stale ### 🚀 The feature, motivation and pitch now i can't use draft model, following is my vllm code: vllm serve /Qwen/Qwen3-4B \ --dtype bfloat16 \ --tensor-pa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e draft model, following is my vllm code: vllm serve /Qwen/Qwen3-4B \ --dtype bfloat16 \ --tensor-parallel-size 1 \ --host 0.0.0.0 \ --port 8199 \ --speculative_config '{"model": "/Qwen/Qwen3-0___6B", "num_speculative_t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: draft model about spec decoding feature request;stale ### 🚀 The feature, motivation and pitch now i can't use draft model, following is my vllm code: vllm serve /Qwen/Qwen3-4B \ --dtype bfloat16 \ --tensor-pa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: medusa, eagle, or mtp. my vllm version is 0.13.0, gpu is NVIDIA GeForce RTX 4070, system is wsl2-ubuntu20.04 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x]...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: culative decoding methods such as ngram, medusa, eagle, or mtp. my vllm version is 0.13.0, gpu is NVIDIA GeForce RTX 4070, system is wsl2-ubuntu20.04 ### Alternatives _No response_ ### Additional context _No response_ #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
