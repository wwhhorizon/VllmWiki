# vllm-project/vllm#21640: [Bug]: calculate_kv_scales leads to dynamo compilation issue; enforce_eager=True leads to another issue

| 字段 | 值 |
| --- | --- |
| Issue | [#21640](https://github.com/vllm-project/vllm/issues/21640) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: calculate_kv_scales leads to dynamo compilation issue; enforce_eager=True leads to another issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am on v0.10.0. The argument `calculate_kv_scales=True` does not seem to work. ### If `enforce_eager=False` With code: ```python import vllm def main(): engine = vllm.LLM( model="/home/ubuntu/models/Qwen3-8B", tensor_parallel_size=2, kv_cache_dtype="fp8_e4m3", calculate_kv_scales=True, ) output = engine.generate("Hello, world!") print(output) if __name__ == "__main__": main() ``` I run into ```bash RuntimeError: Worker failed with error 'Data-dependent branching Explanation: Detected data-dependent branching (e.g. `if my_tensor.sum() > 0:`). Dynamo does not support tracing dynamic control flow. Hint: This graph break is fundamental - it is unlikely that Dynamo will ever be able to trace through your code. Consider finding a workaround. Hint: Use `torch.cond` to express dynamic control flow. Developer debug context: attempted to jump with GetAttrVariable(ConstantVariable(NoneType: None), enable_kv_scales_calculation) from user code: File "/home/ubuntu/miniconda3/envs/vllm-new/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 354, in forward hidden_states, residual = layer( File "/home/ubuntu/miniconda3/envs/...

## 现有链接修复摘要

#24290 [Bugfix] guard missing attn_metadata in KV scales path | #25513 [BugFix][torch.compile] KV scale calculation issues with FP8 quantization (#21640)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: o compilation issue; enforce_eager=True leads to another issue bug;torch.compile ### Your current environment ### 🐛 Describe the bug I am on v0.10.0. The argument `calculate_kv_scales=True` does not seem to work. ### If...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: calculate_kv_scales leads to dynamo compilation issue; enforce_eager=True leads to another issue bug;torch.compile ### Your current environment ### 🐛 Describe the bug I am on v0.10.0. The argument `calculate_kv_s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ebd ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: alculate_kv_scales=True` does not seem to work. ### If `enforce_eager=False` With code: ```python import vllm def main(): engine = vllm.LLM( model="/home/ubuntu/models/Qwen3-8B", tensor_parallel_size=2, kv_cache_dtype="...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: code: ```python import vllm def main(): engine = vllm.LLM( model="/home/ubuntu/models/Qwen3-8B", tensor_parallel_size=2, kv_cache_dtype="fp8_e4m3", calculate_kv_scales=True, ) output = engine.generate("Hello, world!") p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24290](https://github.com/vllm-project/vllm/pull/24290) | closes_keyword | 0.95 | [Bugfix] guard missing attn_metadata in KV scales path | Resolves: #21640 ## Test Plan Manual verification with FP8 KV cache and `calculate_kv_scales=True`: 1) Default (torch.compile) path — no Dynamo error ```python import vllm engi |
| [#25513](https://github.com/vllm-project/vllm/pull/25513) | closes_keyword | 0.95 | [BugFix][torch.compile] KV scale calculation issues with FP8 quantization (#21640) | Fix KV scale calculation incompatibility with torch.compile and enforce_eager mode (#21640) The conditional check `if attn_metadata.enable_kv_scales_calculation`: at line 274 in ` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
