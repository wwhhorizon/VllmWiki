# vllm-project/vllm#37486: [Bug]: Qwen3 + DeepGEMM + dummy-load   Cannot access data pointer of Tensor that doesn't have storage

| 字段 | 值 |
| --- | --- |
| Issue | [#37486](https://github.com/vllm-project/vllm/issues/37486) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 + DeepGEMM + dummy-load   Cannot access data pointer of Tensor that doesn't have storage

### Issue 正文摘录

### Your current environment module file: /root/venv/lib/python3.12/site-packages/deep_gemm/__init__.py version: 2.3.0 has fp8_gemm_nt: True has transform_sf_into_required_layout: True has get_mk_alignment_for_contiguous_layout: True main branch ### 🐛 Describe the bug ``` cat > /tmp/qwen3_async_tp_dump.py &1 | tee /tmp/qwen3_async_tp.log ``` res： https://paste.ubuntu.com/p/4w4FzFnjxv/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: _.py version: 2.3.0 has fp8_gemm_nt: True has transform_sf_into_required_layout: True has get_mk_alignment_for_contiguous_layout: True main branch ### 🐛 Describe the bug ``` cat > /tmp/qwen3_async_tp_dump.py &1 | tee /t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: dule file: /root/venv/lib/python3.12/site-packages/deep_gemm/__init__.py version: 2.3.0 has fp8_gemm_nt: True has transform_sf_into_required_layout: True has get_mk_alignment_for_contiguous_layout: True main branch ###...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nv/lib/python3.12/site-packages/deep_gemm/__init__.py version: 2.3.0 has fp8_gemm_nt: True has transform_sf_into_required_layout: True has get_mk_alignment_for_contiguous_layout: True main branch ### 🐛 Describe the bug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: xv/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen3 + DeepGEMM + dummy-load Cannot access data pointer of Tensor that doesn't have storage bug ### Your current environment module file: /root/venv/lib/python3.12/site-packages/deep_gemm/__init__.py version: 2....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
