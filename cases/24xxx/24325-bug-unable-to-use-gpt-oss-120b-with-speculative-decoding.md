# vllm-project/vllm#24325: [Bug]: Unable to use GPT-OSS-120B with speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#24325](https://github.com/vllm-project/vllm/issues/24325) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unable to use GPT-OSS-120B with speculative decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running the latest vllm main branch (commit b5ee1e3) with local install via: `VLLM_USE_PRECOMPILED=1 pip install --editable .` When I run the following command: `vllm serve "openai/gpt-oss-120b" --host 0.0.0.0 --port 8000 --speculative-config '{"model": "nvidia/gpt-oss-120b-Eagle3", "num_speculative_tokens": 3, "method":"eagle3", "draft_tensor_parallel_size":1}'` However, this returns an error: ``` (APIServer pid=3582) speculative_config = self.create_speculative_config( (APIServer pid=3582) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=3582) File "/root/vllm/vllm/engine/arg_utils.py", line 1082, in create_speculative_config (APIServer pid=3582) return SpeculativeConfig(**self.speculative_config) (APIServer pid=3582) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=3582) File "/usr/local/lib/python3.11/dist-packages/pydantic/_internal/_dataclasses.py", line 123, in __init__ (APIServer pid=3582) s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s) (APIServer pid=3582) pydantic_core._pydantic_core.ValidationError: 1 validation error for SpeculativeConfig (APIServer pid=3582) Value err...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Unable to use GPT-OSS-120B with speculative decoding bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug I am running the latest vllm main branch (commit b5ee1e3) with local install via: `VLLM_U...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: on error for SpeculativeConfig (APIServer pid=3582) Value error, Model architectures ['LlamaForCausalLMEagle3'] are not supported for now. ``` The above error happens both on H100 and A100. Are there plans of supporting...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Unable to use GPT-OSS-120B with speculative decoding bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug I am running the latest vllm main branch (commit b5ee1e3) with local install via: `VLLM_U...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ug I am running the latest vllm main branch (commit b5ee1e3) with local install via: `VLLM_USE_PRECOMPILED=1 pip install --editable .` When I run the following command: `vllm serve "openai/gpt-oss-120b" --host 0.0.0.0 -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Your current environment ### 🐛 Describe the bug I am running the latest vllm main branch (commit b5ee1e3) with local install via: `VLLM_USE_PRECOMPILED=1 pip install --editable .` When I run the following command: `vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
