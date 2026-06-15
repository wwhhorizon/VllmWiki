# vllm-project/vllm#32029: [RFC]: Online Quantization Roadmap

| 字段 | 值 |
| --- | --- |
| Issue | [#32029](https://github.com/vllm-project/vllm/issues/32029) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;kernel;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Online Quantization Roadmap

### Issue 正文摘录

### Motivation. Online quantization (weights passed to vLLM in high precision, quantization of weights done inside of vLLM) is emerging as an important use case for quick experimentation and RL. Today vLLM supports online quantization with a single recipe (float8 per-tensor scaling). I wanted to align on the high level future direction of the specifics of how online quantization is implemented in vLLM as we extend this to more recipes / more hardware types / more use cases. ### Proposed Change. ### Guiding principles * prefer inlining online quantization logic in vLLM directly over calling third party libraries, for simplicity of the common case. * separate online quantization code from offline quantization code as appropriate, sharing underlying utilities as needed. * the basic dtype of the weight (fp8, int8, etc) should be the high level organization axis for online quant UI and code. For example, the high level entrypoint for online quant for fp8 (currently `fp8.py` and `--quantization=fp8` in the CLI) should be the entry point for all fp8 weight recipes (tensorwise, rowwise, deepseek-style blockwise, etc) across all hardware types (NVIDIA, AMD, Intel, etc). ### Planned improve...

## 现有链接修复摘要

#35448 [Quant][Feature] Support online MXFP8 quantization for MoE and dense models

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [RFC]: Online Quantization Roadmap RFC;stale ### Motivation. Online quantization (weights passed to vLLM in high precision, quantization of weights done inside of vLLM) is emerging as an important use case for quick exp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ale ### Motivation. Online quantization (weights passed to vLLM in high precision, quantization of weights done inside of vLLM) is emerging as an important use case for quick experimentation and RL. Today vLLM supports...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### Motivation. Online quantization (weights passed to vLLM in high precision, quantization of weights done inside of vLLM) is emerging as an important use case for quick experimentation and RL. Today vLLM supports onli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pecific `quantize_to_fp8_rowwise` kernel, what is the recommended mechanism to guarantee the same kernel being used in vLLM? Is it an env var, an out-of-tree kernel registration mechanism, something else? ### Feedback P...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ry point for all fp8 weight recipes (tensorwise, rowwise, deepseek-style blockwise, etc) across all hardware types (NVIDIA, AMD, Intel, etc). ### Planned improvements #### fp8 (fp8.py, --quantization="fp8") * improve co...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35448](https://github.com/vllm-project/vllm/pull/35448) | mentioned | 0.6 | [Quant][Feature] Support online MXFP8 quantization for MoE and dense models | his PR implements part of the online quantization support proposed in #32029 and #32412 ### Usage ```bash # Serve any BF16 model with online MXFP8 quantization vllm serve <model>… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
